# data/eventos_supay.py
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

class EventoSupay:
    def __init__(self, ciudad, titulo, dialogos_intro, dialogos_derrota, equipo, recompensa=500, desbloquea_gimnasio=None):
        self.id = "supay_" + ciudad
        self.ciudad = ciudad; self.titulo = titulo
        self.dialogos_intro = dialogos_intro
        self.dialogos_derrota = dialogos_derrota
        self.equipo_nombres = equipo
        self.recompensa = recompensa
        self.desbloquea_gimnasio = desbloquea_gimnasio
        self.completado = False
    def crear_equipo(self):
        eq = []
        for nom, niv in self.equipo_nombres:
            d = POKEDEX_COMPLETA.get(nom)
            if d: eq.append(PokemonBatalla(d, niv))
        return eq

EVENTOS_SUPAY = {
    "ciudad_moche": EventoSupay("ciudad_moche","Asalto en la Huaca del Sol!",
        ["Y tu de donde has salido?","De aqui no pasas!"],
        ["Imposible! Como un novato nos derrota?","Retiremonos!"],
        [("Surito",6),("Cuy",7)],400,"gimnasio_moche"),
    "puerto_ancon": EventoSupay("puerto_ancon","Contrabando en el puerto!",
        ["Nadie interfiere con nuestro cargamento!"],
        ["Maldicion! La carga se perdio..."],
        [("Piranita",14),("Zorrin",15)],600,"gimnasio_ancon"),
    "andahuaylas": EventoSupay("andahuaylas","Alboroto en el valle!",
        ["Team Supay se apodera de las reliquias!"],
        ["Esto no termina aqui!"],
        [("Cuyver",20),("Simiochuro",21)],700,"gimnasio_andahuaylas"),
    "ciudad_imperial": EventoSupay("ciudad_imperial","Atentado en la Ciudad Imperial!",
        ["Team Supay busca los quipus sagrados!"],
        ["Malditos! La ciudad resiste."],
        [("Muquitox",26),("Montazcach",27)],800,"gimnasio_imperial"),
    "puno": EventoSupay("puno","Extrayendo energia del Titicaca!",
        ["El ninito que arruino los planes en Moche.","Estamos extrayendo la esencia del lago."],
        ["Tsk... No creas que has ganado."],
        [("Piranatox",32),("Aruy",33),("Vulandino",34)],900,"gimnasio_puno"),
    "huaraz": EventoSupay("huaraz","Volando el glaciar sagrado!",
        ["Explosivos termicos para derretir el hielo!"],
        ["Esto no se quedara asi!"],
        [("Papa Chunio",38),("Zorro de las Nieves",39),("Ursandino",40)],1000,"gimnasio_huaraz"),
    "puerto_selva": EventoSupay("puerto_selva","Tala ilegal en la reserva!",
        ["Team Supay talando arboles centenarios!"],
        ["Maldicion! La selva nos rechaza."],
        [("Piranatox",44),("Mantis-Buho",45),("Orquidea Negra",46)],1200,"gimnasio_selva"),
    "ciudad_capital": EventoSupay("ciudad_capital","Asalto final a la Capital!",
        ["Es hora de despertar al Amaru!"],
        ["Imposible! La energia ancestral nos rechaza...","Retirada!"],
        [("Vulandino",48),("Montazcach",49),("Piranatox",50),("Amaru",53)],2000,"gimnasio_capital"),
}
def obtener_evento(ciudad_id):
    return EVENTOS_SUPAY.get(ciudad_id)
print("OK data.eventos_supay:", len(EVENTOS_SUPAY))
