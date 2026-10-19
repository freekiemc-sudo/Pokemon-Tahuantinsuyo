# sistemas/contenido_regional.py
from typing import Optional
"""
=====================================================================================
  CONTENIDO REGIONAL DEL TAHUANTINSUYO
  Movimientos, Habilidades, Bayas, MOs y Objetos exclusivos de la región.

  Extraído DIRECTAMENTE del LORE OFICIAL (doc "Lore Oficial de la Región Tahuantinsuyo").

  Uso desde main.py / batalla.py:
      from sistemas.contenido_regional import (
          MOVIMIENTOS_REGIONALES, HABILIDADES_REGIONALES,
          BAYAS_NATIVAS, MOS_REGIONALES, APRENDIZAJES_REGIONALES,
          crear_movimiento_regional, movimiento_de, habilidad_de,
          baya_de, mo_de, pokemon_aprende,
      )

  Todo el módulo es autocontenido: si batalla.py quiere usarlo, sólo importa
  `crear_movimiento_regional` y mete el Movimiento resultante en `pokemon.movimientos`.
=====================================================================================
"""

# =====================================================================================
# 1) MOVIMIENTOS CARACTERÍSTICOS (Ataques Propios de la Región)
# =====================================================================================
# Formato compatible con sistemas.batalla.Movimiento:
#   {nombre, tipo, potencia, precision, categoria, pp}
# Se añaden metadatos (efecto, prioridad, usuario_probable) para que batalla.py
# pueda aplicar efectos especiales cuando quiera (no rompe nada si los ignora).

