# sistemas/sonidos.py
# -*- coding: utf-8 -*-
import pygame
import math
import random

class Sonidos:
    _habilitado = True
    _init = False

    @classmethod
    def _init_audio(cls):
        if not cls._init:
            try:
                pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
            except Exception:
                pass
            cls._init = True

    @classmethod
    def _tono(cls, freq, dur=0.1, vol=0.2, forma="sin", freq_fin=None):
        if not cls._habilitado: return None
        cls._init_audio()
        try:
            import numpy as np
            sr = 22050
            n = int(sr * dur)
            t = np.linspace(0, dur, n, False)
            f = np.full_like(t, freq) if freq_fin is None else np.linspace(freq, freq_fin, n)
            fase = 2 * np.pi * np.cumsum(f) / sr
            if forma == "square": w = np.sign(np.sin(fase))
            elif forma == "tri": w = 2 * np.abs(2 * ((fase / (2 * np.pi)) % 1) - 1) - 1
            elif forma == "noise": w = np.random.uniform(-1, 1, n)
            else: w = np.sin(fase)
            w = (w * vol * 32767).astype(np.int16)
            return pygame.sndarray.make_sound(np.column_stack((w, w)))
        except Exception:
            return None

    @classmethod
    def _play(cls, snd):
        if snd:
            try: snd.play()
            except: pass

    @staticmethod
    def reproducir_select():
        Sonidos._play(Sonidos._tono(800, 0.05, 0.2))

    @staticmethod
    def reproducir_confirmar():
        Sonidos._play(Sonidos._tono(600, 0.05, 0.2))
        Sonidos._play(Sonidos._tono(900, 0.05, 0.2))

    @staticmethod
    def reproducir_cancelar():
        Sonidos._play(Sonidos._tono(400, 0.1, 0.2))

    @staticmethod
    def abrir_menu():
        Sonidos._play(Sonidos._tono(523, 0.05, 0.15))
        Sonidos._play(Sonidos._tono(659, 0.05, 0.15))

    @staticmethod
    def victoria():
        for f in (523, 659, 784, 1047):
            Sonidos._play(Sonidos._tono(f, 0.1, 0.2))

    @staticmethod
    def subir_nivel():
        for f in (440, 554, 659, 880):
            Sonidos._play(Sonidos._tono(f, 0.08, 0.2))

    @staticmethod
    def medalla():
        for f in (523, 659, 784, 1046, 1318):
            Sonidos._play(Sonidos._tono(f, 0.1, 0.2))

    @staticmethod
    def critico():
        Sonidos._play(Sonidos._tono(150, 0.2, 0.3, "noise"))

    @staticmethod
    def golpe():
        Sonidos._play(Sonidos._tono(200, 0.1, 0.3, "square"))

    @staticmethod
    def paso_pasto():
        Sonidos._play(Sonidos._tono(300, 0.05, 0.1, "noise"))

    @staticmethod
    def paso_hierba():
        Sonidos._play(Sonidos._tono(250, 0.05, 0.1, "noise"))

    @staticmethod
    def paso_tierra():
        Sonidos._play(Sonidos._tono(200, 0.05, 0.1, "noise"))

    @staticmethod
    def ataque_por_tipo(tipo):
        Sonidos._play(Sonidos._tono(400, 0.1, 0.2, "square"))

    @staticmethod
    def alternar():
        Sonidos._habilitado = not Sonidos._habilitado
        return Sonidos._habilitado

print("OK Sonidos v2 (arreglados todos los metodos)")
