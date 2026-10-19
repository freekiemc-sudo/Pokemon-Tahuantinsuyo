# data/gimnasios.py
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

class Lider:
    def __init__(self, nombre, tipo, equipo, medalla, dialogo_pre, dialogo_post, titulo="Lider"):
        self.nombre = nombre; self.tipo = tipo
        self.equipo_nombres = equipo
        self.medalla = medalla
        self.dialogo_pre = dialogo_pre
        self.dialogo_post = dialogo_post
        self.titulo = titulo
        self.derrotado = False
    def crear_equipo(self):
        eq = []
        for nom, niv in self.equipo_nombres:
            d = POKEDEX_COMPLETA.get(nom)
            if d: eq.append(PokemonBatalla(d, niv))
            else: print("WARN Lider", self.nombre, ":", nom, "no existe")
        return eq

class Gimnasio:
    def __init__(self, id_gimnasio, nombre, ciudad, tipo, lider, posicion_mapa):
        self.id = id_gimnasio; self.nombre = nombre; self.ciudad = ciudad
        self.tipo = tipo; self.lider = lider
        self.posicion_mapa = posicion_mapa
        self.medalla = lider.medalla

GIMNASIOS = {
    "gimnasio_moche": Gimnasio("gimnasio_moche","Gimnasio de Ciudad Moche","ciudad_moche","Bicho/Normal",
        Lider("Don Fermin","Bicho/Normal",[("Orugueta",9),("Suripullo",10),("Chinchill",11),("Suriwain",12)],
              "Medalla Arcilla",
              ["Asi que tu eres el joven que detuvo a esos intrusos!","Demuestrame si esa determinacion se mantiene."],
              ["Excelente combate!","Toma la Medalla Arcilla."],
              "Agricultor Mayor"),
        ("ciudad_moche",30,12)),
    "gimnasio_ancon": Gimnasio("gimnasio_ancon","Gimnasio de Puerto Ancon","puerto_ancon","Agua",
        Lider("Capitan Chata","Agua",[("Piranita",15),("Tapirex",16),("Bufeito",18)],
              "Medalla Marea",
              ["Ah, un rival con agallas!","Aqui solo los resistentes sobreviven."],
              ["Bien jugado, causa!","Toma la Medalla Marea."],
              "Veterano del Mar"),
        ("puerto_ancon",30,12)),
    "gimnasio_andahuaylas": Gimnasio("gimnasio_andahuaylas","Gimnasio de Andahuaylas","andahuaylas","Lucha",
        Lider("Wayra","Lucha",[("Cuyver",21),("Simiochuro",22),("Cuyzard",24)],
              "Medalla Danza",
              ["La danza no es solo arte, es disciplina.","A ver si sigues mi ritmo!"],
              ["Que elegancia!","Toma la Medalla Danza."],
              "Maestra de Danzas"),
        ("andahuaylas",30,12)),
    "gimnasio_imperial": Gimnasio("gimnasio_imperial","Gimnasio de la Ciudad Imperial","ciudad_imperial","Roca/Tierra",
        Lider("Apu-Capataz","Roca/Tierra",[("Vizcachin",28),("Vicunor",29),("Torito de Pucara",30),("Montazcach",32)],
              "Medalla Cantera",
              ["Las murallas han resistido los embates del tiempo.","Demuestrame si tu voluntad es igual de solida."],
              ["Impresionante.","Toma la Medalla Cantera."],
              "Minero Mayor"),
        ("ciudad_imperial",30,12)),
    "gimnasio_puno": Gimnasio("gimnasio_puno","Gimnasio de Ciudad Lago","puno","Fantasma/Psiquico",
        Lider("Yatiri Mama","Fantasma/Psiquico",[("Aruy",34),("Colibrindes",35),("Huacotrato",36),("Jarjacha",38)],
              "Medalla Mistico",
              ["Las aguas del Titicaca guardan memorias milenarias.","Solo los dignos pueden cruzar el umbral."],
              ["Extraordinario.","Toma la Medalla Mistico."],
              "Chamana del Lago"),
        ("puno",30,12)),
    "gimnasio_huaraz": Gimnasio("gimnasio_huaraz","Gimnasio de Ciudad Huaraz","huaraz","Hielo",
        Lider("Nieves","Hielo",[("Papa Chunio",40),("Zorro de las Nieves",41),("Chinchay",42),("Ursandino",44)],
              "Medalla Glaciar",
              ["El hielo no perdona dudas.","Demuestrame tu agilidad."],
              ["Impecable.","Toma la Medalla Glaciar."],
              "Guia de Alta Montana"),
        ("huaraz",30,12)),
    "gimnasio_selva": Gimnasio("gimnasio_selva","Gimnasio de Puerto Selva","puerto_selva","Veneno/Planta",
        Lider("Dr. Osho","Veneno/Planta",[("Papa Selvatica",46),("Piranatox",47),("Muquitox",48),("Mantis-Buho",50)],
              "Medalla Liana",
              ["La selva no perdona los descuidos.","Demuestra tu resistencia amazonica."],
              ["Impresionante!","Toma la Medalla Liana."],
              "Investigador Amazonico"),
        ("puerto_selva",30,12)),
    "gimnasio_capital": Gimnasio("gimnasio_capital","Gimnasio de Ciudad Capital","ciudad_capital","Acero/Electrico",
        Lider("Ingeniero Aza","Acero/Electrico",[("Tumignus",52),("Muquimetal",53),("Wayra-Wind",54),("Incaflame",56)],
              "Medalla Cobre",
              ["Has recorrido toda la region.","La prueba es entender el equilibrio del Tahuantinsuyo."],
              ["Extraordinario!","Toma la Medalla Cobre."],
              "Magnate Tecnologico"),
        ("ciudad_capital",30,12)),
}

class SistemaGimnasios:
    def __init__(self):
        self.medallas_obtenidas = []
        self.lideres_derrotados = []
    def cantidad_medallas(self): return len(self.medallas_obtenidas)
    def registrar_victoria(self, id_gimnasio):
        g = GIMNASIOS.get(id_gimnasio)
        if not g: return None
        if id_gimnasio not in self.lideres_derrotados:
            self.lideres_derrotados.append(id_gimnasio)
        if g.medalla not in self.medallas_obtenidas:
            self.medallas_obtenidas.append(g.medalla)
        g.lider.derrotado = True
        return g.medalla
    def obtener_gimnasio(self, id_gimnasio): return GIMNASIOS.get(id_gimnasio)
    def tiene_medalla(self, m): return m in self.medallas_obtenidas
print("OK data.gimnasios:", len(GIMNASIOS))