MOVIMIENTOS_REGIONALES = {

    "Silbido de Huaco": {
        "nombre": "Silbido de Huaco",
        "tipo": "Fantasma",
        "potencia": 60,
        "precision": 100,
        "categoria": "Especial",
        "pp": 15,
        "prioridad": 0,
        # Lore: "Tiene alta probabilidad de dejar confundido al objetivo."
        "efecto": {"estado": "confundido", "probabilidad": 0.55},
        "usuario_probable": ["Huacotrato", "Pututos", "Jarjacha", "Llama Espectral",
                             "Tunche", "Khamuy-Mist", "Quipus", "Perro Sin Pelo"],
        "descripcion": "Emite un sonido ancestral que desconcierta al rival.",
    },

    "Danza de Tijeras": {
        "nombre": "Danza de Tijeras",
        "tipo": "Lucha",
        "potencia": 80,
        "precision": 100,
        "categoria": "Físico",
        "pp": 10,
        "prioridad": 0,
        # Lore: "Siempre da golpe crítico si el usuario es más rápido que el rival."
        "efecto": {"critico_si_mas_rapido": True},
        "usuario_probable": ["Danza de Tijeras", "Cuyzard", "Simiochuro",
                             "Ursandino", "Chinchay", "Bronce-Tari"],
        "descripcion": "Un combo rápido de cortes afilados que imita el ritmo tradicional.",
    },

    "Erupción de Rocoto": {
        "nombre": "Erupción de Rocoto",
        "tipo": "Fuego",
        "potencia": 90,
        "precision": 85,
        "categoria": "Especial",
        "pp": 10,
        "prioridad": 0,
        # Lore: "Quema al rival con 50% de probabilidad. Si el usuario recibe
        # daño físico antes de atacar, quema al atacante por el ardor."
        "efecto": {
            "estado": "quemado", "probabilidad": 0.50,
            "quema_al_atacante_si_golpeado_antes": True,
        },
        "usuario_probable": ["Picantox", "Incaflame", "Vulandino", "Chinchay",
                             "Torito de Pucará", "Inti-Can"],
        "descripcion": "Lanza una bola de fuego picante que arde sin piedad.",
    },

    "Mordisco Glaciar": {
        "nombre": "Mordisco Glaciar",
        "tipo": "Hielo",
        "potencia": 75,
        "precision": 100,
        "categoria": "Físico",
        "pp": 15,
        "prioridad": 0,
        # Lore: "Reduce la Velocidad del objetivo en un nivel."
        "efecto": {"bajar_stat": ("vel", 1), "probabilidad": 1.0},
        "usuario_probable": ["Papa Chuño", "Zorro de las Nieves Altas", "Killa-Puma",
                             "Chinchay", "Ursandino", "Tarascom"],
        "descripcion": "Ataque gélido propio de la alta cordillera.",
    },

    "Eco del Amaru": {
        "nombre": "Eco del Amaru",
        "tipo": "Dragón",
        "potencia": 140,
        "precision": 90,
        "categoria": "Especial",
        "pp": 5,
        "prioridad": 0,
        # Lore: "Daño masivo pero obliga a descansar el turno siguiente."
        "efecto": {"recarga": 1},
        "usuario_probable": ["Amaru", "Yacumama", "Serpior", "Tarascom", "Dracuy"],
        "descripcion": "El movimiento definitivo del Pokémon supremo del Tahuantinsuyo.",
    },

    # Extras con sabor regional que complementan el catálogo del doc:
    "Impulso Andino": {
        "nombre": "Impulso Andino", "tipo": "Normal", "potencia": 60,
        "precision": 100, "categoria": "Físico", "pp": 20, "prioridad": 0,
        "efecto": None,
        "usuario_probable": ["Alpaka", "Vicuñor", "Majestuyocc", "Llama Solar",
                             "Llama Lunar", "Aruy"],
        "descripcion": "Una embestida con la fuerza del altiplano.",
    },
    "Cascada Andina": {
        "nombre": "Cascada Andina", "tipo": "Agua", "potencia": 80,
        "precision": 100, "categoria": "Físico", "pp": 15, "prioridad": 0,
        "efecto": None,
        "usuario_probable": ["Yacumist", "Bufeo Colorado", "Carachama",
                             "Pirañatox", "Sachavaca Titán"],
        "descripcion": "Como un río que cae desde la cordillera.",
    },
    "Alud Andino": {
        "nombre": "Alud Andino", "tipo": "Roca", "potencia": 120,
        "precision": 85, "categoria": "Físico", "pp": 5, "prioridad": 0,
        "efecto": None,
        "usuario_probable": ["Wira-Titan", "Apu-Cerro", "Montazcach", "Tarascom"],
        "descripcion": "Un derrumbe de piedras sagradas del Apu.",
    },
    "Llamado Ancestral": {
        "nombre": "Llamado Ancestral", "tipo": "Sonido", "potencia": 80,
        "precision": 100, "categoria": "Especial", "pp": 15, "prioridad": 0,
        "efecto": {"bajar_stat": ("atq_esp", 1), "probabilidad": 0.35},
        "usuario_probable": ["Pututos"],
        "descripcion": "El caracol ceremonial resuena por los valles.",
    },
    "Alarido Andino": {
        "nombre": "Alarido Andino", "tipo": "Sonido", "potencia": 90,
        "precision": 100, "categoria": "Especial", "pp": 10, "prioridad": 0,
        "efecto": {"estado": "paralizado", "probabilidad": 0.20},
        "usuario_probable": ["Pututos"],
        "descripcion": "Un grito que paraliza como el eco de un cerro.",
    },
    "Foco Resplandor": {
        "nombre": "Foco Resplandor", "tipo": "Acero", "potencia": 80,
        "precision": 100, "categoria": "Especial", "pp": 10, "prioridad": 0,
        "efecto": None,
        "usuario_probable": ["Tumignus", "Muquimetal", "Aurum-Inca",
                             "Argentum-Moon", "Bronce-Tari"],
        "descripcion": "Un destello dorado forjado por los orfebres incas.",
    },
    "Lluvia Solar": {
        "nombre": "Lluvia Solar", "tipo": "Planta", "potencia": 120,
        "precision": 85, "categoria": "Especial", "pp": 5, "prioridad": 0,
        "efecto": {"recarga": 0},
        "usuario_probable": ["Majestuyocc", "Simiochuro", "Pach-Avis",
                             "Pachamama-Prime", "Chullachaqui", "Orquídea Negra"],
        "descripcion": "Rallos de luz andina nutren la vida vegetal.",
    },
    "Hidrobomba Mística": {
        "nombre": "Hidrobomba Mística", "tipo": "Agua", "potencia": 120,
        "precision": 80, "categoria": "Especial", "pp": 5, "prioridad": 0,
        "efecto": None,
        "usuario_probable": ["Yacumama", "Yacumist", "Bufeo Colorado",
                             "Lago-Sagu", "Paria-Rain", "Sachavaca Titán"],
        "descripcion": "Una esfera de agua cargada con la energía del Titicaca.",
    },
}


