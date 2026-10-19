# sistemas/tiempo.py
"""Ciclo dia/noche + clima regional para Pokemon Freekie."""
import random

class Tiempo:
    AMANECER = 0
    DIA = 1
    ATARDECER = 2
    NOCHE = 3

    NOMBRES = ["amanecer", "dia", "atardecer", "noche"]

    def __init__(self, duracion_fase=120.0):
        # 120s por fase = 8 min ciclo completo
        self.tiempo_total = 0.0
        self.duracion_fase = duracion_fase
        self.clima_actual = "despejado"
        self.tiempo_clima_restante = 0.0
        self.zona_actual = "costa"

    @property
    def hora_idx(self):
        return int((self.tiempo_total / self.duracion_fase) % 4)

    @property
    def hora(self):
        return self.NOMBRES[self.hora_idx]

    def es_noche(self):
        return self.hora_idx == self.NOCHE

    def es_atardecer(self):
        return self.hora_idx == self.ATARDECER

    def actualizar(self, dt, zona=None):
        self.tiempo_total += dt
        if zona:
            self.zona_actual = zona
        if self.tiempo_clima_restante > 0:
            self.tiempo_clima_restante -= dt
        else:
            self._generar_clima()

    def _generar_clima(self):
        tabla = {
            "costa":     [("despejado", 0.60), ("sol", 0.25), ("niebla", 0.15)],
            "valle":     [("despejado", 0.65), ("sol", 0.20), ("lluvia", 0.15)],
            "sierra":    [("despejado", 0.45), ("granizo", 0.30), ("niebla", 0.25)],
            "paramo":    [("despejado", 0.40), ("granizo", 0.40), ("niebla", 0.20)],
            "altiplano": [("despejado", 0.45), ("niebla", 0.35), ("granizo", 0.20)],
            "selva":     [("despejado", 0.35), ("lluvia", 0.40), ("tormenta", 0.25)],
            "capital":   [("despejado", 0.70), ("niebla", 0.30)],
        }
        opciones = tabla.get(self.zona_actual, [("despejado", 1.0)])
        nombres = [c for c, _ in opciones]
        pesos = [p for _, p in opciones]
        self.clima_actual = random.choices(nombres, weights=pesos, k=1)[0]
        self.tiempo_clima_restante = random.uniform(45, 150)

    def tinte_hora(self):
        """Overlay de color por momento del dia (RGBA)."""
        h = self.hora_idx
        if h == self.AMANECER:
            return (255, 190, 140, 50)
        if h == self.DIA:
            return (255, 255, 255, 0)
        if h == self.ATARDECER:
            return (255, 130, 70, 70)
        return (15, 20, 70, 110)

    def tinte_clima(self):
        c = self.clima_actual
        return {
            "lluvia":   (50, 80, 130, 45),
            "tormenta": (25, 25, 60, 70),
            "niebla":   (200, 200, 210, 75),
            "sol":      (255, 240, 150, 35),
            "granizo":  (200, 220, 240, 45),
        }.get(c, (0, 0, 0, 0))

    def hora_str(self):
        return {
            "amanecer": "Amanecer", "dia": "Mediodia",
            "atardecer": "Atardecer", "noche": "Noche",
        }.get(self.hora, "?")

    def clima_str(self):
        return {
            "despejado": "Despejado", "sol": "Soleado",
            "lluvia": "Lluvia", "tormenta": "Tormenta",
            "niebla": "Niebla", "granizo": "Granizo",
        }.get(self.clima_actual, "?")

    def icono_clima(self):
        return {
            "despejado": "☀", "sol": "☀", "lluvia": "🌧",
            "tormenta": "⛈", "niebla": "🌫", "granizo": "❄",
        }.get(self.clima_actual, "☀")

    def icono_hora(self):
        return {
            "amanecer": "🌅", "dia": "☀",
            "atardecer": "🌇", "noche": "🌙",
        }.get(self.hora, "☀")
