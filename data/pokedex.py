# data/pokedex.py
# -*- coding: utf-8 -*-
M_BASE = {
    "Placaje":      {"nombre":"Placaje","tipo":"Normal","potencia":40,"precision":100,"categoria":"Fisico","pp":35},
    "Aranazo":      {"nombre":"Aranazo","tipo":"Normal","potencia":40,"precision":100,"categoria":"Fisico","pp":35},
    "Grunido":      {"nombre":"Grunido","tipo":"Normal","potencia":0,"precision":100,"categoria":"Estado","pp":40},
    "Latigo Cepa":  {"nombre":"Latigo Cepa","tipo":"Planta","potencia":45,"precision":100,"categoria":"Fisico","pp":25},
    "Hoja Afilada": {"nombre":"Hoja Afilada","tipo":"Planta","potencia":55,"precision":95,"categoria":"Fisico","pp":25},
    "Ascuas":       {"nombre":"Ascuas","tipo":"Fuego","potencia":40,"precision":100,"categoria":"Especial","pp":25},
    "Pirotecnia":   {"nombre":"Pirotecnia","tipo":"Fuego","potencia":70,"precision":100,"categoria":"Especial","pp":15},
    "Pistola Agua": {"nombre":"Pistola Agua","tipo":"Agua","potencia":40,"precision":100,"categoria":"Especial","pp":25},
    "Burbuja":      {"nombre":"Burbuja","tipo":"Agua","potencia":40,"precision":100,"categoria":"Especial","pp":30},
    "Presa Acuatica":{"nombre":"Presa Acuatica","tipo":"Agua","potencia":55,"precision":100,"categoria":"Fisico","pp":25},
    "Impactrueno":  {"nombre":"Impactrueno","tipo":"Electrico","potencia":40,"precision":100,"categoria":"Especial","pp":30},
    "Rayo Hielo":   {"nombre":"Rayo Hielo","tipo":"Hielo","potencia":55,"precision":100,"categoria":"Especial","pp":15},
    "Golpe Karate": {"nombre":"Golpe Karate","tipo":"Lucha","potencia":50,"precision":100,"categoria":"Fisico","pp":25},
    "Picotazo Ven.":{"nombre":"Picotazo Ven.","tipo":"Veneno","potencia":15,"precision":100,"categoria":"Fisico","pp":35},
    "Bofeton Lodo": {"nombre":"Bofeton Lodo","tipo":"Tierra","potencia":20,"precision":100,"categoria":"Especial","pp":10},
    "Picotazo":     {"nombre":"Picotazo","tipo":"Volador","potencia":35,"precision":100,"categoria":"Fisico","pp":35},
    "Confusion":    {"nombre":"Confusion","tipo":"Psiquico","potencia":50,"precision":100,"categoria":"Especial","pp":25},
    "Picadura":     {"nombre":"Picadura","tipo":"Bicho","potencia":60,"precision":100,"categoria":"Fisico","pp":20},
    "Lanzarrocas":  {"nombre":"Lanzarrocas","tipo":"Roca","potencia":50,"precision":90,"categoria":"Fisico","pp":15},
    "Lenguetazo":   {"nombre":"Lenguetazo","tipo":"Fantasma","potencia":30,"precision":100,"categoria":"Fisico","pp":30},
    "Mordisco":     {"nombre":"Mordisco","tipo":"Siniestro","potencia":60,"precision":100,"categoria":"Fisico","pp":25},
    "Furia Dragon": {"nombre":"Furia Dragon","tipo":"Dragon","potencia":60,"precision":100,"categoria":"Especial","pp":20},
    "Ala de Acero": {"nombre":"Ala de Acero","tipo":"Acero","potencia":70,"precision":90,"categoria":"Fisico","pp":25},
    "Beso Drenador":{"nombre":"Beso Drenador","tipo":"Hada","potencia":50,"precision":100,"categoria":"Especial","pp":10},
    "Chirrido":     {"nombre":"Chirrido","tipo":"Sonido","potencia":0,"precision":85,"categoria":"Estado","pp":40},
}
# === MOVIMIENTOS ADICIONALES DE LOS JUEGOS ORIGINALES ===
M_BASE.update({
    "Lanzallamas":   {"nombre":"Lanzallamas","tipo":"Fuego","potencia":90,"precision":100,"categoria":"Especial","pp":15,"efecto":{"estado":"quemado","probabilidad":0.1}},
    "Rayo":          {"nombre":"Rayo","tipo":"Electrico","potencia":90,"precision":100,"categoria":"Especial","pp":15,"efecto":{"estado":"paralizado","probabilidad":0.1}},
    "Trueno":        {"nombre":"Trueno","tipo":"Electrico","potencia":110,"precision":70,"categoria":"Especial","pp":10,"efecto":{"estado":"paralizado","probabilidad":0.3}},
    "Rayo Solar":    {"nombre":"Rayo Solar","tipo":"Planta","potencia":120,"precision":100,"categoria":"Especial","pp":10},
    "Ventisca":      {"nombre":"Ventisca","tipo":"Hielo","potencia":110,"precision":70,"categoria":"Especial","pp":5,"efecto":{"estado":"congelado","probabilidad":0.1}},
    "Terremoto":     {"nombre":"Terremoto","tipo":"Tierra","potencia":100,"precision":100,"categoria":"Fisico","pp":10},
    "Roca Afilada":  {"nombre":"Roca Afilada","tipo":"Roca","potencia":100,"precision":80,"categoria":"Fisico","pp":5},
    "Bola Sombra":   {"nombre":"Bola Sombra","tipo":"Fantasma","potencia":80,"precision":100,"categoria":"Especial","pp":15,"efecto":{"stat_changes":{"def_esp":-1}}},
    "Psicorrayo":    {"nombre":"Psicorrayo","tipo":"Psiquico","potencia":90,"precision":100,"categoria":"Especial","pp":10,"efecto":{"estado":"confundido","probabilidad":0.1}},
    "Puno Trueno":   {"nombre":"Puno Trueno","tipo":"Electrico","potencia":75,"precision":100,"categoria":"Fisico","pp":15,"efecto":{"estado":"paralizado","probabilidad":0.1}},
    "Puno Fuego":    {"nombre":"Puno Fuego","tipo":"Fuego","potencia":75,"precision":100,"categoria":"Fisico","pp":15,"efecto":{"estado":"quemado","probabilidad":0.1}},
    "Puno Hielo":    {"nombre":"Puno Hielo","tipo":"Hielo","potencia":75,"precision":100,"categoria":"Fisico","pp":15,"efecto":{"estado":"congelado","probabilidad":0.1}},
    "Tajo Umbrio":   {"nombre":"Tajo Umbrio","tipo":"Siniestro","potencia":70,"precision":100,"categoria":"Fisico","pp":15},
    "Triturar":      {"nombre":"Triturar","tipo":"Siniestro","potencia":80,"precision":100,"categoria":"Fisico","pp":15,"efecto":{"stat_changes":{"def":-1}}},
    "Garra Dragon":  {"nombre":"Garra Dragon","tipo":"Dragon","potencia":80,"precision":100,"categoria":"Fisico","pp":15},
    "Cometa Draco":  {"nombre":"Cometa Draco","tipo":"Dragon","potencia":130,"precision":90,"categoria":"Especial","pp":5},
    "A Bocajarro":   {"nombre":"A Bocajarro","tipo":"Lucha","potencia":120,"precision":100,"categoria":"Fisico","pp":5,"efecto":{"stat_changes":{"def":-1,"def_esp":-1}}},
    "Patada Salto":  {"nombre":"Patada Salto","tipo":"Lucha","potencia":100,"precision":95,"categoria":"Fisico","pp":10},
    "Zumbido":       {"nombre":"Zumbido","tipo":"Bicho","potencia":90,"precision":100,"categoria":"Especial","pp":10},
    "Hoja Aguda":    {"nombre":"Hoja Aguda","tipo":"Planta","potencia":90,"precision":100,"categoria":"Fisico","pp":15},
    "Latigazo":      {"nombre":"Latigazo","tipo":"Planta","potencia":120,"precision":85,"categoria":"Fisico","pp":10},
    "Hidrobomba":    {"nombre":"Hidrobomba","tipo":"Agua","potencia":110,"precision":80,"categoria":"Especial","pp":5},
    "Acua Cola":     {"nombre":"Acua Cola","tipo":"Agua","potencia":90,"precision":90,"categoria":"Fisico","pp":10},
    "Rayo Burbuja":  {"nombre":"Rayo Burbuja","tipo":"Agua","potencia":65,"precision":100,"categoria":"Especial","pp":20,"efecto":{"stat_changes":{"vel":-1}}},
    "Viento Hielo":  {"nombre":"Viento Hielo","tipo":"Hielo","potencia":55,"precision":95,"categoria":"Especial","pp":15},
    "Avalancha":     {"nombre":"Avalancha","tipo":"Roca","potencia":75,"precision":90,"categoria":"Fisico","pp":10,"efecto":{"flinch":0.3}},
    "Tierra Viva":   {"nombre":"Tierra Viva","tipo":"Tierra","potencia":90,"precision":100,"categoria":"Especial","pp":10},
    "Bola Voltio":   {"nombre":"Bola Voltio","tipo":"Electrico","potencia":120,"precision":100,"categoria":"Especial","pp":15,"efecto":{"stat_changes":{"atq_esp":-1}}},
    "Chispazo":      {"nombre":"Chispazo","tipo":"Electrico","potencia":80,"precision":100,"categoria":"Especial","pp":15},
    "Onda Trueno":   {"nombre":"Onda Trueno","tipo":"Electrico","potencia":0,"precision":90,"categoria":"Estado","pp":20,"efecto":{"estado":"paralizado","probabilidad":1.0}},
    "Puno Sombra":   {"nombre":"Puno Sombra","tipo":"Fantasma","potencia":60,"precision":100,"categoria":"Fisico","pp":20},
    "Pulso Umbrio":  {"nombre":"Pulso Umbrio","tipo":"Siniestro","potencia":80,"precision":100,"categoria":"Especial","pp":15,"efecto":{"flinch":0.2}},
    "Golpe Aereo":   {"nombre":"Golpe Aereo","tipo":"Volador","potencia":60,"precision":100,"categoria":"Fisico","pp":20},
    "Pajaro Osado":  {"nombre":"Pajaro Osado","tipo":"Volador","potencia":120,"precision":100,"categoria":"Fisico","pp":15,"efecto":{"recoil":0.33}},
    "Cabeza Hierro": {"nombre":"Cabeza Hierro","tipo":"Acero","potencia":80,"precision":100,"categoria":"Fisico","pp":15,"efecto":{"flinch":0.3}},
    "Garra Metal":   {"nombre":"Garra Metal","tipo":"Acero","potencia":50,"precision":95,"categoria":"Fisico","pp":35,"efecto":{"stat_changes":{"atq":1}}},
    "Psicoataque":   {"nombre":"Psicoataque","tipo":"Psiquico","potencia":140,"precision":90,"categoria":"Especial","pp":5,"efecto":{"stat_changes":{"def_esp":-1}}},
    "Golpe Bis":     {"nombre":"Golpe Bis","tipo":"Lucha","potencia":25,"precision":100,"categoria":"Fisico","pp":10},
    "Roca Veloz":    {"nombre":"Roca Veloz","tipo":"Roca","potencia":40,"precision":100,"categoria":"Fisico","pp":15,"prioridad":1},
    "Robo":          {"nombre":"Robo","tipo":"Siniestro","potencia":60,"precision":100,"categoria":"Fisico","pp":25},
    "Vendetta":      {"nombre":"Vendetta","tipo":"Fantasma","potencia":60,"precision":100,"categoria":"Fisico","pp":10},
    "Rueda Fuego":   {"nombre":"Rueda Fuego","tipo":"Fuego","potencia":60,"precision":100,"categoria":"Fisico","pp":25},
    "Viento Plata":  {"nombre":"Viento Plata","tipo":"Bicho","potencia":60,"precision":100,"categoria":"Especial","pp":5},
    "Golpe Aereo":   {"nombre":"Golpe Aereo","tipo":"Volador","potencia":60,"precision":100,"categoria":"Fisico","pp":20},
    "Colmillo Igneo":{"nombre":"Colmillo Igneo","tipo":"Fuego","potencia":65,"precision":95,"categoria":"Fisico","pp":15,"efecto":{"estado":"quemado","probabilidad":0.1}},
    "Colmillo Hielo":{"nombre":"Colmillo Hielo","tipo":"Hielo","potencia":65,"precision":95,"categoria":"Fisico","pp":15,"efecto":{"estado":"congelado","probabilidad":0.1}},
    "Colmillo Rayo": {"nombre":"Colmillo Rayo","tipo":"Electrico","potencia":65,"precision":95,"categoria":"Fisico","pp":15,"efecto":{"estado":"paralizado","probabilidad":0.1}},
})

