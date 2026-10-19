# data/rutas.py
# -*- coding: utf-8 -*-
import random
ENCUENTROS = {
    "caleta_norte": {"nivel": (3,5), "tabla": [("Surito",40),("Cuy",35),("Chinchill",25)], "raros": []},
    "ruta_1": {"nivel": (4,7), "tabla": [("Surito",40),("Cuy",35),("Chinchill",15),("Papa Nativa",10)], "raros": []},
    "ruta_2": {"nivel": (8,13), "tabla": [("Vizcachin",25),("Picaflor",20),("Ajito",20),("Orugueta",15),("Cuy",10),("Tunquid",10)], "raros": [("Zorrin",50),("Culpeito",50)]},
    "ruta_3": {"nivel": (13,19), "tabla": [("Piranita",20),("Zorrin",20),("Carachama",15),("Tunquirex",15),("Muquitox",15),("Papa Chunio",15)], "raros": [("Pututos",40),("Ceviche",35),("Tigrillo",25)]},
    "ruta_4": {"nivel": (20,26), "tabla": [("Vizcachin",25),("Huacok",20),("Papa Desertica",20),("Cuyver",15),("Muquitox",10),("Tumito",10)], "raros": [("Torito de Pucara",40),("Tremarcto",35),("Condorito",25)]},
    "ruta_5": {"nivel": (25,31), "tabla": [("Apucondor",22),("Ursandino",22),("Papa Chunio",20),("Aruy",15),("Tunquirex",11),("Montazcach",10)], "raros": [("Zorro de las Nieves",50),("Tigrillo",30),("Colibrindes",20)]},
    "ruta_6": {"nivel": (31,37), "tabla": [("Apucondor",20),("Ursandino",20),("Papa Chunio",15),("Colibrindes",15),("Llama Lunar",10),("Chinchicab",10),("Pututos",10)], "raros": [("Chinchay",40),("Danza de Tijeras",30),("Tunante",30)]},
    "ruta_7": {"nivel": (37,43), "tabla": [("Tunquialt",20),("Monito",20),("Churotail",15),("Muquitox",10),("Crisalida Selva",10),("Sachavacuna",15),("Papa Selvatica",10)], "raros": [("Chullachaqui",35),("Orquidea Negra",35),("Mantis-Buho",30)]},
    "ruta_8": {"nivel": (43,50), "tabla": [("Simiochuro",20),("Tapirex",20),("Piranatox",15),("Mantis-Buho",15),("Suriwain",10),("Papa Selvatica",10),("Orquidea Negra",10)], "raros": [("Sachavaca Titan",40),("Tunche",30),("Muki-Muki",30)]},
}
POSTGAME = {}
def salvaje_para(mapa_id, por_defecto=("Surito",3,5)):
    z = ENCUENTROS.get(mapa_id) or POSTGAME.get(mapa_id)
    if not z:
        nom, a, b = por_defecto
        return nom, random.randint(a, b)
    lista = z["raros"] if (z.get("raros") and random.random() < 0.08) else z["tabla"]
    nombres = [n for n, _ in lista]
    pesos = [w for _, w in lista]
    nombre = random.choices(nombres, weights=pesos, k=1)[0]
    return nombre, random.randint(*z["nivel"])
print("OK data.rutas:", len(ENCUENTROS))


# === ENCUENTROS NOCTURNOS ===
ENCUENTROS_NOCHE = {
    "ruta_1": {"nivel": (3,6), "tabla": [("Cuy",40),("Chinchill",30),("Aruy",20),("Surito",10)], "raros": [("Tunche",50),("Muki-Muki",50)]},
    "ruta_2": {"nivel": (7,12), "tabla": [("Vizcachin",25),("Huacok",25),("Aruy",20),("Zorrin",15),("Tunquid",15)], "raros": [("Pishtaco",50),("Jarjacha",50)]},
    "ruta_3": {"nivel": (12,18), "tabla": [("Aruy",25),("Huacok",25),("Zorrin",20),("Carachama",15),("Ceviche",15)], "raros": [("Pututos",40),("Pishtaco",35),("Jarjacha",25)]},
    "ruta_4": {"nivel": (20,26), "tabla": [("Aruy",25),("Huacotrato",20),("Zorrin",20),("Muquitox",20),("Tumito",15)], "raros": [("Tunche",40),("Quipus",35),("Muki-Muki",25)]},
    "ruta_5": {"nivel": (26,32), "tabla": [("Aruy",25),("Huacotrato",20),("Papa Chunio",20),("Zorro de las Nieves",20),("Chinchicab",15)], "raros": [("Killa-Puma",60),("Pishtaco",40)]},
    "ruta_6": {"nivel": (32,38), "tabla": [("Aruy",25),("Zorro de las Nieves",25),("Llama Lunar",20),("Huacotrato",15),("Chinchay",15)], "raros": [("Killa-Puma",50),("Tunante",30),("Danza de Tijeras",20)]},
    "ruta_7": {"nivel": (38,44), "tabla": [("Tunche",25),("Aruy",25),("Monito",20),("Chullachaqui",15),("Orquidea Negra",15)], "raros": [("Pishtaco",40),("Khamuy-Mist",35),("Quipus",25)]},
    "ruta_8": {"nivel": (44,50), "tabla": [("Tunche",25),("Orquidea Negra",20),("Piranatox",20),("Mantis-Buho",20),("Simiochuro",15)], "raros": [("Khamuy-Mist",40),("Pishtaco",35),("Tunante",25)]},
}

def salvaje_para_nocturno(mapa_id, por_defecto=("Aruy",5,8)):
    z = ENCUENTROS_NOCHE.get(mapa_id)
    if not z:
        return salvaje_para(mapa_id, por_defecto)
    lista = z["raros"] if (z.get("raros") and random.random() < 0.15) else z["tabla"]
    nombres = [n for n, _ in lista]
    pesos = [w for _, w in lista]
    nombre = random.choices(nombres, weights=pesos, k=1)[0]
    return nombre, random.randint(*z["nivel"])
print("OK rutas: encuentros nocturnos cargados")
