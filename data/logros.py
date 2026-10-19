# data/logros.py
# -*- coding: utf-8 -*-
"""D6: Sistema de logros desbloqueables."""


class Logro:
    def __init__(self, id, nombre, descripcion, categoria, objetivo, meta=1):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.categoria = categoria  # captura, batalla, exploracion, historia, especial
        self.objetivo = objetivo     # clave de stats a chequear
        self.meta = meta
        self.desbloqueado = False
        self.fecha = None


LOGROS = {
    # ----- CAPTURA -----
    "primer_pokemon": Logro("primer_pokemon", "Primer Compañero",
        "Captura tu primer Pokemon salvaje.", "captura", "capturas", 1),
    "capturador_novato": Logro("capturador_novato", "Capturador Novato",
        "Captura 10 Pokemon.", "captura", "capturas", 10),
    "coleccionista": Logro("coleccionista", "Coleccionista",
        "Captura 50 Pokemon.", "captura", "capturas", 50),
    "pokedex_completa": Logro("pokedex_completa", "Maestro del Tahuantinsuyo",
        "Captura los 103 Pokemon.", "captura", "capturas", 103),
    "equipo_completo": Logro("equipo_completo", "Equipo Completo",
        "Ten 6 Pokemon en tu equipo.", "captura", "equipo_lleno", 1),

    # ----- BATALLA -----
    "primera_victoria": Logro("primera_victoria", "Primera Sangre",
        "Gana tu primer combate.", "batalla", "batallas_ganadas", 1),
    "guerrero": Logro("guerrero", "Guerrero Andino",
        "Gana 25 combates.", "batalla", "batallas_ganadas", 25),
    "veterano": Logro("veterano", "Veterano de los Apus",
        "Gana 100 combates.", "batalla", "batallas_ganadas", 100),
    "leyenda": Logro("leyenda", "Leyenda del Tahuantinsuyo",
        "Gana 250 combates.", "batalla", "batallas_ganadas", 250),
    "primer_entrenador": Logro("primer_entrenador", "Rival Vencido",
        "Vence a tu primer entrenador de ruta.", "batalla", "entrenadores_vencidos", 1),
    "cazador_entrenadores": Logro("cazador_entrenadores", "Cazador de Entrenadores",
        "Vence a 20 entrenadores.", "batalla", "entrenadores_vencidos", 20),
    "sin_debilitados": Logro("sin_debilitados", "Perfecto",
        "Gana un combate sin que ningun Pokemon se debilite.", "batalla", "combate_perfecto", 1),

    # ----- EXPLORACION -----
    "explorador": Logro("explorador", "Explorador Andino",
        "Recorre 1000 pasos.", "exploracion", "pasos", 1000),
    "caminante": Logro("caminante", "Caminante de los Andes",
        "Recorre 5000 pasos.", "exploracion", "pasos", 5000),
    "viajero": Logro("viajero", "Viajero Eterno",
        "Recorre 20000 pasos.", "exploracion", "pasos", 20000),
    "primera_visita_selva": Logro("primera_visita_selva", "Selva Virgen",
        "Visita la selva por primera vez.", "exploracion", "visito_selva", 1),
    "primera_visita_nieve": Logro("primera_visita_nieve", "Cumbres Heladas",
        "Visita un nevado por primera vez.", "exploracion", "visito_nieve", 1),
    "primera_visita_capital": Logro("primera_visita_capital", "Cosmopolita",
        "Llega a la Ciudad Capital.", "exploracion", "visito_capital", 1),

    # ----- HISTORIA -----
    "primera_medalla": Logro("primera_medalla", "Primera Medalla",
        "Gana tu primera medalla de gimnasio.", "historia", "medallas", 1),
    "cinco_medallas": Logro("cinco_medallas", "Medio Camino",
        "Gana 5 medallas.", "historia", "medallas", 5),
    "ocho_medallas": Logro("ocho_medallas", "Camino Completo",
        "Gana las 8 medallas.", "historia", "medallas", 8),
    "detuvo_supay": Logro("detuvo_supay", "Heroe del Tahuantinsuyo",
        "Deten al Team Supay en 5 ciudades.", "historia", "supay_derrotados", 5),
    "campeon": Logro("campeon", "Campeon del Tahuantinsuyo",
        "Vence al Campeon de la Liga.", "historia", "es_campeon", 1),

    # ----- ESPECIALES -----
    "shiny_cazador": Logro("shiny_cazador", "Cazador de Brillos",
        "Encuentra un Pokemon Shiny.", "especial", "shiny_encontrado", 1),
    "nivel_50": Logro("nivel_50", "Nivel 50",
        "Sube un Pokemon al nivel 50.", "especial", "nivel_max", 50),
    "nivel_100": Logro("nivel_100", "Maestro de Combate",
        "Sube un Pokemon al nivel 100.", "especial", "nivel_max", 100),
    "rico": Logro("rico", "Millonario",
        "Acumula 50.000 soles.", "especial", "dinero_max", 50000),
    "evolucionador": Logro("evolucionador", "Evolucionador",
        "Evoluciona 10 Pokemon.", "especial", "evoluciones", 10),
    "amistad_max": Logro("amistad_max", "Mejor Amigo",
        "Ten un Pokemon con amistad maxima (255).", "especial", "amistad_max", 1),
    "capturador_shiny": Logro("capturador_shiny", "Suerte Dorada",
        "Captura un Pokemon Shiny.", "especial", "shiny_capturado", 1),
    "critico_10": Logro("critico_10", "Golpeador",
        "Consigue 10 golpes criticos.", "especial", "criticos", 10),
    "sin_huir": Logro("sin_huir", "Sin Miedo",
        "Completa el juego sin huir de un combate.", "especial", "huidas", 0),
}