# === MOVIMIENTOS CARACTERISTICOS DE INICIALES FINALES ===
M_BASE.update({
    "Estampida Sagrada": {
        "nombre": "Estampida Sagrada", "tipo": "Tierra",
        "potencia": 120, "precision": 90, "categoria": "Fisico", "pp": 5,
        "efecto": {"stat_changes": {"def": -1}},
        "descripcion": "Majestuyocc convoca la fuerza de los Apus y aplasta con el peso de los Andes."
    },
    "Rugido Sol Inca": {
        "nombre": "Rugido Sol Inca", "tipo": "Fuego",
        "potencia": 120, "precision": 90, "categoria": "Especial", "pp": 5,
        "efecto": {"estado": "quemado", "probabilidad": 0.4},
        "descripcion": "Incaflame ruge con la furia del Inti y el aire se vuelve un infierno dorado."
    },
    "Eco del Yacumama": {
        "nombre": "Eco del Yacumama", "tipo": "Agua",
        "potencia": 120, "precision": 90, "categoria": "Especial", "pp": 5,
        "efecto": {"estado": "confundido", "probabilidad": 0.4},
        "descripcion": "Yacumist invoca el eco profundo del rio y golpea con la fuerza del Yacumama."
    },
})

_RAW = [
    (1,"Alpaka",["Planta"],(45,50,45,45,50,70),["Placaje","Latigo Cepa","Grunido"],"Pokemon Auquenido",0.4,6.5,"Vive en las faldas de los cerros andinos.","Espesura"),
    (2,"Vicunor",["Planta","Tierra"],(65,65,60,60,65,90),["Placaje","Latigo Cepa","Bofeton Lodo"],"Pokemon Camelido",0.9,22.0,"Sus patas agiles escalan rocas.","Espesura"),
    (3,"Majestuyocc",["Planta","Tierra"],(90,105,85,80,90,103),["Hoja Afilada","Bofeton Lodo","Placaje", "Estampida Sagrada"],"Pokemon Soberano",1.7,85.4,"Protector de los pastizales.","Espesura"),
    (4,"Feligaro",["Fuego"],(42,60,40,55,40,68),["Aranazo","Ascuas","Grunido"],"Pokemon Cachorro Sol",0.5,8.0,"Jugueton y veloz.","Mar Llamas"),
    (5,"Jaguaris",["Fuego","Siniestro"],(60,85,55,70,55,90),["Aranazo","Ascuas","Mordisco"],"Pokemon Felino Feroz",1.1,45.0,"Se camufla entre sombras.","Mar Llamas"),
    (6,"Incaflame",["Fuego","Siniestro"],(80,120,75,95,75,108),["Pirotecnia","Mordisco","Aranazo"],"Pokemon Rey Sol",1.6,92.5,"Rugido como estallido volcanico.","Mar Llamas"),
    (7,"Bufeito",["Agua"],(55,45,50,60,50,45),["Placaje","Pistola Agua","Burbuja"],"Pokemon Delfin Rosado",0.6,10.2,"Navega por los rios del Amazonas.","Torrente"),
    (8,"Rosadelf",["Agua","Psiquico"],(75,60,65,85,70,60),["Pistola Agua","Confusion","Burbuja"],"Pokemon Magico",1.2,38.0,"Inteligencia sobresaliente.","Torrente"),
    (9,"Yacumist",["Agua","Psiquico"],(100,75,80,115,95,88),["Presa Acuatica","Confusion","Pistola Agua"],"Pokemon Espiritu Fluvial",1.8,105.0,"Ser venerado en mitos.","Torrente"),
    (10,"Surito",["Bicho"],(45,35,50,20,30,45),["Placaje","Picadura"],"Pokemon Oruga",0.3,2.1,"Oruga peluda de ichu seco.","Enjambre"),
    (11,"Suripullo",["Bicho","Normal"],(50,45,80,25,45,30),["Placaje","Picadura"],"Pokemon Capullo",0.5,8.5,"Capullo con aspecto de huevo.","Mudar"),
    (12,"Suriwain",["Normal","Volador"],(70,85,60,40,60,105),["Picotazo","Placaje","Aranazo"],"Pokemon Suri",1.1,25.0,"Corre a toda velocidad.","Pies Rapidos"),
    (13,"Orugueta",["Bicho"],(40,48,42,30,35,50),["Placaje","Picadura"],"Pokemon Gusanito",0.2,1.5,"Gusano verde con cuerno.","Enjambre"),
    (14,"Crisalida Selva",["Bicho","Planta"],(50,35,85,35,65,20),["Placaje","Latigo Cepa"],"Pokemon Capullo Hoja",0.4,6.0,"Imita una hoja seca.","Mitosis"),
    (15,"Mantis-Buho",["Bicho","Siniestro"],(70,110,70,60,70,100),["Picadura","Mordisco","Aranazo"],"Pokemon Mantis Buho",1.4,35.0,"Patrones de ojos de buho.","Vista Lince"),
    (16,"Tunquid",["Volador"],(40,45,35,35,35,60),["Picotazo","Aranazo","Grunido"],"Pokemon Polluelo",0.4,3.2,"Polluelo de bosques nublados.","Vista Lince"),
    (17,"Tunquirex",["Volador","Fuego"],(60,70,55,55,50,85),["Picotazo","Ascuas","Aranazo"],"Pokemon Ave Ignea",0.9,14.0,"Plumaje escarlata.","Cuerpo Llama"),
    (18,"Tunquialt",["Volador","Fuego"],(78,102,75,80,75,115),["Picotazo","Pirotecnia","Aranazo"],"Pokemon Gallito Rocas",1.3,32.0,"Iconico Gallito de las Rocas.","Cuerpo Llama"),
    (19,"Cuy",["Normal"],(45,50,40,30,35,60),["Placaje","Aranazo","Grunido"],"Pokemon Cobayo",0.3,1.2,"Asustadizo y veloz.","Recogida"),
    (20,"Cuyver",["Normal"],(60,70,55,45,50,85),["Placaje","Aranazo","Grunido"],"Pokemon Roedor",0.6,4.5,"Almacena hierbas en mejillas.","Gula"),
    (21,"Cuyzard",["Normal","Lucha"],(85,100,75,55,70,102),["Golpe Karate","Placaje","Aranazo"],"Pokemon Territorial",1.1,28.0,"Patadas frontales potentes.","Puno Ferreo"),
    (22,"Monito",["Planta"],(45,45,45,45,45,65),["Latigo Cepa","Placaje","Grunido"],"Pokemon Monito",0.4,3.8,"Se columpia entre lianas.","Clorofila"),
    (23,"Churotail",["Planta","Normal"],(60,65,60,60,60,90),["Latigo Cepa","Placaje","Aranazo"],"Pokemon Cola Larga",0.8,14.2,"Cola como tercera mano.","Clorofila"),
    (24,"Simiochuro",["Planta","Lucha"],(80,110,80,70,75,100),["Hoja Afilada","Golpe Karate","Placaje"],"Pokemon Simio Selva",1.5,52.0,"Lider de las copas.","Clorofila"),
    (25,"Sachavacuna",["Normal"],(60,50,55,35,45,40),["Placaje","Aranazo"],"Pokemon Cria Tapir",0.7,20.5,"Rayas como camuflaje.","Hidratacion"),
    (26,"Tapirex",["Normal","Agua"],(85,75,80,50,65,55),["Placaje","Pistola Agua","Presa Acuatica"],"Pokemon Tapir Joven",1.2,85.0,"Sumergido en rios.","Hidratacion"),
    (27,"Sachavaca Titan",["Agua","Tierra"],(115,100,105,65,85,65),["Presa Acuatica","Bofeton Lodo","Placaje"],"Pokemon Tapir Titan",2.1,240.0,"Coloso de rios profundos.","Piel Tosca"),
    (28,"Vizcachin",["Roca"],(50,55,60,40,45,50),["Placaje","Lanzarrocas","Aranazo"],"Pokemon Vizcacha",0.3,2.5,"Salta sobre penascos.","Robustez"),
    (29,"Montazcach",["Roca","Normal"],(70,95,85,50,75,95),["Lanzarrocas","Placaje","Aranazo"],"Pokemon Vizcacha Grande",0.9,31.0,"Dientes cortan rocas.","Pies Rapidos"),
    (30,"Picaflor",["Volador"],(40,35,30,60,35,80),["Picotazo","Aranazo"],"Pokemon Picaflor",0.1,0.1,"Zumbido imperceptible.","Levitacion"),
    (31,"Colibrindes",["Volador","Psiquico"],(60,55,50,105,70,130),["Confusion","Picotazo","Aranazo"],"Pokemon Colibri",0.4,0.8,"Ojos ven destellos misticos.","Levitacion"),
    (32,"Tumito",["Acero"],(45,55,65,45,50,40),["Placaje","Ala de Acero"],"Pokemon Fragmento",0.2,4.0,"Metal antiguo flotante.","Cuerpo Puro"),
    (33,"Tumignus",["Acero","Psiquico"],(65,105,110,95,80,65),["Ala de Acero","Confusion","Placaje"],"Pokemon Tumi",1.0,45.0,"Arma ancestral viviente.","Cuerpo Puro"),
    (34,"Huacok",["Roca"],(65,45,80,55,70,30),["Lanzarrocas","Placaje"],"Pokemon Vasija",0.4,15.0,"Vasija de arcilla.","Armadura"),
    (35,"Huacotrato",["Roca","Fantasma"],(80,60,120,85,100,45),["Lenguetazo","Lanzarrocas","Placaje"],"Pokemon Huaco Retrato",1.3,68.0,"Cambia de expresion.","Cuerpo Maldito"),
    (36,"Ajito",["Planta"],(40,45,40,50,40,55),["Latigo Cepa","Placaje"],"Pokemon Aji",0.2,0.5,"Brote picante.","Punto Toxico"),
    (37,"Picantox",["Fuego","Planta"],(70,90,65,100,65,95),["Ascuas","Hoja Afilada","Picotazo Ven."],"Pokemon Rocoto",0.8,12.0,"Esporas incandescentes.","Cuerpo Llama"),
    (38,"Condorito",["Volador"],(60,65,45,40,45,70),["Picotazo","Aranazo"],"Pokemon Polluelo Condor",0.6,5.2,"Polluelo de abismos.","Vista Lince"),
    (39,"Apucondor",["Volador","Siniestro"],(90,115,75,65,80,85),["Picotazo","Mordisco","Aranazo"],"Pokemon Condor",1.9,75.0,"Sombra presagia tormentas.","Presion"),
    (40,"Chinchill",["Normal"],(55,45,50,55,55,80),["Placaje","Aranazo","Grunido"],"Pokemon Chinchilla",0.3,1.8,"Pelaje suave de costa.","Gran Encanto"),
    (41,"Chinchicab",["Normal","Hada"],(75,65,70,80,85,100),["Placaje","Beso Drenador","Aranazo"],"Pokemon Chinchilla Estelar",0.7,9.5,"Destellos de luz estelar.","Gran Encanto"),
    (42,"Tremarcto",["Lucha"],(65,70,55,40,45,50),["Golpe Karate","Aranazo","Placaje"],"Pokemon Oso Cachorro",0.9,40.0,"Practica con troncos.","Indomable"),
    (43,"Ursandino",["Lucha","Tierra"],(100,120,85,50,75,70),["Golpe Karate","Bofeton Lodo","Placaje"],"Pokemon Oso Andino",1.8,160.0,"Zarpazos sismicos.","Indomable"),
    (44,"Piranita",["Agua"],(40,55,35,35,35,70),["Pistola Agua","Placaje","Aranazo"],"Pokemon Pirana",0.2,0.9,"Nada en cardumenes.","Punto Toxico"),
    (45,"Piranatox",["Agua","Veneno"],(65,105,50,85,50,105),["Presa Acuatica","Picotazo Ven.","Mordisco"],"Pokemon Pirana Toxica",0.8,18.0,"Toxina paralizante.","Punto Toxico"),
    (46,"Papa Nativa",["Planta","Tierra"],(60,55,70,55,65,45),["Placaje","Bofeton Lodo","Latigo Cepa"],"Pokemon Tuberculo",0.4,3.5,"Variedad de colores.","Herbivoro"),
    (47,"Papa Chunio",["Planta","Hielo"],(80,70,95,70,85,50),["Rayo Hielo","Latigo Cepa","Placaje"],"Pokemon Papa Helada",0.4,1.5,"Deshidratada por hielo.","Cuerpo Congelado"),
    (48,"Papa Desertica",["Planta","Roca"],(80,85,95,50,70,70),["Lanzarrocas","Latigo Cepa","Placaje"],"Pokemon Papa Arenosa",0.5,12.0,"Piel endurecida.","Robustez"),
    (49,"Papa Selvatica",["Planta","Veneno"],(80,90,75,75,70,60),["Picotazo Ven.","Latigo Cepa","Placaje"],"Pokemon Papa Picante",0.6,5.0,"Espinas venenosas.","Punto Toxico"),
    (50,"Aruy",["Normal","Fantasma"],(55,50,50,50,50,65),["Lenguetazo","Placaje","Grunido"],"Pokemon Espiritu Camelido",0.5,6.0,"Espiritu translucido.","Cuerpo Maldito"),
    (51,"Llama Solar",["Normal","Fuego"],(80,95,70,85,75,95),["Pirotecnia","Placaje","Aranazo"],"Pokemon Llama Solar",1.2,55.0,"Brilla como mediodia.","Cuerpo Llama"),
    (52,"Llama Lunar",["Normal","Siniestro"],(80,95,75,70,85,95),["Mordisco","Placaje","Aranazo"],"Pokemon Llama Lunar",1.2,52.0,"Vaga bajo la luna.","Allanamiento"),
    (53,"Llama Espectral",["Fantasma"],(80,70,80,100,95,75),["Lenguetazo","Confusion","Placaje"],"Pokemon Llama Fantasmal",1.1,2.0,"Atraviesa paredes.","Levitacion"),
    (54,"Zorrin",["Siniestro"],(55,60,45,40,45,70),["Mordisco","Aranazo","Grunido"],"Pokemon Zorro",0.5,8.0,"Sigiloso por dunas.","Ojos Compuestos"),
    (55,"Sechurax",["Siniestro","Tierra"],(75,95,70,60,70,110),["Mordisco","Bofeton Lodo","Aranazo"],"Pokemon Zorro Desierto",1.0,24.0,"Polvo paralizante.","Ojos Compuestos"),
    (56,"Culpeito",["Fuego"],(55,65,45,55,45,75),["Ascuas","Aranazo","Grunido"],"Pokemon Zorro Fuego",0.5,9.0,"Cola de fuego.","Absorbe Fuego"),
    (57,"Vulandino",["Fuego","Siniestro"],(80,105,70,80,70,105),["Pirotecnia","Mordisco","Aranazo"],"Pokemon Zorro Volcan",1.2,38.0,"Ilumina senderos.","Absorbe Fuego"),
    (58,"Muquitox",["Tierra"],(60,65,70,35,55,35),["Bofeton Lodo","Placaje","Aranazo"],"Pokemon Mineral",0.5,40.0,"Ser mineral de grietas.","Cobre Puro"),
    (59,"Muquimetal",["Tierra","Acero"],(70,110,115,50,80,55),["Ala de Acero","Bofeton Lodo","Placaje"],"Pokemon Mineral Ferreo",0.9,70.0,"Cuerpo de cobre.","Cobre Puro"),
    (60,"Tigrillo",["Fuego"],(60,75,55,50,55,85),["Ascuas","Aranazo","Grunido"],"Pokemon Felino Igneo",0.8,22.0,"Huellas humeantes.","Indomable"),
    (61,"Chinchay",["Fuego","Lucha"],(85,115,80,60,75,102),["Golpe Karate","Pirotecnia","Aranazo"],"Pokemon Puma Igneo",1.4,78.0,"Felino de alturas.","Indomable"),
    (62,"Tarasquito",["Dragon"],(60,65,65,55,60,55),["Furia Dragon","Placaje","Aranazo"],"Pokemon Lagartija",0.6,30.0,"Reptil mitologico.","Escama Dragon"),
    (63,"Tarascom",["Dragon","Roca"],(90,100,105,75,80,60),["Furia Dragon","Lanzarrocas","Placaje"],"Pokemon Dragon Roca",1.6,110.0,"Escamas como minerales.","Cabeza Roca"),
    (64,"Pishtaco",["Siniestro","Fantasma"],(70,110,65,80,70,95),["Mordisco","Lenguetazo","Aranazo"],"Pokemon Sombra Nocturna",1.7,55.0,"Leyenda nocturna.","Presion"),
    (65,"Jarjacha",["Normal","Fantasma"],(85,95,80,60,75,80),["Lenguetazo","Placaje","Mordisco"],"Pokemon Hibrido",1.4,70.0,"Cuerpo de camelido.","Intimidacion"),
    (66,"Pututos",["Agua","Sonido"],(90,60,95,85,95,40),["Chirrido","Burbuja","Placaje"],"Pokemon Caracola",1.0,42.0,"Eco de los valles.","Insonorizar"),
    (67,"Quipus",["Fantasma","Normal"],(60,50,85,95,90,70),["Lenguetazo","Confusion","Placaje"],"Pokemon Nudo Ancestral",0.8,4.5,"Secretos de imperios.","Cuerpo Vinculo"),
    (68,"Ceviche",["Agua","Veneno"],(70,85,60,90,70,100),["Picotazo Ven.","Burbuja","Placaje"],"Pokemon Citrico",0.4,2.0,"Fresco pero picante.","Punto Toxico"),
    (69,"Maiz Morado",["Planta"],(90,50,70,80,85,45),["Latigo Cepa","Placaje","Grunido"],"Pokemon Mazorca",0.9,12.0,"Aroma dulce.","Cura Natural"),
    (70,"Colibri Nasca",["Roca","Psiquico"],(60,90,70,95,70,125),["Confusion","Picotazo","Lanzarrocas"],"Pokemon Geoglifo",0.5,35.0,"Geoglifo cobra vida.","Levitacion"),
    (71,"Arana Nasca",["Roca","Veneno"],(70,85,95,65,85,80),["Picotazo Ven.","Lanzarrocas","Picadura"],"Pokemon Geoglifo Aracnido",0.8,50.0,"Patrones geometricos.","Armadura"),
    (72,"Tunche",["Fantasma","Siniestro"],(60,100,60,95,70,105),["Mordisco","Lenguetazo","Aranazo"],"Pokemon Silbador",0.6,3.0,"Imita silbidos.","Sombra Trampa"),
    (73,"Carachama",["Agua","Roca"],(80,80,120,40,90,40),["Placaje","Pistola Agua","Lanzarrocas"],"Pokemon Pez Acorazado",0.7,15.0,"Piel muy dura.","Robustez"),
    (74,"Bufeo Colorado",["Agua","Psiquico"],(95,65,70,100,85,90),["Confusion","Pistola Agua","Placaje"],"Pokemon Delfin Mistico",2.0,95.0,"Delfin de rios.","Manto Espejo"),
    (75,"Chullachaqui",["Planta","Fantasma"],(70,90,65,85,70,100),["Lenguetazo","Hoja Afilada","Aranazo"],"Pokemon Duende",1.1,30.0,"Imita huellas.","Ilusion"),
    (76,"Muki-Muki",["Tierra","Hada"],(65,60,80,85,95,75),["Confusion","Bofeton Lodo","Placaje"],"Pokemon Espiritu Minero",0.5,9.0,"Guia a mineros.","Alma Curativa"),
    (77,"Tunante",["Normal","Psiquico"],(75,70,70,95,80,95),["Confusion","Placaje","Aranazo"],"Pokemon Enmascarado",1.2,40.0,"Mascara satirica.","Ritmo Propio"),
    (78,"Danza de Tijeras",["Lucha","Psiquico"],(70,110,75,70,75,105),["Golpe Karate","Confusion","Placaje"],"Pokemon Danzante",1.7,65.0,"Acrobacias mortales.","Competitivo"),
    (79,"Orquidea Negra",["Planta","Siniestro"],(75,95,70,100,75,80),["Hoja Afilada","Mordisco","Latigo Cepa"],"Pokemon Flor Carnivora",0.6,4.0,"Fragancia embriagadora.","Trampa Arena"),
    (80,"Torito de Pucara",["Roca","Fuego"],(85,90,105,60,85,50),["Lanzarrocas","Ascuas","Placaje"],"Pokemon Ceramica",0.9,80.0,"Irradia calor.","Cabeza Roca"),
    (81,"Dracuy",["Dragon"],(65,70,65,55,60,65),["Furia Dragon","Placaje","Aranazo"],"Pokemon Serpiente Joven",1.5,40.0,"Serpiente celestial.","Levitacion"),
    (82,"Serpior",["Dragon","Volador"],(85,95,80,85,80,100),["Furia Dragon","Picotazo","Placaje"],"Pokemon Serpiente Alada",3.0,180.0,"Canaliza vientos.","Levitacion"),
    (83,"Amaru",["Dragon","Volador"],(100,135,95,125,85,100),["Furia Dragon","Pirotecnia","Ala de Acero"],"Pokemon Serpiente Celestial",4.5,320.0,"Controla las lluvias.","Presion"),
    (84,"Yacumama",["Agua","Dragon"],(100,100,100,100,100,100),["Presa Acuatica","Furia Dragon","Pistola Agua"],"Pokemon Madre Aguas",8.0,650.0,"Madre de los rios.","Multitipo"),
    (85,"Inti-Can",["Fuego","Psiquico"],(105,110,100,115,100,100),["Pirotecnia","Confusion","Aranazo"],"Pokemon Guardian Solar",1.5,90.0,"Guardian del sol.","Sequia"),
    (86,"Killa-Puma",["Hielo","Fantasma"],(105,110,100,115,100,100),["Rayo Hielo","Lenguetazo","Aranazo"],"Pokemon Guardian Lunar",1.4,85.0,"Guardian de la luna.","Bucle Hielo"),
    (87,"Pach-Avis",["Planta","Tierra"],(105,110,100,115,100,100),["Hoja Afilada","Bofeton Lodo","Placaje"],"Pokemon Guardian Bosques",1.6,95.0,"Guardian de bosques.","Herbogenesis"),
    (88,"Wira-Titan",["Psiquico","Roca"],(110,120,130,120,110,80),["Lanzarrocas","Confusion","Ala de Acero"],"Pokemon Arquitecto",3.5,400.0,"Deidad de la tierra.","Tierra Firme"),
    (89,"Supay-Dread",["Siniestro","Fantasma"],(110,130,100,120,110,90),["Mordisco","Lenguetazo","Aranazo"],"Pokemon Guardian Sombras",3.0,380.0,"Deidad del inframundo.","Terrorifico"),
    (90,"Pachamama-Prime",["Planta","Hada"],(110,100,110,130,120,100),["Beso Drenador","Hoja Afilada","Confusion"],"Pokemon Madre Naturaleza",3.2,350.0,"Deidad de la vida.","Herbogenesis"),
    (91,"Perro Sin Pelo",["Fantasma","Psiquico"],(90,85,85,100,110,90),["Lenguetazo","Confusion","Placaje"],"Pokemon Guia Almas",1.0,20.0,"Guia entre mundos.","Cura Floral"),
    (92,"Zorro de las Nieves",["Hielo","Siniestro"],(90,100,80,100,90,110),["Mordisco","Rayo Hielo","Aranazo"],"Pokemon Zorro Nieve",1.3,45.0,"Guardián de pasos.","Allanamiento"),
    (93,"Aurum-Inca",["Acero","Psiquico"],(95,120,110,100,100,75),["Ala de Acero","Confusion","Placaje"],"Pokemon Guerrero Dorado",1.9,150.0,"Golem de oro.","Filtro"),
    (94,"Argentum-Moon",["Acero","Hada"],(95,100,110,120,110,75),["Beso Drenador","Ala de Acero","Confusion"],"Pokemon Guerrero Plateado",1.9,145.0,"Golem de plata.","Filtro"),
    (95,"Bronce-Tari",["Acero","Lucha"],(95,130,120,80,90,75),["Golpe Karate","Ala de Acero","Placaje"],"Pokemon Guerrero Bronce",2.0,160.0,"Golem de bronce.","Puno Ferreo"),
    (96,"Wayra-Wind",["Volador","Electrico"],(90,85,80,120,90,120),["Impactrueno","Picotazo","Confusion"],"Pokemon Viento",2.5,30.0,"Vientos de altura.","Viento Afin"),
    (97,"Paria-Rain",["Agua","Electrico"],(90,80,85,120,95,115),["Impactrueno","Pistola Agua","Burbuja"],"Pokemon Diluvio",2.0,200.0,"Fuerza de diluvios.","Llovizna"),
    (98,"Khamuy-Mist",["Fantasma","Veneno"],(90,80,90,115,105,90),["Chirrido","Lenguetazo","Picotazo Ven."],"Pokemon Niebla",2.2,25.0,"Neblinas impenetrables.","Cuerpo Maldito"),
    (99,"Constelacion Sur",["Psiquico","Normal"],(95,85,90,130,110,105),["Confusion","Placaje","Aranazo"],"Pokemon Cosmos",1.5,40.0,"Guardian del tiempo.","Levitacion"),
    (100,"Apu-Cerro",["Roca","Tierra"],(120,110,140,90,100,60),["Lanzarrocas","Bofeton Lodo","Placaje"],"Pokemon Apu",5.0,800.0,"Espiritu de cerros.","Terraformacion"),
    (101,"Lago-Sagu",["Agua","Hada"],(110,85,100,125,120,95),["Beso Drenador","Pistola Agua","Confusion"],"Pokemon Lago Sagrado",3.0,200.0,"Memoria del agua.","Cura Lluvia"),
    (102,"Chask-Messenger",["Normal","Volador"],(90,100,85,90,85,140),["Picotazo","Aranazo","Placaje"],"Pokemon Mensajero",1.5,35.0,"Mensajero de dioses.","Velocidad Extrema"),
    (103,"Omega-Inca",["Psiquico"],(140,140,140,140,140,140),["Confusion","Ala de Acero","Furia Dragon"],"Pokemon Origen",10.0,1200.0,"Origen de todo.","Multiescama"),
]
POKEDEX_COMPLETA = {}
for _row in _RAW:
    _id, nombre, tipos, st, movs, cat, alt, pes, desc, hab = _row
    _tasa = 3 if _id >= 99 else 5 if _id >= 84 else 45 if _id >= 81 else 150
    POKEDEX_COMPLETA[nombre] = {
        "id": _id, "nombre": nombre, "tipos": tipos,
        "stats_base": {"ps": st[0], "atq": st[1], "def": st[2],
                       "atq_esp": st[3], "def_esp": st[4], "vel": st[5]},
        "movimientos_iniciales": [M_BASE[m] for m in movs if m in M_BASE],
        "categoria": cat, "altura": alt, "peso": pes,
        "descripcion": desc, "habilidad": hab,
        "tasa_captura": _tasa,
    }