# =====================================================================================
# 2) HABILIDADES NUEVAS (Pasivas de Combate)
# =====================================================================================
# Formato: {id: {nombre, descripcion, efecto}}
# batalla.py puede consultar `pokemon.habilidad` y llamar `aplicar_habilidad(...)`.
# Por ahora dejamos los datos y un stub de efectos para que no rompa nada.

HABILIDADES_REGIONALES = {
    "camuflaje_andino": {
        "id": "camuflaje_andino",
        "nombre": "Camuflaje Andino",
        "descripcion": ("Cambia el tipo secundario o potencia movimientos de Roca/Tierra/Hielo "
                        "según el terreno o clima del combate (niebla, ventisca, montaña)."),
        "efecto": {"potenciar_tipos": ["Roca", "Tierra", "Hielo"],
                   "multiplicador": 1.30,
                   "condicion": ["niebla", "ventisca", "montaña"]},
    },
    "calor_costeno": {
        "id": "calor_costeno",
        "nombre": "Calor Costeño",
        "descripcion": ("Bajo sol intenso o humedad extrema, el Pokémon recupera "
                        "1/16 de sus PS máximos al final de cada turno."),
        "efecto": {"curacion_turno": 1 / 16,
                   "condicion": ["sol", "humedad_extrema"]},
    },
    "espiritu_de_apu": {
        "id": "espiritu_de_apu",
        "nombre": "Espíritu de Apu",
        "descripcion": ("Cuando los PS caen por debajo del 25%, el Ataque y el Ataque Especial "
                        "aumentan drásticamente (versión regional de Poder Pasado)."),
        "efecto": {"umbral_ps": 0.25,
                   "multiplicador_atq": 1.5,
                   "multiplicador_atq_esp": 1.5},
    },
    "veneno_amazonico": {
        "id": "veneno_amazonico",
        "nombre": "Veneno Amazónico",
        "descripcion": ("Los ataques de contacto tienen 30% de probabilidad de infligir "
                        "Envenenamiento Grave (Tóxico) en lugar de normal."),
        "efecto": {"probabilidad": 0.30, "estado": "toxico"},
    },
}


# =====================================================================================
# 3) BAYAS NATIVAS (reemplazo de las clásicas)
# =====================================================================================

BAYAS_NATIVAS = {
    "Aguaymanto": {
        "nombre": "Aguaymanto",
        "tipo": "curacion",
        "descripcion": "Cura estados alterados y restaura 20 PS.",
        "precio": 250,
        "efecto": {"curar_estado": True, "curar_ps": 20},
    },
    "Lúcuma": {
        "nombre": "Lúcuma",
        "tipo": "curacion",
        "descripcion": "Restaura la mitad de los PS cuando el usuario baja del 25%.",
        "precio": 400,
        "efecto": {"curacion_auto_umbral": 0.25, "curar_ps_pct": 0.50},
    },
    "Camu Camu": {
        "nombre": "Camu Camu",
        "tipo": "batalla",
        "descripcion": "Sube la Defensa Especial al recibir un ataque supereficaz.",
        "precio": 450,
        "efecto": {"subir_stat_al_recibir_supereficaz": ("def_esp", 1)},
    },
    "Coca Sagrada": {
        "nombre": "Coca Sagrada",
        "tipo": "utilidad",
        "descripcion": "Evita el cansancio y la pérdida de precisión en alta montaña.",
        "precio": 600,
        "efecto": {"inmunidad_cansancio": True, "inmunidad_precision": True},
    },
}


