"""
Sistema de batalla por turnos completo con captura - v2 limpia.
"""
import random
from data.pokedex import POKEDEX_COMPLETA

try:
    from sistemas.combate_ia import elegir_movimiento_ia
except Exception:
    def elegir_movimiento_ia(a, d, m):
        return m[0] if m else None


class Movimiento:
    def __init__(self, datos: dict):
        self.nombre = datos["nombre"]
        self.tipo = datos["tipo"]
        self.potencia = datos.get("potencia", 40)
        self.precision = datos.get("precision", 100)
        self.categoria = datos.get("categoria", "Físico")
        self.pp = datos.get("pp", 20)
        self.pp_max = self.pp

    def __repr__(self):
        return f"{self.nombre} [{self.tipo} | POT {self.potencia}]"


class PokemonBatalla:
    def __init__(self, datos: dict, nivel: int = 5):
        self.nombre = datos["nombre"]
        self.tipos = datos["tipos"]
        self.nivel = nivel
        self.id = datos.get("id", 0)
        self.tasa_captura = datos.get("tasa_captura", 150)

        st = datos["stats_base"]
        self.ps_base = st["ps"]
        self.atq_base = st["atq"]
        self.def_base = st["def"]
        self.atq_esp_base = st["atq_esp"]
        self.def_esp_base = st["def_esp"]
        self.vel_base = st["vel"]
        self._calcular_stats()

        self.exp = 0
        self.exp_total = 0

        self.movimientos = [Movimiento(m) for m in datos.get("movimientos_iniciales", [])]

        self.estado = None
        self.turnos_estado = 0
        # Shiny
        self.es_shiny = False
        self.color_shiny = None

    def _calcular_stats(self):
        self.ps_max = int(((2 * self.ps_base) * self.nivel / 100) + self.nivel + 10)
        self.ps = self.ps_max
        self.atq = int(((2 * self.atq_base) * self.nivel / 100) + 5)
        self.defensa = int(((2 * self.def_base) * self.nivel / 100) + 5)
        self.atq_esp = int(((2 * self.atq_esp_base) * self.nivel / 100) + 5)
        self.def_esp = int(((2 * self.def_esp_base) * self.nivel / 100) + 5)
        self.vel = int(((2 * self.vel_base) * self.nivel / 100) + 5)

    def esta_vivo(self) -> bool:
        return self.ps > 0

    def recibir_danio(self, cantidad: int):
        self.ps = max(0, self.ps - cantidad)

    def curar(self, cantidad: int):
        self.ps = min(self.ps_max, self.ps + cantidad)

    def exp_para_siguiente_nivel(self) -> int:
        return int(self.nivel ** 2.2 + 10)

    def ganar_exp(self, cantidad: int) -> dict:
        resultado = {"subidas": [], "movimientos_aprendidos": []}
        self.exp += cantidad
        self.exp_total += cantidad
        while self.exp >= self.exp_para_siguiente_nivel() and self.nivel < 100:
            self.exp -= self.exp_para_siguiente_nivel()
            self.nivel += 1
            ps_anterior = self.ps_max
            self._calcular_stats()
            self.ps += (self.ps_max - ps_anterior)
            resultado["subidas"].append(self.nivel)
        return resultado


