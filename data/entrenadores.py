# data/entrenadores.py
# -*- coding: utf-8 -*-
"""Entrenadores de la Region Tahuantinsuyo - 48 entrenadores distribuidos."""
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


class Entrenador:
    def __init__(self, nombre, clase, mapa, posicion, equipo,
                 dialogo_pre, dialogo_derrota, recompensa=200):
        self.nombre = nombre
        self.clase = clase
        self.mapa = mapa
        self.posicion = posicion
        self.equipo_nombres = equipo
        self.dialogo_pre = dialogo_pre
        self.dialogo_derrota = dialogo_derrota
        self.recompensa = recompensa
        self.derrotado = False
        self.rematch_nivel = 0  # E1: cuantas veces lo has vuelto a vencer

    def crear_equipo(self, rematch_override=None):
        """Crea el equipo. Si hay rematch, sube niveles."""
        eq = []
        rn = rematch_override if rematch_override is not None else self.rematch_nivel
        bonus = rn * 5  # +5 niveles por cada rematch
        for nom, niv in self.equipo_nombres:
            d = POKEDEX_COMPLETA.get(nom)
            if d:
                eq.append(PokemonBatalla(d, niv + bonus))
            else:
                print(f"WARN Entrenador {self.nombre}: '{nom}' no esta en Pokedex")
        return eq

    def registrar_rematch(self):
        self.rematch_nivel += 1

    def dialogo_rematch(self):
        frases = {
            1: [f"Otra vez tu! Ya no tienes ventaja, {self.nombre}.",
                "Entrene desde la ultima vez. Vamos!"],
            2: [f"Venciste dos veces... pero esta sera la tercera!",
                "Mi equipo ahora es mucho mas fuerte."],
            3: [f"Esto ya es personal. Mi cuarto equipo!",
                "Ya no soy el de antes."],
        }
        return frases.get(self.rematch_nivel, 
                          [f"Jajaja, {self.nombre} vino a retarme?",
                           "Esta vez tengo un as bajo la manga."])