print("OK pokedex:", len(POKEDEX_COMPLETA), "Pokemon")


# === APRENDIZAJES POR NIVEL ===
_APR_APRENDIZAJES = {
    "Alpaka": [(7, "Hoja Afilada"), (13, "Bofeton Lodo"), (19, "Rayo Hielo")],
    "Vicunor": [(22, "Lenguetazo"), (28, "Lanzarrocas")],
    "Majestuyocc": [(40, "Rayo Hielo"), (48, "Ala de Acero")],
    "Feligaro": [(7, "Ascuas"), (13, "Mordisco"), (19, "Golpe Karate")],
    "Jaguaris": [(22, "Golpe Karate"), (28, "Pirotecnia")],
    "Incaflame": [(44, "Mordisco"), (52, "Furia Dragon")],
    "Bufeito": [(7, "Burbuja"), (13, "Confusion"), (19, "Rayo Hielo")],
    "Rosadelf": [(22, "Impactrueno"), (28, "Rayo Hielo")],
    "Yacumist": [(44, "Confusion"), (52, "Furia Dragon")],
    "Surito": [(6, "Picadura")],
    "Suripullo": [(12, "Latigo Cepa")],
    "Suriwain": [(22, "Ala de Acero")],
    "Orugueta": [(6, "Picadura")],
    "Tunquid": [(9, "Ascuas"), (15, "Picotazo")],
    "Tunquirex": [(28, "Pirotecnia")],
    "Cuy": [(8, "Golpe Karate")],
    "Chinchill": [(10, "Confusion")],
    "Vizcachin": [(12, "Lanzarrocas")],
    "Picaflor": [(12, "Confusion")],
    "Ajito": [(10, "Picotazo Ven.")],
    "Condorito": [(14, "Mordisco")],
    "Piranita": [(12, "Mordisco")],
    "Huacok": [(12, "Lenguetazo")],
    "Tumito": [(14, "Confusion")],
    "Zorrin": [(16, "Mordisco")],
    "Tarasquito": [(16, "Furia Dragon")],
    "Dracuy": [(20, "Furia Dragon")],
    "Aruy": [(16, "Confusion")],
}
for _n, _lst in _APR_APRENDIZAJES.items():
    if _n in POKEDEX_COMPLETA:
        POKEDEX_COMPLETA[_n]["aprendizajes_por_nivel"] = [
            {"nivel": _nv, "movimiento": M_BASE[_m]}
            for _nv, _m in _lst if _m in M_BASE
        ]
