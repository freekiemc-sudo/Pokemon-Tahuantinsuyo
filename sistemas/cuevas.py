# sistemas/cuevas.py
"""
Sistema de cuevas multi-piso estilo Pokémon Esmeralda.
Cada cueva tiene N pisos, conectados por escaleras (subir/bajar).
Los pisos se guardan como tiles separados para que el jugador pueda
recorrerlos individualmente.
"""
import random

# ─── Tiles de cueva (deben coincidir con mapa_visual.py) ───
CUEVA_PISO = 31
CUEVA_PARED = 32
CUEVA_OSCURA = 33
ANTORCHA = 34
ROCA_ROMPIBLE = 30
MT_SUELO = 38
OBJ_BRILLANTE = 39
TELEPORT = 40

# ─── Definición de cuevas ───
# Cada cueva: {id: {pisos: [{w, h, num, tipo}]}}
CUEVAS = {
    "cueva_ruta2": {
        "nombre": "Cueva del Penasco",
        "bioma": "sierra",
        "pokemon": [("Vizcachin", 30), ("Huacok", 30), ("Tumito", 20),
                    ("Muquitox", 20)],
        "pisos": 3,
        "niveles_piso": [(6, 10), (10, 14), (14, 18)],
    },
    "cueva_ruta3": {
        "nombre": "Gruta del Condor",
        "bioma": "costa",
        "pokemon": [("Zorrin", 30), ("Huacok", 30), ("Tumito", 20),
                    ("Orugueta", 20)],
        "pisos": 2,
        "niveles_piso": [(12, 16), (16, 20)],
    },
    "cueva_ruta4": {
        "nombre": "Tunel de la Cordillera",
        "bioma": "sierra",
        "pokemon": [("Vizcachin", 25), ("Huacok", 25), ("Muquitox", 20),
                    ("Tumito", 20), ("Aruy", 10)],
        "pisos": 4,
        "niveles_piso": [(18, 22), (20, 24), (22, 26), (24, 28)],
    },
    "cueva_ruta5": {
        "nombre": "Caverna del Hielo",
        "bioma": "paramo",
        "pokemon": [("Papa Chunio", 30), ("Zorro de las Nieves", 30),
                    ("Aruy", 20), ("Huacok", 20)],
        "pisos": 3,
        "niveles_piso": [(26, 30), (28, 32), (30, 34)],
    },
    "cueva_ruta7": {
        "nombre": "Gruta de la Selva",
        "bioma": "selva",
        "pokemon": [("Tunche", 30), ("Aruy", 30), ("Orugueta", 20),
                    ("Muquitox", 20)],
        "pisos": 3,
        "niveles_piso": [(36, 40), (38, 42), (40, 44)],
    },
}


