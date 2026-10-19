# data/megas.py
# -*- coding: utf-8 -*-
"""E8: Mega Evoluciones con sabor andino."""

MEGA_FORMAS = {
    # Iniciales finales
    "Majestuyocc": {
        "nombre_mega": "Mega Majestuyocc",
        "tipos": ["Planta", "Acero"],
        "stats_boost": {"ps": 15, "atq": 30, "def": 25, "atq_esp": 20, "def_esp": 25, "vel": 20},
        "habilidad": "Alma Andina",
        "piedra": "Esmeralda Solar",
        "color_aura": (100, 240, 120),
        "descripcion": "El poder del Apu Wira-Titan fluye por sus venas doradas.",
    },
    "Incaflame": {
        "nombre_mega": "Mega Incaflame",
        "tipos": ["Fuego", "Dragon"],
        "stats_boost": {"ps": 15, "atq": 35, "def": 20, "atq_esp": 25, "def_esp": 20, "vel": 25},
        "habilidad": "Garra Solar",
        "piedra": "Rubi del Jaguar",
        "color_aura": (255, 160, 60),
        "descripcion": "El rugido del Sol Incaico se materializa en llamas sagradas.",
    },
    "Yacumist": {
        "nombre_mega": "Mega Yacumist",
        "tipos": ["Agua", "Dragon"],
        "stats_boost": {"ps": 20, "atq": 15, "def": 25, "atq_esp": 35, "def_esp": 20, "vel": 20},
        "habilidad": "Encanto Mistico",
        "piedra": "Zafiro del Delfin",
        "color_aura": (100, 180, 255),
        "descripcion": "Su cuerpo se vuelve translucido como el agua del Titicaca.",
    },
    # Legendario mega
    "Amaru": {
        "nombre_mega": "Mega Amaru",
        "tipos": ["Dragon", "Psiquico"],
        "stats_boost": {"ps": 20, "atq": 30, "def": 25, "atq_esp": 30, "def_esp": 25, "vel": 30},
        "habilidad": "Presion",
        "piedra": "Esmeralda del Amaru",
        "color_aura": (200, 240, 100),
        "descripcion": "El dragon celestial despliega alas de constelaciones puras.",
    },
}


# Piedras mega como objetos
PIEDRAS_MEGA = {
    "Esmeralda Solar":      ("Piedra mega para Majestuyocc", (100, 240, 120)),
    "Rubi del Jaguar":      ("Piedra mega para Incaflame", (255, 160, 60)),
    "Zafiro del Delfin":    ("Piedra mega para Yacumist", (100, 180, 255)),
    "Esmeralda del Amaru":  ("Piedra mega para Amaru", (200, 240, 100)),
}


def puede_mega_evolucionar(pokemon):
    """Devuelve los datos de mega si el Pokemon puede mega-evolucionar."""
    if not pokemon:
        return None
    mega = MEGA_FORMAS.get(pokemon.nombre)
    if not mega:
        return None
    # Verificar que lleva la piedra correcta
    if getattr(pokemon, "objeto_equipado", None) != mega["piedra"]:
        return None
    return mega


def aplicar_mega(pokemon):
    """Aplica mega-evolucion temporal a un Pokemon. Devuelve dict con info previa."""
    mega = puede_mega_evolucionar(pokemon)
    if not mega:
        return None
    # Guardar estado previo
    estado_previo = {
        "nombre": pokemon.nombre,
        "tipos": list(pokemon.tipos),
        "habilidad": pokemon.habilidad,
        "ps_base": pokemon.ps_base,
        "atq_base": pokemon.atq_base,
        "def_base": pokemon.def_base,
        "atq_esp_base": pokemon.atq_esp_base,
        "def_esp_base": pokemon.def_esp_base,
        "vel_base": pokemon.vel_base,
    }
    # Aplicar cambios
    boost = mega["stats_boost"]
    pokemon.nombre = mega["nombre_mega"]
    pokemon.tipos = mega["tipos"]
    pokemon.habilidad = mega["habilidad"]
    pokemon.ps_base += boost["ps"]
    pokemon.atq_base += boost["atq"]
    pokemon.def_base += boost["def"]
    pokemon.atq_esp_base += boost["atq_esp"]
    pokemon.def_esp_base += boost["def_esp"]
    pokemon.vel_base += boost["vel"]
    # Recalcular
    ps_antes_max = pokemon.ps_max
    pokemon._calcular_stats() if hasattr(pokemon, "_calcular_stats") else pokemon._calc_stats()
    # Dar PS extra
    pokemon.ps += (pokemon.ps_max - ps_antes_max)
    # Marcar
    pokemon._mega_activa = True
    pokemon._mega_estado_previo = estado_previo
    return estado_previo


def revertir_mega(pokemon):
    """Revierte la mega-evolucion al terminar la batalla."""
    if not getattr(pokemon, "_mega_activa", False):
        return
    prev = getattr(pokemon, "_mega_estado_previo", None)
    if not prev:
        return
    pokemon.nombre = prev["nombre"]
    pokemon.tipos = prev["tipos"]
    pokemon.habilidad = prev["habilidad"]
    pokemon.ps_base = prev["ps_base"]
    pokemon.atq_base = prev["atq_base"]
    pokemon.def_base = prev["def_base"]
    pokemon.atq_esp_base = prev["atq_esp_base"]
    pokemon.def_esp_base = prev["def_esp_base"]
    pokemon.vel_base = prev["vel_base"]
    pokemon._calcular_stats() if hasattr(pokemon, "_calcular_stats") else pokemon._calc_stats()
    pokemon._mega_activa = False
    pokemon._mega_estado_previo = None


print(f"OK data.megas ({len(MEGA_FORMAS)} mega formas)")
