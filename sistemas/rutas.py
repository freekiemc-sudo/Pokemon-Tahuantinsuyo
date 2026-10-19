"""
rutas.py - Tablas de encuentros salvajes por mapa (Región Tahuantinsuyo).

Formato: ENCUENTROS[mapa_id] = {"nivel": (min, max), "tabla": [(nombre, peso), ...], "raros": [(nombre, peso), ...]}
  - "tabla": los Pokémon comunes de la ruta.
  - "raros": aparecen ~8% de las veces (los buenos están aquí).
Todos los nombres son de tu lista de 103 (lore). Si en data/pokedex.py alguno está escrito distinto,
ajusta aquí o en ALIAS de sistemas/sprites_pokes.py.

Puedes agregar rutas nuevas copiando un bloque; la IA del juego usa esto automáticamente.
"""
import random

ENCUENTROS = {
    # ------------------------- COSTA ------------------------------------
    "caleta_norte": {"nivel": (2, 4), "tabla": [("Surito", 40), ("Cuy", 35), ("Chinchill", 25)], "raros": []},
    # Ruta 1 según el lore: Surito 40%, Cuy 35%, Chinchill 15%, Papa Nativa 10% (muy raro)
    "ruta_1": {"nivel": (2, 5),
        "tabla": [("Surito", 40), ("Cuy", 35), ("Chinchill", 15), ("Papa Nativa", 10)],
        "raros": []},
    "ruta_2": {"nivel": (6, 11),
        "tabla": [("Vizcachin", 25), ("Picaflor", 20), ("Ajito", 20), ("Orugüeta", 15), ("Cuy", 10), ("Tunquid", 10)],
        "raros": [("Zorrín", 50), ("Culpeito", 50)]},
    "ruta_3": {"nivel": (11, 17),
        "tabla": [("Pirañita", 20), ("Zorrín", 20), ("Carachama", 15), ("Tunquirex", 15), ("Muquitox", 15), ("Papa Chuño", 15)],
        "raros": [("Pututos", 40), ("Ceviche", 35), ("Tigrillo", 25)]},
    # ------------------------- SIERRA BAJA / VALLE ----------------------
    "ruta_4": {"nivel": (19, 25),
        "tabla": [("Vizcachin", 25), ("Huacok", 20), ("Papa Desértica", 20), ("Cuyver", 15), ("Muquitox", 10), ("Tumito", 10)],
        "raros": [("Torito de Pucará", 40), ("Tremarcto", 35), ("Condorito", 25)]},
    "ruta_5": {"nivel": (25, 31),
        "tabla": [("Apucondor", 22), ("Ursandino", 22), ("Papa Chuño", 20), ("Aruy", 15), ("Tunquirex", 11), ("Montazcach", 10)],
        "raros": [("Zorro de las Nieves Altas", 50), ("Tigrillo", 30), ("Colibrindes", 20)]},
    "ruta_6": {"nivel": (31, 37),
        "tabla": [("Apucondor", 20), ("Ursandino", 20), ("Papa Chuño", 15), ("Colibrindes", 15), ("Llama Lunar", 10), ("Chinchicab", 10), ("Pututos", 10)],
        "raros": [("Chinchay", 40), ("Danza de Tijeras", 30), ("Tunante", 30)]},
    # ------------------------- SELVA ------------------------------------
    "ruta_7": {"nivel": (37, 43),
        "tabla": [("Tunquialt", 20), ("Monito", 20), ("Churotail", 15), ("Muquitox", 10), ("Crisálida Selva", 10),
                  ("Sachavacuna", 15), ("Papa Selvática", 10)],
        "raros": [("Chullachaqui", 35), ("Orquídea Negra", 35), ("Mantis-Búho", 30)]},
    "ruta_8": {"nivel": (43, 50),
        "tabla": [("Simiochuro", 20), ("Tapirex", 20), ("Pirañatox", 15), ("Mantis-Búho", 15), ("Suriwain", 10),
                  ("Papa Selvática", 10), ("Orquídea Negra", 10)],
        "raros": [("Sachavaca Titán", 40), ("Tunche", 30), ("Muki-Muki", 30)]},
}

# Zonas especiales de post-game (para cuando agregues los mapas): descomenta y crea el mapa con ese id.
POSTGAME = {
    "islas_titicaca":  {"nivel": (45, 55), "tabla": [("Lago-Sagu", 100)], "raros": []},
    "templo_selva":    {"nivel": (50, 60), "tabla": [("Supay-Dread", 100)], "raros": []},
    "cumbre_nevado":   {"nivel": (55, 70), "tabla": [("Omega-Inca", 100)], "raros": []},
}


def salvaje_para(mapa_id, por_defecto=("Surito", 3, 5)):
    """Devuelve (nombre, nivel) de un encuentro aleatorio para ese mapa."""
    z = ENCUENTROS.get(mapa_id) or POSTGAME.get(mapa_id)
    if not z:
        nom, a, b = por_defecto
        return nom, random.randint(a, b)
    lista = z["raros"] if (z["raros"] and random.random() < 0.08) else z["tabla"]
    nombres = [n for n, _ in lista]
    pesos = [w for _, w in lista]
    nombre = random.choices(nombres, weights=pesos, k=1)[0]
    return nombre, random.randint(*z["nivel"])