def generar_cueva(id_cueva):
    """Genera los tiles de todos los pisos de una cueva."""
    from sistemas.mapa_visual import (
        CUEVA_PISO, CUEVA_PARED, CUEVA_OSCURA, ANTORCHA,
        ROCA_ROMPIBLE, MT_SUELO, OBJ_BRILLANTE, TELEPORT,
    )
    info = CUEVAS.get(id_cueva)
    if not info:
        return None
    num_pisos = info["pisos"]
    pisos = []
    for i in range(num_pisos):
        w, h = 30, 22
        rng = random.Random(hash(id_cueva + str(i)) & 0xFFFFFFFF)
        t = [[CUEVA_PARED for _ in range(w)] for _ in range(h)]

        # Laberinto: cava túneles y cámaras
        # Cámara principal
        cx, cy = w // 2, h // 2
        for y in range(cy - 6, cy + 6):
            for x in range(cx - 8, cx + 8):
                if 0 <= x < w and 0 <= y < h:
                    # Ruido para bordes orgánicos
                    if abs(x-cx) < 6 or abs(y-cy) < 4 or rng.random() < 0.7:
                        t[y][x] = CUEVA_PISO

        # Túneles aleatorios
        for _ in range(5):
            tx, ty = rng.randint(3, w-4), rng.randint(3, h-4)
            for _ in range(rng.randint(4, 10)):
                if 0 <= tx < w and 0 <= ty < h:
                    t[ty][tx] = CUEVA_PISO
                    # Cava alrededor
                    for dy in (-1, 0, 1):
                        for dx in (-1, 0, 1):
                            if 0 <= tx+dx < w and 0 <= ty+dy < h and rng.random() < 0.6:
                                t[ty+dy][tx+dx] = CUEVA_PISO
                tx += rng.randint(-2, 2)
                ty += rng.randint(-2, 2)

        # Zonas oscuras (decorativas)
        for _ in range(15):
            ox, oy = rng.randint(1, w-2), rng.randint(1, h-2)
            if t[oy][ox] == CUEVA_PARED:
                t[oy][ox] = CUEVA_OSCURA

        # Antorchas en paredes junto a piso caminable
        antorchas_puestas = 0
        intentos = 0
        while antorchas_puestas < 6 and intentos < 200:
            intentos += 1
            x, y = rng.randint(2, w-3), rng.randint(2, h-3)
            if t[y][x] == CUEVA_PARED:
                # ¿Tiene piso caminable junto?
                for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                    if 0 <= x+dx < w and 0 <= y+dy < h and t[y+dy][x+dx] == CUEVA_PISO:
                        t[y][x] = ANTORCHA
                        antorchas_puestas += 1
                        break

        # Escaleras (conexión entre pisos)
        # Escalera para SUBIR (si no es el piso 0)
        pos_escalera_arriba = None
        if i > 0:
            # Busca lugar libre
            for _ in range(50):
                x, y = rng.randint(3, w-4), rng.randint(3, h-4)
                if t[y][x] == CUEVA_PISO:
                    t[y][x] = TELEPORT
                    pos_escalera_arriba = (x, y)
                    break

        # Escalera para BAJAR (si no es el último)
        pos_escalera_abajo = None
        if i < num_pisos - 1:
            for _ in range(50):
                x, y = rng.randint(3, w-4), rng.randint(3, h-4)
                if t[y][x] == CUEVA_PISO:
                    t[y][x] = TELEPORT
                    pos_escalera_abajo = (x, y)
                    break

        # Objetos recogibles
        num_items = rng.randint(1, 2)
        for _ in range(num_items):
            for _ in range(50):
                x, y = rng.randint(3, w-4), rng.randint(3, h-4)
                if t[y][x] == CUEVA_PISO:
                    t[y][x] = MT_SUELO if rng.random() < 0.3 else OBJ_BRILLANTE
                    break

        # Rocas rompibles decorativas
        for _ in range(3):
            for _ in range(20):
                x, y = rng.randint(3, w-4), rng.randint(3, h-4)
                if t[y][x] == CUEVA_PISO:
                    t[y][x] = ROCA_ROMPIBLE
                    break

        pisos.append({
            "tiles": t,
            "w": w, "h": h,
            "escalera_arriba": pos_escalera_arriba,
            "escalera_abajo": pos_escalera_abajo,
            "nivel_min": info["niveles_piso"][i][0],
            "nivel_max": info["niveles_piso"][i][1],
        })

    return {
        "id": id_cueva,
        "nombre": info["nombre"],
        "bioma": info["bioma"],
        "pokemon": info["pokemon"],
        "pisos": pisos,
        "num_pisos": num_pisos,
    }


def encontrar_escalera_para_bajar(cueva, piso_actual):
    """Devuelve la posición (x,y) del tile de TELEPORT para bajar del piso actual."""
    return cueva["pisos"][piso_actual].get("escalera_abajo")


def encontrar_escalera_para_subir(cueva, piso_actual):
    return cueva["pisos"][piso_actual].get("escalera_arriba")