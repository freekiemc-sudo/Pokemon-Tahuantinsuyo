# sistemas/mo_system.py
"""
Sistema de MOs (Máquinas Ocultas). Cada MO se desbloquea con medallas.
El juego comprueba qué MOs tienes activas para dejar pasar al jugador.
"""

MOS = {
    "Escalada Andina": {
        "descripcion": "Trepa muros de piedra sagrada y andenes.",
        "medalla_requerida": "Medalla Cantera",
    },
    "Navegación Fluvial": {
        "descripcion": "Surcar ríos, lagos y el mar.",
        "medalla_requerida": "Medalla Marea",
    },
    "Vaguada": {
        "descripcion": "Volar a ciudades ya visitadas.",
        "medalla_requerida": "Medalla Místico",
    },
    "Corte / Tala": {
        "descripcion": "Corta arbustos espinosos.",
        "medalla_requerida": "Medalla Liana",
    },
    "Golpe Roca": {
        "descripcion": "Rompe rocas pequeñas.",
        "medalla_requerida": "Medalla Arcilla",
    },
}


def mos_activas(gimnasios):
    """Devuelve un set con las MOs desbloqueadas según las medallas del jugador."""
    activas = set()
    medallas = set(getattr(gimnasios, "medallas_obtenidas", []))
    for mo, info in MOS.items():
        if info["medalla_requerida"] in medallas:
            activas.add(mo)
    return activas


def puede_usar_mo(gimnasios, nombre_mo):
    return nombre_mo in mos_activas(gimnasios)