# =====================================================================================
# 4) MÁQUINAS OCULTAS REGIONALES (MOs)
# =====================================================================================

MOS_REGIONALES = {
    "MO01": {
        "id": "MO01",
        "nombre": "Escalada Andina",
        "uso": "Trepar muros de piedra sagrada, andenes empinados y riscos verticales.",
        "requisito_medalla": "Medalla Cantera",
        "pokemon_sugeridos": ["Vizcachin", "Montazcach", "Ursandino", "Chinchay"],
    },
    "MO02": {
        "id": "MO02",
        "nombre": "Navegación Fluvial",
        "uso": "Surcar ríos caudalosos de la Ceja de Selva y el Lago Titicaca.",
        "requisito_medalla": "Medalla Marea",
        "pokemon_sugeridos": ["Bufeo Colorado", "Carachama", "Tapirex",
                              "Sachavaca Titán", "Yacumist"],
    },
    "MO03": {
        "id": "MO03",
        "nombre": "Vaguada",
        "uso": "Volar montado sobre un Tunquialt o un Apucondor a ciudades visitadas.",
        "requisito_medalla": "Medalla Místico",
        "pokemon_sugeridos": ["Tunquialt", "Apucondor", "Wayra-Wind", "Chask-Messenger"],
    },
    "MO04": {
        "id": "MO04",
        "nombre": "Corte / Tala",
        "uso": "Abrir paso entre matorrales de la costa y pajonales altos.",
        "requisito_medalla": "Medalla Liana",
        "pokemon_sugeridos": ["Mantis-Búho", "Danza de Tijeras", "Simiochuro",
                              "Tigrillo", "Chinchay"],
    },
}


# =====================================================================================
# 5) APRENDIZAJES REGIONALES
# =====================================================================================
# Por nivel: al alcanzar el nivel, el Pokémon aprende el movimiento (si no lo tiene).
# Formato: {nombre_pokemon: [(nivel, nombre_movimiento), ...]}

