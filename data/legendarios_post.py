# data/legendarios_post.py
# -*- coding: utf-8 -*-
"""E8: Caceria de legendarios con historia."""

# Leyendas (Menores) - todos capturables
LEYENDAS_MENORES = {
    "Inti-Can": {
        "mapa": "ciudad_imperial", "pos": (25, 12),
        "nivel": 60, "es_noche": False, "requiere_medalla": "Medalla Sol de Oro",
        "dialogos": [
            "El aire se vuelve calido de golpe...",
            "!Una silueta dorada desciende del cielo!",
            "Inti-Can: He esperado al digno que porta el Sol de Oro.",
            "Inti-Can: Muestrame tu fuerza, mortal.",
        ],
        "pos_batalla": ["Inti-Can"],
    },
    "Killa-Puma": {
        "mapa": "puno", "pos": (15, 15),
        "nivel": 60, "es_noche": True, "requiere_medalla": "Medalla Sol de Oro",
        "dialogos": [
            "La luna ilumina el lago con un brillo fantasmal...",
            "!Un puma espectral aparece entre las totoras!",
            "Killa-Puma: Solo aparezco ante quien ha probado su valia.",
            "Killa-Puma: Baila conmigo bajo la luna.",
        ],
        "pos_batalla": ["Killa-Puma"],
    },
    "Pach-Avis": {
        "mapa": "puerto_selva", "pos": (10, 10),
        "nivel": 60, "es_noche": False, "requiere_medalla": "Medalla Liana",
        "dialogos": [
            "La selva entera susurra un nombre...",
            "!Pach-Avis, el guardian alado, baja de las copas!",
            "Pach-Avis: El pulmon del mundo me ha hablado de ti.",
            "Pach-Avis: Defiende mi selva y seras recompensado.",
        ],
        "pos_batalla": ["Pach-Avis"],
    },
    "Zorro de las Nieves": {
        "mapa": "huaraz", "pos": (20, 10),
        "nivel": 58, "es_noche": False, "requiere_medalla": "Medalla Glaciar",
        "dialogos": [
            "El viento helado trae un aullido...",
            "!El Zorro de las Nieves se materializa!",
            "Zorro: El frio templa a los debiles.",
            "Zorro: Solo los fuertes merecen mi compania.",
        ],
        "pos_batalla": ["Zorro de las Nieves"],
    },
    "Perro Sin Pelo": {
        "mapa": "ciudad_moche", "pos": (20, 8),
        "nivel": 62, "es_noche": True, "requiere_medalla": "Medalla Sol de Oro",
        "dialogos": [
            "Un ser translucido aparece en la huaca...",
            "!El Perro Sin Pelo custodia el paso entre mundos!",
            "Perro: He guiado almas por milenios.",
            "Perro: Guiare la tuya si lo mereces.",
        ],
        "pos_batalla": ["Perro Sin Pelo"],
    },
    "Aurum-Inca": {
        "mapa": "ciudad_capital", "pos": (30, 8),
        "nivel": 62, "es_noche": False, "requiere_medalla": "Medalla Sol de Oro",
        "dialogos": [
            "Una estatua dorada cobra vida!",
            "Aurum-Inca: Forjado con el oro de los incas.",
            "Aurum-Inca: Solo el mejor forjara su destino.",
        ],
        "pos_batalla": ["Aurum-Inca"],
    },
    "Argentum-Moon": {
        "mapa": "puno", "pos": (28, 20),
        "nivel": 62, "es_noche": True, "requiere_medalla": "Medalla Sol de Oro",
        "dialogos": [
            "El reflejo de la luna se vuelve solido...",
            "Argentum-Moon: La plata lunar me dio forma.",
            "Argentum-Moon: Bailaras conmigo?",
        ],
        "pos_batalla": ["Argentum-Moon"],
    },
    "Bronce-Tari": {
        "mapa": "andahuaylas", "pos": (30, 12),
        "nivel": 62, "es_noche": False, "requiere_medalla": "Medalla Danza",
        "dialogos": [
            "El suelo tiembla con cada paso...",
            "Bronce-Tari: Forjado en bronce, templado en batalla.",
            "Bronce-Tari: Si me vences, te acompanare.",
        ],
        "pos_batalla": ["Bronce-Tari"],
    },
    "Wayra-Wind": {
        "mapa": "ruta_7", "pos": (50, 15),
        "nivel": 58, "es_noche": False, "requiere_medalla": "Medalla Mistico",
        "clima_req": "sol",
        "dialogos": [
            "El viento ruge desde las alturas...",
            "Wayra-Wind: Soy la respiracion de los Andes.",
            "Wayra-Wind: Corre conmigo.",
        ],
        "pos_batalla": ["Wayra-Wind"],
    },
    "Paria-Rain": {
        "mapa": "ruta_8", "pos": (40, 20),
        "nivel": 58, "es_noche": False, "requiere_medalla": "Medalla Liana",
        "clima_req": "lluvia",
        "dialogos": [
            "La lluvia se intensifica de repente...",
            "Paria-Rain: Cada gota lleva mi esencia.",
            "Paria-Rain: El diluvio te limpiara o te ahogara.",
        ],
        "pos_batalla": ["Paria-Rain"],
    },
    "Khamuy-Mist": {
        "mapa": "huaraz", "pos": (40, 15),
        "nivel": 58, "es_noche": False, "requiere_medalla": "Medalla Glaciar",
        "clima_req": "niebla",
        "dialogos": [
            "La niebla se vuelve densa y amenazante...",
            "Khamuy-Mist: Soy el aliento de los pantanos.",
            "Khamuy-Mist: Ven, si puedes verme.",
        ],
        "pos_batalla": ["Khamuy-Mist"],
    },
}


