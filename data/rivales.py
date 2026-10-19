# data/rivales.py
# -*- coding: utf-8 -*-
try:
    from data.pokedex import POKEDEX_COMPLETA
    from sistemas.batalla import PokemonBatalla
except Exception:
    POKEDEX_COMPLETA = {}
    class PokemonBatalla:
        def __init__(self, d, n=5):
            self.nombre = d.get("nombre","?"); self.nivel = n
            self.ps = 40; self.ps_max = 40; self.movimientos = []
        def esta_vivo(self): return self.ps > 0


class Rival:
    def __init__(self, nombre, mapa, equipo, dialogo_pre, dialogo_post, inicial_ventaja=None):
        self.nombre = nombre
        self.mapa = mapa
        self.equipo_nombres = equipo
        self.dialogo_pre = dialogo_pre
        self.dialogo_post = dialogo_post
        self.inicial_ventaja = inicial_ventaja
        self.derrotado = False
    def crear_equipo(self):
        eq = []
        for nom, niv in self.equipo_nombres:
            d = POKEDEX_COMPLETA.get(nom)
            if d: eq.append(PokemonBatalla(d, niv))
        return eq


RIVAL_AMISTOSO = Rival(
    "Mateo", "caleta_norte",
    [("Cuy", 5)],
    ["Habla, causa! Conque al final si te animaste por ese bicho, no?",
     "Ya sabes como es la ley del barrio."],
    ["Pucha, mano! Estas con punteria fina, ah.",
     "Reconozco que jugaste mejor hoy dia."],
)

RIVAL_ANTAGONISTA = Rival(
    "Inca-Roca", "ciudad_imperial",
    [("Vicunor", 20), ("Chinchicab", 19)],
    ["Los entrenadores comunes no entienden el verdadero peso historico.",
     "Yo si. Preparate."],
    ["Imposible... mi linaje no puede perder...",
     "Esto no quedara asi."],
)


def rival_en(mapa_id):
    if RIVAL_AMISTOSO.mapa == mapa_id:
        return RIVAL_AMISTOSO
    return None


print("OK data.rivales")