APRENDIZAJES_REGIONALES = {
    # Iniciales
    "Alpaka":       [(12, "Impulso Andino")],
    "Vicuñor":      [(20, "Impulso Andino"), (28, "Mordisco Glaciar")],
    "Majestuyocc":  [(40, "Lluvia Solar"), (48, "Alud Andino")],

    "Feligaro":     [(12, "Erupción de Rocoto")],
    "Jaguaris":     [(22, "Erupción de Rocoto"), (30, "Danza de Tijeras")],
    "Incaflame":    [(44, "Erupción de Rocoto"), (52, "Eco del Amaru")],

    "Bufeito":      [(12, "Cascada Andina")],
    "Rosadelf":     [(22, "Cascada Andina"), (30, "Hidrobomba Mística")],
    "Yacumist":     [(44, "Hidrobomba Mística"), (55, "Eco del Amaru")],

    # Fauna de ruta
    "Cuyzard":      [(30, "Danza de Tijeras")],
    "Simiochuro":   [(32, "Danza de Tijeras"), (45, "Lluvia Solar")],
    "Chinchill":    [(18, "Impulso Andino")],
    "Chinchicab":   [(30, "Danza de Tijeras")],
    "Sachavaca Titán": [(40, "Cascada Andina"), (50, "Hidrobomba Mística")],
    "Pirañatox":    [(28, "Cascada Andina")],
    "Ursandino":    [(35, "Danza de Tijeras")],
    "Chinchay":     [(35, "Danza de Tijeras"), (45, "Erupción de Rocoto")],
    "Apucondor":    [(38, "Impulso Andino")],

    # Tuberculos y espiritus
    "Papa Chuño":   [(28, "Mordisco Glaciar")],
    "Papa Desértica": [(28, "Alud Andino")],
    "Papa Selvática": [(28, "Cascada Andina")],
    "Llama Solar":  [(30, "Erupción de Rocoto")],
    "Llama Lunar":  [(30, "Mordisco Glaciar")],
    "Llama Espectral": [(30, "Silbido de Huaco")],
    "Aruy":         [(24, "Silbido de Huaco")],

    # Objetos / mitos
    "Huacotrato":   [(26, "Silbido de Huaco")],
    "Jarjacha":     [(30, "Silbido de Huaco")],
    "Pututos":      [(24, "Llamado Ancestral"), (34, "Alarido Andino")],
    "Quipus":       [(28, "Silbido de Huaco")],
    "Tumignus":     [(30, "Foco Resplandor")],
    "Muquimetal":   [(30, "Foco Resplandor")],
    "Tarascom":     [(38, "Mordisco Glaciar"), (50, "Eco del Amaru")],
    "Orquídea Negra": [(36, "Lluvia Solar")],
    "Torito de Pucará": [(30, "Erupción de Rocoto")],

    # Supremos
    "Dracuy":       [(20, "Mordisco Glaciar")],
    "Serpior":      [(35, "Mordisco Glaciar"), (45, "Eco del Amaru")],
    "Amaru":        [(30, "Eco del Amaru"), (50, "Alud Andino")],
    "Yacumama":     [(30, "Hidrobomba Mística"), (50, "Eco del Amaru")],
    "Wira-Titan":   [(50, "Alud Andino")],
    "Supay-Dread":  [(50, "Silbido de Huaco")],
    "Pachamama-Prime": [(50, "Lluvia Solar")],
    "Inti-Can":     [(50, "Erupción de Rocoto")],
    "Killa-Puma":   [(50, "Mordisco Glaciar")],
    "Pach-Avis":    [(50, "Lluvia Solar")],
    "Aurum-Inca":   [(50, "Foco Resplandor")],
    "Argentum-Moon": [(50, "Foco Resplandor")],
    "Bronce-Tari":  [(50, "Danza de Tijeras")],
    "Wayra-Wind":   [(50, "Impulso Andino")],
    "Paria-Rain":   [(50, "Hidrobomba Mística")],
    "Khamuy-Mist":  [(50, "Silbido de Huaco")],
    "Apu-Cerro":    [(50, "Alud Andino")],
    "Lago-Sagu":    [(50, "Hidrobomba Mística")],
    "Chask-Messenger": [(50, "Impulso Andino")],
    "Omega-Inca":   [(70, "Eco del Amaru")],
}


# =====================================================================================
# 6) CONSULTAS RÁPIDAS
# =====================================================================================

def movimiento_de(nombre: str) ->Optional[dict]:
    """Devuelve el dict (con efecto y metadatos) de un movimiento regional."""
    return MOVIMIENTOS_REGIONALES.get(nombre)


def habilidad_de(pid: str) ->Optional[dict]:
    """Devuelve el dict de una habilidad regional por su id."""
    return HABILIDADES_REGIONALES.get(pid)


def baya_de(nombre: str) ->Optional[dict]:
    """Devuelve el dict de una baya nativa."""
    return BAYAS_NATIVAS.get(nombre)


def mo_de(mid: str) ->Optional[dict]:
    """Devuelve el dict de una MO regional por su id ('MO01', 'MO02', ...)."""
    return MOS_REGIONALES.get(mid)


def pokemon_aprende(nombre: str, nivel: int) -> list[str]:
    """
    Devuelve la lista de movimientos regionales que un Pokémon aprende
    exactamente al subir a `nivel` (lista vacía si no aprende nada).
    """
    aprendidos = []
    for nv, mov in APRENDIZAJES_REGIONALES.get(nombre, []):
        if nv == nivel:
            aprendidos.append(mov)
    return aprendidos


def movimientos_regionales_de(nombre: str) -> list[str]:
    """Todos los movimientos regionales que puede aprender ese Pokémon."""
    return [m for _, m in APRENDIZAJES_REGIONALES.get(nombre, [])]