class SistemaLogros:
    def __init__(self):
        self.desbloqueados = {}  # {id: timestamp}
        self.stats_internos = {
            "combate_perfecto": 0,
            "visito_selva": 0,
            "visito_nieve": 0,
            "visito_capital": 0,
            "supay_derrotados": 0,
            "shiny_encontrado": 0,
            "shiny_capturado": 0,
            "nivel_max": 0,
            "dinero_max": 0,
            "evoluciones": 0,
            "amistad_max": 0,
            "criticos": 0,
            "huidas": 0,
            "equipo_lleno": 0,
            "es_campeon": 0,
        }
        self._nuevos_pendientes = []  # para mostrar notificacion

    def chequear(self, juego):
        """Verifica todos los logros. Devuelve lista de nuevos desbloqueados."""
        import time
        nuevos = []
        for logro in LOGROS.values():
            if logro.id in self.desbloqueados:
                continue
            valor = 0
            # Buscar en stats de partida
            if hasattr(juego, "_stats_partida"):
                valor = juego._stats_partida.get(logro.objetivo, valor)
            # Buscar en stats internos
            if logro.objetivo in self.stats_internos:
                valor = max(valor, self.stats_internos[logro.objetivo])
            # Buscar en otras fuentes
            try:
                if logro.objetivo == "medallas":
                    valor = juego.gimnasios.cantidad_medallas()
                elif logro.objetivo == "capturas":
                    valor = juego.pokedex.total_capturados()
                elif logro.objetivo == "entrenadores_vencidos":
                    valor = len(juego.gimnasios.lideres_derrotados)
                elif logro.objetivo == "dinero_max":
                    valor = max(valor, juego.inventario.dinero)
                elif logro.objetivo == "es_campeon":
                    valor = 1 if getattr(juego.liga, "es_campeon", False) else 0
                elif logro.objetivo == "equipo_lleno":
                    valor = 1 if len(juego.equipo.pokemons) >= 6 else 0
                elif logro.objetivo == "nivel_max":
                    max_nv = max((p.nivel for p in juego.equipo.pokemons), default=0)
                    valor = max(valor, max_nv)
                elif logro.objetivo == "amistad_max":
                    valor = 1 if any(getattr(p, "amistad", 0) >= 250 for p in juego.equipo.pokemons) else 0
            except Exception:
                pass
            # Verificar
            if logro.objetivo == "huidas":
                # Logro invertido: sin huir
                if valor == 0 and juego._stats_partida.get("batallas_ganadas", 0) >= 10:
                    logro.desbloqueado = True
                    logro.fecha = time.time()
                    self.desbloqueados[logro.id] = time.time()
                    nuevos.append(logro)
            elif valor >= logro.meta:
                logro.desbloqueado = True
                logro.fecha = time.time()
                self.desbloqueados[logro.id] = time.time()
                nuevos.append(logro)
        if nuevos:
            self._nuevos_pendientes.extend(nuevos)
        return nuevos

    def pop_nuevo(self):
        if self._nuevos_pendientes:
            return self._nuevos_pendientes.pop(0)
        return None

    def total(self):
        return len(LOGROS)

    def cantidad(self):
        return len(self.desbloqueados)

    def progreso(self):
        return self.cantidad() / max(1, self.total())


print(f"OK data.logros ({len(LOGROS)} logros)")
