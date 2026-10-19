# data/legendarios.py
# -*- coding: utf-8 -*-
try:
    from data.legendarios_post import SistemaLegendariosPost as SistemaLegendarios
except Exception:
    class SistemaLegendarios:
        def __init__(self): self.capturados = set()
        def puede_encontrar(self, n, m, c, no=False): return False
        def registrar_captura(self, n): self.capturados.add(n)
        def obtener_lista_disponibles(self, m, c, no=False): return []

print("OK data.legendarios")
