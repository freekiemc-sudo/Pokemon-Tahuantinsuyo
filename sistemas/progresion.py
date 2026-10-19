# sistemas/progresion.py
"""
Sistema de progresión regional: obliga al jugador a vencer gimnasios
en orden antes de avanzar a la siguiente zona.
"""

ORDEN_MUNDO = [
    "caleta_norte",
    "ruta_1",
    "ciudad_moche",
    "ruta_2",
    "puerto_ancon",
    "ruta_3",
    "andahuaylas",
    "ruta_4",
    "ciudad_imperial",
    "ruta_5",
    "puno",
    "ruta_6",
    "huaraz",
    "ruta_7",
    "puerto_selva",
    "ruta_8",
    "ciudad_capital",
]

CIUDAD_A_GIMNASIO = {
    "ciudad_moche":    "gimnasio_moche",
    "puerto_ancon":    "gimnasio_ancon",
    "andahuaylas":     "gimnasio_andahuaylas",
    "ciudad_imperial": "gimnasio_imperial",
    "puno":            "gimnasio_puno",
    "huaraz":          "gimnasio_huaraz",
    "puerto_selva":    "gimnasio_selva",
    "ciudad_capital":  "gimnasio_capital",
}

LIDER_POR_CIUDAD = {
    "ciudad_moche":    "Don Fermín",
    "puerto_ancon":    "Capitán Chata",
    "andahuaylas":     "Wayra",
    "ciudad_imperial": "Apu-Capataz",
    "puno":            "Yatiri Mama",
    "huaraz":          "Nieves",
    "puerto_selva":    "Dr. Osho",
    "ciudad_capital":  "Ingeniero Aza",
}


def gym_derrotado(sistema_gimnasios, id_gimnasio):
    return id_gimnasio in getattr(sistema_gimnasios, "lideres_derrotados", [])


def puede_avanzar_a(id_destino, sistema_gimnasios):
    """Devuelve (True, '') si se puede entrar. Si no, (False, motivo)."""
    if id_destino not in ORDEN_MUNDO:
        return True, ""
    idx = ORDEN_MUNDO.index(id_destino)
    for i in range(idx):
        id_at = ORDEN_MUNDO[i]
        if id_at in CIUDAD_A_GIMNASIO:
            gim = CIUDAD_A_GIMNASIO[id_at]
            if not gym_derrotado(sistema_gimnasios, gim):
                lider = LIDER_POR_CIUDAD.get(id_at, "el líder")
                ciudad_nombre = id_at.replace("_", " ").title()
                return False, f"¡Aún no vences a {lider} en {ciudad_nombre}!"
    return True, ""


def proximo_objetivo(sistema_gimnasios, liga=None):
    for ciudad in ["ciudad_moche", "puerto_ancon", "andahuaylas",
                   "ciudad_imperial", "puno", "huaraz",
                   "puerto_selva", "ciudad_capital"]:
        gim = CIUDAD_A_GIMNASIO[ciudad]
        if not gym_derrotado(sistema_gimnasios, gim):
            lider = LIDER_POR_CIUDAD.get(ciudad, "el líder")
            return f"Vence a {lider} ({ciudad.replace('_',' ').title()})"
    if liga is not None and not getattr(liga, "es_campeon", False):
        return "¡Desafía al Alto Mando y al Campeón! [L]"
    return "Post-game: captura a los legendarios"


def medallas_para(id_mapa):
    """Cuántas medallas necesitas para entrar a ese mapa (0-8)."""
    if id_mapa not in ORDEN_MUNDO:
        return 0
    idx = ORDEN_MUNDO.index(id_mapa)
    count = 0
    for i in range(idx):
        id_at = ORDEN_MUNDO[i]
        if id_at in CIUDAD_A_GIMNASIO:
            count += 1
    return count