ENTRENADORES = [
    # ==================== RUTA 1 - VALLE DE LOS INICIALES ====================
    Entrenador("Don Lucho","Agricultor","ruta_1",(20,15),
        [("Surito",3),("Surito",4)],
        ["Buena, muchacho! Vas a Moche?","Demuestrame que sabes pisar firme."],
        ["Buena, muchacho!","Asi se pisa firme en la chacra."],150),
    Entrenador("Anita","Nina de la Caleta","ruta_1",(40,12),
        [("Cuy",4),("Chinchill",5)],
        ["Mi Cuy es el mas rapido!","Vamos a ver quien corre mas!"],
        ["Ay, mi Cuy!","Eres bueno, eh?"],180),
    Entrenador("Chico Tito","Pescador","ruta_1",(55,15),
        [("Surito",5),("Cuy",6)],
        ["Oe, causa! Vas a Moche?","A ver si aguantas mi cana!"],
        ["Buena, mano! Tienes punteria."],180),
    Entrenador("Pastorcita Maria","Pastora","ruta_1",(70,20),
        [("Cuy",5),("Chinchill",6),("Tunquid",7)],
        ["Mis animalitos te van a ensenar humildad.","Vamos alla!"],
        ["Aprendiste bien.","Sigue tu camino."],200),
    Entrenador("Nino Explorador","Colegial","ruta_1",(80,14),
        [("Surito",6),("Cuy",6)],
        ["Mi mama me dejo salir a entrenar!","No me ganes muy rapido, porfa!"],
        ["Increible!","Quiero ser como tu de grande."],180),

    # ==================== CIUDAD MOCHE ====================
    Entrenador("Nino Curioso","Colegial","ciudad_moche",(8,12),
        [("Cuy",7),("Surito",8)],
        ["Mi tio dice que el Team Supay es malo!","Pero yo soy mas fuerte que ellos!"],
        ["Ay! Me falta entrenar."],200),
    Entrenador("Dona Rosa","Curandera","ciudad_moche",(12,20),
        [("Chinchill",8),("Pirañita",9)],
        ["Mis yerbas curan todo, menos la derrota.","Quieres probar suerte?"],
        ["Ay, hijito! Eres bueno."],250),
    Entrenador("Pescador Beto","Pescador","ciudad_moche",(28,22),
        [("Pirañita",9),("Carachama",10)],
        ["El mar me dio su fuerza.","A ver si puedes conmigo!"],
        ["Buen combate, chico!"],250),

    # ==================== RUTA 2 - ASCENSO ANDINO ====================
    Entrenador("Pastor Rumi","Pastor Andino","ruta_2",(25,14),
        [("Vizcachin",10),("Tunquid",11),("Orugueta",12)],
        ["El aire de la sierra no perdona.","Tu equipo esta listo para la altura?"],
        ["Tienes buen temple.","Sigue subiendo."],350),
    Entrenador("Arriero Quispe","Arriero","ruta_2",(45,18),
        [("Cuyver",12),("Picaflor",13)],
        ["Voy al Cusco con mis llamas.","Tu me acompanas?"],
        ["Buena pelea!"],400),
    Entrenador("Montanista Juana","Montanista","ruta_2",(65,12),
        [("Vizcachin",13),("Tunquirex",14)],
        ["Escalo estos cerros desde nina!","A ver si sigues mi ritmo."],
        ["Wow, tienes aguante!"],450),
    Entrenador("Nina Flor","Botanica","ruta_2",(80,20),
        [("Ajito",13),("Cuyver",14),("Picaflor",15)],
        ["Las flores de la sierra son magicas!","Pero mis Pokemon son mas fuertes."],
        ["Perfecto! Ahora cuidare mis flores."],400),

    # ==================== PUERTO ANCON ====================
    Entrenador("Capitan Tiburon","Marino","puerto_ancon",(15,25),
        [("Pirañita",16),("Carachama",17)],
        ["El mar de Grau es mi hogar!","Nadie me gana aqui!"],
        ["Bien peleado!"],500),
    Entrenador("Nadadora Sofi","Nadadora","puerto_ancon",(40,22),
        [("Bufeito",17),("Rosadelf",18)],
        ["Nado todos los dias!","Soy como una sirena!"],
        ["Increible! Dejame entrenar mas."],550),
    Entrenador("Viejo Marinero","Veterano","puerto_ancon",(50,25),
        [("Tapirex",18),("Carachama",19),("Bufeito",20)],
        ["Treinta anos navegando!","Y nadie ha vencido a mi equipo."],
        ["Hoy es un dia historico!"],600),

    # ==================== RUTA 3 - PARAMO HELADO ====================
    Entrenador("Arriero Cusi","Arriero","ruta_3",(30,16),
        [("Huacok",18),("Zorrin",19)],
        ["Llevo veinte anos cruzando este paramo.","A ver si aguantas el frio!"],
        ["Buena pelea, forastero.","El lago Titicaca te espera."],500),
    Entrenador("Esquiador Local","Esquiador","ruta_3",(50,14),
        [("Papa Chunio",19),("Vizcachin",20),("Tunquirex",21)],
        ["Bajo de las cumbres a entrenar.","El hielo templa mi espiritu."],
        ["Impresionante! Eres como el viento."],600),
    Entrenador("Pastorcita Nieve","Pastora","ruta_3",(70,20),
        [("Chinchill",20),("Aruy",21)],
        ["Mis ovejas son mi tesoro.","Pero mis Pokemon cuidan de ellas!"],
        ["Eres muy fuerte! Cuida tus pasos."],550),

    # ==================== ANDAHUAYLAS ====================
    Entrenador("Maestra Danza","Danzante","andahuaylas",(10,18),
        [("Cuyver",21),("Simiochuro",22)],
        ["La danza es la vida del valle!","Sigue mis pasos si puedes."],
        ["Tu ritmo es excelente!"],650),
    Entrenador("Musico Local","Musico","andahuaylas",(40,20),
        [("Chinchicab",22),("Picaflor",23)],
        ["Mi flauta hipnotiza a los Pokemon!","No te distraigas!"],
        ["Gran talento tienes!"],700),
    Entrenador("Guerrero Wari","Guerrero","andahuaylas",(50,14),
        [("Tremarcto",23),("Ursandino",24),("Cuyzard",25)],
        ["Nieto del gran Wari!","Mi poder viene de mis ancestros!"],
        ["Lo lograste! Pasas."],800),

    # ==================== RUTA 4 - CORDILLERA ROJA ====================
    Entrenador("Mineros Subterraneos","Minero","ruta_4",(30,16),
        [("Muquitox",24),("Huacok",25)],
        ["Conozco cada tunel de estas montanas.","Nadie me vence en la oscuridad!"],
        ["Buena, sabes pelear en altura."],700),
    Entrenador("Guerra de Piedra","Luchador","ruta_4",(60,14),
        [("Tremarcto",25),("Vizcachin",26),("Ursandino",27)],
        ["Fuerza bruta vence todo!","Ven aqui si te atreves."],
        ["Tienes mas que fuerza! Eso me gusta."],900),

    # ==================== CIUDAD IMPERIAL ====================
    Entrenador("Sabio del Monolito","Anciano","ciudad_imperial",(10,14),
        [("Huacok",27),("Vizcachin",28)],
        ["La piedra ensena paciencia.","Demuestrame que has aprendido!"],
        ["La juventud siempre sorprende."],1000),
    Entrenador("Escriba Real","Escriba","ciudad_imperial",(28,20),
        [("Tumito",28),("Tumignus",29),("Quipus",30)],
        ["Los quipus guardan historias.","Mi equipo tambien cuenta!"],
        ["Sabes leer el combate. Bien."],1100),
    Entrenador("Sacerdote del Sol","Sacerdote","ciudad_imperial",(46,18),
        [("Inti-Can",30),("Apucondor",31),("Condorito",30)],
        ["El sol guia mi mano.","A ti te falta luz!"],
        ["El sol te sonrie. Adios."],1200),

    # ==================== RUTA 5 - ALTIPLANO ====================
    Entrenador("Guia de Altura","Guia","ruta_5",(25,16),
        [("Apucondor",30),("Ursandino",31),("Aruy",30)],
        ["Estas tierras son sagradas.","Debes demostrar respeto!"],
        ["Vaya, si sabes. Continua."],1100),
    Entrenador("Llamero Local","Pastor","ruta_5",(55,14),
        [("Llama Solar",31),("Llama Lunar",32)],
        ["Mis llamas son mi familia.","Mira su poder!"],
        ["Hermoso. Eres bienvenido."],1200),

    # ==================== PUNO ====================
    Entrenador("Barquero Totora","Barquero","puno",(15,25),
        [("Carachama",33),("Bufeo Colorado",34)],
        ["Las islas flotantes son mi hogar.","Mi balsa tiene magia!"],
        ["Bien navegas el lago, amigo."],1300),
    Entrenador("Yatiri Joven","Chamana","puno",(40,22),
        [("Aruy",34),("Huacotrato",35)],
        ["Puedo ver tu espiritu.","Y no es tan fuerte como crees!"],
        ["Tu espiritu es noble. Sigue."],1500),
    Entrenador("Bailarin Diablada","Danzante","puno",(50,20),
        [("Jarjacha",35),("Tunche",36),("Pishtaco",37)],
        ["La diablada es mi vida!","Bailo con espiritus!"],
        ["Impresionante! Los espiritus te aceptan."],1700),

    # ==================== RUTA 6 - NEVADOS ====================
    Entrenador("Alpinista Silvia","Alpinista","ruta_6",(30,14),
        [("Papa Chunio",38),("Zorro de las Nieves",39),("Chinchay",40)],
        ["Conquiste los picos mas altos!","Nadie me gana aqui arriba."],
        ["Asombroso! Eres un verdadero montanista."],1600),
    Entrenador("Nieve Eterna","Veterano","ruta_6",(65,18),
        [("Tunquirex",40),("Apucondor",41),("Ursandino",42)],
        ["Vivo en estas cumbres desde nino.","El frio es mi aliado."],
        ["Gran victoria! Buen viaje."],1900),

    # ==================== HUARAZ ====================
    Entrenador("Guia Cumbre","Guia","huaraz",(15,20),
        [("Chinchay",42),("Zorro de las Nieves",43)],
        ["Solo suben los dignos.","Tu seras uno de ellos?"],
        ["Lo eres! Bienvenido a la cumbre."],2100),
    Entrenador("Mistico Killa","Mistico","huaraz",(45,22),
        [("Killa-Puma",44),("Llama Espectral",43),("Huacotrato",44)],
        ["La luna me dio su bendicion.","Y tu no tienes ninguna!"],
        ["La luna te sonrie tambien. Pasa."],2500),

    # ==================== RUTA 7 - CEJA DE SELVA ====================
    Entrenador("Guia Selva","Guia","ruta_7",(30,18),
        [("Simiochuro",45),("Monito",44),("Churotail",44)],
        ["Conozco cada sendero.","Tu no te pierdas!"],
        ["Buen instinto!"],2200),
    Entrenador("Curandero Amazonico","Curandero","ruta_7",(60,20),
        [("Orquidea Negra",46),("Papa Selvatica",45),("Chullachaqui",46)],
        ["Mis plantas curan y matan.","Cuidado!"],
        ["Tu si sabes de plantas!"],2500),

    # ==================== PUERTO SELVA ====================
    Entrenador("Pescador Amazonico","Pescador","puerto_selva",(15,25),
        [("Piranatox",47),("Carachama",48),("Bufeo Colorado",47)],
        ["El rio me dio todo!","A ver si me lo quitas!"],
        ["Buen combate, hermano!"],2700),
    Entrenador("Brujo de la Tribu","Brujo","puerto_selva",(40,22),
        [("Chullachaqui",48),("Tunche",49),("Mantis-Buho",50)],
        ["Los espiritus me protegen!","No te metas conmigo!"],
        ["Venciste a los espiritus... Increible."],3000),
    Entrenador("Nina Selva","Exploradora","puerto_selva",(50,20),
        [("Simiochuro",49),("Orquidea Negra",50),("Tapirex",49)],
        ["Soy la mejor exploradora del Amazonas!","Sigueme si puedes."],
        ["Eres increible! Gran viaje."],2800),

    # ==================== RUTA 8 - COSTA SUR ====================
    Entrenador("Marino del Sur","Marino","ruta_8",(30,14),
        [("Paria-Rain",51),("Carachama",52),("Sachavaca Titan",51)],
        ["El mar del sur me dio su poder!","A ver si me vences!"],
        ["Buen viajero! Gran batalla."],3000),
    Entrenador("Veterano de Liga","Veterano","ruta_8",(65,18),
        [("Chinchay",52),("Apucondor",53),("Incaflame",53),("Majestuyocc",54)],
        ["He desafiado la Liga tres veces!","Tu no llegaras tan lejos."],
        ["Vaya! Quizas tu si llegues. Suerte."],4000),

    # ==================== CIUDAD CAPITAL ====================
    Entrenador("Ejecutivo de Elite","Ejecutivo","ciudad_capital",(20,20),
        [("Tumignus",53),("Muquimetal",54),("Wayra-Wind",53)],
        ["Mi empresa entrena a los mejores!","No eres uno de ellos."],
        ["Contratarte seria interesante. Adios."],3500),
    Entrenador("Ingeniera de Combate","Cientifica","ciudad_capital",(45,25),
        [("Muquimetal",54),("Tumignus",55),("Incaflame",55),("Aurum-Inca",56)],
        ["La tecnologia vence a la tradicion!","Ya veras!"],
        ["Ambas cosas son importantes. Bien hecho."],4500),

    # ==================== RUTAS ESPECIALES POST-LIGA ====================
    Entrenador("Campeon Retirado","Veterano","ciudad_capital",(30,15),
        [("Amaru",60),("Inti-Can",60),("Killa-Puma",60)],
        ["Fui Campeon hace 20 anos.","Mi equipo sigue siendo temible!"],
        ["Eres mas fuerte que yo en mi mejor momento. Excelente."],10000),
]


