# sistemas/ambiente.py
# -*- coding: utf-8 -*-
"""D4: Sonido ambiental por bioma y hora del dia."""
import pygame
import math
import random


class Ambiente:
    """Genera sonidos ambientales procedurales segun bioma y hora."""

    SR = 22050

    def __init__(self):
        self.activo = False
        self.canal = None
        self.sonidos = {}
        self.actual = None
        self._timer_prox = 0.0
        self._habilitado = True
        try:
            if not pygame.mixer.get_init():
                return
            import numpy  # noqa
            self.np = numpy
            self.activo = True
            # Canal 3 reservado para ambiente
            self.canal = pygame.mixer.Channel(3)
            self.canal.set_volume(0.25)
        except Exception:
            self.activo = False

    # ---------------- sintesis basica ----------------
    def _tono(self, freq, dur, vol=0.2, forma="sin", freq_fin=None):
        if not self.activo:
            return None
        np = self.np
        try:
            sr = self.SR
            n = int(sr * dur)
            t = np.linspace(0, dur, n, False)
            f = np.full_like(t, freq) if freq_fin is None else np.linspace(freq, freq_fin, n)
            fase = 2 * np.pi * np.cumsum(f) / sr
            if forma == "sin":
                w = np.sin(fase)
            elif forma == "tri":
                w = 2 * np.abs(2 * ((fase / (2 * np.pi)) % 1) - 1) - 1
            elif forma == "noise":
                w = np.random.uniform(-1, 1, n)
            elif forma == "chirp":
                # barrido exponencial
                w = np.sin(fase) * np.exp(-2.5 * t)
            else:
                w = np.sin(fase)
            env = np.ones(n)
            atk = min(int(sr * 0.01), n // 4)
            rel = min(int(sr * 0.15), n // 3)
            if atk > 0:
                env[:atk] = np.linspace(0, 1, atk)
            if rel > 0:
                env[-rel:] = np.linspace(1, 0, rel)
            w = (w * env * vol * 32767).astype(np.int16)
            return pygame.sndarray.make_sound(np.column_stack((w, w)))
        except Exception:
            return None

    # ---------------- sonidos especificos ----------------
    def _pajarito(self):
        """Trino de pajaro costeno/andino."""
        if not self.activo: return None
        np = self.np
        try:
            sr = self.SR
            total = 0.6
            n = int(sr * total)
            out = np.zeros(n, dtype=np.float32)
            # 3 notas rapidas
            for i, (f1, f2, dur, t0) in enumerate([
                (2400, 3200, 0.08, 0.00),
                (2800, 3600, 0.07, 0.10),
                (2200, 2800, 0.10, 0.20),
            ]):
                n2 = int(sr * dur)
                t2 = np.linspace(0, dur, n2, False)
                fase = 2 * np.pi * np.cumsum(np.linspace(f1, f2, n2)) / sr
                w = np.sin(fase) * 0.15
                env = np.exp(-4.0 * t2)
                ini = int(sr * t0)
                out[ini:ini+n2] += (w * env).astype(np.float32)
            out = (out * 32767).astype(np.int16)
            return pygame.sndarray.make_sound(np.column_stack((out, out)))
        except Exception:
            return None

    def _grillo(self):
        """Chirrido de grillo nocturno."""
        if not self.activo: return None
        np = self.np
        try:
            sr = self.SR
            total = 0.4
            n = int(sr * total)
            t = np.linspace(0, total, n, False)
            # Tren de pulsos
            w = np.zeros(n, dtype=np.float32)
            for k in range(6):
                ini = int(sr * k * 0.06)
                dur_pulso = int(sr * 0.03)
                if ini + dur_pulso > n:
                    break
                tp = np.linspace(0, 0.03, dur_pulso, False)
                pulso = np.sin(2 * np.pi * 4200 * tp) * np.exp(-15 * tp)
                w[ini:ini+dur_pulso] += pulso * 0.10
            w = (w * 32767).astype(np.int16)
            return pygame.sndarray.make_sound(np.column_stack((w, w)))
        except Exception:
            return None

    def _agua(self):
        """Burbujeo de agua (rios, mar)."""
        if not self.activo: return None
        np = self.np
        try:
            sr = self.SR
            total = 1.2
            n = int(sr * total)
            t = np.linspace(0, total, n, False)
            # Ruido filtrado + ondas bajas
            ruido = np.random.uniform(-1, 1, n).astype(np.float32)
            # Suavizar (pasa bajos simple)
            for _ in range(3):
                ruido = np.convolve(ruido, np.ones(20)/20, mode="same").astype(np.float32)
            onda = np.sin(2 * np.pi * 250 * t + 0.5 * np.sin(2 * np.pi * 4 * t))
            w = (ruido * 0.08 + onda * 0.03).astype(np.float32)
            env = np.ones(n)
            env[:int(sr*0.2)] = np.linspace(0, 1, int(sr*0.2))
            env[-int(sr*0.3):] = np.linspace(1, 0, int(sr*0.3))
            w *= env
            w = (w * 32767).astype(np.int16)
            return pygame.sndarray.make_sound(np.column_stack((w, w)))
        except Exception:
            return None

    def _viento(self):
        """Viento de sierra/paramo."""
        if not self.activo: return None
        np = self.np
        try:
            sr = self.SR
            total = 1.5
            n = int(sr * total)
            t = np.linspace(0, total, n, False)
            ruido = np.random.uniform(-1, 1, n).astype(np.float32)
            # Pasa bajos fuerte
            for _ in range(6):
                ruido = np.convolve(ruido, np.ones(40)/40, mode="same").astype(np.float32)
            mod = 0.4 + 0.6 * (0.5 + 0.5 * np.sin(2 * np.pi * 0.4 * t))
            w = (ruido * mod * 0.10).astype(np.float32)
            env = np.ones(n)
            env[:int(sr*0.3)] = np.linspace(0, 1, int(sr*0.3))
            env[-int(sr*0.4):] = np.linspace(1, 0, int(sr*0.4))
            w *= env
            w = (w * 32767).astype(np.int16)
            return pygame.sndarray.make_sound(np.column_stack((w, w)))
        except Exception:
            return None

    def _olas(self):
        """Olas del mar (costa)."""
        if not self.activo: return None
        np = self.np
        try:
            sr = self.SR
            total = 1.8
            n = int(sr * total)
            t = np.linspace(0, total, n, False)
            ruido = np.random.uniform(-1, 1, n).astype(np.float32)
            for _ in range(4):
                ruido = np.convolve(ruido, np.ones(30)/30, mode="same").astype(np.float32)
            # Olas: 2 pulsos
            env = np.zeros(n)
            for ini in [0.0, 0.9]:
                ii = int(sr * ini)
                dur = int(sr * 0.7)
                if ii + dur > n: break
                tt = np.linspace(0, 1, dur)
                env[ii:ii+dur] = np.maximum(env[ii:ii+dur],
                                             np.sin(tt * np.pi) ** 1.5)
            w = (ruido * env * 0.10).astype(np.float32)
            w = (w * 32767).astype(np.int16)
            return pygame.sndarray.make_sound(np.column_stack((w, w)))
        except Exception:
            return None

    def _selva_fondo(self):
        """Fondo de selva: hojas + bichos."""
        if not self.activo: return None
        np = self.np
        try:
            sr = self.SR
            total = 1.5
            n = int(sr * total)
            t = np.linspace(0, total, n, False)
            ruido = np.random.uniform(-1, 1, n).astype(np.float32)
            for _ in range(5):
                ruido = np.convolve(ruido, np.ones(25)/25, mode="same").astype(np.float32)
            # bichitos: chirridos agudos rapidos
            bichos = np.zeros(n, dtype=np.float32)
            for k in range(4):
                ini = int(sr * (k * 0.35 + random.random() * 0.15))
                dur = int(sr * 0.08)
                if ini + dur > n: break
                tp = np.linspace(0, 0.08, dur, False)
                bichos[ini:ini+dur] = np.sin(2 * np.pi * 6500 * tp) * np.exp(-8*tp) * 0.05
            w = (ruido * 0.06 + bichos).astype(np.float32)
            w = (w * 32767).astype(np.int16)
            return pygame.sndarray.make_sound(np.column_stack((w, w)))
        except Exception:
            return None

    # ---------------- reproduccion ----------------
    def _obtener(self, nombre, gen_fn):
        if nombre in self.sonidos:
            return self.sonidos[nombre]
        try:
            snd = gen_fn()
            self.sonidos[nombre] = snd
            return snd
        except Exception:
            self.sonidos[nombre] = None
            return None

    def _quena_lejana(self):
        """Quena andina lejana."""
        if not self.activo: return None
        np = self.np
        try:
            sr = self.SR
            total = 2.0
            n = int(sr * total)
            out = np.zeros(n, dtype=np.float32)
            # Melodia pentatonica andina
            notas = [(587, 0.4), (659, 0.4), (784, 0.5), (659, 0.3), (587, 0.4)]
            t_ini = 0.0
            for f, d in notas:
                n2 = int(sr * d)
                t2 = np.linspace(0, d, n2, False)
                # Vibrato tipo quena
                fase = 2 * np.pi * np.cumsum(f * (1 + 0.02 * np.sin(2*np.pi*5*t2))) / sr
                w = np.sin(fase) * 0.12
                env = np.ones(n2)
                atk = min(int(sr*0.05), n2//4)
                rel = min(int(sr*0.15), n2//3)
                env[:atk] = np.linspace(0, 1, atk)
                env[-rel:] = np.linspace(1, 0, rel)
                ini = int(sr * t_ini)
                if ini + n2 <= n:
                    out[ini:ini+n2] = w * env
                t_ini += d * 0.9
            w = (out * 32767).astype(np.int16)
            return pygame.sndarray.make_sound(np.column_stack((w, w)))
        except Exception:
            return None

    def _brisa_suave(self):
        """Brisa muy suave."""
        if not self.activo: return None
        np = self.np
        try:
            sr = self.SR
            total = 2.5
            n = int(sr * total)
            ruido = np.random.uniform(-1, 1, n).astype(np.float32)
            for _ in range(8):
                ruido = np.convolve(ruido, np.ones(60)/60, mode="same").astype(np.float32)
            mod = 0.5 + 0.5 * np.sin(2 * np.pi * 0.3 * np.arange(n) / sr)
            w = (ruido * mod * 0.06).astype(np.float32)
            env = np.ones(n)
            env[:int(sr*0.4)] = np.linspace(0, 1, int(sr*0.4))
            env[-int(sr*0.5):] = np.linspace(1, 0, int(sr*0.5))
            w *= env
            w = (w * 32767).astype(np.int16)
            return pygame.sndarray.make_sound(np.column_stack((w, w)))
        except Exception:
            return None

    def _campanas_lejanas(self):
        """Campanas de pueblo lejano."""
        if not self.activo: return None
        np = self.np
        try:
            sr = self.SR
            total = 1.5
            n = int(sr * total)
            out = np.zeros(n, dtype=np.float32)
            for f, t0 in [(523, 0), (659, 0.3), (784, 0.6), (523, 0.9)]:
                n2 = int(sr * 0.5)
                t2 = np.linspace(0, 0.5, n2, False)
                w = (np.sin(2*np.pi*f*t2) * np.exp(-3.5*t2) * 0.10).astype(np.float32)
                ini = int(sr * t0)
                if ini + n2 <= n:
                    out[ini:ini+n2] += w
            w = (out * 32767).astype(np.int16)
            return pygame.sndarray.make_sound(np.column_stack((w, w)))
        except Exception:
            return None

    def _sonidos_para(self, bioma, es_noche):
        """Devuelve lista de (nombre, generador) posibles para ese contexto."""
        lista = []
        if bioma == "costa":
            if es_noche:
                lista.append(("grillo_costa", self._grillo))
            else:
                lista.append(("pajaro_costa", self._pajarito))
                lista.append(("olas", self._olas))
                lista.append(("brisa_costa", self._brisa_suave))
        elif bioma == "valle":
            if es_noche:
                lista.append(("grillo_valle", self._grillo))
            else:
                lista.append(("pajaro_valle", self._pajarito))
                lista.append(("quena_lejana", self._quena_lejana))
        elif bioma == "capital":
            if es_noche:
                lista.append(("grillo_capital", self._grillo))
            else:
                lista.append(("pajaro_capital", self._pajarito))
                lista.append(("campanas", self._campanas_lejanas))
        elif bioma in ("sierra", "paramo", "altiplano"):
            lista.append(("viento_sierra", self._viento))
            if es_noche:
                lista.append(("grillo_sierra", self._grillo))
            else:
                lista.append(("quena_sierra", self._quena_lejana))
        elif bioma == "selva":
            lista.append(("selva_fondo", self._selva_fondo))
            if not es_noche:
                lista.append(("pajaro_selva", self._pajarito))
                lista.append(("brisa_selva", self._brisa_suave))
        else:
            if not es_noche:
                lista.append(("pajaro_generico", self._pajarito))
        return lista

    def actualizar(self, dt, bioma="valle", es_noche=False, clima="despejado", activo=True):
        """Actualiza el ambiente. Se llama cada frame."""
        if not self.activo or not self._habilitado or not activo:
            return
        self._timer_prox -= dt
        # Solo reproducir si estamos en exploracion (o cerca)
        if self._timer_prox > 0:
            return
        # Elegir sonido segun contexto
        candidatos = self._sonidos_para(bioma, es_noche)
        if not candidatos:
            self._timer_prox = 2.0
            return
        # Filtrar por clima
        if clima in ("lluvia", "tormenta"):
            # Poner "agua" como fondo durante lluvia
            candidatos.append(("agua_lluvia", self._agua))
        nombre, gen = random.choice(candidatos)
        snd = self._obtener(nombre, gen)
        if snd is None:
            self._timer_prox = 4.0
            return
        try:
            # Volumen bajo para no molestar
            self.canal.set_volume(0.20)
            self.canal.play(snd, loops=0)
        except Exception:
            pass
        # Proximo sonido en 6-14 segundos (menos frecuente)
        self._timer_prox = random.uniform(6.0, 14.0)

    def alternar(self):
        self._habilitado = not self._habilitado
        if not self._habilitado and self.canal is not None:
            try:
                self.canal.stop()
            except Exception:
                pass
        return self._habilitado

    def detener(self):
        if self.canal is not None:
            try:
                self.canal.stop()
            except Exception:
                pass
        self._timer_prox = 0.0


print("OK sistemas.ambiente")
