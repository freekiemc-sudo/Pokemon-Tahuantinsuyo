# data/intercambios.py
# -*- coding: utf-8 -*-
"""E6: Intercambios con NPCs - Pokemon unicos."""


class IntercambioNPC:
    def __init__(self, id, npc_nombre, mapa, pos, pide_nombre, pide_nivel_min,
                 da_nombre, da_nivel, da_shiny=False, dialogo_pre=None,
                 dialogo_ok=None, dialogo_fail=None):
        self.id = id
        self.npc_nombre = npc_nombre
        self.mapa = mapa
        self.pos = pos
        self.pide_nombre = pide_nombre
        self.pide_nivel_min = pide_nivel_min
        self.da_nombre = da_nombre
        self.da_nivel = da_nivel
        self.da_shiny = da_shiny
        self.dialogo_pre = dialogo_pre or [
            f"Hola! Cambiarias un {pide_nombre} por mi {da_nombre}?",
            f"Necesito un {pide_nombre} de nivel {pide_nivel_min} o mas.",
        ]
        self.dialogo_ok = dialogo_ok or [
            f"!Excelente! Toma mi {da_nombre}.",
            "!Cuidalo bien!",
        ]
        self.dialogo_fail = dialogo_fail or [
            f"Lo siento, necesito un {pide_nombre} de nivel {pide_nivel_min}+.",
            "Vuelve cuando lo tengas.",
        ]
        self.completado = False


INTERCAMBIOS = {
    # Caleta Norte
    "cuy_por_chinchilla": IntercambioNPC(
        "cuy_por_chinchilla", "Viejo Pescador", "caleta_norte", (40, 25),
        "Cuy", 5, "Chinchill", 8),
    "surito_por_tunquid": IntercambioNPC(
        "surito_por_tunquid", "Nino Curioso", "caleta_norte", (15, 25),
        "Surito", 6, "Tunquid", 9),

    # Ciudad Moche
    "piranita_por_carachama": IntercambioNPC(
        "piranita_por_carachama", "Pescador Beto", "ciudad_moche", (45, 20),
        "Piranita", 10, "Carachama", 14),
    "chinchill_por_alpaka": IntercambioNPC(
        "chinchill_por_alpaka", "Granjero Juan", "ciudad_moche", (35, 25),
        "Chinchill", 8, "Alpaka", 12),

    # Puerto Ancon
    "tapirex_por_rosadelf": IntercambioNPC(
        "tapirex_por_rosadelf", "Capitan Retirado", "puerto_ancon", (20, 25),
        "Tapirex", 15, "Rosadelf", 18, da_shiny=False),

    # Andahuaylas
    "cuyver_por_monito": IntercambioNPC(
        "cuyver_por_monito", "Botanica Local", "andahuaylas", (25, 25),
        "Cuyver", 20, "Monito", 22),
    "simiochuro_por_tremarcto": IntercambioNPC(
        "simiochuro_por_tremarcto", "Cazador Arrepentido", "andahuaylas", (50, 15),
        "Simiochuro", 22, "Tremarcto", 25),

    # Ciudad Imperial
    "vizcachin_por_montazcach": IntercambioNPC(
        "vizcachin_por_montazcach", "Minero Retirado", "ciudad_imperial", (25, 20),
        "Vizcachin", 25, "Montazcach", 28),
    "tumito_por_tumignus": IntercambioNPC(
        "tumito_por_tumignus", "Orfebre", "ciudad_imperial", (35, 22),
        "Tumito", 20, "Tumignus", 30, da_shiny=True),  # SHINY!

    # Puno
    "carachama_por_bufeo": IntercambioNPC(
        "carachama_por_bufeo", "Pescador del Lago", "puno", (30, 25),
        "Carachama", 28, "Bufeo Colorado", 32),
    "aruy_por_llama": IntercambioNPC(
        "aruy_por_llama", "Pastorcito", "puno", (40, 28),
        "Aruy", 25, "Llama Solar", 35),

    # Huaraz
    "papa_chunio_por_zorro": IntercambioNPC(
        "papa_chunio_por_zorro", "Montanista Local", "huaraz", (30, 20),
        "Papa Chunio", 35, "Zorro de las Nieves", 40, da_shiny=True),

    # Puerto Selva
    "piranatox_por_mantis": IntercambioNPC(
        "piranatox_por_mantis", "Explorador Selvatico", "puerto_selva", (30, 25),
        "Piranatox", 40, "Mantis-Buho", 45),
    "monito_por_simiochuro": IntercambioNPC(
        "monito_por_simiochuro", "Shaman", "puerto_selva", (45, 20),
        "Monito", 35, "Simiochuro", 42),

    # Ciudad Capital
    "chinchay_por_incaflame": IntercambioNPC(
        "chinchay_por_incaflame", "Coleccionista Elite", "ciudad_capital", (25, 25),
        "Chinchay", 45, "Incaflame", 50, da_shiny=True),
    "tarascom_por_amaru": IntercambioNPC(
        "tarascom_por_amaru", "Cientifico Loco", "ciudad_capital", (45, 25),
        "Tarascom", 45, "Dracuy", 55),
}


def obtener_intercambio(mapa, pos):
    """Devuelve el intercambio en esa posicion o None."""
    for intc in INTERCAMBIOS.values():
        if intc.mapa == mapa and tuple(intc.pos) == tuple(pos):
            return intc
    return None


def obtener_intercambios_en(mapa):
    return [i for i in INTERCAMBIOS.values() if i.mapa == mapa]


print(f"OK data.intercambios ({len(INTERCAMBIOS)} intercambios)")
