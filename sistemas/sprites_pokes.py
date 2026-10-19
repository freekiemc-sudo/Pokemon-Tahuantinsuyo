# sistemas/sprites_pokes.py
# -*- coding: utf-8 -*-
"""
Sprites de Pokemon estilo GBA (32x32) con formas orgánicas, sombreado
y animaciones de idle y caminar.
"""
import pygame
import math
import hashlib


class SpriteGenerator:
    _cache = {}
    _FRAMES_IDLE = 4
    _FRAMES_WALK = 4

    # Paletas de 5 tonos: (sombra_profunda, sombra, base, luz, brillo)
    PALETA_TIPO = {
        "Planta":    ((20, 60, 20),    (40, 120, 40),   (90, 200, 90),   (180, 240, 160), (230, 255, 220)),
        "Fuego":     ((90, 20, 10),    (160, 50, 20),   (240, 130, 60),  (255, 200, 130), (255, 240, 200)),
        "Agua":      ((20, 50, 110),   (40, 90, 170),   (90, 160, 230),  (170, 220, 250), (230, 245, 255)),
        "Normal":    ((100, 80, 60),   (150, 130, 100), (210, 190, 160), (245, 235, 210), (255, 250, 240)),
        "Bicho":     ((60, 80, 20),    (110, 140, 40),  (170, 200, 80),  (220, 240, 150), (250, 255, 200)),
        "Tierra":    ((80, 50, 20),    (130, 90, 40),   (200, 160, 90),  (240, 210, 150), (255, 240, 210)),
        "Hada":      ((140, 60, 100),  (200, 100, 160),(240, 160, 210), (255, 220, 240), (255, 240, 250)),
        "Psiquico":  ((100, 20, 80),   (170, 50, 120),  (230, 100, 180), (255, 180, 220), (255, 240, 250)),
        "Psíquico":  ((100, 20, 80),   (170, 50, 120),  (230, 100, 180), (255, 180, 220), (255, 240, 250)),
        "Siniestro": ((30, 15, 45),    (50, 30, 70),    (110, 80, 130),  (170, 140, 190), (220, 200, 240)),
        "Volador":   ((60, 80, 130),   (100, 130, 190),(160, 190, 230), (220, 235, 250), (255, 255, 255)),
        "Roca":      ((70, 50, 30),    (110, 85, 55),   (170, 140, 100), (210, 190, 150), (240, 230, 200)),
        "Acero":     ((70, 80, 100),   (110, 120, 145),(170, 185, 205), (220, 230, 245), (255, 255, 255)),
        "Lucha":     ((80, 20, 10),    (130, 40, 20),   (200, 85, 60),   (240, 150, 130), (255, 220, 200)),
        "Veneno":    ((70, 20, 90),    (110, 40, 140),  (170, 90, 200),  (220, 160, 240), (255, 230, 255)),
        "Fantasma":  ((50, 30, 80),    (80, 50, 120),   (140, 100, 180), (190, 160, 220), (240, 220, 255)),
        "Hielo":     ((40, 100, 150),  (80, 160, 200),  (150, 220, 245), (220, 245, 255), (255, 255, 255)),
        "Dragon":    ((30, 30, 100),   (50, 60, 160),   (100, 110, 220), (180, 190, 250), (230, 240, 255)),
        "Dragón":    ((30, 30, 100),   (50, 60, 160),   (100, 110, 220), (180, 190, 250), (230, 240, 255)),
        "Electrico": ((100, 80, 10),   (170, 140, 20),  (240, 210, 70),  (255, 245, 150), (255, 255, 220)),
        "Eléctrico": ((100, 80, 10),   (170, 140, 20),  (240, 210, 70),  (255, 245, 150), (255, 255, 220)),
        "Sonido":    ((40, 100, 100),  (80, 160, 160),  (150, 220, 220), (210, 245, 245), (255, 255, 255)),
    }

    CATEGORIAS = {
        "Alpaka":"cuadrupedo","Vicunor":"cuadrupedo","Majestuyocc":"cuadrupedo",
        "Feligaro":"cuadrupedo","Jaguaris":"cuadrupedo","Incaflame":"cuadrupedo",
        "Cuy":"cuadrupedo","Cuyver":"cuadrupedo","Cuyzard":"cuadrupedo",
        "Chinchill":"cuadrupedo","Chinchicab":"cuadrupedo",
        "Vizcachin":"cuadrupedo","Montazcach":"cuadrupedo",
        "Tremarcto":"cuadrupedo","Ursandino":"cuadrupedo",
        "Zorrin":"cuadrupedo","Sechurax":"cuadrupedo",
        "Culpeito":"cuadrupedo","Vulandino":"cuadrupedo",
        "Tigrillo":"cuadrupedo","Chinchay":"cuadrupedo",
        "Sachavacuna":"cuadrupedo","Tapirex":"cuadrupedo","Sachavaca Titan":"cuadrupedo",
        "Aruy":"cuadrupedo","Llama Solar":"cuadrupedo","Llama Lunar":"cuadrupedo",
        "Llama Espectral":"cuadrupedo","Perro Sin Pelo":"cuadrupedo",
        "Zorro de las Nieves":"cuadrupedo","Tarasquito":"cuadrupedo","Tarascom":"cuadrupedo",
        "Killa-Puma":"cuadrupedo","Muki-Muki":"cuadrupedo",
        "Tunquid":"ave","Tunquirex":"ave","Tunquialt":"ave",
        "Condorito":"ave","Apucondor":"ave","Picaflor":"ave","Colibrindes":"ave",
        "Colibri Nasca":"ave","Arana Nasca":"ave","Chask-Messenger":"ave",
        "Bufeito":"acuatico","Rosadelf":"acuatico","Yacumist":"acuatico",
        "Piranita":"acuatico","Piranatox":"acuatico","Carachama":"acuatico",
        "Bufeo Colorado":"acuatico","Ceviche":"acuatico","Pututos":"acuatico",
        "Yacumama":"acuatico","Lago-Sagu":"acuatico","Paria-Rain":"acuatico",
        "Dracuy":"serpiente","Serpior":"serpiente","Amaru":"serpiente",
        "Pishtaco":"espiritu","Jarjacha":"espiritu","Tunche":"espiritu",
        "Khamuy-Mist":"espiritu","Chullachaqui":"espiritu","Quipus":"espiritu",
        "Tunante":"humanoide","Danza de Tijeras":"humanoide","Supay-Dread":"humanoide",
        "Wira-Titan":"humanoide","Apu-Cerro":"humanoide","Pachamama-Prime":"humanoide",
        "Omega-Inca":"humanoide","Aurum-Inca":"humanoide","Argentum-Moon":"humanoide",
        "Bronce-Tari":"humanoide","Wayra-Wind":"humanoide","Inti-Can":"humanoide",
        "Surito":"oruga","Suripullo":"capullo","Suriwain":"insecto",
        "Orugueta":"oruga","Crisalida Selva":"capullo","Mantis-Buho":"insecto",
        "Ajito":"planta","Picantox":"planta","Papa Nativa":"planta","Papa Chunio":"planta",
        "Papa Desertica":"planta","Papa Selvatica":"planta",
        "Maiz Morado":"planta","Orquidea Negra":"planta",
        "Tumito":"objeto","Tumignus":"objeto","Muquitox":"objeto","Muquimetal":"objeto",
        "Huacok":"objeto","Huacotrato":"objeto","Torito de Pucara":"objeto",
        "Monito":"mono","Churotail":"mono","Simiochuro":"mono",
        "Constelacion Sur":"cosmico","Astro Andino":"cosmico",
    }

    @staticmethod
    def _seed(nombre):
        return int(hashlib.md5(nombre.encode("utf-8")).hexdigest()[:8], 16)

    @staticmethod
    def _paleta(nombre, tipos):
        tipo = (tipos or ["Normal"])[0]
        return SpriteGenerator.PALETA_TIPO.get(tipo, SpriteGenerator.PALETA_TIPO["Normal"])

    @staticmethod
    def _categoria(nombre):
        if nombre in SpriteGenerator.CATEGORIAS:
            return SpriteGenerator.CATEGORIAS[nombre]
        n = nombre.lower()
        if any(k in n for k in ("ave","pajar","condor","tunq","colib","picaflor")): return "ave"
        if any(k in n for k in ("pira","caracha","bufeo","yacum","pez","delfin")): return "acuatico"
        if any(k in n for k in ("serp","drac","amaru")): return "serpiente"
        if any(k in n for k in ("papa","aji","hoja","flor","planta")): return "planta"
        if any(k in n for k in ("tumi","huaco","muqui","torito")): return "objeto"
        if any(k in n for k in ("monito","churo","simio")): return "mono"
        return "cuadrupedo"

    @staticmethod
    def _anim_params(anim, frame):
        if anim == "walk":
            # Frame 0: neutral, Frame 1: paso izq, Frame 2: neutral arriba, Frame 3: paso der
            dy = [0, -1, -2, -1][frame % 4]
            legs = [0, 1, 0, -1][frame % 4]
            blink = False
        elif anim == "attack":
            dy = [0, -3, 2, 0][frame % 4]
            legs = 0
            blink = False
        elif anim == "hurt":
            dy = [0, 2, 3, 1][frame % 4]
            legs = 0
            blink = False
        else:  # idle
            dy = [0, -1, 0, 1][frame % 4]
            legs = 0
            blink = (frame % 4) == 2
        return dy, legs, blink

    # ---------- Herramientas de dibujo ----------
    @staticmethod
    def _px(surf, x, y, c):
        if 0 <= x < surf.get_width() and 0 <= y < surf.get_height() and c is not None:
            surf.set_at((x, y), c)

    @staticmethod
    def _ellipse(surf, x, y, w, h, c):
        pygame.draw.ellipse(surf, c, (x, y, w, h))

    @staticmethod
    def _poly(surf, points, c):
        pygame.draw.polygon(surf, c, points)

    @staticmethod
    def _dither(surf, x0, y0, w, h, c1, c2):
        for y in range(y0, y0 + h):
            for x in range(x0, x0 + w):
                if (x + y) % 2 == 0:
                    SpriteGenerator._px(surf, x, y, c1)
                else:
                    SpriteGenerator._px(surf, x, y, c2)

    @staticmethod
    def _generar_outline(surf, color=(20, 15, 25)):
        w, h = surf.get_size()
        outline = []
        for x in range(w):
            for y in range(h):
                if surf.get_at((x, y))[3] > 0:
                    for dx in (-1, 0, 1):
                        for dy in (-1, 0, 1):
                            if dx == 0 and dy == 0:
                                continue
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < w and 0 <= ny < h:
                                if surf.get_at((nx, ny))[3] == 0:
                                    outline.append((nx, ny))
        for (px, py) in outline:
            surf.set_at((px, py), color)

    @staticmethod
    def _dib_ojos_gba(surf, cx, cy, sep, blink=False):
        """Ojos estilo GBA con brillo interior"""
        if blink:
            for dx in (-sep, sep):
                SpriteGenerator._px(surf, cx + dx - 1, cy, (20, 15, 25))
                SpriteGenerator._px(surf, cx + dx, cy, (20, 15, 25))
                SpriteGenerator._px(surf, cx + dx + 1, cy, (20, 15, 25))
            return
        for dx in (-sep, sep):
            ex = cx + dx
            # Cuenca oscura
            SpriteGenerator._ellipse(surf, ex - 3, cy - 2, 6, 6, (20, 15, 25))
            # Blanco del ojo
            SpriteGenerator._ellipse(surf, ex - 2, cy - 2, 5, 5, (255, 255, 255))
            # Pupila
            SpriteGenerator._ellipse(surf, ex - 1, cy - 1, 3, 4, (40, 30, 50))
            # Brillo
            SpriteGenerator._px(surf, ex - 1, cy - 2, (255, 255, 255))
            SpriteGenerator._px(surf, ex + 1, cy + 1, (255, 255, 255))

    # ---------- Generadores de partes orgánicas ----------
    @staticmethod
    def _patas_cuadrupedo(surf, sombra, dy, legs):
        # Delanteras
        l1_dy = 2 if legs == 1 else (0 if legs == -1 else 1)
        l2_dy = 0 if legs == 1 else (2 if legs == -1 else 1)
        # Traseras
        l3_dy = 0 if legs == 1 else (2 if legs == -1 else 1)
        l4_dy = 2 if legs == 1 else (0 if legs == -1 else 1)
        
        # Pata 1 (delantera izq)
        SpriteGenerator._poly(surf, [(8, 22+dy), (11, 22+dy), (10, 30+l1_dy), (7, 30+l1_dy)], sombra)
        # Pata 2 (delantera der)
        SpriteGenerator._poly(surf, [(13, 22+dy), (16, 22+dy), (15, 30+l2_dy), (12, 30+l2_dy)], sombra)
        # Pata 3 (trasera izq)
        SpriteGenerator._poly(surf, [(18, 22+dy), (21, 22+dy), (20, 30+l3_dy), (17, 30+l3_dy)], sombra)
        # Pata 4 (trasera der)
        SpriteGenerator._poly(surf, [(23, 22+dy), (26, 22+dy), (25, 30+l4_dy), (22, 30+l4_dy)], sombra)

    @staticmethod
    def _cuadrupedo(surf, c, dy, legs, blink, seed):
        s_prof, s_osc, base, luz, brillo = c
        SpriteGenerator._patas_cuadrupedo(surf, s_osc, dy, legs)
        
        # Cuerpo orgánico (lomo y barriga)
        SpriteGenerator._poly(surf, [
            (6, 16+dy), (10, 14+dy), (18, 14+dy), (24, 16+dy), 
            (26, 20+dy), (24, 24+dy), (10, 24+dy), (6, 20+dy)
        ], s_osc)
        SpriteGenerator._poly(surf, [
            (7, 17+dy), (10, 15+dy), (18, 15+dy), (23, 17+dy),
            (25, 20+dy), (23, 23+dy), (11, 23+dy), (7, 20+dy)
        ], base)
        # Sombra barriga
        SpriteGenerator._poly(surf, [
            (9, 21+dy), (23, 21+dy), (23, 23+dy), (11, 23+dy)
        ], s_prof)
        # Luz lomo
        SpriteGenerator._poly(surf, [
            (11, 16+dy), (19, 16+dy), (21, 18+dy), (9, 18+dy)
        ], luz)

        # Cabeza
        cx, cy = 22, 12+dy
        SpriteGenerator._ellipse(surf, cx-7, cy-7, 14, 14, s_osc)
        SpriteGenerator._ellipse(surf, cx-6, cy-6, 12, 12, base)
        # Hocico
        SpriteGenerator._ellipse(surf, cx+2, cy-1, 6, 5, luz)
        
        # Orejas según seed
        if seed % 3 == 0:  # Largas (Alpaca)
            SpriteGenerator._poly(surf, [(cx-4, cy-6), (cx-4, cy-16), (cx-1, cy-6)], s_osc)
            SpriteGenerator._poly(surf, [(cx+1, cy-6), (cx+3, cy-14), (cx+4, cy-6)], s_osc)
        elif seed % 3 == 1:  # Puntiagudas (Felino)
            SpriteGenerator._poly(surf, [(cx-6, cy-4), (cx-3, cy-12), (cx, cy-4)], s_osc)
            SpriteGenerator._poly(surf, [(cx+2, cy-4), (cx+5, cy-12), (cx+7, cy-4)], s_osc)
        else:  # Redondas (Oso)
            SpriteGenerator._ellipse(surf, cx-8, cy-9, 6, 6, s_osc)
            SpriteGenerator._ellipse(surf, cx+2, cy-9, 6, 6, s_osc)

        # Cola
        if seed % 2 == 0:
            SpriteGenerator._poly(surf, [(6, 18+dy), (0, 14+dy), (2, 22+dy)], luz)
        else:
            SpriteGenerator._poly(surf, [(6, 18+dy), (0, 16+dy), (0, 20+dy)], base)
            SpriteGenerator._poly(surf, [(0, 16+dy), (-2, 18+dy), (0, 20+dy)], luz)

        # Ojos y boca
        SpriteGenerator._dib_ojos_gba(surf, cx, cy, 3, blink)
        SpriteGenerator._px(surf, cx+1, cy+3, (20, 15, 25))
        SpriteGenerator._px(surf, cx+2, cy+3, (20, 15, 25))

    @staticmethod
    def _ave(surf, c, dy, legs, blink, seed):
        s_prof, s_osc, base, luz, brillo = c
        # Patas
        SpriteGenerator._poly(surf, [(12, 26+dy), (14, 26+dy), (14, 31)], (200, 150, 30))
        SpriteGenerator._poly(surf, [(18, 26+dy), (20, 26+dy), (20, 31)], (200, 150, 30))
        
        # Cuerpo
        SpriteGenerator._ellipse(surf, 10, 12+dy, 14, 16, s_osc)
        SpriteGenerator._ellipse(surf, 11, 13+dy, 12, 14, base)
        SpriteGenerator._ellipse(surf, 12, 15+dy, 8, 10, luz)
        
        # Cabeza
        cx, cy = 18, 6+dy
        SpriteGenerator._ellipse(surf, cx-6, cy-6, 12, 12, s_osc)
        SpriteGenerator._ellipse(surf, cx-5, cy-5, 10, 10, base)
        
        # Pico
        SpriteGenerator._poly(surf, [(cx+4, cy), (cx+10, cy+2), (cx+4, cy+4)], (240, 180, 40))
        
        # Cresta
        if seed % 2 == 0:
            SpriteGenerator._poly(surf, [(cx-2, cy-5), (cx-4, cy-12), (cx, cy-6)], base)
            SpriteGenerator._poly(surf, [(cx-4, cy-12), (cx-6, cy-10), (cx-5, cy-6)], s_osc)
            
        # Ala (orgánica y con movimiento)
        wdy = 2 if legs == 1 else (-2 if legs == -1 else 0)
        SpriteGenerator._poly(surf, [(10, 16+dy), (0, 14+dy+wdy), (2, 22+dy), (10, 24+dy)], s_osc)
        SpriteGenerator._poly(surf, [(11, 17+dy), (2, 16+dy+wdy), (4, 21+dy), (11, 23+dy)], base)
        
        # Cola
        SpriteGenerator._poly(surf, [(12, 24+dy), (10, 30+dy), (16, 28+dy), (18, 32+dy)], base)

        SpriteGenerator._dib_ojos_gba(surf, cx, cy-1, 3, blink)

    @staticmethod
    def _acuatico(surf, c, dy, legs, blink, seed):
        s_prof, s_osc, base, luz, brillo = c
        # Aleta dorsal
        SpriteGenerator._poly(surf, [(12, 8+dy), (16, 16+dy), (8, 16+dy)], s_osc)
        SpriteGenerator._poly(surf, [(12, 9+dy), (15, 15+dy), (9, 15+dy)], base)
        
        # Cuerpo
        SpriteGenerator._ellipse(surf, 4, 12+dy, 24, 16, s_osc)
        SpriteGenerator._ellipse(surf, 5, 13+dy, 22, 14, base)
        SpriteGenerator._ellipse(surf, 6, 16+dy, 20, 8, luz)
        
        # Aleta cola
        SpriteGenerator._poly(surf, [(28, 16+dy), (32, 10+dy), (32, 22+dy), (28, 20+dy)], s_osc)
        
        # Ojo
        SpriteGenerator._ellipse(surf, 8, 16+dy, 7, 7, (20,15,25))
        SpriteGenerator._ellipse(surf, 9, 17+dy, 5, 5, (255,255,255))
        SpriteGenerator._px(surf, 10, 18+dy, (20,15,25))
        
        # Aleta pectoral
        SpriteGenerator._poly(surf, [(16, 20+dy), (22, 26+dy), (12, 24+dy)], base)

    @staticmethod
    def _serpiente(surf, c, dy, legs, blink, seed):
        s_prof, s_osc, base, luz, brillo = c
        # Cuerpo serpenteante (S)
        puntos = [
            (16, 30+dy), (22, 26+dy), (24, 20+dy), (22, 14+dy),
            (16, 12+dy), (12, 8+dy), (14, 2+dy)
        ]
        for i in range(len(puntos)-1):
            x1, y1 = puntos[i]
            x2, y2 = puntos[i+1]
            for t in range(15):
                x = int(x1 + (x2-x1) * t / 14)
                y = int(y1 + (y2-y1) * t / 14)
                SpriteGenerator._ellipse(surf, x-2, y-2, 5, 5, s_osc)
                SpriteGenerator._ellipse(surf, x-1, y-1, 3, 3, base)
        
        # Cabeza
        cx, cy = 15, 2+dy
        SpriteGenerator._ellipse(surf, cx-6, cy-4, 12, 10, s_osc)
        SpriteGenerator._ellipse(surf, cx-5, cy-3, 10, 8, base)
        
        # Cuernos
        if seed % 2 == 0:
            SpriteGenerator._poly(surf, [(cx-3, cy-3), (cx-6, cy-10), (cx-1, cy-4)], base)
            SpriteGenerator._poly(surf, [(cx+3, cy-3), (cx+6, cy-10), (cx+1, cy-4)], base)

        SpriteGenerator._dib_ojos_gba(surf, cx, cy, 3, blink)
        # Lengua
        SpriteGenerator._px(surf, cx+7, cy+1, (220, 60, 90))
        SpriteGenerator._px(surf, cx+8, cy+2, (220, 60, 90))

    @staticmethod
    def _humanoide(surf, c, dy, legs, blink, seed):
        s_prof, s_osc, base, luz, brillo = c
        # Piernas
        l1 = 1 if legs == 1 else 0
        l2 = 1 if legs == -1 else 0
        SpriteGenerator._poly(surf, [(10, 22+dy), (14, 22+dy), (12, 31+l1)], s_osc)
        SpriteGenerator._poly(surf, [(18, 22+dy), (22, 22+dy), (20, 31+l2)], s_osc)
        
        # Torso
        SpriteGenerator._poly(surf, [(8, 10+dy), (24, 10+dy), (22, 22+dy), (10, 22+dy)], s_osc)
        SpriteGenerator._poly(surf, [(9, 11+dy), (23, 11+dy), (21, 21+dy), (11, 21+dy)], base)
        
        # Brazos
        SpriteGenerator._poly(surf, [(4, 12+dy), (8, 12+dy), (8, 18+dy), (4, 18+dy)], s_osc)
        SpriteGenerator._poly(surf, [(24, 12+dy), (28, 12+dy), (28, 18+dy), (24, 18+dy)], s_osc)
        
        # Cabeza
        cx, cy = 16, 6+dy
        SpriteGenerator._ellipse(surf, cx-6, cy-6, 12, 12, s_osc)
        SpriteGenerator._ellipse(surf, cx-5, cy-5, 10, 10, base)
        
        SpriteGenerator._dib_ojos_gba(surf, cx, cy, 3, blink)
        SpriteGenerator._px(surf, cx, cy+3, (20,15,25))

    @staticmethod
    def _planta(surf, c, dy, legs, blink, seed):
        s_prof, s_osc, base, luz, brillo = c
        # Hojas
        for i in (-1, 0, 1):
            SpriteGenerator._poly(surf, [(16, 14+dy), (16+i*8, 2+dy), (16+i*5, 14+dy)], s_osc)
            SpriteGenerator._poly(surf, [(16, 15+dy), (16+i*6, 4+dy), (16+i*4, 15+dy)], base)
        
        # Bulbo
        SpriteGenerator._ellipse(surf, 6, 14+dy, 20, 16, s_osc)
        SpriteGenerator._ellipse(surf, 7, 15+dy, 18, 14, base)
        SpriteGenerator._ellipse(surf, 8, 17+dy, 16, 10, luz)
        
        SpriteGenerator._dib_ojos_gba(surf, 16, 20+dy, 4, blink)
        SpriteGenerator._px(surf, 15, 24+dy, (20,15,25))
        SpriteGenerator._px(surf, 16, 24+dy, (20,15,25))
        SpriteGenerator._px(surf, 17, 24+dy, (20,15,25))

    @staticmethod
    def _objeto(surf, c, dy, legs, blink, seed):
        s_prof, s_osc, base, luz, brillo = c
        # Base
        SpriteGenerator._poly(surf, [(8, 14+dy), (24, 14+dy), (26, 30+dy), (6, 30+dy)], s_osc)
        SpriteGenerator._poly(surf, [(9, 15+dy), (23, 15+dy), (25, 29+dy), (7, 29+dy)], base)
        # Cuello
        SpriteGenerator._poly(surf, [(12, 8+dy), (20, 8+dy), (20, 14+dy), (12, 14+dy)], s_osc)
        # Tapa
        SpriteGenerator._poly(surf, [(10, 4+dy), (22, 4+dy), (22, 8+dy), (10, 8+dy)], luz)
        
        # Símbolo
        if seed % 2 == 0:
            SpriteGenerator._poly(surf, [(16, 18+dy), (19, 22+dy), (16, 26+dy), (13, 22+dy)], brillo)
        else:
            SpriteGenerator._ellipse(surf, 14, 18+dy, 4, 8, brillo)
        
        SpriteGenerator._dib_ojos_gba(surf, 16, 20+dy, 4, blink)

    @staticmethod
    def _oruga(surf, c, dy, legs, blink, seed):
        s_prof, s_osc, base, luz, brillo = c
        for i in range(4):
            x = 6 + i * 6
            y = 22 + dy + (1 if (i + legs) % 2 else 0)
            SpriteGenerator._ellipse(surf, x, y, 10, 10, s_osc)
            SpriteGenerator._ellipse(surf, x+1, y+1, 8, 8, base)
            SpriteGenerator._ellipse(surf, x+2, y+2, 4, 4, luz)
        
        # Cabeza
        cx, cy = 10, 12 + dy
        SpriteGenerator._ellipse(surf, cx-7, cy-7, 14, 14, s_osc)
        SpriteGenerator._ellipse(surf, cx-6, cy-6, 12, 12, base)
        
        # Antenas
        SpriteGenerator._px(surf, cx-3, cy-8, s_osc)
        SpriteGenerator._px(surf, cx-4, cy-10, brillo)
        SpriteGenerator._px(surf, cx+3, cy-8, s_osc)
        SpriteGenerator._px(surf, cx+4, cy-10, brillo)
        
        SpriteGenerator._dib_ojos_gba(surf, cx, cy, 4, blink)

    @staticmethod
    def _espiritu(surf, c, dy, legs, blink, seed):
        s_prof, s_osc, base, luz, brillo = c
        # Aura
        SpriteGenerator._ellipse(surf, 4, 4+dy, 24, 24, (*s_prof, 100))
        # Cuerpo
        SpriteGenerator._ellipse(surf, 8, 8+dy, 16, 16, s_osc)
        SpriteGenerator._ellipse(surf, 9, 9+dy, 14, 14, base)
        SpriteGenerator._ellipse(surf, 11, 11+dy, 10, 10, luz)
        
        # Cola ondulante
        for i in range(8):
            x = 16 + int(math.sin((i + legs) * 0.8) * 4)
            y = 22 + dy + i
            SpriteGenerator._ellipse(surf, x-1, y-1, 3, 3, base)
        
        # Ojos vacíos
        SpriteGenerator._ellipse(surf, 12, 12+dy, 4, 4, (20,15,25))
        SpriteGenerator._ellipse(surf, 18, 12+dy, 4, 4, (20,15,25))
        SpriteGenerator._px(surf, 13, 13+dy, brillo)
        SpriteGenerator._px(surf, 19, 13+dy, brillo)

    @staticmethod
    def _cosmico(surf, c, dy, legs, blink, seed):
        s_prof, s_osc, base, luz, brillo = c
        cx, cy = 16, 16 + dy
        off = (legs + (1 if blink else 0)) * 0.3
        puntos = []
        for i in range(10):
            ang = math.pi/2 + i * math.pi/5 + off
            r = 14 if i % 2 == 0 else 6
            puntos.append((cx + math.cos(ang)*r, cy - math.sin(ang)*r))
        SpriteGenerator._poly(surf, puntos, s_osc)
        
        puntos2 = []
        for i in range(10):
            ang = math.pi/2 + i * math.pi/5 + off
            r = 10 if i % 2 == 0 else 4
            puntos2.append((cx + math.cos(ang)*r, cy - math.sin(ang)*r))
        SpriteGenerator._poly(surf, puntos2, base)
        
        SpriteGenerator._ellipse(surf, cx-4, cy-4, 8, 8, luz)
        SpriteGenerator._ellipse(surf, cx-2, cy-2, 4, 4, brillo)

    # ============================================================
    # API pública
    # ============================================================
    @staticmethod
    def crear_sprite_pokemon(nombre, tam=64, anim="idle", frame=0):
        key = ("poke", nombre, tam, anim, frame)
        if key in SpriteGenerator._cache:
            return SpriteGenerator._cache[key]

        try:
            from data.pokedex import POKEDEX_COMPLETA
            tipos = POKEDEX_COMPLETA.get(nombre, {}).get("tipos", ["Normal"])
        except Exception:
            tipos = ["Normal"]

        paleta = SpriteGenerator._paleta(nombre, tipos)
        seed = SpriteGenerator._seed(nombre)
        cat = SpriteGenerator._categoria(nombre)

        dy, legs, blink = SpriteGenerator._anim_params(anim, frame)

        canvas = pygame.Surface((32, 32), pygame.SRCALPHA)

        forma_fn = {
            "cuadrupedo": SpriteGenerator._cuadrupedo,
            "ave":        SpriteGenerator._ave,
            "acuatico":   SpriteGenerator._acuatico,
            "serpiente":  SpriteGenerator._serpiente,
            "espiritu":   SpriteGenerator._espiritu,
            "humanoide":  SpriteGenerator._humanoide,
            "planta":     SpriteGenerator._planta,
            "oruga":      SpriteGenerator._oruga,
            "objeto":     SpriteGenerator._objeto,
            "cosmico":    SpriteGenerator._cosmico,
        }.get(cat, SpriteGenerator._cuadrupedo)

        forma_fn(canvas, paleta, dy, legs, blink, seed)
        SpriteGenerator._generar_outline(canvas)

        result = pygame.transform.scale(canvas, (tam, tam))
        SpriteGenerator._cache[key] = result
        return result

    @staticmethod
    def crear_frames_animacion(nombre, anim="idle", tam=64):
        n = SpriteGenerator._FRAMES_WALK if anim == "walk" else SpriteGenerator._FRAMES_IDLE
        return [SpriteGenerator.crear_sprite_pokemon(nombre, tam, anim, i) for i in range(n)]

    # Aliases
    @staticmethod
    def crear_sprite_alpaka(tam=64): return SpriteGenerator.crear_sprite_pokemon("Alpaka", tam)
    @staticmethod
    def crear_sprite_feligaro(tam=64): return SpriteGenerator.crear_sprite_pokemon("Feligaro", tam)
    @staticmethod
    def crear_sprite_bufeito(tam=64): return SpriteGenerator.crear_sprite_pokemon("Bufeito", tam)
    @staticmethod
    def crear_sprite_salvaje(nombre, tam=64): return SpriteGenerator.crear_sprite_pokemon(nombre, tam)

print("OK sistemas.sprites_pokes (GBA organico y animado)")
