"""
Sistema de crianza Pokémon (Guardería / Daycare)
"""

import random
from data.pokedex import POKEDEX_COMPLETA
from sistemas.batalla import PokemonBatalla


# Pares de Pokémon compatibles para criar (simplificado)
PARES_COMPATIBLES = {
    frozenset(["Alpaka", "Alpaka"]),
    frozenset(["Feligaro", "Feligaro"]),
    frozenset(["Bufeito", "Bufeito"]),
    frozenset(["Cuy", "Cuy"]),
    frozenset(["Surito", "Surito"]),
    frozenset(["Chinchill", "Chinchill"]),
    frozenset(["Tunquid", "Tunquid"]),
}


class Huevo:
    """Representa un huevo Pokémon."""
    
    def __init__(self, especie: str, pasos_restantes: int = 100):
        self.especie = especie
        self.pasos_restantes = pasos_restantes
        self.pasos_totales = pasos_restantes
        self.eclosionado = False
    
    def caminar(self, pasos: int = 1) -> bool:
        """Avanza los pasos del huevo. Devuelve True si eclosiona."""
        self.pasos_restantes = max(0, self.pasos_restantes - pasos)
        if self.pasos_restantes == 0:
            self.eclosionado = True
            return True
        return False
    
    def progreso(self) -> float:
        return 1.0 - (self.pasos_restantes / self.pasos_totales)
    
    def eclosionar(self) -> PokemonBatalla:
        """Eclosiona el huevo y devuelve el Pokémon."""
        if not self.eclosionado:
            return None
        
        datos = POKEDEX_COMPLETA.get(self.especie)
        if not datos:
            return None
        
        # Pokémon nivel 1
        return PokemonBatalla(datos, nivel=1)


class Guarderia:
    """Guardería Pokémon donde dejar 2 Pokémon para criar."""
    
    MAX_DEPOSITADOS = 2
    MAX_HUEVOS = 5
    
    def __init__(self):
        self.depositados = []  # Lista de Pokémon depositados
        self.huevos = []       # Lista de huevos
        self.timer_cria = 0
        self.tiempo_para_huevo = 60  # segundos
    
    def depositar(self, pokemon: PokemonBatalla) -> bool:
        """Deposita un Pokémon en la guardería."""
        if len(self.depositados) >= self.MAX_DEPOSITADOS:
            return False
        self.depositados.append(pokemon)
        
        # Verificar si pueden criar
        self._verificar_cria()
        return True
    
    def retirar(self, indice: int) -> PokemonBatalla:
        """Retira un Pokémon depositado."""
        if 0 <= indice < len(self.depositados):
            return self.depositados.pop(indice)
        return None
    
    def _verificar_cria(self):
        """Verifica si los Pokémon depositados pueden criar."""
        if len(self.depositados) != 2:
            return
        
        # Simplificado: ambos deben ser de la misma especie
        if self.depositados[0].nombre == self.depositados[1].nombre:
            # Pueden criar
            pass
    
    def actualizar(self, dt: float):
        """Actualiza el timer de crianza."""
        if len(self.depositados) == 2 and len(self.huevos) < self.MAX_HUEVOS:
            self.timer_cria += dt
            if self.timer_cria >= self.tiempo_para_huevo:
                self.timer_cria = 0
                self._generar_huevo()
    
    def _generar_huevo(self):
        """Genera un huevo de la especie de los padres."""
        if len(self.depositados) < 1:
            return
        
        # El huevo es de la especie del primer padre
        especie = self.depositados[0].nombre
        
        # Posibilidad de shiny (1/8192)
        es_shiny = random.random() < (1 / 8192)
        
        huevo = Huevo(especie, pasos_restantes=100)
        huevo.es_shiny = es_shiny
        self.huevos.append(huevo)
    
    def recoger_huevo(self, indice: int) -> Huevo:
        """Recoge un huevo de la guardería."""
        if 0 <= indice < len(self.huevos):
            return self.huevos.pop(indice)
        return None
    
    def puede_crear(self) -> bool:
        return len(self.depositados) == 2 and self.depositados[0].nombre == self.depositados[1].nombre