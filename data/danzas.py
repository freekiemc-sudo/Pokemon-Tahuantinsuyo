# data/danzas.py
# -*- coding: utf-8 -*-
"""E3: Festival de Danzas - Concursos estilo Pokemon Esmeralda."""

# Categorias de danza
CATEGORIAS = {
    "Belleza":  {"color": (240, 130, 200), "emoji": "B",
                 "tipo_fav": ["Planta", "Hada", "Agua"]},
    "Dureza":   {"color": (200, 80, 60),   "emoji": "D",
                 "tipo_fav": ["Roca", "Tierra", "Acero", "Lucha"]},
    "Dulzura":  {"color": (240, 220, 120), "emoji": "S",
                 "tipo_fav": ["Normal", "Hada", "Electrico"]},
    "Ingenio":  {"color": (100, 200, 240), "emoji": "I",
                 "tipo_fav": ["Psiquico", "Fantasma", "Acero"]},
    "Carisma":  {"color": (240, 100, 100), "emoji": "C",
                 "tipo_fav": ["Fuego", "Dragon", "Siniestro"]},
}


class MovimientoConcurso:
    """Un movimiento tiene una categoria y puntos base."""
    def __init__(self, nombre_mov, categoria="Belleza", puntos=3, bonus_tipo=None):
        self.nombre = nombre_mov
        self.categoria = categoria
        self.puntos = puntos
        self.bonus_tipo = bonus_tipo


def clasificar_mov(mov):
    """Clasifica un movimiento en una categoria de concurso."""
    tipo = getattr(mov, "tipo", "Normal")
    categoria = "Belleza"
    for cat, info in CATEGORIAS.items():
        if tipo in info["tipo_fav"]:
            categoria = cat
            break
    # Puntos base segun potencia
    pot = getattr(mov, "potencia", 40) or 40
    if pot < 40: puntos = 2
    elif pot < 70: puntos = 3
    elif pot < 100: puntos = 4
    else: puntos = 5
    return MovimientoConcurso(mov.nombre, categoria, puntos, tipo)


class Participante:
    def __init__(self, pokemon, es_jugador=False):
        self.pokemon = pokemon
        self.es_jugador = es_jugador
        self.puntos = 0
        self.fase1_puntos = 0
        self.fase2_puntos = 0
        self.movimientos = []
        # Clasificar movimientos
        for mov in getattr(pokemon, "movimientos", []):
            self.movimientos.append(clasificar_mov(mov))
        # Rellenar hasta 4
        while len(self.movimientos) < 4:
            self.movimientos.append(MovimientoConcurso("Placaje", "Dureza", 2, "Normal"))
        # Bonus por amistad
        self.bonus_amistad = 1.0
        try:
            amistad = getattr(pokemon, "amistad", 70)
            self.bonus_amistad = 1.0 + (amistad - 70) / 255.0 * 0.5
        except Exception:
            pass


def _rival_fake(indice):
    """Genera un rival ficticio para el festival."""
    nombres = ["Rosa", "Inti", "Killa", "Wayra", "Rumi", "Sami", "Nina", "Chaska"]
    clases = ["Danzante", "Musico", "Poeta", "Guerrero", "Chamana", "Artista"]
    import random as rnd
    return {
        "nombre": rnd.choice(nombres) + " " + str(indice + 1),
        "clase": rnd.choice(clases),
        "puntos_f1": rnd.randint(10, 30),
        "puntos_f2": rnd.randint(15, 40),
    }


def simular_festival(pokemon_jugador):
    """Simula un festival completo. Devuelve dict con resultados."""
    import random as rnd
    jugador = Participante(pokemon_jugador, True)
    # 3 rivales
    rivales = [_rival_fake(i) for i in range(3)]
    # Fase 1: Movimientos (cada uno da puntos)
    for mov in jugador.movimientos:
        p = mov.puntos * 3
        # Bonus si coincide con la categoria dominante del Pokemon
        jugador.fase1_puntos += p
    # Fase 2: Combinaciones (simplificado, suma aleatoria)
    for _ in range(4):
        jugador.fase2_puntos += rnd.randint(3, 8)
    jugador.fase2_puntos = int(jugador.fase2_puntos * jugador.bonus_amistad)
    jugador.puntos = jugador.fase1_puntos + jugador.fase2_puntos
    # Puntajes de rivales
    for r in rivales:
        r["total"] = r["puntos_f1"] + r["puntos_f2"]
    rivales_totales = [r["total"] for r in rivales]
    # Ranking
    todos = [(jugador.puntos, "Tu")] + [(r["total"], r["nombre"]) for r in rivales]
    todos.sort(reverse=True)
    ranking = todos
    posicion = next(i for i, (_, n) in enumerate(todos) if n == "Tu") + 1
    # Recompensas
    if posicion == 1:
        premio = 5000
        cinta = "Cinta del Sol"
    elif posicion == 2:
        premio = 2000
        cinta = "Cinta de Plata"
    else:
        premio = 800
        cinta = "Cinta de Bronce"
    return {
        "puntos_jugador": jugador.puntos,
        "fase1": jugador.fase1_puntos,
        "fase2": jugador.fase2_puntos,
        "rivales": rivales,
        "ranking": ranking,
        "posicion": posicion,
        "premio": premio,
        "cinta": cinta,
    }


print("OK data.danzas")
