# data/liga.py
# -*- coding: utf-8 -*-


class SistemaLiga:
    def __init__(self):
        self.es_campeon = False
        self.alto_mando_idx = 0
        self.derrotados = []

    def puede_desafiar(self, gimnasios):
        return gimnasios.cantidad_medallas() >= 8

    def siguiente_oponente(self):
        return None


print("OK data.liga")