# Legendario MAYOR - Wira-Titan
LEYENDA_MAYOR = {
    "Wira-Titan": {
        "mapa": "ciudad_imperial", "pos": (40, 5),
        "nivel": 75,
        "requiere_medalla": "Medalla Sol de Oro",
        "requiere_capturas": ["Inti-Can", "Killa-Puma", "Pach-Avis",
                              "Aurum-Inca", "Bronce-Tari"],
        "dialogos": [
            "La tierra entera tiembla.",
            "!Los muros de la Ciudad Imperial se agrietan!",
            "Wira-Titan: He sentido despertar a mis hermanos.",
            "Wira-Titan: Has reunido a los guardianes elementales.",
            "Wira-Titan: El equilibrio exige un nuevo arquitecto.",
            "Wira-Titan: Demuestrame que eres digno de mi poder.",
        ],
        "pos_batalla": ["Wira-Titan"],
    },
}


class SistemaLegendariosPost:
    def __init__(self):
        self.capturados = set()
        self.derrotados = set()
        self.invocados = set()  # ya se encontraron

    def puede_invocar(self, nombre, juego):
        """Verifica si el jugador cumple los requisitos."""
        if nombre in self.capturados:
            return False
        leyenda = LEYENDAS_MENORES.get(nombre) or LEYENDA_MAYOR.get(nombre)
        if not leyenda:
            return False
        # Requisito de medalla
        req_med = leyenda.get("requiere_medalla")
        if req_med:
            try:
                if req_med not in juego.gimnasios.medallas_obtenidas:
                    return False
            except Exception:
                return False
        # Requisito de capturas (para mayor)
        req_caps = leyenda.get("requiere_capturas", [])
        for cap in req_caps:
            if cap not in self.capturados:
                return False
        # Requisito de hora
        if leyenda.get("es_noche") is not None:
            try:
                noche_actual = juego.tiempo.es_noche()
                if leyenda["es_noche"] and not noche_actual:
                    return False
                if not leyenda["es_noche"] and noche_actual:
                    return False
            except Exception:
                pass
        # Requisito de clima
        req_clima = leyenda.get("clima_req")
        if req_clima:
            try:
                if juego.tiempo.clima_actual != req_clima:
                    return False
            except Exception:
                pass
        return True

    def registrar_captura(self, nombre):
        self.capturados.add(nombre)

    def registrar_derrota(self, nombre):
        self.derrotados.add(nombre)

    def todos_menores_capturados(self):
        return all(n in self.capturados for n in LEYENDAS_MENORES.keys())


print(f"OK data.legendarios_post ({len(LEYENDAS_MENORES)} menores + {len(LEYENDA_MAYOR)} mayor)")
