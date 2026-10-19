# sistemas/mapa_regional.py
# -*- coding: utf-8 -*-
"""Mapa regional estilo Pokemon Emerald."""
import math
import pygame

POSICIONES = {
    "caleta_norte":    (70, 400),
    "ruta_1":          (170, 400),
    "ciudad_moche":    (270, 400),
    "ruta_2":          (370, 400),
    "puerto_ancon":    (470, 400),
    "ruta_3":          (570, 400),
    "andahuaylas":     (570, 260),
    "ruta_4":          (470, 260),
    "ciudad_imperial": (370, 260),
    "ruta_5":          (270, 260),
    "puno":            (170, 260),
    "ruta_6":          (70, 260),
    "huaraz":          (70, 120),
    "ruta_7":          (200, 120),
    "puerto_selva":    (330, 120),
    "ruta_8":          (460, 120),
    "ciudad_capital":  (570, 120),
}

GIMNASIO_DE_CIUDAD = {
    "ciudad_moche":    "gimnasio_moche",
    "puerto_ancon":    "gimnasio_ancon",
    "andahuaylas":     "gimnasio_andahuaylas",
    "ciudad_imperial": "gimnasio_imperial",
    "puno":            "gimnasio_puno",
    "huaraz":          "gimnasio_huaraz",
    "puerto_selva":    "gimnasio_selva",
    "ciudad_capital":  "gimnasio_capital",
}

NOMBRES_CORTOS = {
    "caleta_norte": "Caleta Norte",
    "ruta_1": "Ruta 1",
    "ciudad_moche": "Cd. Moche",
    "ruta_2": "Ruta 2",
    "puerto_ancon": "Pto. Ancon",
    "ruta_3": "Ruta 3",
    "andahuaylas": "Andahuaylas",
    "ruta_4": "Ruta 4",
    "ciudad_imperial": "Cd. Imperial",
    "ruta_5": "Ruta 5",
    "puno": "Puno",
    "ruta_6": "Ruta 6",
    "huaraz": "Huaraz",
    "ruta_7": "Ruta 7",
    "puerto_selva": "Pto. Selva",
    "ruta_8": "Ruta 8",
    "ciudad_capital": "Cd. Capital",
}

CAMINO = [
    "caleta_norte", "ruta_1", "ciudad_moche", "ruta_2",
    "puerto_ancon", "ruta_3", "andahuaylas", "ruta_4",
    "ciudad_imperial", "ruta_5", "puno", "ruta_6",
    "huaraz", "ruta_7", "puerto_selva", "ruta_8",
    "ciudad_capital",
]


