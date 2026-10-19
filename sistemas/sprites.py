# sprites.py - Version profesional v2 (GBA 16x24)
"""Sprites pixel art profesionales estilo Pokemon Esmeralda."""
import pygame


class SpriteGenerator:
    W, H = 16, 24
    _cache = {}

    # ==== PALETA BASE ====
    PIEL   = (252, 210, 170)
    PIEL_S = (206, 154, 116)
    PIEL_L = (255, 232, 200)
    PIEL_X = (168, 118, 82)
    NEGRO  = (22, 14, 26)
    LUZ    = (255, 255, 255)
    SOMBRA = (0, 0, 0, 90)

    @staticmethod
    def _px(sp, x, y, c):
        if 0 <= x < 16 and 0 <= y < 24 and c is not None:
            sp.set_at((x, y), c)

    @staticmethod
    def _fill(sp, x0, y0, x1, y1, c):
        for y in range(y0, y1):
            for x in range(x0, x1):
                SpriteGenerator._px(sp, x, y, c)

    @staticmethod
    def _line(sp, x0, y0, x1, y1, c):
        n = max(abs(x1-x0), abs(y1-y0), 1)
        for i in range(n+1):
            x = round(x0 + (x1-x0)*i/n)
            y = round(y0 + (y1-y0)*i/n)
            SpriteGenerator._px(sp, x, y, c)

    # =================================================================
    # DIBUJO DE CUERPO BASE
    # =================================================================
    @staticmethod
    def _cuerpo(sp, direccion, frame, pal):
        """Dibuja cuerpo humanoide base. Devuelve tupla de coords de cabeza."""
        piel    = pal.get("piel", SpriteGenerator.PIEL)
        piel_s  = pal.get("piel_s", SpriteGenerator.PIEL_S)
        piel_l  = pal.get("piel_l", SpriteGenerator.PIEL_L)
        pelo    = pal.get("pelo", (60, 40, 30))
        pelo_s  = pal.get("pelo_s", (30, 20, 15))
        ropa    = pal.get("ropa", (100, 130, 180))
        ropa_s  = pal.get("ropa_s", (60, 80, 120))
        ropa_l  = pal.get("ropa_l", (140, 170, 220))
        panta   = pal.get("pantalon", (50, 56, 92))
        panta_s = pal.get("pantalon_s", (30, 34, 62))
        zapato  = pal.get("zapato", (40, 30, 26))
        zapato_l= pal.get("zapato_l", (86, 66, 52))

        walk = frame  # 0=idle, 1=step izq, 2=step der

        # ==== PIERNAS + ZAPATOS (animacion mejorada) ====
        # 4 frames: 0=idle (pies juntos), 1=paso izq adelante, 2=idle, 3=paso der adelante
        # Para direcciones laterales solo movemos 1 pierna visible
        if walk == 0:
            # Idle: piernas juntas y simetricas
            SpriteGenerator._fill(sp, 5, 18, 7, 22, panta)
            SpriteGenerator._px(sp, 5, 18, panta_s)
            SpriteGenerator._px(sp, 6, 21, panta_s)
            SpriteGenerator._fill(sp, 9, 18, 11, 22, panta)
            SpriteGenerator._px(sp, 10, 18, panta_s)
            SpriteGenerator._px(sp, 9, 21, panta_s)
            # Zapatos
            SpriteGenerator._fill(sp, 4, 22, 7, 23, zapato)
            SpriteGenerator._fill(sp, 9, 22, 12, 23, zapato)
            SpriteGenerator._px(sp, 5, 22, zapato_l)
            SpriteGenerator._px(sp, 10, 22, zapato_l)
        elif walk == 1:
            # Paso con PIERNA IZQUIERDA adelante
            # Pierna izq adelante y levantada
            SpriteGenerator._fill(sp, 4, 16, 6, 22, panta)
            SpriteGenerator._px(sp, 4, 16, panta_s)
            SpriteGenerator._px(sp, 5, 21, panta_s)
            # Pierna derecha atras
            SpriteGenerator._fill(sp, 10, 18, 12, 22, panta)
            SpriteGenerator._px(sp, 11, 18, panta_s)
            # Zapato izq adelantado
            SpriteGenerator._fill(sp, 3, 21, 6, 22, zapato)
            SpriteGenerator._px(sp, 3, 21, zapato_l)
            # Zapato der atras
            SpriteGenerator._fill(sp, 10, 22, 13, 23, zapato)
            SpriteGenerator._px(sp, 11, 22, zapato_l)
        elif walk == 2:
            # Idle intermedio (cuerpo arriba)
            SpriteGenerator._fill(sp, 5, 18, 7, 22, panta)
            SpriteGenerator._px(sp, 5, 18, panta_s)
            SpriteGenerator._fill(sp, 9, 18, 11, 22, panta)
            SpriteGenerator._px(sp, 10, 18, panta_s)
            SpriteGenerator._fill(sp, 4, 22, 7, 23, zapato)
            SpriteGenerator._fill(sp, 9, 22, 12, 23, zapato)
            SpriteGenerator._px(sp, 5, 22, zapato_l)
            SpriteGenerator._px(sp, 10, 22, zapato_l)
        else:
            # walk == 3: Paso con PIERNA DERECHA adelante
            # Pierna izq atras
            SpriteGenerator._fill(sp, 5, 18, 7, 22, panta)
            SpriteGenerator._px(sp, 5, 18, panta_s)
            # Pierna der adelante y levantada
            SpriteGenerator._fill(sp, 9, 16, 11, 22, panta)
            SpriteGenerator._px(sp, 10, 16, panta_s)
            SpriteGenerator._px(sp, 9, 21, panta_s)
            # Zapato izq atras
            SpriteGenerator._fill(sp, 4, 22, 7, 23, zapato)
            SpriteGenerator._px(sp, 5, 22, zapato_l)
            # Zapato der adelantado
            SpriteGenerator._fill(sp, 9, 21, 12, 22, zapato)
            SpriteGenerator._px(sp, 11, 21, zapato_l)

        # ==== TORSO ====
        SpriteGenerator._fill(sp, 4, 9, 12, 18, ropa_s)
        SpriteGenerator._fill(sp, 5, 9, 11, 17, ropa)
        # Highlight superior izquierdo
        SpriteGenerator._fill(sp, 5, 9, 9, 11, ropa_l)
        SpriteGenerator._px(sp, 5, 11, ropa_l)
        # Cierre/franja central
        SpriteGenerator._fill(sp, 7, 10, 9, 17, ropa_s)
        # Cinturon
        SpriteGenerator._fill(sp, 5, 17, 11, 18, (80, 60, 40))

        # ==== BRAZOS (con swing de animacion) ====
        # El brazo contrario a la pierna adelantada va adelante
        arm_offset = 0
        if walk == 1:
            arm_offset = 1  # Brazo derecho adelante
        elif walk == 3:
            arm_offset = -1  # Brazo izquierdo adelante

        if direccion in ("abajo", "arriba"):
            # Brazo izquierdo
            SpriteGenerator._fill(sp, 3, 10 + arm_offset, 5, 15 + arm_offset, ropa_s)
            SpriteGenerator._px(sp, 3, 11 + arm_offset, ropa_l)
            # Brazo derecho
            SpriteGenerator._fill(sp, 11, 10 - arm_offset, 13, 15 - arm_offset, ropa_s)
            SpriteGenerator._px(sp, 12, 11 - arm_offset, ropa)
            # Manos
            SpriteGenerator._fill(sp, 3, 15 + arm_offset, 5, 17 + arm_offset, piel)
            SpriteGenerator._fill(sp, 11, 15 - arm_offset, 13, 17 - arm_offset, piel)
            SpriteGenerator._px(sp, 3, 15 + arm_offset, piel_l)
            SpriteGenerator._px(sp, 11, 15 - arm_offset, piel_l)
        elif direccion == "izquierda":
            SpriteGenerator._fill(sp, 4, 10 + arm_offset, 6, 15 + arm_offset, ropa_s)
            SpriteGenerator._px(sp, 4, 11 + arm_offset, ropa_l)
            SpriteGenerator._fill(sp, 4, 15 + arm_offset, 6, 17 + arm_offset, piel)
        elif direccion == "derecha":
            SpriteGenerator._fill(sp, 10, 10 - arm_offset, 12, 15 - arm_offset, ropa_s)
            SpriteGenerator._px(sp, 11, 11 - arm_offset, ropa)
            SpriteGenerator._fill(sp, 10, 15 - arm_offset, 12, 17 - arm_offset, piel)

        # ==== CABEZA ====
        # Base de la cabeza (cuello + cráneo)
        SpriteGenerator._fill(sp, 5, 7, 11, 10, piel_s)
        SpriteGenerator._fill(sp, 4, 3, 12, 9, piel)
        SpriteGenerator._px(sp, 4, 3, piel_l)
        SpriteGenerator._px(sp, 5, 3, piel_l)
        # Sombra a la derecha
        SpriteGenerator._fill(sp, 11, 3, 12, 9, piel_s)
        SpriteGenerator._px(sp, 10, 9, piel_s)

        # ==== OREJAS ====
        if direccion == "abajo":
            SpriteGenerator._px(sp, 3, 5, piel)
            SpriteGenerator._px(sp, 3, 6, piel)
            SpriteGenerator._px(sp, 12, 5, piel)
            SpriteGenerator._px(sp, 12, 6, piel)
        elif direccion == "izquierda":
            SpriteGenerator._px(sp, 3, 5, piel)
            SpriteGenerator._px(sp, 3, 6, piel)
        elif direccion == "derecha":
            SpriteGenerator._px(sp, 12, 5, piel)
            SpriteGenerator._px(sp, 12, 6, piel)

        # ==== PELO ====
        SpriteGenerator._fill(sp, 4, 2, 12, 5, pelo)
        SpriteGenerator._fill(sp, 4, 5, 5, 7, pelo)
        SpriteGenerator._fill(sp, 11, 5, 12, 7, pelo)
        # Flequillo
        SpriteGenerator._fill(sp, 5, 4, 11, 5, pelo_s)
        SpriteGenerator._px(sp, 6, 3, pelo)
        SpriteGenerator._px(sp, 9, 3, pelo)
        # Mechones
        SpriteGenerator._px(sp, 4, 1, pelo)
        SpriteGenerator._px(sp, 5, 1, pelo)
        SpriteGenerator._px(sp, 8, 1, pelo)
        SpriteGenerator._px(sp, 10, 1, pelo)
        SpriteGenerator._px(sp, 11, 1, pelo)

        # ==== OJOS ====
        if direccion == "abajo":
            SpriteGenerator._fill(sp, 5, 6, 7, 8, SpriteGenerator.LUZ)
            SpriteGenerator._fill(sp, 9, 6, 11, 8, SpriteGenerator.LUZ)
            SpriteGenerator._px(sp, 5, 6, SpriteGenerator.NEGRO)
            SpriteGenerator._px(sp, 6, 6, SpriteGenerator.NEGRO)
            SpriteGenerator._px(sp, 9, 6, SpriteGenerator.NEGRO)
            SpriteGenerator._px(sp, 10, 6, SpriteGenerator.NEGRO)
            SpriteGenerator._px(sp, 5, 7, SpriteGenerator.NEGRO)
            SpriteGenerator._px(sp, 10, 7, SpriteGenerator.NEGRO)
            # Brillo
            SpriteGenerator._px(sp, 5, 6, SpriteGenerator.LUZ)
            SpriteGenerator._px(sp, 9, 6, SpriteGenerator.LUZ)
            # Boca
            SpriteGenerator._px(sp, 7, 9, piel_x := SpriteGenerator.PIEL_X)
            SpriteGenerator._px(sp, 8, 9, piel_x)
        elif direccion == "izquierda":
            SpriteGenerator._px(sp, 5, 6, SpriteGenerator.NEGRO)
            SpriteGenerator._px(sp, 5, 7, SpriteGenerator.NEGRO)
            SpriteGenerator._px(sp, 4, 6, SpriteGenerator.LUZ)
        elif direccion == "derecha":
            SpriteGenerator._px(sp, 10, 6, SpriteGenerator.NEGRO)
            SpriteGenerator._px(sp, 10, 7, SpriteGenerator.NEGRO)
            SpriteGenerator._px(sp, 11, 6, SpriteGenerator.LUZ)

        return (6, 3)  # posicion de cabeza para extras

    # =================================================================
    # EXTRAS (sombreros, accesorios)
    # =================================================================
    @staticmethod
    def _extra_sombrero_paja(sp, tipo_col=(220, 180, 90)):
        SpriteGenerator._fill(sp, 2, 2, 14, 4, tipo_col)
        SpriteGenerator._fill(sp, 4, 0, 12, 3, tipo_col)
        SpriteGenerator._fill(sp, 4, 3, 12, 4, (160, 120, 60))
        SpriteGenerator._px(sp, 5, 1, (255, 220, 130))

    @staticmethod
    def _extra_chullo(sp):
        # Chullo andino multicolor
        SpriteGenerator._fill(sp, 4, 1, 12, 4, (200, 50, 60))
        SpriteGenerator._fill(sp, 4, 2, 12, 3, (250, 220, 60))
        SpriteGenerator._fill(sp, 4, 3, 12, 4, (60, 130, 200))
        SpriteGenerator._px(sp, 7, 0, (200, 50, 60))
        SpriteGenerator._px(sp, 8, 0, (200, 50, 60))
        SpriteGenerator._px(sp, 7, 1, (250, 220, 60))

    @staticmethod
    def _extra_bandana(sp, color=(72, 178, 92)):
        SpriteGenerator._fill(sp, 3, 3, 13, 5, color)
        SpriteGenerator._px(sp, 3, 3, tuple(max(0, c-40) for c in color))

    @staticmethod
    def _extra_capucha(sp, color=(50, 30, 70)):
        SpriteGenerator._fill(sp, 2, 0, 14, 6, color)
        SpriteGenerator._fill(sp, 4, 5, 12, 7, tuple(max(0, c-30) for c in color))
        SpriteGenerator._px(sp, 4, 6, (240, 100, 240))
        SpriteGenerator._px(sp, 11, 6, (240, 100, 240))

    @staticmethod
    def _extra_gorra_jugador(sp):
        """Gorra estilo Brendan de Emerald, con visera."""
        # Base de la gorra (parte de arriba)
        SpriteGenerator._fill(sp, 4, 1, 12, 4, (230, 60, 50))
        # Reflejo claro
        SpriteGenerator._fill(sp, 5, 1, 11, 2, (255, 130, 110))
        # Visera (franja delantera)
        SpriteGenerator._fill(sp, 3, 4, 13, 5, (150, 30, 25))
        # Reflejo visera
        SpriteGenerator._fill(sp, 4, 4, 12, 4, (200, 50, 40))
        # Logo/estrella en el centro
        SpriteGenerator._px(sp, 8, 2, (255, 240, 100))
        SpriteGenerator._px(sp, 7, 2, (255, 240, 100))
        SpriteGenerator._px(sp, 8, 3, (255, 240, 100))
        # Boton lateral
        SpriteGenerator._px(sp, 11, 3, (255, 240, 150))
        # Sombra bajo la gorra
        SpriteGenerator._fill(sp, 4, 5, 12, 6, (40, 22, 12))

    @staticmethod
    @staticmethod
    def _extra_gorra(sp, color=(220, 60, 60)):
        SpriteGenerator._fill(sp, 4, 1, 12, 4, color)
        SpriteGenerator._fill(sp, 3, 3, 13, 5, color)
        SpriteGenerator._px(sp, 5, 1, tuple(min(255, c+40) for c in color))

    @staticmethod
    def _extra_vincha_plumas(sp):
        SpriteGenerator._fill(sp, 4, 2, 12, 4, (200, 40, 80))
        for k, col in enumerate([(250, 220, 60), (60, 200, 220), (250, 220, 60)]):
            x = 5 + k * 3
            SpriteGenerator._px(sp, x, 1, col)
            SpriteGenerator._px(sp, x, 0, col)

    @staticmethod
    def _extra_casco_metal(sp):
        SpriteGenerator._fill(sp, 4, 1, 12, 4, (180, 190, 210))
        SpriteGenerator._fill(sp, 4, 3, 12, 4, (120, 130, 150))
        SpriteGenerator._px(sp, 5, 1, (230, 235, 245))
        SpriteGenerator._px(sp, 8, 0, (220, 60, 60))

    @staticmethod
    def _extra_anteojos(sp):
        SpriteGenerator._px(sp, 5, 6, (30, 30, 40))
        SpriteGenerator._px(sp, 6, 6, (30, 30, 40))
        SpriteGenerator._px(sp, 9, 6, (30, 30, 40))
        SpriteGenerator._px(sp, 10, 6, (30, 30, 40))
        SpriteGenerator._px(sp, 7, 6, (30, 30, 40))
        SpriteGenerator._px(sp, 8, 6, (30, 30, 40))

    @staticmethod
    def _extra_capa(sp, color=(80, 30, 40)):
        SpriteGenerator._fill(sp, 3, 9, 13, 18, color)
        SpriteGenerator._fill(sp, 5, 10, 11, 17, tuple(min(255, c+20) for c in color))
        SpriteGenerator._px(sp, 3, 9, tuple(max(0, c-30) for c in color))

    @staticmethod
    def _extra_labio(sp, color=(120, 180, 220)):
        SpriteGenerator._fill(sp, 4, 9, 12, 18, SpriteGenerator.LUZ)
        SpriteGenerator._fill(sp, 4, 9, 6, 18, (200, 210, 220))
        SpriteGenerator._fill(sp, 5, 17, 11, 18, (200, 210, 220))

    # =================================================================
    # PALETAS POR TIPO
    # =================================================================
    @staticmethod
    def _paleta_jugador():
        # Estilo Emerald: gorra roja, chaqueta, pelo castano oscuro
        return {
            "piel": (250, 210, 170),
            "piel_s": (210, 165, 125),
            "piel_l": (255, 230, 205),
            "pelo": (75, 45, 25),      # Castano oscuro
            "pelo_s": (40, 22, 12),
            "ropa": (230, 70, 60),     # Chaqueta roja (Brendan-style)
            "ropa_s": (170, 35, 30),
            "ropa_l": (255, 130, 110),
            "pantalon": (60, 65, 95),  # Azul oscuro
            "pantalon_s": (35, 40, 60),
            "zapato": (240, 240, 245), # Zapatillas blancas
            "zapato_l": (180, 180, 190),
            "gorra": (230, 60, 50),    # Gorra roja
            "gorra_s": (150, 30, 25),
            "gorra_l": (255, 130, 110),
            "mochila": (240, 200, 80),  # Mochila amarilla
            "mochila_s": (160, 120, 30),
        }

    @staticmethod
    def _paleta_npc(tipo):
        paletas = {
            "pescador": {
                "ropa": (250, 220, 90), "ropa_s": (200, 170, 50),
                "ropa_l": (255, 240, 140), "pelo": (60, 40, 25),
                "pelo_s": (30, 20, 15),
            },
            "campesino": {
                "ropa": (200, 170, 120), "ropa_s": (150, 120, 80),
                "ropa_l": (230, 200, 150), "pelo": (80, 55, 30),
                "pelo_s": (40, 25, 15),
            },
            "anciano": {
                "ropa": (140, 120, 90), "ropa_s": (100, 80, 60),
                "ropa_l": (180, 160, 130), "pelo": (220, 220, 220),
                "pelo_s": (160, 160, 170), "piel": (240, 200, 160),
                "piel_s": (200, 160, 120),
            },
            "dama": {
                "ropa": (240, 100, 150), "ropa_s": (190, 60, 110),
                "ropa_l": (255, 150, 190), "pelo": (60, 30, 25),
                "pelo_s": (30, 15, 10), "pantalon": (200, 80, 120),
                "pantalon_s": (150, 50, 80),
            },
            "nino": {
                "ropa": (100, 180, 240), "ropa_s": (60, 130, 200),
                "ropa_l": (150, 210, 250), "pelo": (80, 50, 30),
                "pelo_s": (40, 25, 15),
            },
            "nina": {
                "ropa": (250, 160, 210), "ropa_s": (200, 110, 160),
                "ropa_l": (255, 200, 230), "pelo": (80, 50, 30),
                "pelo_s": (40, 25, 15),
            },
            "danzante": {
                "ropa": (220, 60, 80), "ropa_s": (160, 30, 50),
                "ropa_l": (255, 120, 130), "pelo": (60, 30, 25),
                "pelo_s": (30, 15, 10),
            },
            "supay": {
                "ropa": (50, 30, 70), "ropa_s": (30, 15, 50),
                "ropa_l": (80, 60, 110), "pelo": (20, 15, 25),
                "pelo_s": (10, 5, 15), "piel": (200, 180, 200),
                "piel_s": (160, 140, 170),
            },
            "chamana": {
                "ropa": (140, 60, 160), "ropa_s": (100, 30, 120),
                "ropa_l": (180, 100, 200), "pelo": (40, 30, 30),
                "pelo_s": (20, 15, 15),
            },
            "guerrero": {
                "ropa": (170, 180, 200), "ropa_s": (120, 130, 150),
                "ropa_l": (210, 220, 240), "pelo": (60, 30, 25),
                "pelo_s": (30, 15, 10),
            },
            "vendedor": {
                "ropa": (200, 100, 100), "ropa_s": (150, 60, 60),
                "ropa_l": (240, 150, 150), "pelo": (50, 30, 20),
                "pelo_s": (25, 15, 10),
            },
            "cientifico": {
                "ropa": (245, 245, 250), "ropa_s": (200, 200, 210),
                "ropa_l": (255, 255, 255), "pelo": (40, 30, 30),
                "pelo_s": (20, 15, 15),
            },
            "sacerdote": {
                "ropa": (180, 50, 60), "ropa_s": (120, 30, 40),
                "ropa_l": (230, 90, 100), "pelo": (50, 30, 20),
                "pelo_s": (25, 15, 10),
            },
            "enfermera": {
                "ropa": (255, 255, 255), "ropa_s": (220, 220, 230),
                "ropa_l": (255, 255, 255), "pelo": (150, 100, 60),
                "pelo_s": (100, 60, 30),
            },
            "tendero": {
                "ropa": (100, 140, 200), "ropa_s": (60, 100, 160),
                "ropa_l": (150, 180, 230), "pelo": (60, 40, 30),
                "pelo_s": (30, 20, 15),
            },
            "profesor": {
                "ropa": (250, 250, 250), "ropa_s": (210, 210, 220),
                "ropa_l": (255, 255, 255), "pelo": (230, 230, 230),
                "pelo_s": (170, 170, 180),
            },
            "guardia": {
                "ropa": (60, 80, 120), "ropa_s": (40, 55, 90),
                "ropa_l": (90, 120, 160), "pelo": (40, 30, 25),
                "pelo_s": (20, 15, 10),
            },
            "montanista": {
                "ropa": (200, 60, 50), "ropa_s": (150, 30, 20),
                "ropa_l": (240, 110, 90), "pelo": (80, 50, 30),
                "pelo_s": (40, 25, 15),
            },
            "explorador": {
                "ropa": (100, 160, 100), "ropa_s": (60, 120, 60),
                "ropa_l": (150, 200, 150), "pelo": (60, 40, 25),
                "pelo_s": (30, 20, 15),
            },
            "empresario": {
                "ropa": (60, 60, 80), "ropa_s": (40, 40, 60),
                "ropa_l": (100, 100, 120), "pelo": (30, 25, 25),
                "pelo_s": (15, 10, 10),
            },
            "civil": {
                "ropa": (150, 150, 160), "ropa_s": (100, 100, 110),
                "ropa_l": (190, 190, 200), "pelo": (60, 40, 30),
                "pelo_s": (30, 20, 15),
            },
        }
        base = SpriteGenerator._paleta_jugador()
        base.update(paletas.get(tipo, {}))
        return base

    # =================================================================
    # EXTRAS SEGUN TIPO
    # =================================================================
    @staticmethod
    def _extras_por_tipo(sp, tipo, direccion):
        if tipo == "jugador":
            SpriteGenerator._extra_gorra_jugador(sp)
        elif tipo == "pescador":
            SpriteGenerator._extra_sombrero_paja(sp, (240, 200, 100))
        elif tipo == "campesino":
            SpriteGenerator._extra_sombrero_paja(sp, (220, 190, 130))
        elif tipo == "anciano":
            SpriteGenerator._extra_sombrero_paja(sp, (170, 150, 100))
        elif tipo == "dama":
            # Moño de pelo
            SpriteGenerator._fill(sp, 3, 3, 5, 7, (60, 30, 25))
            SpriteGenerator._fill(sp, 11, 3, 13, 7, (60, 30, 25))
        elif tipo == "danzante":
            SpriteGenerator._extra_vincha_plumas(sp)
        elif tipo == "supay":
            SpriteGenerator._extra_capucha(sp, (50, 30, 70))
        elif tipo == "chamana":
            SpriteGenerator._extra_vincha_plumas(sp)
            SpriteGenerator._extra_capa(sp, (100, 40, 120))
        elif tipo == "guerrero":
            SpriteGenerator._extra_casco_metal(sp)
        elif tipo == "vendedor":
            SpriteGenerator._extra_gorra(sp, (180, 80, 80))
        elif tipo == "cientifico":
            SpriteGenerator._extra_labio(sp)
            SpriteGenerator._extra_anteojos(sp)
        elif tipo == "sacerdote":
            SpriteGenerator._extra_capa(sp, (160, 40, 50))
        elif tipo == "enfermera":
            # Coña blanca
            SpriteGenerator._fill(sp, 4, 2, 12, 4, (250, 250, 255))
            SpriteGenerator._px(sp, 8, 1, (220, 60, 60))
            SpriteGenerator._px(sp, 8, 2, (220, 60, 60))
        elif tipo == "tendero":
            SpriteGenerator._extra_gorra(sp, (80, 120, 180))
        elif tipo == "profesor":
            SpriteGenerator._extra_labio(sp)
            SpriteGenerator._extra_anteojos(sp)
        elif tipo == "guardia":
            SpriteGenerator._extra_casco_metal(sp)
        elif tipo == "montanista":
            SpriteGenerator._extra_gorra(sp, (200, 60, 50))
        elif tipo == "explorador":
            SpriteGenerator._extra_sombrero_paja(sp, (100, 140, 90))
        elif tipo == "empresario":
            SpriteGenerator._extra_gorra(sp, (40, 40, 60))
            SpriteGenerator._extra_anteojos(sp)
        elif tipo == "nino" or tipo == "nina":
            # Pelo con colita
            SpriteGenerator._px(sp, 12, 3, (80, 50, 30))
            SpriteGenerator._px(sp, 12, 4, (80, 50, 30))

    # =================================================================
    # FUNCIONES PUBLICAS
    # =================================================================
    @staticmethod
    def crear_personaje(tipo, direccion="abajo", frame=0, tam=32):
        """Crea un personaje 16x24 escalado a tam."""
        key = ("chars", tipo, direccion, frame, tam)
        if key in SpriteGenerator._cache:
            return SpriteGenerator._cache[key]

        sp = pygame.Surface((16, 24), pygame.SRCALPHA)
        pal = SpriteGenerator._paleta_npc(tipo) if tipo != "jugador" else SpriteGenerator._paleta_jugador()
        SpriteGenerator._cuerpo(sp, direccion, frame, pal)
        SpriteGenerator._extras_por_tipo(sp, tipo, direccion)

        result = pygame.transform.scale(sp, (tam, int(tam * 24 / 16)))
        SpriteGenerator._cache[key] = result
        return result

    @staticmethod
    def crear_jugador_animado(direccion, frame, tam=32):
        return SpriteGenerator.crear_personaje("jugador", direccion, frame, tam)

    @staticmethod
    def crear_sprite_jugador(direccion="abajo", tam=32):
        return SpriteGenerator.crear_jugador_animado(direccion, 0, tam)

    # =================================================================
    # POKEBALLS + OTROS (mantener)
    # =================================================================
    @staticmethod
    def crear_pokeball(tipo="Freekie", tam=32):
        sp = pygame.Surface((tam, tam), pygame.SRCALPHA)
        cx = cy = tam // 2
        r = tam // 2 - 2
        paleta = {
            "Freekie": ((220, 40, 40), (250, 250, 250)),
            "Super":   ((40, 120, 220), (250, 250, 250)),
            "Ultra":   ((240, 200, 40), (40, 40, 40)),
            "Apu":     ((240, 180, 40), (255, 255, 255)),
        }
        arriba, abajo = paleta.get(tipo, paleta["Freekie"])
        pygame.draw.circle(sp, arriba, (cx, cy), r)
        pygame.draw.rect(sp, abajo, (cx - r, cy, r*2, r))
        pygame.draw.rect(sp, (40, 40, 40), (cx - r, cy - 2, r*2, 4))
        pygame.draw.circle(sp, (250, 250, 250), (cx, cy), 5)
        pygame.draw.circle(sp, (40, 40, 40), (cx, cy), 5, 2)
        pygame.draw.circle(sp, (200, 200, 200), (cx, cy), 2)
        pygame.draw.circle(sp, (40, 40, 40), (cx, cy), r, 2)
        return sp

    # Alias legacy
    @staticmethod
    def crear_sprite_alpaka(tam=64): return pygame.Surface((tam, tam), pygame.SRCALPHA)
    @staticmethod
    def crear_sprite_feligaro(tam=64): return pygame.Surface((tam, tam), pygame.SRCALPHA)
    @staticmethod
    def crear_sprite_bufeito(tam=64): return pygame.Surface((tam, tam), pygame.SRCALPHA)
    @staticmethod
    def crear_sprite_salvaje(nombre, tam=64): return pygame.Surface((tam, tam), pygame.SRCALPHA)
