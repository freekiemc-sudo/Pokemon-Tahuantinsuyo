"""
Sistema de PC / Box para almacenar Pokémon cuando el equipo está lleno
Estilo Pokémon Esmeralda
"""


class Box:
    """Representa una caja del PC (guarda hasta 30 Pokémon)."""
    
    MAX_POR_CAJA = 30
    
    def __init__(self, numero: int):
        self.numero = numero
        self.pokemons = []
    
    def agregar(self, pokemon) -> bool:
        if len(self.pokemons) >= self.MAX_POR_CAJA:
            return False
        self.pokemons.append(pokemon)
        return True
    
    def remover(self, indice: int):
        if 0 <= indice < len(self.pokemons):
            return self.pokemons.pop(indice)
        return None
    
    def esta_llena(self) -> bool:
        return len(self.pokemons) >= self.MAX_POR_CAJA


class SistemaPC:
    """Gestiona todas las cajas del PC (hasta 30 cajas = 900 Pokémon)."""
    
    MAX_CAJAS = 30
    
    def __init__(self):
        self.cajas = [Box(i + 1) for i in range(self.MAX_CAJAS)]
        self.caja_actual = 0
    
    def guardar_pokemon(self, pokemon) -> bool:
        """Guarda un Pokémon en la primera caja disponible."""
        for caja in self.cajas:
            if not caja.esta_llena():
                return caja.agregar(pokemon)
        return False
    
    def obtener_pokemon(self, num_caja: int, indice: int):
        """Obtiene un Pokémon de una caja específica."""
        if 0 <= num_caja < len(self.cajas):
            return self.cajas[num_caja].remover(indice)
        return None
    
    def total_almacenados(self) -> int:
        """Devuelve el total de Pokémon almacenados."""
        return sum(len(caja.pokemons) for caja in self.cajas)
    
    def caja_tiene_pokemons(self, num_caja: int) -> bool:
        if 0 <= num_caja < len(self.cajas):
            return len(self.cajas[num_caja].pokemons) > 0
        return False
    
    def obtener_lista_caja(self, num_caja: int) -> list:
        """Devuelve la lista de Pokémon de una caja."""
        if 0 <= num_caja < len(self.cajas):
            return self.cajas[num_caja].pokemons
        return []