# sistemas/equipo.py
"""
Sistema de gestión del equipo Pokémon (máximo 6 Pokémon)
"""

class Equipo:
    """Gestiona el equipo activo del jugador (hasta 6 Pokémon)."""
    
    MAX_EQUIPO = 6
    
    def __init__(self):
        self.pokemons = []  # Lista de instancias de Pokemon
    
    def agregar(self, pokemon) -> bool:
        """Agrega un Pokémon al equipo. Devuelve True si se pudo agregar."""
        if len(self.pokemons) >= self.MAX_EQUIPO:
            return False
        self.pokemons.append(pokemon)
        return True
    
    def remover(self, indice: int):
        """Remueve un Pokémon del equipo por su índice."""
        if 0 <= indice < len(self.pokemons):
            return self.pokemons.pop(indice)
        return None
    
    def obtener(self, indice: int):
        """Obtiene un Pokémon del equipo por su índice."""
        if 0 <= indice < len(self.pokemons):
            return self.pokemons[indice]
        return None
    
    def obtener_primero_vivo(self):
        """Devuelve el primer Pokémon vivo del equipo."""
        for poke in self.pokemons:
            if poke.esta_vivo():
                return poke
        return None
    
    def todos_debilitados(self) -> bool:
        """Comprueba si todo el equipo está debilitado."""
        if not self.pokemons:
            return True
        for poke in self.pokemons:
            if poke.esta_vivo():
                return False
        return True