def _acomodar_entrenadores_auto():
    """Mueve cada entrenador a la celda caminable mas cercana si no esta en una."""
    try:
        from sistemas.mapa_visual import CAMINABLES, MapaVisual
        for ent in ENTRENADORES:
            try:
                mv = MapaVisual(ent.mapa)
                x, y = ent.posicion
                # Si la posicion original es caminable, dejar asi
                if 0 <= x < mv.ancho and 0 <= y < mv.alto:
                    if mv.tiles[y][x] in CAMINABLES:
                        continue
                # Buscar cerca en espiral
                encontrado = False
                for radio in range(1, 15):
                    for dy in range(-radio, radio + 1):
                        for dx in range(-radio, radio + 1):
                            # Solo el anillo externo
                            if max(abs(dx), abs(dy)) != radio:
                                continue
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < mv.ancho and 0 <= ny < mv.alto:
                                if mv.tiles[ny][nx] in CAMINABLES:
                                    ent.posicion = (nx, ny)
                                    encontrado = True
                                    break
                        if encontrado:
                            break
                    if encontrado:
                        break
            except Exception:
                pass
    except Exception:
        pass


# Ejecutar al importar
_acomodar_entrenadores_auto()



# === ENTRENADORES EXTRA (para balance de EXP antes del gimnasio) ===
ENTRENADORES += [
    Entrenador("Practicante Rosa", "Estudiante", "ruta_1", (30, 18),
        [("Surito", 5), ("Cuy", 5)],
        ["Estoy practicando para ser entrenadora!",
         "Me ayudas con un combate de prueba?"],
        ["Gracias! Aprendi mucho de ti."],
        120),
    Entrenador("Hermano Mayor", "Colegial", "ruta_1", (50, 12),
        [("Surito", 6), ("Cuy", 6), ("Chinchill", 7)],
        ["Mi hermana menor no puede conmigo!",
         "A ver si tu puedes!"],
        ["Bueno, tu si tienes nivel."],
        180),
    Entrenador("Cuidador Tadeo", "Guardia", "ruta_1", (60, 20),
        [("Cuy", 7), ("Surito", 7), ("Chinchill", 8)],
        ["Debo proteger este campo de los Pokemon salvajes.",
         "Pero si quieres pelear, dale!"],
        ["Buena pelea! Vas bien preparado."],
        250),
]


def obtener_entrenador(indice):
    if 0 <= indice < len(ENTRENADORES):
        return ENTRENADORES[indice]
    return None


def entrenadores_en(mapa_id):
    return [e for e in ENTRENADORES if e.mapa == mapa_id]


def interior_de(mapa_id, pos):
    return None


print(f"OK data.entrenadores ({len(ENTRENADORES)} entrenadores)")
