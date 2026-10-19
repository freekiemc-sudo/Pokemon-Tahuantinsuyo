"""
combate_ia.py - IA sencilla pero sensata para rivales, líderes y salvajes.

  elegir_movimiento_ia(atacante, defensor, movimientos) -> movimiento
  ia_debe_usar_pocion(pokemon, entrenador)             -> bool
"""
import random

# Efectividad ofensiva: ATAQUE -> {DEFENSA: multiplicador}
EFECT = {
    "Fuego":     {"Planta": 2, "Hielo": 2, "Bicho": 2, "Acero": 2, "Fuego": .5, "Agua": .5, "Roca": .5, "Dragón": .5},
    "Agua":      {"Fuego": 2, "Tierra": 2, "Roca": 2, "Agua": .5, "Planta": .5, "Dragón": .5},
    "Planta":    {"Agua": 2, "Tierra": 2, "Roca": 2, "Fuego": .5, "Planta": .5, "Veneno": .5, "Volador": .5, "Bicho": .5, "Dragón": .5, "Acero": .5},
    "Eléctrico": {"Agua": 2, "Volador": 2, "Planta": .5, "Eléctrico": .5, "Dragón": .5, "Tierra": 0},
    "Tierra":    {"Fuego": 2, "Eléctrico": 2, "Veneno": 2, "Roca": 2, "Acero": 2, "Planta": .5, "Bicho": .5, "Volador": 0},
    "Roca":      {"Fuego": 2, "Hielo": 2, "Volador": 2, "Bicho": 2, "Lucha": .5, "Tierra": .5, "Acero": .5},
    "Hielo":     {"Planta": 2, "Tierra": 2, "Volador": 2, "Dragón": 2, "Fuego": .5, "Agua": .5, "Hielo": .5, "Acero": .5},
    "Lucha":     {"Normal": 2, "Hielo": 2, "Roca": 2, "Siniestro": 2, "Acero": 2, "Veneno": .5, "Volador": .5, "Psíquico": .5, "Bicho": .5, "Hada": .5, "Fantasma": 0},
    "Veneno":    {"Planta": 2, "Hada": 2, "Veneno": .5, "Tierra": .5, "Roca": .5, "Fantasma": .5, "Acero": 0},
    "Psíquico":  {"Lucha": 2, "Veneno": 2, "Psíquico": .5, "Acero": .5, "Siniestro": 0},
    "Bicho":     {"Planta": 2, "Psíquico": 2, "Siniestro": 2, "Fuego": .5, "Lucha": .5, "Veneno": .5, "Volador": .5, "Fantasma": .5, "Acero": .5, "Hada": .5},
    "Fantasma":  {"Psíquico": 2, "Fantasma": 2, "Siniestro": .5, "Normal": 0},
    "Dragón":    {"Dragón": 2, "Acero": .5, "Hada": 0},
    "Siniestro": {"Psíquico": 2, "Fantasma": 2, "Lucha": .5, "Siniestro": .5, "Hada": .5},
    "Acero":     {"Hielo": 2, "Roca": 2, "Hada": 2, "Fuego": .5, "Agua": .5, "Eléctrico": .5, "Acero": .5},
    "Hada":      {"Lucha": 2, "Dragón": 2, "Siniestro": 2, "Fuego": .5, "Veneno": .5, "Acero": .5},
    "Volador":   {"Planta": 2, "Lucha": 2, "Bicho": 2, "Eléctrico": .5, "Roca": .5, "Acero": .5},
    "Normal":    {"Roca": .5, "Acero": .5, "Fantasma": 0},
}


def multiplicador(tipo_ataque, tipos_defensor):
    m = 1.0
    for t in tipos_defensor or []:
        m *= EFECT.get(tipo_ataque, {}).get(t, 1.0)
    return m


def _pp(mov):
    pp = getattr(mov, "pp", None)
    return 99 if pp is None else pp


def elegir_movimiento_ia(atacante, defensor, movimientos):
    """Elige el movimiento con mayor daño esperado (con un poco de azar para no ser predecible)."""
    if not movimientos:
        return None
    usables = [m for m in movimientos if _pp(m) > 0] or list(movimientos)
    tipos_def = getattr(defensor, "tipos", ["Normal"])
    tipos_atq = getattr(atacante, "tipos", [])
    puntajes = []
    for m in usables:
        poder = getattr(m, "poder", None)
        if poder is None:
            poder = getattr(m, "potencia", 40) or 0
        precision = getattr(m, "precision", 100) or 100
        tipo = getattr(m, "tipo", "Normal")
        stab = 1.5 if tipo in tipos_atq else 1.0
        score = poder * multiplicador(tipo, tipos_def) * stab * (precision / 100.0)
        if poder == 0:          # movimiento de estado: valor bajo pero no nulo
            score = 12
        # el rival con poca vida prefiere pegar fuerte; el sano mezcla un poco
        score *= random.uniform(0.85, 1.15)
        puntajes.append((score, m))
    puntajes.sort(key=lambda t: t[0], reverse=True)
    return puntajes[0][1]


def ia_debe_usar_pocion(pokemon, entrenador=None):
    """Usa poción si le queda <30% de PS y el entrenador todavía tiene pociones."""
    ps, ps_max = getattr(pokemon, "ps", 1), getattr(pokemon, "ps_max", 1) or 1
    if ps / ps_max >= 0.30 or ps <= 0:
        return False
    if entrenador is None:
        return False
    pociones = getattr(entrenador, "pociones", 0)
    return pociones > 0 and random.random() < 0.6