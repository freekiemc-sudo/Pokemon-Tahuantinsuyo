# sistemas/retratos.py - v3 profesional
"""Retratos estilo GBA con detalles unicos por personaje."""
import math
import pygame


class Retratos:
    _cache = {}

    # =================================================================
    # PALETAS INDIVIDUALES
    # =================================================================
    PALETAS = {
        # === PRINCIPALES ===
        "Profesor Kuntur": {
            "piel": (252, 215, 175), "piel_s": (206, 155, 118), "piel_l": (255, 235, 205),
            "pelo": (240, 240, 240), "pelo_s": (180, 180, 190),
            "ropa": (240, 245, 250), "ropa_s": (185, 190, 210),
            "acento": (100, 180, 230), "iris": (95, 145, 200),
            "estilo": "profesor",
        },
        "Mateo": {
            "piel": (245, 195, 150), "piel_s": (200, 145, 105), "piel_l": (255, 225, 190),
            "pelo": (70, 45, 28), "pelo_s": (35, 22, 12),
            "ropa": (225, 70, 70), "ropa_s": (165, 40, 40),
            "acento": (255, 220, 120), "iris": (70, 95, 140),
            "estilo": "gorra",
        },
        "Inca-Roca": {
            "piel": (235, 185, 145), "piel_s": (185, 135, 95), "piel_l": (255, 210, 175),
            "pelo": (25, 18, 12), "pelo_s": (8, 5, 3),
            "ropa": (210, 170, 50), "ropa_s": (140, 105, 20),
            "acento": (255, 230, 100), "iris": (120, 75, 40),
            "estilo": "corona",
        },
        # === GIMNASIO 1 - MOCHE ===
        "Don Fermín": {
            "piel": (220, 165, 125), "piel_s": (170, 120, 85), "piel_l": (245, 195, 155),
            "pelo": (75, 50, 30), "pelo_s": (45, 28, 15),
            "ropa": (220, 185, 140), "ropa_s": (165, 130, 90),
            "acento": (245, 220, 160), "iris": (110, 75, 45),
            "estilo": "sombrero_bigote",
        },
        # === GIMNASIO 2 - ANCON ===
        "Capitán Chata": {
            "piel": (215, 165, 125), "piel_s": (165, 115, 80), "piel_l": (245, 195, 155),
            "pelo": (60, 45, 35), "pelo_s": (30, 22, 18),
            "ropa": (45, 90, 155), "ropa_s": (28, 60, 105),
            "acento": (255, 240, 160), "iris": (75, 105, 140),
            "estilo": "gorra_marino",
        },
        # === GIMNASIO 3 - ANDAHUAYLAS ===
        "Wayra": {
            "piel": (240, 195, 155), "piel_s": (200, 150, 115), "piel_l": (255, 225, 190),
            "pelo": (25, 20, 18), "pelo_s": (10, 8, 8),
            "ropa": (215, 55, 75), "ropa_s": (150, 30, 50),
            "acento": (255, 220, 120), "iris": (85, 50, 35),
            "estilo": "vincha_plumas",
        },
        # === GIMNASIO 4 - IMPERIAL ===
        "Apu-Capataz": {
            "piel": (215, 165, 125), "piel_s": (165, 118, 85), "piel_l": (245, 195, 155),
            "pelo": (35, 25, 18), "pelo_s": (18, 12, 8),
            "ropa": (135, 105, 75), "ropa_s": (85, 65, 45),
            "acento": (230, 200, 90), "iris": (85, 65, 40),
            "estilo": "casco_inca",
        },
        # === GIMNASIO 5 - PUNO ===
        "Yatiri Mama": {
            "piel": (215, 165, 130), "piel_s": (170, 120, 90), "piel_l": (245, 195, 165),
            "pelo": (35, 30, 32), "pelo_s": (15, 12, 15),
            "ropa": (105, 60, 145), "ropa_s": (60, 30, 100),
            "acento": (240, 200, 250), "iris": (70, 45, 90),
            "estilo": "chamana",
        },
        # === GIMNASIO 6 - HUARAZ ===
        "Nieves": {
            "piel": (245, 205, 175), "piel_s": (205, 165, 135), "piel_l": (255, 235, 210),
            "pelo": (200, 210, 235), "pelo_s": (150, 165, 200),
            "ropa": (200, 230, 250), "ropa_s": (150, 185, 215),
            "acento": (130, 220, 245), "iris": (105, 155, 200),
            "estilo": "montanista",
        },
        # === GIMNASIO 7 - SELVA ===
        "Dr. Osho": {
            "piel": (215, 165, 125), "piel_s": (170, 118, 80), "piel_l": (240, 195, 155),
            "pelo": (40, 30, 22), "pelo_s": (20, 15, 12),
            "ropa": (95, 160, 95), "ropa_s": (60, 115, 60),
            "acento": (220, 240, 160), "iris": (85, 120, 75),
            "estilo": "explorador",
        },
        # === GIMNASIO 8 - CAPITAL ===
        "Ingeniero Aza": {
            "piel": (230, 180, 140), "piel_s": (185, 130, 95), "piel_l": (250, 210, 175),
            "pelo": (55, 40, 30), "pelo_s": (28, 20, 15),
            "ropa": (60, 80, 115), "ropa_s": (40, 55, 85),
            "acento": (170, 220, 255), "iris": (75, 100, 140),
            "estilo": "empresario",
        },
        # === EQUIPO SUPAY ===
        "Recluta Alfa": {
            "piel": (200, 155, 120), "piel_s": (155, 110, 80), "piel_l": (230, 185, 145),
            "pelo": (15, 12, 18), "pelo_s": (5, 3, 8),
            "ropa": (55, 35, 75), "ropa_s": (30, 18, 45),
            "acento": (230, 80, 230), "iris": (210, 60, 210),
            "estilo": "capucha_supay",
        },
        "Comandante Sacha": {
            "piel": (200, 155, 120), "piel_s": (150, 105, 75), "piel_l": (230, 185, 145),
            "pelo": (25, 15, 10), "pelo_s": (12, 6, 4),
            "ropa": (70, 30, 60), "ropa_s": (40, 15, 35),
            "acento": (240, 200, 80), "iris": (200, 40, 180),
            "estilo": "mascara_dorada",
        },
        "Gran Inquisidor Túpac": {
            "piel": (200, 155, 120), "piel_s": (150, 105, 75), "piel_l": (230, 185, 145),
            "pelo": (10, 8, 8), "pelo_s": (5, 3, 3),
            "ropa": (45, 25, 55), "ropa_s": (25, 12, 30),
            "acento": (255, 200, 60), "iris": (240, 40, 120),
            "estilo": "corona_dorada_supay",
        },
        "Doctora Killa": {
            "piel": (230, 185, 145), "piel_s": (185, 135, 100), "piel_l": (250, 210, 175),
            "pelo": (30, 25, 40), "pelo_s": (12, 10, 20),
            "ropa": (150, 60, 180), "ropa_s": (95, 30, 120),
            "acento": (230, 190, 255), "iris": (180, 60, 200),
            "estilo": "cientifica",
        },
        "Comandante Illa": {
            "piel": (220, 170, 130), "piel_s": (175, 125, 90), "piel_l": (245, 200, 160),
            "pelo": (15, 15, 20), "pelo_s": (5, 5, 10),
            "ropa": (90, 45, 65), "ropa_s": (55, 25, 40),
            "acento": (255, 190, 100), "iris": (150, 100, 50),
            "estilo": "mascara_plata",
        },
        "Comandante Rumi": {
            "piel": (215, 165, 125), "piel_s": (170, 118, 85), "piel_l": (240, 195, 155),
            "pelo": (55, 50, 45), "pelo_s": (25, 22, 20),
            "ropa": (75, 75, 90), "ropa_s": (45, 45, 60),
            "acento": (200, 210, 230), "iris": (110, 130, 150),
            "estilo": "casco_metalico",
        },
        # === NPCs IMPORTANTES ===
        "Enfermera Tambostop": {
            "piel": (250, 215, 180), "piel_s": (210, 170, 135), "piel_l": (255, 235, 210),
            "pelo": (110, 60, 30), "pelo_s": (70, 35, 15),
            "ropa": (255, 250, 245), "ropa_s": (215, 205, 195),
            "acento": (225, 60, 60), "iris": (85, 105, 65),
            "estilo": "enfermera",
        },
        "Tendero": {
            "piel": (230, 185, 140), "piel_s": (185, 135, 100), "piel_l": (250, 210, 170),
            "pelo": (60, 45, 30), "pelo_s": (30, 22, 15),
            "ropa": (95, 145, 205), "ropa_s": (60, 100, 155),
            "acento": (245, 220, 150), "iris": (85, 105, 130),
            "estilo": "gorra_tendero",
        },
    }

    ALIASES = {
        "prof": "Profesor Kuntur", "kuntur": "Profesor Kuntur",
        "profesor": "Profesor Kuntur", "molle": "Profesor Kuntur",
        "mateo": "Mateo", "rival": "Mateo",
        "inca-roca": "Inca-Roca", "inca": "Inca-Roca", "roca": "Inca-Roca",
        "fermin": "Don Fermín", "fermín": "Don Fermín",
        "chata": "Capitán Chata", "capitan": "Capitán Chata",
        "wayra": "Wayra", "danzante": "Wayra",
        "apu-capataz": "Apu-Capataz", "capataz": "Apu-Capataz", "kallpa": "Apu-Capataz",
        "yatiri": "Yatiri Mama", "chamana": "Yatiri Mama",
        "nieves": "Nieves", "killa-wasi": "Nieves",
        "osho": "Dr. Osho", "doctor osho": "Dr. Osho",
        "aza": "Ingeniero Aza", "ingeniero": "Ingeniero Aza",
        "recluta": "Recluta Alfa", "supay": "Recluta Alfa", "alfa": "Recluta Alfa",
        "sacha": "Comandante Sacha", "comandante sacha": "Comandante Sacha",
        "tupac": "Gran Inquisidor Túpac", "túpac": "Gran Inquisidor Túpac",
        "killa": "Doctora Killa", "doctora killa": "Doctora Killa",
        "illa": "Comandante Illa", "rumi": "Comandante Rumi",
        "enfermera": "Enfermera Tambostop", "tambo": "Enfermera Tambostop",
        "tendero": "Tendero", "vendedor": "Tendero",
    }

    @classmethod
    def _resolver(cls, nombre):
        if not nombre:
            return "Mateo"
        if nombre in cls.PALETAS:
            return nombre
        bajo = str(nombre).lower().strip()
        for k, v in cls.ALIASES.items():
            if k in bajo:
                return v
        for key in cls.PALETAS:
            if key.lower() in bajo or bajo in key.lower():
                return key
        return "Mateo"

    # =================================================================
    @classmethod
    def obtener(cls, nombre, tam=100, t=0.0):
        quien = cls._resolver(nombre)
        frame = int(t * 30) % 120
        key = (quien, tam, frame)
        if key in cls._cache:
            return cls._cache[key]
        try:
            surf = cls._dibujar(quien, tam, frame)
        except Exception:
            import traceback; traceback.print_exc()
            surf = pygame.Surface((tam, tam), pygame.SRCALPHA)
        cls._cache[key] = surf
        return surf

    @classmethod
    def obtener_animado(cls, nombre, tam=100, t=0.0, hablando=False, expresion="normal", **kw):
        quien = cls._resolver(nombre)
        frame = int(t * 60) % 240
        parpadeo = (frame % 180) < 4
        # F4: en expresion "sorpresa" o "feliz" no parpadea
        if expresion in ("sorpresa", "feliz"):
            parpadeo = False
        boca_abierta = hablando and ((frame // 8) % 2 == 0)
        # En sorpresa, la boca siempre esta abierta
        if expresion == "sorpresa":
            boca_abierta = True
        bob = int(math.sin(t * 1.8) * 1)
        key = (quien, tam, "anim", parpadeo, boca_abierta, bob, expresion)
        if key in cls._cache:
            return cls._cache[key]
        try:
            surf = cls._dibujar(quien, tam, frame, parpadeo, boca_abierta, bob, expresion)
        except Exception:
            import traceback; traceback.print_exc()
            surf = pygame.Surface((tam, tam), pygame.SRCALPHA)
        cls._cache[key] = surf
        return surf

    # =================================================================
    # RENDER PRINCIPAL 64x64
    # =================================================================
    @classmethod
    def _dibujar(cls, nombre, tam, frame, parpadeo=False, boca_abierta=False, bob=0, expresion="normal"):
        p = cls.PALETAS[nombre]
        s = pygame.Surface((64, 64), pygame.SRCALPHA)
        # Cuerpo / ropa
        cls._cuerpo(s, p, bob)
        # Cara
        cls._cara(s, p, bob)
        # Orejas
        cls._orejas(s, p, bob)
        # Pelo
        cls._pelo(s, p, bob, nombre)
        # Ojos
        cls._ojos(s, p, bob, parpadeo)
        # Cejas
        cls._cejas(s, p, bob, nombre)
        # Nariz y boca
        cls._nariz_boca(s, p, bob, boca_abierta)
        # Detalles de estilo
        cls._extras_estilo(s, p, bob, nombre, p.get("estilo", ""))
        # F4: aplicar expresion (sobreescribe ojos/boca/cejas)
        cls._aplicar_expresion(s, p, bob, expresion)
        return pygame.transform.smoothscale(s, (tam, tam))

    @classmethod
    def _aplicar_expresion(cls, s, p, bob, expresion):
        """F4: sobreescribe partes del rostro segun la expresion."""
        if expresion == "normal" or expresion is None:
            return
        C = (18, 12, 20)
        piel = p["piel"]
        piel_s = p["piel_s"]
        pelo_s = p["pelo_s"]
        iris = p.get("iris", (80, 100, 140))

        # Zona de ojos a limpiar
        OJOS_RECT = (18, 24 + bob, 30, 12)  # x, y, w, h
        BOCA_RECT = (24, 37 + bob, 18, 12)

        if expresion == "feliz":
            # Limpiar ojos y cejas
            pygame.draw.rect(s, piel, OJOS_RECT)
            pygame.draw.rect(s, piel, (18, 21 + bob, 30, 4))
            # Ojos curvos felices
            pygame.draw.arc(s, C, (18, 26 + bob, 12, 8), math.pi + 0.2, 2*math.pi - 0.2, 2)
            pygame.draw.arc(s, C, (36, 26 + bob, 12, 8), math.pi + 0.2, 2*math.pi - 0.2, 2)
            # Cejas altas
            pygame.draw.line(s, pelo_s, (18, 22 + bob), (28, 21 + bob), 2)
            pygame.draw.line(s, pelo_s, (38, 21 + bob), (48, 22 + bob), 2)
            # Boca sonriente grande
            pygame.draw.rect(s, piel, BOCA_RECT)
            pygame.draw.ellipse(s, C, (26, 39 + bob, 14, 6))
            pygame.draw.ellipse(s, (170, 80, 100), (28, 40 + bob, 10, 4))
            pygame.draw.line(s, (240, 210, 220), (28, 40 + bob), (36, 40 + bob), 1)

        elif expresion == "enojado":
            # Limpiar ojos y cejas
            pygame.draw.rect(s, piel, OJOS_RECT)
            pygame.draw.rect(s, piel, (18, 21 + bob, 30, 4))
            # Cejas anguladas hacia el centro (mas bajas)
            for i in range(7):
                x = 18 + i
                y = 22 + bob + i // 2
                s.set_at((x, y), pelo_s)
                s.set_at((x, y + 1), pelo_s)
                x = 39 + i
                y = 22 + bob + (6 - i) // 2
                s.set_at((x, y), pelo_s)
                s.set_at((x, y + 1), pelo_s)
            # Ojos entrecerrados
            pygame.draw.ellipse(s, C, (18, 27 + bob, 12, 5))
            pygame.draw.ellipse(s, C, (36, 27 + bob, 12, 5))
            pygame.draw.ellipse(s, (250, 250, 250), (19, 28 + bob, 8, 3))
            pygame.draw.ellipse(s, (250, 250, 250), (37, 28 + bob, 8, 3))
            pygame.draw.ellipse(s, iris, (20, 28 + bob, 4, 3))
            pygame.draw.ellipse(s, iris, (38, 28 + bob, 4, 3))
            # Boca con comilla
            pygame.draw.rect(s, piel, BOCA_RECT)
            pygame.draw.arc(s, C, (26, 42 + bob, 14, 6), 0.3, math.pi - 0.3, 2)

        elif expresion == "triste":
            pygame.draw.rect(s, piel, OJOS_RECT)
            pygame.draw.rect(s, piel, (18, 21 + bob, 30, 4))
            # Cejas tristes
            pygame.draw.line(s, pelo_s, (18, 25 + bob), (28, 23 + bob), 2)
            pygame.draw.line(s, pelo_s, (38, 23 + bob), (48, 25 + bob), 2)
            # Ojos con lagrima
            pygame.draw.ellipse(s, C, (20, 27 + bob, 10, 6))
            pygame.draw.ellipse(s, C, (36, 27 + bob, 10, 6))
            pygame.draw.ellipse(s, (250, 250, 250), (21, 28 + bob, 7, 4))
            pygame.draw.ellipse(s, (250, 250, 250), (37, 28 + bob, 7, 4))
            pygame.draw.ellipse(s, iris, (22, 29 + bob, 4, 3))
            pygame.draw.ellipse(s, iris, (38, 29 + bob, 4, 3))
            # Lagrima
            pygame.draw.circle(s, (150, 200, 240), (20, 34 + bob), 1)
            pygame.draw.circle(s, (200, 230, 250), (20, 34 + bob), 1)
            # Boca triste
            pygame.draw.rect(s, piel, BOCA_RECT)
            pygame.draw.arc(s, C, (26, 41 + bob, 14, 5), math.pi + 0.3, 2*math.pi - 0.3, 2)

        elif expresion == "sorpresa":
            pygame.draw.rect(s, piel, OJOS_RECT)
            pygame.draw.rect(s, piel, (18, 21 + bob, 30, 4))
            # Cejas muy altas
            pygame.draw.line(s, pelo_s, (18, 20 + bob), (28, 19 + bob), 2)
            pygame.draw.line(s, pelo_s, (38, 19 + bob), (48, 20 + bob), 2)
            # Ojos muy abiertos
            pygame.draw.circle(s, C, (24, 29 + bob), 6)
            pygame.draw.circle(s, C, (40, 29 + bob), 6)
            pygame.draw.circle(s, (250, 250, 250), (24, 29 + bob), 5)
            pygame.draw.circle(s, (250, 250, 250), (40, 29 + bob), 5)
            pygame.draw.circle(s, iris, (24, 29 + bob), 3)
            pygame.draw.circle(s, iris, (40, 29 + bob), 3)
            pygame.draw.circle(s, C, (24, 29 + bob), 2)
            pygame.draw.circle(s, C, (40, 29 + bob), 2)
            s.set_at((22, 27 + bob), (255, 255, 255))
            s.set_at((38, 27 + bob), (255, 255, 255))
            # Boca abierta O
            pygame.draw.rect(s, piel, BOCA_RECT)
            pygame.draw.ellipse(s, C, (28, 39 + bob, 10, 7))
            pygame.draw.ellipse(s, (170, 80, 100), (30, 41 + bob, 6, 4))

        elif expresion == "pensando":
            pygame.draw.rect(s, piel, OJOS_RECT)
            pygame.draw.rect(s, piel, (18, 21 + bob, 30, 4))
            # Una ceja arriba, otra normal
            pygame.draw.line(s, pelo_s, (18, 22 + bob), (28, 21 + bob), 2)
            pygame.draw.line(s, pelo_s, (38, 22 + bob), (48, 22 + bob), 2)
            # Ojos mirando hacia arriba
            pygame.draw.ellipse(s, C, (20, 27 + bob, 10, 6))
            pygame.draw.ellipse(s, C, (36, 27 + bob, 10, 6))
            pygame.draw.ellipse(s, (250, 250, 250), (21, 27 + bob, 8, 4))
            pygame.draw.ellipse(s, (250, 250, 250), (37, 27 + bob, 8, 4))
            pygame.draw.ellipse(s, iris, (22, 27 + bob, 4, 3))
            pygame.draw.ellipse(s, iris, (38, 27 + bob, 4, 3))
            # Boca recta
            pygame.draw.rect(s, piel, BOCA_RECT)
            pygame.draw.line(s, C, (27, 41 + bob), (37, 41 + bob), 1)

    @classmethod
    def _cuerpo(cls, s, p, bob):
        C = (18, 12, 20)
        # Cuello
        pygame.draw.rect(s, C, (26, 44 + bob, 12, 10))
        pygame.draw.rect(s, p["piel_s"], (28, 44 + bob, 8, 9))
        pygame.draw.rect(s, p["piel"], (30, 44 + bob, 5, 7))
        # Hombrera
        pygame.draw.rect(s, C, (4, 52 + bob, 56, 12))
        pygame.draw.polygon(s, p["ropa"], [
            (6, 53 + bob), (58, 53 + bob), (60, 64), (4, 64)
        ])
        # Highlight superior
        pygame.draw.polygon(s, p["ropa_s"], [
            (26, 53 + bob), (38, 53 + bob), (37, 57 + bob), (27, 57 + bob)
        ])
        # Detalle de cuello/accento
        pygame.draw.polygon(s, p["acento"], [
            (30, 53 + bob), (34, 53 + bob), (33, 56 + bob), (31, 56 + bob)
        ])

    @classmethod
    def _cara(cls, s, p, bob):
        C = (18, 12, 20)
        # Silueta de cara (mejor forma, mas ancha arriba)
        cara = [
            (18, 14), (46, 14), (49, 19), (50, 28),
            (48, 38), (42, 44), (22, 44), (16, 38),
            (14, 28), (15, 19),
        ]
        # Sombra del contorno
        pygame.draw.polygon(s, C, [(x+1, y+1+bob) for x, y in cara])
        # Cara base
        pygame.draw.polygon(s, p["piel"], [(x, y+bob) for x, y in cara])
        # Sombra derecha (efecto 3D)
        pygame.draw.polygon(s, p["piel_s"], [
            (38, 15+bob), (46, 15+bob), (49, 19+bob), (50, 28+bob),
            (48, 38+bob), (42, 44+bob),
            (40, 40+bob), (44, 30+bob), (42, 20+bob), (38, 16+bob)
        ])
        # Sombra bajo mentón
        pygame.draw.polygon(s, p["piel_s"], [
            (22, 42+bob), (42, 42+bob), (40, 45+bob), (24, 45+bob)
        ])
        # Mejilla iluminada (izquierda)
        pygame.draw.ellipse(s, p["piel_l"], (17, 26+bob, 8, 7))
        # Rubor suave
        pygame.draw.ellipse(s, (250, 170, 160, 100), (17, 34+bob, 7, 4))

    @classmethod
    def _orejas(cls, s, p, bob):
        C = (18, 12, 20)
        # Izquierda
        pygame.draw.ellipse(s, C, (11, 24+bob, 6, 12))
        pygame.draw.ellipse(s, p["piel"], (12, 25+bob, 4, 10))
        pygame.draw.ellipse(s, p["piel_s"], (12, 28+bob, 2, 5))
        # Derecha
        pygame.draw.ellipse(s, C, (47, 24+bob, 6, 12))
        pygame.draw.ellipse(s, p["piel"], (47, 25+bob, 4, 10))
        pygame.draw.ellipse(s, p["piel_s"], (47, 28+bob, 2, 5))

    @classmethod
    def _pelo(cls, s, p, bob, nombre):
        pelo, pelo_s = p["pelo"], p["pelo_s"]
        estilo = p.get("estilo", "")
        # Base de pelo
        pygame.draw.polygon(s, pelo, [
            (14, 13+bob), (48, 13+bob), (50, 18+bob),
            (46, 16+bob), (32, 22+bob), (18, 16+bob),
            (13, 19+bob)
        ])
        # Sombra derecha
        pygame.draw.polygon(s, pelo_s, [
            (40, 14+bob), (46, 16+bob), (49, 20+bob), (46, 17+bob)
        ])
        # Linea divisoria
        pygame.draw.line(s, pelo_s, (17, 19+bob), (46, 19+bob), 1)
        # Mechones laterales (mas natural)
        pygame.draw.polygon(s, pelo, [(13, 17+bob), (18, 15+bob), (17, 30+bob), (13, 28+bob)])
        pygame.draw.polygon(s, pelo, [(50, 17+bob), (45, 15+bob), (46, 30+bob), (50, 28+bob)])
        # Mechones sueltos arriba
        if estilo == "profesor":
            for cx in (20, 26, 32, 38, 44):
                pygame.draw.polygon(s, pelo, [(cx-2, 13+bob), (cx, 8+bob), (cx+2, 13+bob)])
        elif estilo in ("gorra", "gorra_marino", "gorra_tendero"):
            pass  # la gorra tapa
        else:
            pygame.draw.polygon(s, pelo, [(22, 13+bob), (24, 9+bob), (26, 13+bob)])
            pygame.draw.polygon(s, pelo, [(35, 13+bob), (37, 9+bob), (39, 13+bob)])

    @classmethod
    def _ojos(cls, s, p, bob, parpadeo):
        oy = 29 + bob
        cls._ojo(s, 23, oy, p, parpadeo, espejo=False)
        cls._ojo(s, 41, oy, p, parpadeo, espejo=True)

    @classmethod
    def _ojo(cls, s, cx, cy, p, parpadeo, espejo=False):
        C = (18, 12, 20)
        if parpadeo:
            pygame.draw.line(s, C, (cx-4, cy), (cx+3, cy), 2)
            pygame.draw.line(s, C, (cx-3, cy-1), (cx+2, cy-1), 1)
            return
        # Cuenca
        pygame.draw.ellipse(s, C, (cx-5, cy-4, 11, 8))
        # Blanco
        pygame.draw.ellipse(s, (252, 252, 250), (cx-4, cy-3, 8, 6))
        # Iris
        iris_col = p.get("iris", (80, 100, 140))
        pygame.draw.ellipse(s, iris_col, (cx-3, cy-3, 5, 5))
        # Pupila
        pygame.draw.ellipse(s, (14, 14, 24), (cx-2, cy-2, 3, 4))
        # Brillo (mas grande y definido)
        s.set_at((cx-3, cy-2), (255, 255, 255))
        s.set_at((cx-2, cy-2), (255, 255, 255))
        s.set_at((cx+1, cy), (230, 230, 240))
        # Pestana superior gruesa
        pygame.draw.line(s, C, (cx-5, cy-4), (cx+4, cy-4), 2)
        # Pestana inferior
        pygame.draw.line(s, C, (cx-4, cy+3), (cx+3, cy+3), 1)
        # Lagrimal
        if not espejo:
            s.set_at((cx-4, cy+2), (200, 180, 180))

    @classmethod
    def _cejas(cls, s, p, bob, nombre):
        pelo_s = p["pelo_s"]
        oy = 24 + bob
        # Cejas con forma (mas expresivas)
        # Cejas izq
        for i in range(6):
            x = 19 + i
            y = oy - int(abs(i - 2.5) * 0.4)
            s.set_at((x, y), pelo_s)
            s.set_at((x, y + 1), pelo_s)
        # Cejas der
        for i in range(6):
            x = 39 + i
            y = oy - int(abs(i - 2.5) * 0.4)
            s.set_at((x, y), pelo_s)
            s.set_at((x, y + 1), pelo_s)
        # Cejas de enojo para algunos
        if p.get("estilo") in ("corona", "corona_dorada_supay", "capucha_supay"):
            # Cejas bajas
            for i in range(6):
                x = 19 + i
                s.set_at((x, oy + 1), pelo_s)
                x = 39 + i
                s.set_at((x, oy + 1), pelo_s)

    @classmethod
    def _nariz_boca(cls, s, p, bob, boca_abierta):
        C = (18, 12, 20)
        ny = 36 + bob
        # Nariz mas definida
        s.set_at((31, ny), p["piel_s"])
        s.set_at((32, ny), p["piel_s"])
        s.set_at((31, ny+1), p["piel_s"])
        s.set_at((32, ny+1), p["piel_s"])
        s.set_at((32, ny+2), p["piel_s"])
        s.set_at((30, ny), p["piel_l"])
        # Boca
        by = 41 + bob
        if boca_abierta:
            pygame.draw.ellipse(s, C, (27, by, 10, 5))
            pygame.draw.ellipse(s, (160, 70, 95), (29, by+1, 6, 3))
            pygame.draw.line(s, (240, 210, 220), (29, by+1), (35, by+1), 1)
        else:
            # Sonrisa leve
            pygame.draw.arc(s, C, (27, by-1, 10, 5),
                           math.pi + 0.4, 2 * math.pi - 0.4, 1)
            s.set_at((37, by), C)

    # =================================================================
    # EXTRAS POR ESTILO
    # =================================================================
    @classmethod
    def _extras_estilo(cls, s, p, bob, nombre, estilo):
        C = (18, 12, 20)
        acento = p["acento"]

        if estilo == "profesor":
            # Lentes redondos
            pygame.draw.circle(s, C, (23, 29+bob), 8, 2)
            pygame.draw.circle(s, C, (41, 29+bob), 8, 2)
            pygame.draw.rect(s, C, (30, 28+bob, 4, 2))
            pygame.draw.line(s, C, (15, 29+bob), (11, 28+bob), 2)
            pygame.draw.line(s, C, (49, 29+bob), (53, 28+bob), 2)
            # Brillos de lentes
            pygame.draw.line(s, (240, 250, 255), (19, 26+bob), (22, 25+bob), 1)
            pygame.draw.line(s, (240, 250, 255), (37, 26+bob), (40, 25+bob), 1)
            # Barba tupida blanca
            pygame.draw.polygon(s, p["pelo"], [
                (16, 42+bob), (18, 48+bob), (32, 54+bob),
                (46, 48+bob), (48, 42+bob), (46, 48+bob),
                (38, 52+bob), (32, 52+bob), (26, 50+bob),
                (20, 47+bob)
            ])
            pygame.draw.polygon(s, p["pelo_s"], [
                (40, 44+bob), (46, 48+bob), (44, 50+bob), (38, 52+bob)
            ])
            pygame.draw.rect(s, p["pelo"], (24, 40+bob, 16, 3))

        elif estilo == "gorra":
            # Gorra roja con visera
            pygame.draw.ellipse(s, C, (10, 5+bob, 44, 15))
            pygame.draw.ellipse(s, p["ropa"], (11, 6+bob, 42, 13))
            pygame.draw.ellipse(s, (255, 120, 120), (12, 6+bob, 40, 5))
            # Logo pokebola
            pygame.draw.circle(s, (252, 252, 252), (32, 13+bob), 5)
            pygame.draw.line(s, C, (27, 13+bob), (37, 13+bob), 2)
            pygame.draw.circle(s, C, (32, 13+bob), 5, 2)
            pygame.draw.circle(s, acento, (32, 13+bob), 2)
            # Visera
            pygame.draw.polygon(s, C, [(8, 19+bob), (56, 19+bob), (58, 24+bob), (6, 24+bob)])
            pygame.draw.polygon(s, p["ropa_s"], [(9, 20+bob), (55, 20+bob), (57, 23+bob), (7, 23+bob)])
            pygame.draw.line(s, (255, 200, 200), (13, 21+bob), (48, 21+bob), 1)
            # Boton
            pygame.draw.circle(s, acento, (32, 8+bob), 2)
            pygame.draw.circle(s, (252, 252, 252), (32, 8+bob), 1)

        elif estilo == "corona":
            for k in (-8, 0, 8):
                x0 = 32 + k
                pygame.draw.polygon(s, C, [(x0-3, 12+bob), (x0, 2+bob), (x0+3, 12+bob)])
                pygame.draw.polygon(s, acento, [(x0-2, 11+bob), (x0, 3+bob), (x0+2, 11+bob)])
                pygame.draw.circle(s, (255, 240, 140), (x0, 5+bob), 2)
            pygame.draw.rect(s, C, (18, 12+bob, 28, 4))
            pygame.draw.rect(s, acento, (19, 12+bob, 26, 3))
            pygame.draw.rect(s, (240, 60, 60), (30, 13+bob, 4, 2))

        elif estilo == "sombrero_bigote":
            # Sombrero de paja
            pygame.draw.ellipse(s, C, (0, 12+bob, 64, 12))
            pygame.draw.ellipse(s, acento, (1, 13+bob, 62, 10))
            pygame.draw.ellipse(s, (150, 110, 60), (2, 20+bob, 60, 4))
            pygame.draw.ellipse(s, C, (20, 2+bob, 24, 14))
            pygame.draw.ellipse(s, acento, (21, 3+bob, 22, 12))
            pygame.draw.rect(s, (130, 90, 50), (21, 12+bob, 22, 3))
            # Bigote
            pygame.draw.rect(s, p["pelo_s"], (24, 42+bob, 16, 2))
            pygame.draw.rect(s, p["pelo_s"], (24, 43+bob, 4, 2))
            pygame.draw.rect(s, p["pelo_s"], (36, 43+bob, 4, 2))
            pygame.draw.rect(s, p["pelo_s"], (26, 40+bob, 12, 2))

        elif estilo == "gorra_marino":
            pygame.draw.ellipse(s, C, (12, 6+bob, 40, 12))
            pygame.draw.ellipse(s, p["ropa"], (13, 7+bob, 38, 10))
            pygame.draw.ellipse(s, (100, 150, 220), (14, 7+bob, 36, 4))
            # Insignia dorada
            pygame.draw.circle(s, acento, (32, 12+bob), 4)
            pygame.draw.circle(s, C, (32, 12+bob), 4, 1)
            pygame.draw.line(s, C, (30, 12+bob), (34, 12+bob), 1)
            pygame.draw.line(s, C, (32, 10+bob), (32, 14+bob), 1)
            # Visera
            pygame.draw.polygon(s, C, [(10, 18+bob), (54, 18+bob), (56, 22+bob), (8, 22+bob)])
            pygame.draw.polygon(s, p["ropa_s"], [(11, 19+bob), (53, 19+bob), (55, 21+bob), (9, 21+bob)])

        elif estilo == "vincha_plumas":
            pygame.draw.rect(s, C, (14, 14+bob, 36, 5))
            for i, col in enumerate([(250, 220, 60), (60, 200, 220), (250, 220, 60), (200, 80, 200)]):
                x = 16 + i * 9
                pygame.draw.rect(s, col, (x, 14+bob, 6, 4))
            # Plumas
            for i, (col, dx) in enumerate([((250, 220, 60), -1), ((60, 200, 220), 1), ((250, 60, 120), -1)]):
                px = 32 + i * 8 - 8
                pygame.draw.polygon(s, col, [
                    (px, 14+bob), (px+2, 4+bob), (px+4, 14+bob)
                ])

        elif estilo == "casco_inca":
            # Casco de oro
            pygame.draw.polygon(s, C, [(10, 16+bob), (54, 16+bob), (52, 4+bob), (12, 4+bob)])
            pygame.draw.polygon(s, acento, [(11, 15+bob), (53, 15+bob), (51, 5+bob), (13, 5+bob)])
            # Detalle de plumas
            for x in (18, 26, 34, 42):
                pygame.draw.polygon(s, (240, 60, 60), [(x, 5+bob), (x+2, 1+bob), (x+4, 5+bob)])
            # Banda frontal
            pygame.draw.rect(s, (150, 30, 30), (12, 12+bob, 40, 3))
            # Circulo central
            pygame.draw.circle(s, (255, 240, 180), (32, 8+bob), 3)
            pygame.draw.circle(s, C, (32, 8+bob), 3, 1)

        elif estilo == "chamana":
            # Vincha y plumas de colores
            pygame.draw.rect(s, C, (14, 14+bob, 36, 5))
            colores = [(240, 60, 60), (240, 200, 60), (60, 180, 100), (80, 120, 220)]
            for i, col in enumerate(colores):
                x = 14 + i * 9
                pygame.draw.rect(s, col, (x, 14+bob, 8, 4))
            # Colgantes de cuentas
            for x in (18, 46):
                for k in range(3):
                    col = [(240, 60, 60), (240, 200, 60), (60, 180, 100)][k]
                    pygame.draw.circle(s, col, (x, 20+bob + k*2), 1)
            # Linea vertical entre los ojos (chamana)
            pygame.draw.line(s, (240, 200, 100), (32, 20+bob), (32, 26+bob), 1)

        elif estilo == "montanista":
            # Gorra beanie
            pygame.draw.ellipse(s, C, (12, 4+bob, 40, 16))
            pygame.draw.ellipse(s, p["ropa"], (13, 5+bob, 38, 14))
            pygame.draw.ellipse(s, (255, 120, 120), (14, 5+bob, 36, 5))
            # Vuelta
            pygame.draw.rect(s, p["ropa_s"], (13, 16+bob, 38, 5))
            # Pompon
            pygame.draw.circle(s, (255, 255, 255), (32, 4+bob), 3)
            pygame.draw.circle(s, (220, 220, 220), (32, 5+bob), 2)

        elif estilo == "explorador":
            # Sombrero tipo safari
            pygame.draw.ellipse(s, C, (6, 14+bob, 52, 8))
            pygame.draw.ellipse(s, acento, (7, 15+bob, 50, 6))
            pygame.draw.ellipse(s, C, (20, 4+bob, 24, 14))
            pygame.draw.ellipse(s, acento, (21, 5+bob, 22, 12))
            pygame.draw.rect(s, (100, 60, 30), (21, 14+bob, 22, 3))
            # Cinta
            pygame.draw.rect(s, (140, 40, 40), (21, 10+bob, 22, 2))

        elif estilo == "empresario":
            # Cabello engominado
            pygame.draw.polygon(s, p["pelo_s"], [
                (14, 14+bob), (50, 14+bob), (48, 10+bob), (16, 10+bob)
            ])
            # Anteojos rectangulares
            pygame.draw.rect(s, C, (16, 25+bob, 14, 8), 2)
            pygame.draw.rect(s, C, (34, 25+bob, 14, 8), 2)
            pygame.draw.line(s, C, (30, 28+bob), (34, 28+bob), 2)
            # Reflejo
            pygame.draw.line(s, (240, 250, 255), (18, 27+bob), (24, 27+bob), 1)
            # Corbata
            pygame.draw.polygon(s, (140, 40, 40), [
                (30, 54+bob), (34, 54+bob), (33, 60+bob), (31, 60+bob)
            ])

        elif estilo == "capucha_supay":
            # Capucha
            pygame.draw.polygon(s, p["ropa"], [
                (10, 10+bob), (54, 10+bob), (52, 30+bob), (48, 30+bob),
                (48, 16+bob), (16, 16+bob), (16, 30+bob), (12, 30+bob)
            ])
            pygame.draw.polygon(s, p["ropa_s"], [
                (48, 16+bob), (52, 24+bob), (50, 30+bob), (48, 30+bob)
            ])
            # Capucha bajando
            pygame.draw.polygon(s, p["ropa_s"], [
                (16, 15+bob), (48, 15+bob), (48, 16+bob), (16, 16+bob)
            ])
            # Ojos rojos brillantes
            pygame.draw.circle(s, acento, (24, 28+bob), 3)
            pygame.draw.circle(s, acento, (40, 28+bob), 3)
            pygame.draw.circle(s, (255, 240, 255), (24, 28+bob), 1)
            pygame.draw.circle(s, (255, 240, 255), (40, 28+bob), 1)

        elif estilo == "mascara_dorada":
            # Capucha y mascara ceremonial
            pygame.draw.polygon(s, p["ropa"], [
                (8, 12+bob), (56, 12+bob), (54, 34+bob), (10, 34+bob)
            ])
            # Mascara dorada
            pygame.draw.polygon(s, acento, [
                (16, 18+bob), (48, 18+bob), (46, 44+bob), (18, 44+bob)
            ])
            pygame.draw.polygon(s, (180, 130, 20), [
                (18, 20+bob), (46, 20+bob), (44, 42+bob), (20, 42+bob)
            ])
            # Ojos de mascara
            pygame.draw.polygon(s, C, [(22, 26+bob), (28, 26+bob), (26, 32+bob), (24, 32+bob)])
            pygame.draw.polygon(s, C, [(36, 26+bob), (42, 26+bob), (40, 32+bob), (38, 32+bob)])
            # Ojos rojos
            pygame.draw.circle(s, (200, 40, 180), (25, 29+bob), 2)
            pygame.draw.circle(s, (200, 40, 180), (39, 29+bob), 2)
            # Lineas decorativas
            pygame.draw.line(s, (100, 60, 0), (22, 36+bob), (42, 36+bob), 1)
            pygame.draw.line(s, (100, 60, 0), (24, 40+bob), (40, 40+bob), 1)

        elif estilo == "corona_dorada_supay":
            # Capucha
            pygame.draw.polygon(s, p["ropa"], [
                (8, 10+bob), (56, 10+bob), (54, 40+bob), (10, 40+bob)
            ])
            # Cara visible (palida)
            pygame.draw.polygon(s, (200, 180, 190), [
                (18, 18+bob), (46, 18+bob), (44, 42+bob), (20, 42+bob)
            ])
            # Ojos brillantes rojo
            pygame.draw.circle(s, (240, 40, 120), (24, 28+bob), 3)
            pygame.draw.circle(s, (240, 40, 120), (40, 28+bob), 3)
            pygame.draw.circle(s, (255, 220, 240), (24, 28+bob), 1)
            pygame.draw.circle(s, (255, 220, 240), (40, 28+bob), 1)
            # Sonrisa malvada
            pygame.draw.arc(s, (100, 20, 60), (24, 36+bob, 16, 6), 0.2, math.pi - 0.2, 2)
            # Corona dorada
            for k in (-10, -3, 3, 10):
                x0 = 32 + k
                pygame.draw.polygon(s, acento, [(x0-2, 8+bob), (x0, 0+bob), (x0+2, 8+bob)])
            pygame.draw.rect(s, acento, (18, 8+bob, 28, 4))
            pygame.draw.circle(s, (240, 40, 120), (32, 10+bob), 2)

        elif estilo == "cientifica":
            # Lentes
            pygame.draw.circle(s, C, (23, 29+bob), 7, 2)
            pygame.draw.circle(s, C, (41, 29+bob), 7, 2)
            pygame.draw.rect(s, C, (30, 28+bob, 4, 2))
            # Labio blanco
            pygame.draw.polygon(s, (250, 250, 255), [
                (16, 52+bob), (48, 52+bob), (46, 64), (18, 64)
            ])
            # Pelo recogido
            pygame.draw.polygon(s, p["pelo"], [
                (10, 13+bob), (14, 10+bob), (50, 10+bob), (54, 13+bob),
                (54, 16+bob), (10, 16+bob)
            ])

        elif estilo == "mascara_plata":
            pygame.draw.polygon(s, p["ropa"], [
                (8, 10+bob), (56, 10+bob), (54, 40+bob), (10, 40+bob)
            ])
            # Mascara de plata
            pygame.draw.polygon(s, (200, 210, 230), [
                (18, 18+bob), (46, 18+bob), (44, 42+bob), (20, 42+bob)
            ])
            pygame.draw.polygon(s, (150, 160, 180), [
                (18, 20+bob), (46, 20+bob), (44, 42+bob), (20, 42+bob), (20, 20+bob)
            ])
            # Ojos
            pygame.draw.polygon(s, C, [(22, 26+bob), (28, 26+bob), (26, 32+bob), (24, 32+bob)])
            pygame.draw.polygon(s, C, [(36, 26+bob), (42, 26+bob), (40, 32+bob), (38, 32+bob)])
            # Reflejos plateados
            pygame.draw.line(s, (255, 255, 255), (20, 22+bob), (22, 22+bob), 1)
            pygame.draw.line(s, (255, 255, 255), (42, 22+bob), (44, 22+bob), 1)

        elif estilo == "casco_metalico":
            # Casco completo
            pygame.draw.polygon(s, C, [
                (10, 16+bob), (54, 16+bob), (52, 0+bob), (12, 0+bob)
            ])
            pygame.draw.polygon(s, (140, 155, 180), [
                (11, 15+bob), (53, 15+bob), (51, 1+bob), (13, 1+bob)
            ])
            # Reflejos
            pygame.draw.line(s, (240, 250, 255), (16, 4+bob), (20, 12+bob), 1)
            pygame.draw.line(s, (240, 250, 255), (40, 4+bob), (44, 12+bob), 1)
            # Visor
            pygame.draw.rect(s, (40, 60, 90), (14, 14+bob, 36, 4))
            pygame.draw.line(s, (150, 200, 240), (16, 15+bob), (48, 15+bob), 1)
            # Tornillos
            pygame.draw.circle(s, (200, 210, 230), (14, 18+bob), 1)
            pygame.draw.circle(s, (200, 210, 230), (50, 18+bob), 1)

        elif estilo == "enfermera":
            # Coña blanca con cruz roja
            pygame.draw.ellipse(s, C, (14, 2+bob, 36, 14))
            pygame.draw.ellipse(s, (250, 250, 255), (15, 3+bob, 34, 12))
            pygame.draw.rect(s, p["acento"], (30, 4+bob, 4, 10))
            pygame.draw.rect(s, p["acento"], (27, 7+bob, 10, 4))
            # Pelo suave
            pygame.draw.polygon(s, p["pelo"], [
                (14, 15+bob), (18, 12+bob), (46, 12+bob), (50, 15+bob)
            ])

        elif estilo == "gorra_tendero":
            pygame.draw.ellipse(s, C, (10, 6+bob, 44, 14))
            pygame.draw.ellipse(s, p["ropa"], (11, 7+bob, 42, 12))
            pygame.draw.ellipse(s, (140, 180, 230), (12, 7+bob, 40, 4))
            pygame.draw.polygon(s, C, [(8, 17+bob), (56, 17+bob), (58, 21+bob), (6, 21+bob)])
            pygame.draw.polygon(s, p["ropa_s"], [(9, 18+bob), (55, 18+bob), (57, 20+bob), (7, 20+bob)])


print("OK sistemas.retratos v3")