TABLA_TIPOS = {  # (sin cambios)
    "Fuego":     {"Planta": 2.0, "Hielo": 2.0, "Acero": 2.0, "Agua": 0.5, "Roca": 0.5, "Fuego": 0.5, "Dragón": 0.5},
    "Agua":      {"Fuego": 2.0, "Tierra": 2.0, "Roca": 2.0, "Agua": 0.5, "Planta": 0.5, "Dragón": 0.5},
    "Planta":    {"Agua": 2.0, "Tierra": 2.0, "Roca": 2.0, "Fuego": 0.5, "Planta": 0.5, "Veneno": 0.5,
                  "Volador": 0.5, "Bicho": 0.5, "Dragón": 0.5, "Acero": 0.5},
    "Eléctrico": {"Agua": 2.0, "Volador": 2.0, "Tierra": 0.0, "Eléctrico": 0.5, "Planta": 0.5, "Dragón": 0.5},
    "Hielo":     {"Planta": 2.0, "Tierra": 2.0, "Volador": 2.0, "Dragón": 2.0, "Fuego": 0.5, "Agua": 0.5,
                  "Hielo": 0.5, "Acero": 0.5},
    "Lucha":     {"Normal": 2.0, "Hielo": 2.0, "Roca": 2.0, "Siniestro": 2.0, "Acero": 2.0,
                  "Veneno": 0.5, "Volador": 0.5, "Psíquico": 0.5, "Bicho": 0.5, "Hada": 0.5, "Fantasma": 0.0},
    "Veneno":    {"Planta": 2.0, "Hada": 2.0, "Veneno": 0.5, "Tierra": 0.5, "Roca": 0.5, "Fantasma": 0.5,
                  "Acero": 0.0},
    "Tierra":    {"Fuego": 2.0, "Eléctrico": 2.0, "Veneno": 2.0, "Roca": 2.0, "Acero": 2.0,
                  "Planta": 0.5, "Bicho": 0.5, "Volador": 0.0},
    "Volador":   {"Planta": 2.0, "Lucha": 2.0, "Bicho": 2.0, "Eléctrico": 0.5, "Roca": 0.5, "Acero": 0.5},
    "Psíquico":  {"Lucha": 2.0, "Veneno": 2.0, "Psíquico": 0.5, "Acero": 0.5, "Siniestro": 0.0},
    "Bicho":     {"Planta": 2.0, "Psíquico": 2.0, "Siniestro": 2.0, "Fuego": 0.5, "Lucha": 0.5,
                  "Volador": 0.5, "Fantasma": 0.5, "Acero": 0.5, "Hada": 0.5},
    "Roca":      {"Fuego": 2.0, "Hielo": 2.0, "Volador": 2.0, "Bicho": 2.0, "Lucha": 0.5,
                  "Tierra": 0.5, "Acero": 0.5},
    "Fantasma":  {"Psíquico": 2.0, "Fantasma": 2.0, "Siniestro": 0.5, "Normal": 0.0},
    "Siniestro": {"Psíquico": 2.0, "Fantasma": 2.0, "Lucha": 0.5, "Siniestro": 0.5, "Hada": 0.5},
    "Dragón":    {"Dragón": 2.0, "Acero": 0.5, "Hada": 0.0},
    "Acero":     {"Hielo": 2.0, "Roca": 2.0, "Hada": 2.0, "Fuego": 0.5, "Agua": 0.5,
                  "Eléctrico": 0.5, "Acero": 0.5},
    "Hada":      {"Lucha": 2.0, "Dragón": 2.0, "Siniestro": 2.0, "Fuego": 0.5, "Veneno": 0.5, "Acero": 0.5},
    "Normal":    {"Roca": 0.5, "Acero": 0.5, "Fantasma": 0.0},
    "Sonido":    {},  # tipo regional, neutro
}


def calcular_efectividad(tipo_ataque, tipos_defensor):
    mult = 1.0
    tabla = TABLA_TIPOS.get(tipo_ataque, {})
    for t in tipos_defensor or []:
        mult *= tabla.get(t, 1.0)
    return mult


def calcular_danio(atacante, defensor, mov):
    if mov.potencia == 0:
        return 0
    if mov.categoria and "fisic" in mov.categoria.lower():
        atk, dfn = atacante.atq, defensor.defensa
    elif mov.categoria and "especial" in mov.categoria.lower():
        atk, dfn = atacante.atq_esp, defensor.def_esp
    else:
        return 0
    danio = (((2 * atacante.nivel / 5) + 2) * mov.potencia * (atk / max(1, dfn))) / 50 + 2
    if mov.tipo in atacante.tipos:
        danio *= 1.5
    danio *= calcular_efectividad(mov.tipo, defensor.tipos)
    danio *= random.uniform(0.85, 1.0)
    return max(1, int(danio))


def calcular_exp_ganada(rival):
    base = 40 + (rival.ps_base + rival.atq_base + rival.vel_base) // 3
    return max(10, int((base * rival.nivel) / 7))