# =====================================================================================
# 7) ENGANCHAR CON sistemas.batalla.Movimiento
# =====================================================================================

def crear_movimiento_regional(nombre: str):
    """
    Devuelve una instancia de sistemas.batalla.Movimiento lista para meter en
    `pokemon.movimientos`. Devuelve None si el nombre no existe.
    """
    datos = MOVIMIENTOS_REGIONALES.get(nombre)
    if not datos:
        return None
    try:
        from sistemas.batalla import Movimiento  # import diferido para evitar ciclos
    except Exception:
        return None
    # Movimiento espera {nombre, tipo, potencia, precision, categoria, pp}
    return Movimiento({
        "nombre": datos["nombre"],
        "tipo": datos["tipo"],
        "potencia": datos["potencia"],
        "precision": datos["precision"],
        "categoria": datos["categoria"],
        "pp": datos["pp"],
    })


def enganchar_aprendizaje(pokemon) -> list[str]:
    """
    Si `pokemon` acaba de subir de nivel, esta función mira la tabla regional y
    mete los movimientos que correspondan (respetando el tope de 4). Devuelve
    la lista de nombres aprendidos. Es seguro llamarla aunque el Pokémon no
    tenga nada que aprender.
    """
    aprendidos = pokemon_aprende(pokemon.nombre, pokemon.nivel)
    if not aprendidos:
        return []
    ya_tiene = {getattr(m, "nombre", "") for m in pokemon.movimientos}
    realmente = []
    for nv in aprendidos:
        if nv in ya_tiene:
            continue
        mov = crear_movimiento_regional(nv)
        if mov is None:
            continue
        if len(pokemon.movimientos) < 4:
            pokemon.movimientos.append(mov)
        else:
            # reemplaza el movimiento más débil (heurística simple)
            peor_idx, peor_pow = 0, 10 ** 9
            for i, m in enumerate(pokemon.movimientos):
                pow_ = getattr(m, "potencia", 0) or 0
                if pow_ < peor_pow:
                    peor_pow, peor_idx = pow_, i
            pokemon.movimientos[peor_idx] = mov
        realmente.append(nv)
    return realmente


# =====================================================================================
# 8) EFECTOS GENÉRICOS (para que batalla.py los pueda aplicar cuando quiera)
# =====================================================================================

def aplicar_efecto_movimiento(mov_datos: dict, atacante, defensor, *,
                              defensor_golpeo_antes: bool = False,
                              atacante_mas_rapido: bool = False) -> list[str]:
    """
    Aplica el efecto regional del movimiento (estado, baja de stats, crítico
    asegurado, recarga, quema al atacante…). Devuelve una lista de mensajes
    para que batalla.py los añada al log del turno.

    No asume nada del sistema de batalla: sólo modifica atributos simples
    (`.estado`, `.turnos_estado`, `.defensa`, `.vel`, `.atq_esp`, `.recarga`).
    Todo es defensivo (getattr/setattr) para no romper si algo no existe.
    """
    msgs = []
    if not mov_datos:
        return msgs
    ef = mov_datos.get("efecto") or {}

    # --- Estado alterado (confundido, quemado, paralizado, tóxico) ---
    if "estado" in ef:
        import random as _r
        if _r.random() < ef.get("probabilidad", 1.0):
            setattr(defensor, "estado", ef["estado"])
            setattr(defensor, "turnos_estado", 3)
            msgs.append(f"¡{getattr(defensor, 'nombre', '?')} quedó {ef['estado']}!")

    # --- Reducir stats ---
    if "bajar_stat" in ef:
        stat, grados = ef["bajar_stat"]
        if hasattr(defensor, stat):
            actual = getattr(defensor, stat)
            setattr(defensor, stat, max(1, int(actual * (1 - 0.15 * grados))))
            msgs.append(f"¡La {stat} de {getattr(defensor, 'nombre', '?')} bajó!")

    # --- Golpe crítico asegurado si el usuario es más rápido ---
    if ef.get("critico_si_mas_rapido") and atacante_mas_rapido:
        setattr(atacante, "_critico_seguro_este_turno", True)
        msgs.append("¡El ritmo perfecto del danzante asegura el impacto crítico!")

    # --- Recarga: el usuario descansa el turno siguiente ---
    if "recarga" in ef:
        setattr(atacante, "_turnos_recarga", ef["recarga"])
        msgs.append(f"¡{getattr(atacante, 'nombre', '?')} debe descansar tras el golpe!")

    # --- Quema al atacante si el defensor golpeó antes ---
    if ef.get("quema_al_atacante_si_golpeado_antes") and defensor_golpeo_antes:
        setattr(defensor, "estado", "quemado")
        setattr(defensor, "turnos_estado", 3)
        msgs.append(f"¡El ardor del rocoto quema a {getattr(defensor, 'nombre', '?')}!")

    return msgs


