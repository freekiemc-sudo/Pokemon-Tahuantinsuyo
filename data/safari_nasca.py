# data/safari_nasca.py
# -*- coding: utf-8 -*-
"""Safari Zone de las Lineas de Nasca - estilo Emerald."""
import random

# Zonas del safari
ZONAS_SAFARI = {
    "colibri": {
        "nombre": "Zona del Colibri",
        "descripcion": "Colinas con geoglifos del Colibri.",
        "pokemon": [
            ("Colibri Nasca", 15, 25),
            ("Picaflor", 20, 30),
            ("Colibrindes", 10, 15),
            ("Vizcachin", 20, 30),
            ("Piedra Nasca" if False else "Muquitox", 15, 25),
        ],
        "items": ["Pocion", "Super Ball", "Piedra Lunar"],
    },
    "arania": {
        "nombre": "Zona de la Arana",
        "descripcion": "Desierto abierto con el geoglifo de la Arana.",
        "pokemon": [
            ("Arana Nasca", 15, 25),
            ("Picotazo Ven.", 15, 20),
            ("Carachama", 20, 30),
            ("Tigrillo", 10, 15),
            ("Muquitox", 15, 25),
        ],
        "items": ["Super Ball", "Revivir", "Piedra Sol"],
    },
    "mono": {
        "nombre": "Zona del Mono",
        "descripcion": "Valles con el geoglifo del Mono.",
        "pokemon": [
            ("Monito", 25, 35),
            ("Churotail", 20, 30),
            ("Simiochuro", 10, 15),
            ("Tunquid", 20, 30),
            ("Mono Titi" if False else "Monito", 15, 25),
        ],
        "items": ["Hiperpocion", "Piedra Hoja", "Chasqui Ball"],
    },
    "astronauta": {
        "nombre": "Zona del Astronauta",
        "descripcion": "Meseta con el geoglifo mas enigmatico.",
        "pokemon": [
            ("Constelacion Sur", 5, 10),
            ("Colibri Nasca", 15, 20),
            ("Arana Nasca", 15, 20),
            ("Tumignus", 10, 15),
            ("Quipus", 5, 10),
        ],
        "items": ["Apu Ball", "Piedra Trueno", "Maxipocion"],
    },
}


class SistemaSafari:
    def __init__(self):
        self.activo = False
        self.bolas_restantes = 30
        self.pasos_restantes = 500
        self.zona_actual = "colibri"
        self.capturados_sesion = []
        self.zona_idx = 0

    def iniciar(self):
        self.activo = True
        self.bolas_restantes = 30
        self.pasos_restantes = 500
        self.zona_actual = "colibri"
        self.capturados_sesion = []
        self.zona_idx = 0

    def terminar(self):
        self.activo = False
        return self.capturados_sesion

    def puede_capturar(self):
        return self.activo and self.bolas_restantes > 0 and self.pasos_restantes > 0

    def usar_bola(self):
        if self.bolas_restantes > 0:
            self.bolas_restantes -= 1
            return True
        return False

    def dar_pasos(self, n=1):
        self.pasos_restantes = max(0, self.pasos_restantes - n)

    def pokemon_aleatorio(self):
        zona = ZONAS_SAFARI.get(self.zona_actual)
        if not zona:
            return None, 0
        poke, nivel = random.choice(zona["pokemon"])[:2]
        nivel = random.randint(nivel, min(nivel + 10, 40))
        return poke, nivel

    def item_aleatorio(self):
        zona = ZONAS_SAFARI.get(self.zona_actual)
        if not zona:
            return None
        if random.random() < 0.15:
            return random.choice(zona["items"])
        return None

    def cambiar_zona(self):
        zonas = list(ZONAS_SAFARI.keys())
        self.zona_idx = (self.zona_idx + 1) % len(zonas)
        self.zona_actual = zonas[self.zona_idx]


print(f"OK data.safari_nasca ({len(ZONAS_SAFARI)} zonas)")