def calcular_tasa_captura(pokemon, tipo_ball, estado=None):
    tasas_ball = {
        "Freekie Ball": 1.0, "Súper Ball": 1.5, "Super Ball": 1.5,
        "Ultra Ball": 2.0,
        "Chasqui Ball": 3.0 if pokemon.ps == pokemon.ps_max else 1.0,
        "Selva Ball": 2.5, "Apu Ball": 255.0,
    }
    tasa_base = tasas_ball.get(tipo_ball, 1.0)
    if tasa_base >= 255.0:
        return 1.0
    mod_estado = 1.0
    if estado in ("dormido", "congelado"):
        mod_estado = 2.0
    elif estado in ("paralizado", "quemado", "envenenado"):
        mod_estado = 1.5
    tc = getattr(pokemon, "tasa_captura", 150)
    factor_rareza = 255 / max(1, tc)
    factor_hp = (3 * pokemon.ps_max - 2 * pokemon.ps) / (3 * pokemon.ps_max)
    a = min(255, factor_hp * tasa_base * mod_estado * factor_rareza)
    return min(1.0, a / 255)


def intentar_capturar(pokemon, tipo_ball, estado=None):
    resultado = {"exito": False, "intentos": 0, "mensajes": []}
    prob = calcular_tasa_captura(pokemon, tipo_ball, estado)
    if prob >= 1.0:
        resultado["intentos"] = 1
        resultado["exito"] = True
        resultado["mensajes"].append(f"¡{pokemon.nombre} fue capturado directamente!")
    else:
        for i in range(4):
            resultado["intentos"] = i + 1
            if random.random() < prob:
                resultado["exito"] = True
                resultado["mensajes"].append(f"¡Gotcha! ¡{pokemon.nombre} fue capturado!")
                break
            else:
                if i < 3:
                    resultado["mensajes"].append(f"¡Casi! {pokemon.nombre} escapó...")
                else:
                    resultado["mensajes"].append(f"¡Oh no! {pokemon.nombre} se liberó.")
    return resultado