print("Aprendizajes cargados:", len(_APR_APRENDIZAJES))


# === MOVS CARACTERISTICOS: se aprenden al evolucionar a etapa final ===
_MOVS_CARACTERISTICOS = {
    "Majestuyocc": [(36, "Estampida Sagrada")],
    "Incaflame":   [(36, "Rugido Sol Inca")],
    "Yacumist":    [(36, "Eco del Yacumama")],
}
for _n, _lst in _MOVS_CARACTERISTICOS.items():
    if _n in POKEDEX_COMPLETA:
        aprend = POKEDEX_COMPLETA[_n].setdefault("aprendizajes_por_nivel", [])
        existentes = {e["nivel"] for e in aprend}
        for _nv, _m in _lst:
            if _m in M_BASE and _nv not in existentes:
                aprend.append({"nivel": _nv, "movimiento": M_BASE[_m]})
print("OK movs caracteristicos cargados:", list(_MOVS_CARACTERISTICOS.keys()))


# === APRENDIZAJES COMPLETOS POR NIVEL (103 POKEMON) ===
_APRENDIZAJES_FULL = {
    # ----- INICIALES -----
    "Alpaka":       [(7, "Hoja Aguda"), (13, "Bofeton Lodo"), (19, "Rayo Solar"), (25, "Beso Drenador"), (32, "Latigazo")],
    "Vicunor":      [(24, "Lenguetazo"), (30, "Lanzarrocas"), (36, "Psicoataque"), (42, "Latigazo")],
    "Majestuyocc":  [(40, "Rayo Solar"), (48, "Ala de Acero"), (56, "Estampida Sagrada")],

    "Feligaro":     [(7, "Ascuas"), (13, "Mordisco"), (19, "Golpe Karate"), (25, "Rueda Fuego"), (32, "Colmillo Igneo")],
    "Jaguaris":     [(24, "Golpe Karate"), (30, "Pirotecnia"), (36, "Triturar"), (42, "Lanzallamas")],
    "Incaflame":    [(44, "Lanzallamas"), (52, "Pulso Umbrio"), (56, "Rugido Sol Inca")],

    "Bufeito":      [(7, "Burbuja"), (13, "Confusion"), (19, "Rayo Burbuja"), (25, "Beso Drenador"), (32, "Hidrobomba")],
    "Rosadelf":     [(24, "Impactrueno"), (30, "Rayo Hielo"), (36, "Psicorrayo"), (42, "Hidrobomba")],
    "Yacumist":     [(44, "Hidrobomba"), (52, "Psicoataque"), (56, "Eco del Yacumama")],

    # ----- BICHOS DE RUTA -----
    "Surito":       [(6, "Picadura"), (12, "Viento Plata")],
    "Suripullo":    [(12, "Latigo Cepa"), (18, "Viento Plata")],
    "Suriwain":     [(22, "Ala de Acero"), (28, "Golpe Aereo"), (34, "Pajaro Osado")],
    "Orugueta":     [(6, "Picadura"), (12, "Viento Plata")],
    "Crisalida Selva": [(12, "Bofeton Lodo"), (18, "Latigazo")],
    "Mantis-Buho":  [(28, "Golpe Karate"), (34, "Tajo Umbrio"), (40, "Zumbido")],

    # ----- AVE REGIONAL -----
    "Tunquid":      [(9, "Ascuas"), (15, "Picotazo"), (21, "Golpe Aereo")],
    "Tunquirex":    [(28, "Pirotecnia"), (34, "Ala de Acero"), (40, "Pajaro Osado")],
    "Tunquialt":    [(42, "Ala de Acero"), (50, "Pajaro Osado"), (56, "Lanzallamas")],

    # ----- FAUNA COMUN -----
    "Cuy":          [(8, "Golpe Karate"), (14, "Aranazo"), (20, "Patada Salto")],
    "Cuyver":       [(24, "Golpe Karate"), (30, "Patada Salto"), (36, "A Bocajarro")],
    "Cuyzard":      [(34, "A Bocajarro"), (42, "Golpe Bis"), (48, "Patada Salto")],
    "Monito":       [(10, "Latigo Cepa"), (16, "Hoja Aguda"), (22, "Zumbido")],
    "Churotail":    [(22, "Latigazo"), (28, "Hoja Aguda"), (34, "A Bocajarro")],
    "Simiochuro":   [(34, "A Bocajarro"), (42, "Latigazo"), (48, "Golpe Bis")],
    "Sachavacuna":  [(14, "Pistola Agua"), (20, "Rayo Burbuja"), (26, "Acua Cola")],
    "Tapirex":      [(28, "Acua Cola"), (34, "Hidrobomba"), (40, "Terremoto")],
    "Sachavaca Titan": [(42, "Terremoto"), (50, "Hidrobomba"), (56, "A Bocajarro")],

    # ----- 2 ETAPAS -----
    "Vizcachin":    [(12, "Lanzarrocas"), (18, "Avalancha"), (24, "Roca Afilada")],
    "Montazcach":   [(28, "Roca Afilada"), (34, "Terremoto"), (40, "Ala de Acero")],
    "Picaflor":     [(12, "Confusion"), (18, "Golpe Aereo"), (24, "Psicoataque")],
    "Colibrindes":  [(28, "Rayo Hielo"), (34, "Psicoataque"), (40, "Pajaro Osado")],
    "Tumito":       [(14, "Confusion"), (20, "Cabeza Hierro"), (26, "Garra Metal")],
    "Tumignus":     [(30, "Ala de Acero"), (38, "Psicoataque"), (46, "Cabeza Hierro")],
    "Huacok":       [(12, "Lenguetazo"), (18, "Lanzarrocas"), (24, "Vendetta")],
    "Huacotrato":   [(28, "Confusion"), (34, "Bola Sombra"), (40, "Psicoataque")],
    "Ajito":        [(10, "Picotazo Ven."), (16, "Latigo Cepa"), (22, "Colmillo Igneo")],
    "Picantox":     [(28, "Ascuas"), (34, "Lanzallamas"), (40, "Rayo Solar")],
    "Condorito":    [(14, "Mordisco"), (20, "Golpe Aereo"), (26, "Tajo Umbrio")],
    "Apucondor":    [(34, "Lenguetazo"), (40, "Pajaro Osado"), (46, "Triturar")],
    "Chinchill":    [(10, "Confusion"), (16, "Beso Drenador"), (22, "Golpe Bis")],
    "Chinchicab":   [(28, "Beso Drenador"), (34, "Psicorrayo"), (40, "A Bocajarro")],
    "Tremarcto":    [(16, "Golpe Karate"), (22, "Golpe Bis"), (28, "Patada Salto")],
    "Ursandino":    [(34, "A Bocajarro"), (42, "Terremoto"), (48, "Golpe Bis")],
    "Piranita":     [(12, "Mordisco"), (18, "Rayo Burbuja"), (24, "Acua Cola")],
    "Piranatox":    [(28, "Picotazo Ven."), (34, "Acua Cola"), (40, "Hidrobomba")],

    # ----- RAMIFICADAS -----
    "Papa Nativa":   [(10, "Bofeton Lodo"), (16, "Latigo Cepa"), (22, "Rayo Solar")],
    "Papa Chunio":   [(30, "Rayo Hielo"), (36, "Ventisca"), (42, "Rayo Solar")],
    "Papa Desertica":[(30, "Roca Afilada"), (36, "Terremoto"), (42, "Latigazo")],
    "Papa Selvatica":[(30, "Picotazo Ven."), (36, "Zumbido"), (42, "Rayo Solar")],
    "Aruy":          [(16, "Confusion"), (22, "Lenguetazo"), (28, "Bola Sombra")],
    "Llama Solar":   [(34, "Lanzallamas"), (40, "Rayo Solar"), (46, "Colmillo Igneo")],
    "Llama Lunar":   [(34, "Pulso Umbrio"), (40, "Bola Sombra"), (46, "Tajo Umbrio")],
    "Llama Espectral":[(34, "Bola Sombra"), (40, "Vendetta"), (46, "Psicoataque")],

    # ----- POR PIEDRAS -----
    "Zorrin":        [(16, "Mordisco"), (22, "Tajo Umbrio"), (28, "Pulso Umbrio")],
    "Sechurax":      [(30, "Triturar"), (36, "Terremoto"), (42, "Pulso Umbrio")],
    "Culpeito":      [(16, "Ascuas"), (22, "Rueda Fuego"), (28, "Lanzallamas")],
    "Vulandino":     [(30, "Pulso Umbrio"), (36, "Lanzallamas"), (42, "Tajo Umbrio")],
    "Muquitox":      [(14, "Ala de Acero"), (20, "Bofeton Lodo"), (26, "Roca Afilada")],
    "Muquimetal":    [(32, "Ala de Acero"), (38, "Terremoto"), (44, "Cabeza Hierro")],
    "Tigrillo":      [(20, "Rueda Fuego"), (26, "Colmillo Igneo"), (32, "Patada Salto")],
    "Chinchay":      [(36, "A Bocajarro"), (42, "Lanzallamas"), (48, "Roca Afilada")],
    "Tarasquito":    [(16, "Furia Dragon"), (22, "Garra Dragon"), (28, "Roca Afilada")],
    "Tarascom":      [(38, "Cometa Draco"), (44, "Roca Afilada"), (50, "Garra Dragon")],

    # ----- 1 ETAPA -----
    "Pishtaco":      [(30, "Tajo Umbrio"), (40, "Bola Sombra"), (50, "A Bocajarro")],
    "Jarjacha":      [(30, "Lenguetazo"), (40, "Bola Sombra"), (50, "Triturar")],
    "Pututos":       [(24, "Chirrido"), (34, "Hidrobomba"), (44, "Psicorrayo")],
    "Quipus":        [(28, "Lenguetazo"), (38, "Bola Sombra"), (48, "Psicorrayo")],
    "Ceviche":       [(30, "Picotazo Ven."), (40, "Hidrobomba"), (50, "Triturar")],
    "Maiz Morado":   [(28, "Latigo Cepa"), (38, "Rayo Solar"), (48, "Psicorrayo")],
    "Colibri Nasca": [(30, "Confusion"), (40, "Psicoataque"), (50, "Rayo Solar")],
    "Arana Nasca":   [(30, "Picotazo Ven."), (40, "Roca Afilada"), (50, "Terremoto")],
    "Tunche":        [(30, "Tajo Umbrio"), (40, "Bola Sombra"), (50, "Pulso Umbrio")],
    "Carachama":     [(30, "Pistola Agua"), (40, "Hidrobomba"), (50, "Terremoto")],
    "Bufeo Colorado":[(30, "Confusion"), (40, "Psicorrayo"), (50, "Hidrobomba")],
    "Chullachaqui":  [(30, "Lenguetazo"), (40, "Hoja Aguda"), (50, "Bola Sombra")],
    "Muki-Muki":     [(30, "Confusion"), (40, "Roca Afilada"), (50, "Terremoto")],
    "Tunante":       [(30, "Confusion"), (40, "Psicorrayo"), (50, "Golpe Bis")],
    "Danza de Tijeras":[(30, "Golpe Karate"), (40, "A Bocajarro"), (50, "Patada Salto")],
    "Orquidea Negra":[(30, "Hoja Aguda"), (40, "Tajo Umbrio"), (50, "Rayo Solar")],
    "Torito de Pucara":[(30, "Lanzarrocas"), (40, "Lanzallamas"), (50, "Roca Afilada")],

    # ----- PSEUDO Y LEGENDARIOS -----
    "Dracuy":        [(20, "Furia Dragon"), (30, "Garra Dragon"), (40, "Cometa Draco")],
    "Serpior":       [(38, "Ala de Acero"), (48, "Cometa Draco"), (58, "Garra Dragon")],
    "Amaru":         [(50, "Furia Dragon"), (60, "Cometa Draco"), (70, "A Bocajarro")],
    "Yacumama":      [(50, "Hidrobomba"), (60, "Cometa Draco"), (70, "Psicoataque")],
    "Inti-Can":      [(50, "Lanzallamas"), (60, "Rayo Solar"), (70, "Psicoataque")],
    "Killa-Puma":    [(50, "Ventisca"), (60, "Bola Sombra"), (70, "Rayo Hielo")],
    "Pach-Avis":     [(50, "Rayo Solar"), (60, "Terremoto"), (70, "Latigazo")],
    "Wira-Titan":    [(50, "Terremoto"), (60, "Psicoataque"), (70, "Roca Afilada")],
    "Supay-Dread":   [(50, "Tajo Umbrio"), (60, "Bola Sombra"), (70, "A Bocajarro")],
    "Pachamama-Prime":[(50, "Rayo Solar"), (60, "Psicoataque"), (70, "Beso Drenador")],
    "Perro Sin Pelo":[(40, "Lenguetazo"), (50, "Bola Sombra"), (60, "Psicorrayo")],
    "Zorro de las Nieves":[(40, "Ventisca"), (50, "Tajo Umbrio"), (60, "Rayo Hielo")],
    "Aurum-Inca":    [(45, "Cabeza Hierro"), (55, "Psicoataque"), (65, "Ala de Acero")],
    "Argentum-Moon": [(45, "Beso Drenador"), (55, "Ala de Acero"), (65, "Psicorrayo")],
    "Bronce-Tari":   [(45, "A Bocajarro"), (55, "Ala de Acero"), (65, "Golpe Bis")],
    "Wayra-Wind":    [(45, "Trueno"), (55, "Pajaro Osado"), (65, "Bola Voltio")],
    "Paria-Rain":    [(45, "Hidrobomba"), (55, "Trueno"), (65, "Rayo")],
    "Khamuy-Mist":   [(45, "Bola Sombra"), (55, "Tajo Umbrio"), (65, "Pulso Umbrio")],
    "Constelacion Sur":[(50, "Psicoataque"), (60, "Bola Sombra"), (70, "Rayo Solar")],
    "Apu-Cerro":     [(55, "Terremoto"), (65, "Roca Afilada"), (75, "Avalancha")],
    "Lago-Sagu":     [(55, "Hidrobomba"), (65, "Beso Drenador"), (75, "Psicorrayo")],
    "Chask-Messenger":[(55, "Pajaro Osado"), (65, "Golpe Aereo"), (75, "A Bocajarro")],
    "Omega-Inca":    [(70, "Psicoataque"), (80, "Cometa Draco"), (90, "Rayo Solar")],
}

# Aplicar a la Pokedex
_aplicados = 0
for _n, _lst in _APRENDIZAJES_FULL.items():
    if _n in POKEDEX_COMPLETA:
        _aprend = POKEDEX_COMPLETA[_n].setdefault("aprendizajes_por_nivel", [])
        _niveles_existentes = {e["nivel"] for e in _aprend}
        for _nv, _m in _lst:
            if _m in M_BASE and _nv not in _niveles_existentes:
                _aprend.append({"nivel": _nv, "movimiento": M_BASE[_m]})
        _aplicados += 1

print(f"OK aprendizajes FULL: {_aplicados} Pokemon")