def dibujar_mapa(pantalla, juego, fuente_peque, fuente_media, fuente_grande, fuente_titulo, anim_t):
    ANCHO, ALTO = pantalla.get_size()

    for i in range(ALTO):
        t = i / ALTO
        r = int(238 - 20 * t)
        g = int(222 - 25 * t)
        b = int(180 - 30 * t)
        pygame.draw.line(pantalla, (r, g, b), (0, i), (ANCHO, i))

    for x in range(0, ANCHO, 32):
        pygame.draw.line(pantalla, (215, 200, 160), (x, 0), (x, ALTO), 1)
    for y in range(0, ALTO, 32):
        pygame.draw.line(pantalla, (215, 200, 160), (0, y), (ANCHO, y), 1)

    pygame.draw.rect(pantalla, (60, 40, 90), (0, 0, ANCHO, 44))
    pygame.draw.rect(pantalla, (240, 200, 60), (0, 42, ANCHO, 2))
    titulo = fuente_titulo.render("MAPA DEL TAHUANTINSUYO", True, (255, 240, 180))
    pantalla.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 6))

    try:
        actual = juego.mapa_actual.id
    except Exception:
        actual = None

    for i in range(len(CAMINO) - 1):
        a = CAMINO[i]
        b = CAMINO[i + 1]
        if a in POSICIONES and b in POSICIONES:
            x1, y1 = POSICIONES[a]
            x2, y2 = POSICIONES[b]
            pygame.draw.line(pantalla, (140, 110, 70), (x1, y1), (x2, y2), 7)
            pygame.draw.line(pantalla, (200, 175, 120), (x1, y1), (x2, y2), 4)
            pygame.draw.line(pantalla, (255, 240, 200), (x1, y1), (x2, y2), 1)

    for nodo, (x, y) in POSICIONES.items():
        es_actual = (nodo == actual)
        visitado = es_actual
        try:
            if nodo in getattr(juego, "_ciudades_visitadas", set()):
                visitado = True
        except Exception:
            pass
        gym_id = GIMNASIO_DE_CIUDAD.get(nodo)
        gym_ganado = False
        if gym_id:
            try:
                gym_ganado = gym_id in juego.gimnasios.lideres_derrotados
            except Exception:
                pass

        if es_actual:
            pulso = 1 + 0.15 * math.sin(anim_t * 5)
            r = int(18 * pulso)
            pygame.draw.circle(pantalla, (255, 220, 80), (x, y), r + 4)
            pygame.draw.circle(pantalla, (255, 250, 200), (x, y), r)
            pygame.draw.circle(pantalla, (180, 120, 20), (x, y), r + 4, 2)
        elif gym_id and gym_ganado:
            pygame.draw.circle(pantalla, (180, 130, 20), (x, y), 16)
            pygame.draw.circle(pantalla, (255, 220, 80), (x, y), 13)
            pygame.draw.circle(pantalla, (255, 250, 200), (x - 3, y - 3), 6)
        elif gym_id and visitado:
            pygame.draw.circle(pantalla, (150, 60, 20), (x, y), 16)
            pygame.draw.circle(pantalla, (240, 140, 60), (x, y), 13)
        elif visitado:
            pygame.draw.circle(pantalla, (30, 80, 30), (x, y), 13)
            pygame.draw.circle(pantalla, (100, 200, 100), (x, y), 10)
        else:
            pygame.draw.circle(pantalla, (80, 70, 60), (x, y), 12)
            pygame.draw.circle(pantalla, (140, 130, 120), (x, y), 9)

        nombre = NOMBRES_CORTOS.get(nodo, nodo)
        col_txt = (40, 20, 20) if (visitado or es_actual) else (110, 100, 90)
        if es_actual:
            col_txt = (180, 40, 40)
        t_nom = fuente_peque.render(nombre, True, col_txt)
        t_s = fuente_peque.render(nombre, True, (245, 235, 205))
        tx = x - t_nom.get_width() // 2
        ty = y + 18
        pantalla.blit(t_s, (tx + 1, ty + 1))
        pantalla.blit(t_nom, (tx, ty))

        if gym_id and gym_ganado:
            pygame.draw.circle(pantalla, (140, 90, 20), (x, y - 20), 6)
            pygame.draw.circle(pantalla, (255, 220, 80), (x, y - 20), 5)
            pygame.draw.circle(pantalla, (255, 255, 255), (x - 1, y - 21), 1)

    if actual in POSICIONES:
        px, py = POSICIONES[actual]
        ofs = int(2 * math.sin(anim_t * 6))
        pygame.draw.polygon(pantalla, (200, 30, 30), [
            (px, py - 22 + ofs), (px - 7, py - 31 + ofs), (px + 7, py - 31 + ofs)
        ])
        pygame.draw.polygon(pantalla, (255, 80, 80), [
            (px, py - 20 + ofs), (px - 6, py - 29 + ofs), (px + 6, py - 29 + ofs)
        ])
        pygame.draw.polygon(pantalla, (255, 240, 200), [
            (px, py - 20 + ofs), (px - 3, py - 25 + ofs), (px + 3, py - 25 + ofs)
        ])

    pie_h = 44
    pygame.draw.rect(pantalla, (60, 40, 90), (0, ALTO - pie_h, ANCHO, pie_h))
    pygame.draw.rect(pantalla, (240, 200, 60), (0, ALTO - pie_h, ANCHO, 2))

    try:
        medallas = juego.gimnasios.cantidad_medallas()
    except Exception:
        medallas = 0
    txt_med = fuente_media.render("Medallas:", True, (255, 240, 180))
    pantalla.blit(txt_med, (12, ALTO - pie_h + 14))

    for i in range(8):
        cx = 110 + i * 22
        cy = ALTO - pie_h + 22
        tiene = i < medallas
        col = (255, 220, 80) if tiene else (90, 80, 70)
        pygame.draw.circle(pantalla, (20, 15, 30), (cx, cy), 8)
        pygame.draw.circle(pantalla, col, (cx, cy), 7)
        if tiene:
            pygame.draw.circle(pantalla, (255, 255, 255), (cx - 2, cy - 2), 2)

    obj = ""
    try:
        from sistemas.progresion import proximo_objetivo as _prox
        obj = _prox(juego.gimnasios, getattr(juego, "liga", None))
    except Exception:
        obj = ""
    if obj:
        obj_txt = fuente_peque.render("Objetivo: " + obj, True, (255, 240, 180))
        pantalla.blit(obj_txt, (ANCHO - obj_txt.get_width() - 12, ALTO - pie_h + 6))

    tip = fuente_peque.render("[T]/[ESC] Cerrar", True, (220, 200, 160))
    pantalla.blit(tip, (ANCHO - tip.get_width() - 12, ALTO - pie_h + 24))
