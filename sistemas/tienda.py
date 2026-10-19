"""
Sistema de tiendas (PokéMart) de la Región Tahuantinsuyo
"""

try:
    from data.bayas import BAYAS as _BAYAS
    from sistemas.inventario import Objeto as _Obj
    _BAYAS_OBJ = {n: _Obj(n, "curacion", b.descripcion, 350) for n, b in _BAYAS.items()}
except Exception:
    _BAYAS_OBJ = {}

from sistemas.inventario import (
    CURACIONES, POKEBALLS, BATALLA, REVIVIRES, EVOLUCION, OBJETOS_CLAVE
)


class Tienda:
    """Representa una tienda con catálogo de productos."""
    
    def __init__(self, nombre: str, catalogo: dict, ubicacion: str = ""):
        self.nombre = nombre
        self.catalogo = catalogo  # {nombre_objeto: Objeto}
        self.ubicacion = ubicacion
    
    def obtener_lista_compra(self) -> list:
        """Devuelve lista de (nombre, objeto, precio)."""
        return [(nombre, obj, obj.precio) for nombre, obj in self.catalogo.items()]


# =========================================================================
# TIENDAS DE LA REGIÓN
# =========================================================================

# Tienda básica de Caleta Norte
TIENDA_CALETANORTE = Tienda(
    nombre="Mart de Caleta Norte",
    catalogo={
        "Poción": CURACIONES["Pocion"],
        "Antídoto": BATALLA["Antidoto"],
        "Freekie Ball": POKEBALLS["Freekie Ball"],
    },
    ubicacion="caleta_norte"
)

# Tienda de Ciudad Moche
TIENDA_MOCHE = Tienda(
    nombre="Mart de Ciudad Moche",
    catalogo={
        "Poción": CURACIONES["Pocion"],
        "Superpoción": CURACIONES["Superpocion"],
        "Antídoto": BATALLA["Antidoto"],
        "Antiparaliz": BATALLA["Antiparaliz"],
        "Freekie Ball": POKEBALLS["Freekie Ball"],
        "Súper Ball": POKEBALLS["Super Ball"],
        "Mate de Muna": CURACIONES["Mate de Muna"],
    },
    ubicacion="ciudad_moche"
)

# Tienda de Ciudad Imperial
TIENDA_IMPERIAL = Tienda(
    nombre="Mart Imperial",
    catalogo={
        "Superpoción": CURACIONES["Superpocion"],
        "Hiperpoción": CURACIONES["Hiperpocion"],
        "Antídoto": BATALLA["Antidoto"],
        "Antiparaliz": BATALLA["Antiparaliz"],
        "Antiquemar": BATALLA["Antiquemar"],
        "Despertar": BATALLA["Despertar"],
        "Freekie Ball": POKEBALLS["Freekie Ball"],
        "Súper Ball": POKEBALLS["Super Ball"],
        "Ultra Ball": POKEBALLS["Ultra Ball"],
        "Revivir": REVIVIRES["Revivir"],
        "Agua de Florida": CURACIONES["Agua de Florida"],
    },
    ubicacion="ciudad_imperial"
)

# Tienda de Ciudad Lago
TIENDA_LAGO = Tienda(
    nombre="Mart del Lago",
    catalogo={
        "Hiperpoción": CURACIONES["Hiperpocion"],
        "Maxipoción": CURACIONES["Maxipocion"],
        "Cura Total": BATALLA["Cura Total"],
        "Hielo Seco": BATALLA["Hielo Seco"],
        "Súper Ball": POKEBALLS["Super Ball"],
        "Ultra Ball": POKEBALLS["Ultra Ball"],
        "Revivir": REVIVIRES["Revivir"],
        "Maxi Revivir": REVIVIRES["Maxi Revivir"],
    },
    ubicacion="ciudad_lago"
)

# Tienda de Ciudad Selva
TIENDA_SELVA = Tienda(
    nombre="Mart de la Selva",
    catalogo={
        "Hiperpoción": CURACIONES["Hiperpocion"],
        "Maxipoción": CURACIONES["Maxipocion"],
        "Cura Total": BATALLA["Cura Total"],
        "Ultra Ball": POKEBALLS["Ultra Ball"],
        "Selva Ball": POKEBALLS["Selva Ball"],
        "Chasqui Ball": POKEBALLS["Chasqui Ball"],
        "Maxi Revivir": REVIVIRES["Maxi Revivir"],
        "Jarabe de Camu-Camu": CURACIONES["Jarabe de Camu-Camu"],
    },
    ubicacion="ciudad_selva"
)

# Tienda de Ciudad Capital (la más completa)
TIENDA_CAPITAL = Tienda(
    nombre="Mart Metrópolis",
    catalogo={
        "Maxipoción": CURACIONES["Maxipocion"],
        "Supermiel Andina": CURACIONES["Supermiel Andina"],
        "Cura Total": BATALLA["Cura Total"],
        "Elixir": BATALLA["Elixir"],
        "Ultra Ball": POKEBALLS["Ultra Ball"],
        "Selva Ball": POKEBALLS["Selva Ball"],
        "Chasqui Ball": POKEBALLS["Chasqui Ball"],
        "Maxi Revivir": REVIVIRES["Maxi Revivir"],
        "Aguaymanto": _BAYAS_OBJ.get("Aguaymanto"),
        "Lucuma": _BAYAS_OBJ.get("Lucuma"),
        "Camu Camu": _BAYAS_OBJ.get("Camu Camu"),
        "Piedra Solar": EVOLUCION["Piedra Solar"],
        "Piedra Lunar": EVOLUCION["Piedra Lunar"],
        "Piedra Fuego": EVOLUCION["Piedra Fuego"],
        "Piedra Agua": EVOLUCION["Piedra Agua"],
        "Piedra Hoja": EVOLUCION["Piedra Hoja"],
        "Piedra Trueno": EVOLUCION["Piedra Trueno"],
    },
    ubicacion="ciudad_capital"
)

# Diccionario de todas las tiendas por ubicación
TIENDAS_POR_UBICACION = {
    "caleta_norte": TIENDA_CALETANORTE,
    "ciudad_moche": TIENDA_MOCHE,
    "ciudad_imperial": TIENDA_IMPERIAL,
    "ciudad_lago": TIENDA_LAGO,
    "ciudad_selva": TIENDA_SELVA,
    "ciudad_capital": TIENDA_CAPITAL,
}


def obtener_tienda(ubicacion: str) -> Tienda:
    """Obtiene la tienda de una ubicación."""
    return TIENDAS_POR_UBICACION.get(ubicacion)


def hay_tienda_en(ubicacion: str) -> bool:
    """Verifica si hay tienda en la ubicación."""
    return ubicacion in TIENDAS_POR_UBICACION