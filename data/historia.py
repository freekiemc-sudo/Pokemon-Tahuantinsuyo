# data/historia.py
# -*- coding: utf-8 -*-
DIALOGOS_PROFESOR = {
    "inicio": [
        "Bienvenido al mundo de los Pokemon, joven entrenador!",
        "Mi nombre es Profesor Kuntur, estudio la biodiversidad del Tahuantinsuyo.",
        "Nuestra region es hogar de criaturas extraordinarias, descendientes de los Apus.",
        "Pero una sombra se cierne sobre nuestra tierra...",
        "El Team Supay busca despertar al legendario Omega-Inca.",
        "Necesito tu ayuda. Elige a tu companero y comienza tu aventura.",
        "Que los Apus te guien!",
    ],
    "primer_encuentro": [
        "Ah, ya elegiste a tu companero!",
        "Recuerda: cada Pokemon tiene su propia personalidad.",
        "Antes de irte, deja que te de esto: un Quipu Magico.",
        "Con el podras leer el mapa y saber siempre a donde ir.",
        "Buena suerte, joven campeon!",
    ],
    "tras_primer_gimnasio": [
        "Excelente trabajo ganando tu primera medalla!",
        "Pero el Team Supay sigue activo.",
        "Investiga y deten sus planes antes de que sea tarde.",
    ],
}
DIALOGOS_TEAM_SUPAY = {
    "recluta": ["Y tu de donde has salido?","Crees que puedes jugar al heroe?","De aqui no pasas!"],
    "recluta_derrotado": ["Imposible? Como un novato nos derrota?","Retiremonos!"],
    "comandante_sacha": ["Vaya, vaya...","Este lago guarda corrientes de energia milenarias.","Si interfieres, te daremos una leccion."],
    "comandante_derrotado": ["Tsk... No creas que has ganado.","El despertar del Amaru es inevitable!"],
}
class EventoHistoria:
    def __init__(self, id_evento, nombre, descripcion, ubicacion, dialogos, completado=False):
        self.id = id_evento; self.nombre = nombre; self.descripcion = descripcion
        self.ubicacion = ubicacion; self.dialogos = dialogos; self.completado = completado
EVENTOS_PRINCIPALES = [
    EventoHistoria("evento_1_huaca","El robo en la Huaca","El Team Supay roba reliquias.",
        ("ciudad_moche",8,3),
        DIALOGOS_TEAM_SUPAY["recluta"] + DIALOGOS_TEAM_SUPAY["recluta_derrotado"]),
    EventoHistoria("evento_2_lago","Misterio en el Titicaca","El Team Supay extrae energia.",
        ("puno",10,8),
        DIALOGOS_TEAM_SUPAY["comandante_sacha"] + DIALOGOS_TEAM_SUPAY["comandante_derrotado"]),
]
class SistemaHistoria:
    def __init__(self):
        self.eventos_completados = []
        self.dialogos_vistos = set()
        self.capitulo_actual = 1
    def completar_evento(self, id_evento):
        if id_evento not in self.eventos_completados:
            self.eventos_completados.append(id_evento); return True
        return False
    def evento_completado(self, id_evento): return id_evento in self.eventos_completados
    def marcar_dialogo_visto(self, id_dialogo): self.dialogos_vistos.add(id_dialogo)
    def dialogo_ya_visto(self, id_dialogo): return id_dialogo in self.dialogos_vistos
    def avanzar_capitulo(self): self.capitulo_actual += 1
    def obtener_eventos_activos(self):
        return [e for e in EVENTOS_PRINCIPALES if e.id not in self.eventos_completados]
print("OK data.historia")
