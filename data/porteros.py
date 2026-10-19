# data/porteros.py
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

class Portero:
    def __init__(self, id_gimnasio, nombre, equipo, dialogo_pre, dialogo_derrota, acertijo, recompensa=500):
        self.id_gimnasio = id_gimnasio
        self.nombre = nombre
        self.equipo_nombres = equipo
        self.dialogo_pre = dialogo_pre
        self.dialogo_derrota = dialogo_derrota
        self.dialogo_puzzle_fail = ["Respuesta incorrecta. Vuelve a intentarlo."]
        self.acertijo = acertijo
        self.recompensa = recompensa
        self.derrotado = False
        self.puzzle_resuelto = False
    def crear_equipo(self):
        eq = []
        for nom, niv in self.equipo_nombres:
            d = POKEDEX_COMPLETA.get(nom)
            if d: eq.append(PokemonBatalla(d, niv))
        return eq

PORTEROS = {
    "gimnasio_moche": Portero("gimnasio_moche","Cuidador de la Huaca",
        [("Surito",8),("Cuy",9)],
        ["Alto ahi! Nadie entra hasta vencer al cuidador."],
        ["Buena! Tienes madera de campeon."],
        {"pregunta":"Que ave sagrada guia a los incas?",
         "opciones":["El condor","El jaguar","El puma"],"respuesta":"El condor"}),
    "gimnasio_ancon": Portero("gimnasio_ancon","Pescador Vigia",
        [("Pirañita",15),("Cuyver",16)],
        ["Solo pescadores experimentados pasan!"],
        ["Bien, causa! Puedes entrar."],
        {"pregunta":"Como se llama el mar frente a Peru?",
         "opciones":["Mar Caribe","Mar de Grau","Oceano Indico"],"respuesta":"Mar de Grau"}),
    "gimnasio_andahuaylas": Portero("gimnasio_andahuaylas","Danzante Joven",
        [("Simiochuro",20),("Cuyver",21)],
        ["Solo entra el que siga el ritmo del danzante."],
        ["Tu ritmo es puro fuego!"],
        {"pregunta":"Que instrumento de viento es tipico andino?",
         "opciones":["La quena","El violin","La trompeta"],"respuesta":"La quena"}),
    "gimnasio_imperial": Portero("gimnasio_imperial","Guardian de Canteras",
        [("Vizcachin",25),("Muquitox",26)],
        ["La piedra solo abre paso al digno."],
        ["Has demostrado la firmeza de los Andes."],
        {"pregunta":"Que cultura construyo Machu Picchu?",
         "opciones":["Moche","Inca","Nasca"],"respuesta":"Inca"}),
    "gimnasio_puno": Portero("gimnasio_puno","Barquero de Totora",
        [("Carachama",30),("Huacotrato",31)],
        ["Solo el que entiende el lago puede cruzarlo."],
        ["Las aguas te reconocen como hijo del Titicaca."],
        {"pregunta":"Como se llaman las islas de totora en el Titicaca?",
         "opciones":["Uros","Galapagos","Malvinas"],"respuesta":"Uros"}),
    "gimnasio_huaraz": Portero("gimnasio_huaraz","Montañista",
        [("Papa Chunio",36),("Chinchay",37)],
        ["El nevado solo acepta a los de corazon firme."],
        ["Eres mas duro que el hielo eterno!"],
        {"pregunta":"Cual es el nevado mas alto del Peru?",
         "opciones":["Huascaran","Aconcagua","Cotopaxi"],"respuesta":"Huascaran"}),
    "gimnasio_selva": Portero("gimnasio_selva","Guia Amazonico",
        [("Mantis-Buho",40),("Piranatox",41)],
        ["Nadie pasa sin respetar a la selva."],
        ["La selva te reconoce como aliado."],
        {"pregunta":"Cual es el rio mas caudaloso del Peru?",
         "opciones":["Rio Amazonas","Rio Rimac","Rio Maranon"],"respuesta":"Rio Amazonas"}),
    "gimnasio_capital": Portero("gimnasio_capital","Guardia Metropolitano",
        [("Tumignus",46),("Muquimetal",47)],
        ["Solo los que superaron la region pueden pasar."],
        ["Adelante, aspirante a campeon!"],
        {"pregunta":"Cual es la capital del Peru?",
         "opciones":["Cusco","Arequipa","Lima"],"respuesta":"Lima"}),
}
def obtener_portero(id_gimnasio):
    return PORTEROS.get(id_gimnasio)
print("OK data.porteros:", len(PORTEROS))