class Batalla:
    """Sistema de batalla completo."""

    def __init__(self, equipo_jugador, pokemon_salvaje):
        self.equipo_jugador = equipo_jugador
        self.pokemon_salvaje = pokemon_salvaje
        self.pokemon_activo_jugador = equipo_jugador[0] if equipo_jugador else pokemon_salvaje
        self.turno = 1
        self.mensajes = []
        self.terminada = False
        self.resultado = None
        self.pokemon_capturado = None
        self.sub_estado = "menu_principal"

        # Flags
        self.es_gimnasio = False
        self.gimnasio_id = None
        self.es_rival = False
        self.es_supay = False
        self.es_portero = False
        self.rival_equipo = []
        self.rival_poke_idx = 0

        # Animación
        self._flash_rival = 0.0
        self._flash_jugador = 0.0
        self._atacando = None

        self.es_shiny = False
        self.color_shiny = None

    def ejecutar_turno(self, mov_jugador):
        mensajes = []
        jug = self.pokemon_activo_jugador
        riv = self.pokemon_salvaje

        # FIX_PP_AGOTADO
        if mov_jugador and getattr(mov_jugador, "pp", 1) <= 0:
            mensajes.append(f"!{mov_jugador.nombre} no tiene PP!")
            return mensajes
        if not jug.movimientos:
            mensajes.append(f"¡{jug.nombre} no tiene movimientos!")
            return mensajes

        if jug.vel >= riv.vel:
            mensajes.extend(self._ejecutar_ataque_jugador(mov_jugador))
            if riv.esta_vivo():
                mensajes.extend(self._ejecutar_ataque_rival())
        else:
            mensajes.extend(self._ejecutar_ataque_rival())
            if jug.esta_vivo():
                mensajes.extend(self._ejecutar_ataque_jugador(mov_jugador))

        if not riv.esta_vivo():
            self.terminada = True
            self.resultado = "victoria"
            mensajes.append(f"¡{riv.nombre} se debilitó!")
        elif not jug.esta_vivo():
            siguiente = self._buscar_siguiente_vivo()
            if siguiente:
                self.pokemon_activo_jugador = siguiente
                mensajes.append(f"¡Adelante, {siguiente.nombre}!")
            else:
                self.terminada = True
                self.resultado = "derrota"
                mensajes.append("¡Todos tus Pokémon se debilitaron!")

        self.turno += 1
        return mensajes

    def _ejecutar_ataque_jugador(self, mov):
        mensajes = []
        mov.pp = max(0, mov.pp - 1)

        # 1) Anuncio
        mensajes.append(f"¡{self.pokemon_activo_jugador.nombre} usó {mov.nombre}!")

        # 2) Precisión
        if random.randint(1, 100) > mov.precision:
            mensajes.append(f"¡Pero falló!")
            return mensajes

        # 3) Daño
        danio = calcular_danio(self.pokemon_activo_jugador, self.pokemon_salvaje, mov)
        self.pokemon_salvaje.recibir_danio(danio)

        # 4) Efectividad por separado
        ef = calcular_efectividad(mov.tipo, self.pokemon_salvaje.tipos)
        if ef > 1.5:
            mensajes.append(f"¡Es súper eficaz! ({danio} de daño)")
        elif ef > 1.0:
            mensajes.append(f"¡Es eficaz! ({danio} de daño)")
        elif ef == 0:
            mensajes.append("¡No afecta al rival!")
        elif ef < 1.0:
            mensajes.append(f"No es muy eficaz... ({danio})")

        # 5) Estado
        if self.pokemon_salvaje.ps <= 0:
            mensajes.append(f"¡{self.pokemon_salvaje.nombre} se debilitó!")

        self._flash_rival = 0.3
        return mensajes

    def _ejecutar_ataque_rival(self):
        mensajes = []
        if not self.pokemon_salvaje.movimientos:
            return mensajes

        mov = elegir_movimiento_ia(self.pokemon_salvaje,
                                   self.pokemon_activo_jugador,
                                   self.pokemon_salvaje.movimientos)
        if not mov:
            return mensajes

        mov.pp = max(0, mov.pp - 1)
        mensajes.append(f"¡El {self.pokemon_salvaje.nombre} rival usó {mov.nombre}!")

        if random.randint(1, 100) > mov.precision:
            mensajes.append("¡Pero falló!")
            return mensajes

        danio = calcular_danio(self.pokemon_salvaje, self.pokemon_activo_jugador, mov)
        self.pokemon_activo_jugador.recibir_danio(danio)

        ef = calcular_efectividad(mov.tipo, self.pokemon_activo_jugador.tipos)
        if ef > 1.5:
            mensajes.append(f"¡Es súper eficaz! ({danio} de daño)")
        elif ef > 1.0:
            mensajes.append(f"¡Es eficaz! ({danio} de daño)")
        elif ef == 0:
            mensajes.append("¡No te afecta!")
        elif ef < 1.0:
            mensajes.append(f"No es muy eficaz... ({danio})")

        if self.pokemon_activo_jugador.ps <= 0:
            mensajes.append(f"¡{self.pokemon_activo_jugador.nombre} se debilitó!")

        self._flash_jugador = 0.3
        return mensajes

    def _buscar_siguiente_vivo(self):
        for poke in self.equipo_jugador:
            if poke.esta_vivo() and poke is not self.pokemon_activo_jugador:
                return poke
        return None

    def intentar_huir(self):
        if self.es_gimnasio:
            return False, "¡No puedes huir de un combate de entrenador!"
        if random.random() < 0.7:
            self.terminada = True
            self.resultado = "huida"
            return True, "¡Huiste sin problemas!"
        return False, "¡No pudiste escapar!"


# =========================================================================
# SHINY
# =========================================================================
PROBABILIDAD_SHINY = 1 / 4096

COLORES_SHINY = {
    "Alpaka":    ((255, 220, 180), (200, 160, 120)),
    "Feligaro":  ((255, 200, 100), (240, 160, 60)),
    "Bufeito":   ((200, 220, 255), (150, 180, 220)),
    "Surito":    ((220, 240, 120), (180, 200, 80)),
    "Cuy":       ((255, 240, 220), (220, 200, 180)),
    "Chinchill": ((255, 255, 255), (220, 220, 240)),
    "Tunquid":   ((255, 220, 180), (220, 180, 140)),
}


def es_shiny():
    return random.random() < PROBABILIDAD_SHINY


def aplicar_shiny(pokemon, forzar=False):
    if forzar or es_shiny():
        pokemon.es_shiny = True
        pokemon.color_shiny = COLORES_SHINY.get(pokemon.nombre, None)
        return True
    pokemon.es_shiny = False
    pokemon.color_shiny = None
    return False


def obtener_colores_shiny(pokemon):
    if getattr(pokemon, "es_shiny", False):
        return getattr(pokemon, "color_shiny", None)
    return None
# FIX_DANO_VISIBLE
