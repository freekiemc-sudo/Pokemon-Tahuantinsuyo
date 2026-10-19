"""
Sistema de Pokédex - Registro de capturados
"""

from data.pokedex import POKEDEX_COMPLETA


class Pokedex:
    """Gestiona el registro de Pokémon capturados/vistos."""
    
    def __init__(self):
        self.vistos = set()      # Pokémon que has visto
        self.capturados = set()  # Pokémon que has capturado
    
    def registrar_visto(self, nombre: str):
        """Registra que has visto un Pokémon."""
        self.vistos.add(nombre)
    
    def registrar_capturado(self, nombre: str):
        """Registra que has capturado un Pokémon."""
        self.capturados.add(nombre)
    
    def ha_visto(self, nombre: str) -> bool:
        return nombre in self.vistos
    
    def ha_capturado(self, nombre: str) -> bool:
        return nombre in self.capturados
    
    def total_vistos(self) -> int:
        return len(self.vistos)
    
    def total_capturados(self) -> int:
        return len(self.capturados)
    
    def total_registrados(self) -> int:
        return len(POKEDEX_COMPLETA)
    
    def porcentaje_completado(self) -> float:
        return (self.total_capturados() / self.total_registrados()) * 100
    
    def obtener_lista_completa(self) -> list:
        """Devuelve lista de todos los Pokémon con su estado."""
        lista = []
        for nombre, datos in POKEDEX_COMPLETA.items():
            estado = "—"
            if self.ha_capturado(nombre):
                estado = "✓"
            elif self.ha_visto(nombre):
                estado = "○"
            
            lista.append({
                "id": datos.get("id", 0),
                "nombre": nombre,
                "tipos": datos["tipos"],
                "estado": estado,
                "datos": datos
            })
        
        return sorted(lista, key=lambda x: x["id"])