def aplicar_habilidad_regional(habilidad_id: str, pokemon, *, contexto: dict | None = None) -> dict:
    """
    Devuelve un dict con las modificaciones que el llamante puede aplicar:
        {"multiplicadores": {...}, "curacion_ps": int, "mensajes": [...]}
    `contexto` puede llevar cosas como {"clima": "sol", "hps_pct": 0.20, ...}.
    No muta al Pokémon por sí sola: sólo describe lo que debería pasar.
    """
    h = HABILIDADES_REGIONALES.get(habilidad_id)
    out = {"multiplicadores": {}, "curacion_ps": 0, "mensajes": []}
    if not h:
        return out
    ef = h.get("efecto", {})
    ctx = contexto or {}

    if habilidad_id == "camuflaje_andino":
        if ctx.get("clima") in ef.get("condicion", []):
            out["multiplicadores"]["tipos_potenciados"] = ef["potenciar_tipos"]
            out["multiplicadores"]["multiplicador"] = ef["multiplicador"]
            out["mensajes"].append(f"¡{pokemon.nombre} se camufla con el terreno!")

    elif habilidad_id == "calor_costeno":
        if ctx.get("clima") in ef.get("condicion", []):
            out["curacion_ps"] = max(1, int(pokemon.ps_max * ef["curacion_turno"]))
            out["mensajes"].append(f"¡{pokemon.nombre} recupera energía del sol!")

    elif habilidad_id == "espiritu_de_apu":
        hps_pct = ctx.get("hps_pct", pokemon.ps / max(1, pokemon.ps_max))
        if hps_pct < ef["umbral_ps"]:
            out["multiplicadores"]["atq"] = ef["multiplicador_atq"]
            out["multiplicadores"]["atq_esp"] = ef["multiplicador_atq_esp"]
            out["mensajes"].append(f"¡El Apu despierta en {pokemon.nombre}!")

    elif habilidad_id == "veneno_amazonico":
        if ctx.get("contacto_fisico"):
            out["multiplicadores"]["prob_estado"] = ef["probabilidad"]
            out["multiplicadores"]["estado"] = ef["estado"]
    return out


# =====================================================================================
# 9) AUTO-CHECK (útil en desarrollo, inocuo en producción)
# =====================================================================================

if __name__ == "__main__":
    print(f"Movimientos regionales:   {len(MOVIMIENTOS_REGIONALES)}")
    print(f"Habilidades regionales:   {len(HABILIDADES_REGIONALES)}")
    print(f"Bayas nativas:            {len(BAYAS_NATIVAS)}")
    print(f"MOs regionales:           {len(MOS_REGIONALES)}")
    print(f"Pokémon con aprendizajes: {len(APRENDIZAJES_REGIONALES)}")
    print()
    print("Ejemplo:", movimiento_de("Eco del Amaru")["descripcion"])
    print("Ejemplo:", habilidad_de("espiritu_de_apu")["descripcion"])
    print("Ejemplo:", "Amaru aprende:", movimientos_regionales_de("Amaru"))