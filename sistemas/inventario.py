"""
Sistema de inventario - VERSIÓN FINAL CORREGIDA
"""

class Objeto:
    def __init__(self, nombre: str, tipo: str, descripcion: str, precio: int = 0):
        self.nombre = nombre
        self.tipo = tipo
        self.descripcion = descripcion
        self.precio = precio
    
    def __repr__(self):
        return f"{self.nombre} ({self.tipo})"


class Inventario:
    def __init__(self):
        self.objetos = {}
        self.dinero = 3000
    
    def agregar(self, objeto, cantidad: int = 1) -> bool:
        if cantidad <= 0:
            return False
        nombre = objeto.nombre if hasattr(objeto, 'nombre') else str(objeto)
        if nombre in self.objetos:
            self.objetos[nombre]["cantidad"] += cantidad
        else:
            self.objetos[nombre] = {"objeto": objeto, "cantidad": cantidad}
        return True
    
    def remover(self, nombre: str, cantidad: int = 1) -> bool:
        if nombre not in self.objetos:
            return False
        if self.objetos[nombre]["cantidad"] < cantidad:
            return False
        self.objetos[nombre]["cantidad"] -= cantidad
        if self.objetos[nombre]["cantidad"] == 0:
            del self.objetos[nombre]
        return True
    
    def tiene_objeto(self, nombre: str) -> bool:
        return nombre in self.objetos and self.objetos[nombre]["cantidad"] > 0
    
    def obtener_lista(self) -> list:
        return [(data["objeto"], data["cantidad"]) for data in self.objetos.values()]


# =========================================================================
# CATÁLOGO DE OBJETOS
# =========================================================================

CURACIONES = {
    "Pocion": Objeto("Pocion", "curacion", "Restaura 20 PS", 300),
    "Superpocion": Objeto("Superpocion", "curacion", "Restaura 50 PS", 700),
    "Hiperpocion": Objeto("Hiperpocion", "curacion", "Restaura 200 PS", 1500),
    "Maxipocion": Objeto("Maxipocion", "curacion", "Restaura todos los PS", 3000),
    "Agua de Florida": Objeto("Agua de Florida", "curacion", "Cura 50 PS y estados", 500),
    "Mate de Muna": Objeto("Mate de Muna", "curacion", "Cura congelacion", 400),
    "Jarabe de Camu-Camu": Objeto("Jarabe de Camu-Camu", "curacion", "Cura veneno", 350),
    "Incienso de Palo Santo": Objeto("Incienso de Palo Santo", "curacion", "Despierta", 300),
    "Supermiel Andina": Objeto("Supermiel Andina", "curacion", "Restaura 100% PS", 2500),
}

POKEBALLS = {
    "Freekie Ball": Objeto("Freekie Ball", "pokeball", "Pokébola estándar", 200),
    "Super Ball": Objeto("Super Ball", "pokeball", "Mayor tasa de captura", 600),
    "Ultra Ball": Objeto("Ultra Ball", "pokeball", "Muy alta tasa de captura", 1200),
    "Chasqui Ball": Objeto("Chasqui Ball", "pokeball", "Efectiva en primer turno", 1000),
    "Selva Ball": Objeto("Selva Ball", "pokeball", "Efectiva en hierba alta", 1000),
    "Apu Ball": Objeto("Apu Ball", "pokeball", "Captura asegurada", 0),
}

BATALLA = {
    "Antidoto": Objeto("Antidoto", "battle", "Cura envenenamiento", 100),
    "Antiparaliz": Objeto("Antiparaliz", "battle", "Cura paralisis", 200),
    "Antiquemar": Objeto("Antiquemar", "battle", "Cura quemaduras", 250),
    "Despertar": Objeto("Despertar", "battle", "Despierta del sueno", 250),
    "Hielo Seco": Objeto("Hielo Seco", "battle", "Cura congelacion", 250),
    "Cura Total": Objeto("Cura Total", "battle", "Cura todos los estados", 600),
    "Elixir": Objeto("Elixir", "battle", "Restaura PP", 3000),
}

REVIVIRES = {
    "Revivir": Objeto("Revivir", "curacion", "Revive con 50% PS", 1500),
    "Maxi Revivir": Objeto("Maxi Revivir", "curacion", "Revive con 100% PS", 4000),
}

EVOLUCION = {
    "Piedra Solar": Objeto("Piedra Solar", "evolucion", "Evoluciona Pokémon de fuego", 2100),
    "Piedra Lunar": Objeto("Piedra Lunar", "evolucion", "Evoluciona Pokémon nocturnos", 2100),
    "Piedra Fuego": Objeto("Piedra Fuego", "evolucion", "Evoluciona Pokémon de fuego", 2100),
    "Piedra Agua": Objeto("Piedra Agua", "evolucion", "Evoluciona Pokémon de agua", 2100),
    "Piedra Hoja": Objeto("Piedra Hoja", "evolucion", "Evoluciona Pokémon de planta", 2100),
    "Piedra Trueno": Objeto("Piedra Trueno", "evolucion", "Evoluciona Pokémon eléctricos", 2100),
}

OBJETOS_CLAVE = {
    "Quipu Magico": Objeto("Quipu Magico", "llave", "Mapa interactivo", 0),
    "Ocarina de Arcilla": Objeto("Ocarina de Arcilla", "llave", "Invoca corrientes", 0),
    "Pico y Cincel": Objeto("Pico y Cincel", "llave", "Rompe rocas", 0),
    "Orbe del Sol": Objeto("Orbe del Sol", "llave", "Tesoro sagrado", 0),
    "Medalla Arcilla": Objeto("Medalla Arcilla", "llave", "Primera medalla", 0),
    "Medalla Marea": Objeto("Medalla Marea", "llave", "Segunda medalla", 0),
    "Medalla Danza": Objeto("Medalla Danza", "llave", "Tercera medalla", 0),
    "Medalla Cantera": Objeto("Medalla Cantera", "llave", "Cuarta medalla", 0),
    "Medalla Mistico": Objeto("Medalla Mistico", "llave", "Quinta medalla", 0),
    "Medalla Glaciar": Objeto("Medalla Glaciar", "llave", "Sexta medalla", 0),
    "Medalla Liana": Objeto("Medalla Liana", "llave", "Séptima medalla", 0),
    "Medalla Cobre": Objeto("Medalla Cobre", "llave", "Octava medalla", 0),
}


def crear_inventario_inicial() -> Inventario:
    """Crea un inventario con objetos iniciales."""
    inv = Inventario()
    inv.agregar(CURACIONES["Pocion"], 5)
    inv.agregar(BATALLA["Antidoto"], 2)
    inv.agregar(POKEBALLS["Freekie Ball"], 10)
    inv.agregar(POKEBALLS["Super Ball"], 3)
    inv.agregar(OBJETOS_CLAVE["Quipu Magico"], 1)
    return inv
