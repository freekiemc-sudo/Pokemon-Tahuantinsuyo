"""
Sistema multijugador local (Link Cable simulado)
Dos jugadores en la misma máquina pueden intercambiar Pokémon o batallar.
"""

import random


class JugadorLocal:
    """Representa un jugador local (humano o IA)."""
    
    def __init__(self, nombre: str, es_ia: bool = False):
        self.nombre = nombre
        self.es_ia = es_ia
        self.equipo = []  # Lista de PokemonBatalla
        self.dinero = 3000
        self.medallas = 0
    
    def agregar_pokemon(self, pokemon):
        if len(self.equipo) < 6:
            self.equipo.append(pokemon)
            return True
        return False
    
    def remover_pokemon(self, indice: int):
        if 0 <= indice < len(self.equipo):
            return self.equipo.pop(indice)
        return None


class SistemaLinkCable:
    """Simula el Link Cable de Pokémon Esmeralda."""
    
    MODO_MENU = 0
    MODO_INTERCAMBIO = 1
    MODO_BATALLA = 2
    
    def __init__(self):
        self.jugador1 = None
        self.jugador2 = None
        self.modo = self.MODO_MENU
        self.mensaje = ""
        
        # Estado de intercambio
        self.idx_seleccion_j1 = 0
        self.idx_seleccion_j2 = 0
        self.j1_confirmo = False
        self.j2_confirmo = False
    
    def configurar_jugadores(self, j1_equipo: list, j2_equipo: list,
                            nombre_j1: str = "Jugador 1",
                            nombre_j2: str = "Rival IA"):
        """Configura los dos jugadores."""
        self.jugador1 = JugadorLocal(nombre_j1, es_ia=False)
        self.jugador1.equipo = j1_equipo.copy()
        
        self.jugador2 = JugadorLocal(nombre_j2, es_ia=True)
        self.jugador2.equipo = j2_equipo.copy()
    
    def iniciar_intercambio(self):
        """Inicia el modo intercambio."""
        self.modo = self.MODO_INTERCAMBIO
        self.idx_seleccion_j1 = 0
        self.idx_seleccion_j2 = 0
        self.j1_confirmo = False
        self.j2_confirmo = False
        self.mensaje = "¡Intercambio iniciado!"
    
    def seleccionar_j1(self, indice: int):
        """Jugador 1 selecciona un Pokémon para intercambiar."""
        if 0 <= indice < len(self.jugador1.equipo):
            self.idx_seleccion_j1 = indice
    
    def seleccionar_j2(self, indice: int):
        """Jugador 2 (IA) selecciona un Pokémon para intercambiar."""
        if 0 <= indice < len(self.jugador2.equipo):
            self.idx_seleccion_j2 = indice
    
    def confirmar_j1(self):
        """Jugador 1 confirma su selección."""
        self.j1_confirmo = True
        # La IA confirma automáticamente
        if self.jugador2.es_ia:
            self.j2_confirmo = True
            self.idx_seleccion_j2 = random.randint(0, len(self.jugador2.equipo) - 1)
    
    def ejecutar_intercambio(self) -> bool:
        """Ejecuta el intercambio si ambos confirmaron."""
        if not (self.j1_confirmo and self.j2_confirmo):
            return False
        
        # Intercambiar Pokémon
        poke1 = self.jugador1.equipo[self.idx_seleccion_j1]
        poke2 = self.jugador2.equipo[self.idx_seleccion_j2]
        
        self.jugador1.equipo[self.idx_seleccion_j1] = poke2
        self.jugador2.equipo[self.idx_seleccion_j2] = poke1
        
        self.mensaje = f"¡{poke1.nombre} y {poke2.nombre} intercambiados!"
        return True
    
    def cancelar_intercambio(self):
        """Cancela el intercambio."""
        self.modo = self.MODO_MENU
        self.j1_confirmo = False
        self.j2_confirmo = False
        self.mensaje = "Intercambio cancelado."
    
    def iniciar_batalla(self):
        """Inicia el modo batalla."""
        self.modo = self.MODO_BATALLA
        self.mensaje = "¡Batalla iniciada!"
    
    def finalizar(self):
        """Finaliza la sesión Link Cable."""
        self.modo = self.MODO_MENU
        self.mensaje = ""