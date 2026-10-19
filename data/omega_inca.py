# data/omega_inca.py
# -*- coding: utf-8 -*-
"""E8: Omega-Inca - jefe final multi-fase."""

# Requisito: capturar todos los legendarios menores + Wira-Titan + ser campeon
REQUISITOS_OMEGA = {
    "legendarios": ["Inti-Can", "Killa-Puma", "Pach-Avis",
                    "Zorro de las Nieves", "Perro Sin Pelo",
                    "Aurum-Inca", "Argentum-Moon", "Bronce-Tari",
                    "Wayra-Wind", "Paria-Rain", "Khamuy-Mist",
                    "Wira-Titan"],
    "ser_campeon": True,
}


FASES_OMEGA = {
    1: {
        "nombre": "Omega-Inca - Manifestacion",
        "nivel": 80,
        "hp_mult": 1.0,
        "stats_mult": 1.0,
        "color": (200, 200, 240),
        "dialogo": [
            "!El espacio se distorsiona!",
            "!Una figura de pura energia aparece!",
            "Omega-Inca: He dormido por eones...",
            "Omega-Inca: Y me despiertas con el rugido de tus leyendas.",
            "Omega-Inca: Muy bien, hijo del Tahuantinsuyo.",
            "Omega-Inca: Te mostrare el verdadero poder del origen.",
        ],
    },
    2: {
        "nombre": "Omega-Inca - Despertar",
        "nivel": 90,
        "hp_mult": 1.3,
        "stats_mult": 1.2,
        "color": (255, 180, 100),
        "dialogo": [
            "Omega-Inca: Has resistido el primer asalto.",
            "Omega-Inca: Ahora, liberare mi verdadera forma.",
            "!El aire arde con energia cosmica!",
        ],
    },
    3: {
        "nombre": "Omega-Inca - Origen",
        "nivel": 100,
        "hp_mult": 1.5,
        "stats_mult": 1.4,
        "color": (255, 60, 60),
        "dialogo": [
            "Omega-Inca: !Este es el poder del principio!",
            "Omega-Inca: !El universo entero tiembla!",
            "Omega-Inca: !Destruyeme, si puedes, mortal!",
        ],
    },
}


DIALOGO_VICTORIA = [
    "!El campo entero se ilumina!",
    "Omega-Inca: ...Extraordinario.",
    "Omega-Inca: Has reescrito el destino del Tahuantinsuyo.",
    "Omega-Inca: Los Apus te reconocen como su igual.",
    "Omega-Inca: Que tu leyenda nunca sea olvidada.",
    "!Omega-Inca se desvanece en particulas de luz!",
    "!Has completado el juego!",
]


class SistemaOmegaInca:
    def __init__(self):
        self.fase_actual = 1
        self.activo = False
        self.completado = False

    def puede_desafiar(self, juego):
        """Verifica si el jugador cumple los requisitos."""
        if self.completado:
            return False, "Ya venciste a Omega-Inca."
        # Campeon?
        if REQUISITOS_OMEGA["ser_campeon"]:
            try:
                if not getattr(juego.liga, "es_campeon", False):
                    return False, "Debes ser Campeon de la Liga."
            except Exception:
                return False, "Debes ser Campeon."
        # Legendarios?
        try:
            capturados = juego.legendarios_post.capturados
        except Exception:
            capturados = set()
        faltan = [n for n in REQUISITOS_OMEGA["legendarios"] if n not in capturados]
        if faltan:
            return False, f"Faltan {len(faltan)} leyendas: {faltan[0]}, ..."
        return True, ""


print("OK data.omega_inca")
