"""
Sistema de evoluciones de Pokémon
"""

from data.pokedex import POKEDEX_COMPLETA
from sistemas.batalla import PokemonBatalla


# Tabla de evoluciones: {nombre_pokemon: condicion}
# Condiciones: {"nivel": X}, {"piedra": "nombre"}, {"felicidad": X}, etc.

TABLA_EVOLUCIONES = {
    # Iniciales
    "Alpaka":    {"tipo": "nivel", "nivel": 16, "evoluciona_a": "Vicuñor"},
    "Vicuñor":   {"tipo": "nivel", "nivel": 36, "evoluciona_a": "Majestuyocc"},
    
    "Feligaro":  {"tipo": "nivel", "nivel": 16, "evoluciona_a": "Jaguaris"},
    "Jaguaris":  {"tipo": "nivel", "nivel": 36, "evoluciona_a": "Incaflame"},
    
    "Bufeito":   {"tipo": "nivel", "nivel": 16, "evoluciona_a": "Rosadelf"},
    "Rosadelf":  {"tipo": "nivel", "nivel": 36, "evoluciona_a": "Yacumist"},
    
    # Bichos
    "Surito":    {"tipo": "nivel", "nivel": 7,  "evoluciona_a": "Suripullo"},
    "Suripullo": {"tipo": "nivel", "nivel": 10, "evoluciona_a": "Suriwain"},
    
    # Roedores
    "Cuy":       {"tipo": "nivel", "nivel": 15, "evoluciona_a": "Cuyver"},
    "Cuyver":    {"tipo": "nivel", "nivel": 30, "evoluciona_a": "Cuyzard"},
    
    # Chinchilla
    "Chinchill": {"tipo": "nivel", "nivel": 20, "evoluciona_a": "Chinchicab"},
    
    # Aves
    "Tunquid":   {"tipo": "nivel", "nivel": 18, "evoluciona_a": "Tunquirex"},
    "Tunquirex": {"tipo": "nivel", "nivel": 36, "evoluciona_a": "Tunquialt"},
}


# C4: evoluciones por amistad alta
EVOLUCIONES_AMISTAD = {
    "Aruy":          {"evoluciona_a": "Llama Solar",   "min_amistad": 220},
    "Chinchill":     {"evoluciona_a": "Chinchicab",    "min_amistad": 200},
    "Cuy":           {"evoluciona_a": "Cuyver",        "min_amistad": 200},
    "Surito":        {"evoluciona_a": "Suripullo",     "min_amistad": 180},
}


def puede_evolucionar(pokemon: PokemonBatalla) -> dict:
    """
    Verifica si un Pokémon puede evolucionar.
    Devuelve dict: {"puede": bool, "evoluciona_a": str, "tipo": str}
    """
    if pokemon.nombre not in TABLA_EVOLUCIONES:
        return {"puede": False, "evoluciona_a": None, "tipo": None}
    
    evolucion = TABLA_EVOLUCIONES[pokemon.nombre]
    
    # C4: verificar evolucion por amistad primero
    if pokemon.nombre in EVOLUCIONES_AMISTAD:
        ev = EVOLUCIONES_AMISTAD[pokemon.nombre]
        amistad = getattr(pokemon, "amistad", 70)
        if amistad >= ev["min_amistad"]:
            return {
                "puede": True,
                "evoluciona_a": ev["evoluciona_a"],
                "tipo": "amistad"
            }
    
    if evolucion["tipo"] == "nivel":
        if pokemon.nivel >= evolucion["nivel"]:
            return {
                "puede": True,
                "evoluciona_a": evolucion["evoluciona_a"],
                "tipo": "nivel"
            }
    
    return {"puede": False, "evoluciona_a": None, "tipo": evolucion["tipo"]}


def evolucionar(pokemon: PokemonBatalla) -> PokemonBatalla:
    """
    Evoluciona un Pokémon y devuelve la nueva instancia.
    Mantiene: nivel, EXP, movimientos compatibles.
    """
    resultado = puede_evolucionar(pokemon)
    if not resultado["puede"]:
        return pokemon
    
    nombre_nuevo = resultado["evoluciona_a"]
    datos_nuevos = POKEDEX_COMPLETA.get(nombre_nuevo)
    
    if not datos_nuevos:
        return pokemon
    
    # Crear nuevo Pokémon con el mismo nivel
    nuevo = PokemonBatalla(datos_nuevos, nivel=pokemon.nivel)
    
    # Conservar EXP
    nuevo.exp = pokemon.exp
    nuevo.exp_total = pokemon.exp_total
    
    # Conservar PS proporcional
    ratio_ps = pokemon.ps / pokemon.ps_max if pokemon.ps_max > 0 else 1.0
    nuevo.ps = max(1, int(nuevo.ps_max * ratio_ps))
    
    # Conservar movimientos compatibles (hasta 4)
    movimientos_nuevos = []
    for mov in pokemon.movimientos[:4]:
        # Verificar si el nuevo Pokémon puede aprender este movimiento
        # Por simplicidad, conservamos todos los movimientos
        movimientos_nuevos.append(mov)
    
    # Agregar movimientos iniciales de la nueva forma si hay espacio
    for mov_data in datos_nuevos.get("movimientos_iniciales", []):
        if len(movimientos_nuevos) >= 4:
            break
        # Evitar duplicados
        if not any(m.nombre == mov_data["nombre"] for m in movimientos_nuevos):
            from sistemas.batalla import Movimiento
            movimientos_nuevos.append(Movimiento(mov_data))
    
    nuevo.movimientos = movimientos_nuevos
    
    return nuevo


def verificar_evoluciones_equipo(equipo: list) -> list:
    """
    Verifica todo el equipo y devuelve lista de Pokémon que pueden evolucionar.
    """
    pueden_ev = []
    for i, poke in enumerate(equipo):
        resultado = puede_evolucionar(poke)
        if resultado["puede"]:
            pueden_ev.append({
                "indice": i,
                "pokemon": poke,
                "evoluciona_a": resultado["evoluciona_a"]
            })
    return pueden_ev    # ✅ devuelve la LISTA, no la función