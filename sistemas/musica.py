"""
musica.py — Banda sonora chiptune procedural para Pokémon Freekie.
Genera las pistas al vuelo con numpy (NO requiere archivos .ogg externos).
Cada pista es un loop corto que se repite infinitamente.
"""
import math
import pygame


class Musica:
    SR = 22050

    ESCALAS = {
        "menor":  [0, 2, 3, 5, 7, 8, 10],
        "mayor":  [0, 2, 4, 5, 7, 9, 11],
        "andina": [0, 2, 3, 7, 8, 10],   # pentatónica andina
    }

    def __init__(self):
        self.activa = False
        self.silenciada = False
        self.canal = None
        self.actual = None
        self.cache = {}
        self.volumen = 0.22
        self._jingle_hasta = 0.0   # ← NUEVO
        try:
            if not pygame.mixer.get_init():
                return
            import numpy as np
            self.np = np
            self.activa = True
            self.canal = pygame.mixer.Channel(7)
            self.canal.set_volume(self.volumen)
        except Exception:
            self.activa = False


    # --------------------------- síntesis ---------------------------
    def _nota(self, freq, dur, onda="sin", vol=0.5):
        np = self.np
        n = int(self.SR * dur)
        if n <= 0 or freq <= 0:
            return np.zeros(max(0, n), dtype=np.float32)
        t = np.linspace(0, dur, n, False)
        fase = 2 * np.pi * freq * t
        if onda == "sin":
            w = np.sin(fase)
        elif onda == "square":
            w = np.sign(np.sin(fase))
        elif onda == "tri":
            w = 2 * np.abs(2 * ((fase / (2 * np.pi)) % 1) - 1) - 1
        elif onda == "quena":         # flauta con vibrato
            w = np.sin(fase + 0.5 * np.sin(2 * np.pi * 5.5 * t))
        elif onda == "charango":      # cuerda pulsada
            w = (2 * ((fase / (2 * np.pi)) % 1) - 1) * np.exp(-3.5 * t)
        elif onda == "bombo":         # percusivo, ruido con decaimiento
            w = np.random.uniform(-1, 1, n).astype(np.float32) * np.exp(-10 * t)
        else:
            w = np.sin(fase)
        env = np.ones(n)
        atk = min(int(self.SR * 0.006), n // 4)
        rel = min(int(self.SR * 0.06), n // 4)
        if atk > 0:
            env[:atk] = np.linspace(0, 1, atk)
        if rel > 0:
            env[-rel:] = np.linspace(1, 0, rel)
        return (w * env * vol).astype(np.float32)

    def _secuencia(self, notas, bpm):
        np = self.np
        beat = 60.0 / bpm
        partes = []
        for f, d, onda in notas:
            if f <= 0:
                n = int(self.SR * d * beat)
                partes.append(np.zeros(n, dtype=np.float32))
            else:
                # Suavizar: square -> tri, tri -> sin
                if onda == "square":
                    onda = "tri"
                elif onda == "tri":
                    onda = "sin"
                partes.append(self._nota(f, d * beat, onda))
        return np.concatenate(partes) if partes else np.zeros(0, dtype=np.float32)

    def _a_sound(self, onda_float):
        np = self.np
        if onda_float.size == 0:
            return pygame.sndarray.make_sound(np.zeros((256, 2), dtype=np.int16))
        peak = np.abs(onda_float).max()
        if peak > 0:
            onda_float = onda_float / peak * 0.45
        datos = (onda_float * 32767).astype(np.int16)
        est = np.column_stack((datos, datos)).copy()
        return pygame.sndarray.make_sound(est)

    def _midi(self, m):
        return 440.0 * (2 ** ((m - 69) / 12.0))

    def _mel(self, grados, raiz, escala, extender=True):
        # F: extender la melodia para reducir la sensacion de repeticion
        if extender and len(grados) > 0:
            grados = self._extender_melodia(grados)
        notas = self.ESCALAS.get(escala, self.ESCALAS["andina"])
        out = []
        for g, oct_, dur in grados:
            if g < 0:
                out.append((0, dur, "sin"))
            else:
                idx = g % len(notas)
                oct_extra = g // len(notas)
                out.append((self._midi(raiz + notas[idx] + 12 * (oct_ + oct_extra)), dur, "quena"))
        return out

    def _extender_melodia(self, mel):
        """Toma una melodia y devuelve una version 2x con variacion en la segunda mitad."""
        if not mel:
            return mel
        variacion = []
        for i, (g, o, d) in enumerate(mel):
            if g < 0:
                variacion.append((g, o, d))
                continue
            # Cada 3 notas, variamos
            mod3 = i % 3
            if mod3 == 0:
                # Subir un grado (con salto de octava si pasa)
                nuevo_g = g + 1
                nuevo_o = o + nuevo_g // 7
                variacion.append((nuevo_g % 7, nuevo_o, d))
            elif mod3 == 1:
                # Bajar un grado (nunca por debajo de 0)
                nuevo_g = max(0, g - 1)
                variacion.append((nuevo_g, o, d))
            else:
                # Repetir el original
                variacion.append((g, o, d))
        # Devolver la melodia original + la variacion
        return mel + variacion

    # --------------------------- pistas ---------------------------
    def _construir(self, nombre):
        if nombre == "noche":
            mel = [(0,0,2),(3,0,2),(2,0,2),(0,0,3),(-1,0,1),(0,0,1),(3,0,2),(2,0,4),
                   (5,0,2),(4,0,1),(3,0,1),(2,0,2),(0,0,2),(-1,0,3)]
            return self._secuencia(self._mel(mel, 58, "menor"), 78)

        if nombre == "noche_selva":
            mel = [(0,0,2),(2,0,1),(3,0,1),(5,0,2),(3,0,2),(2,0,3),
                   (0,0,1),(2,0,1),(3,0,1),(2,0,2),(0,0,2),(-1,0,3)]
            return self._secuencia(self._mel(mel, 60, "andina"), 88)

        if nombre == "noche_nieve":
            mel = [(0,0,3),(3,0,2),(5,0,3),(7,0,2),(5,0,3),(3,0,3),(0,0,4)]
            return self._secuencia(self._mel(mel, 55, "menor"), 72)

        if nombre == "titulo":
            mel = [(0,0,2),(2,0,1),(4,0,1),(2,0,2),(0,0,1),(4,0,1),(2,1,3),
                   (7,0,2),(4,0,1),(2,0,1),(0,0,2),(2,0,1),(4,0,1),(6,0,1),
                   (7,0,2),(9,0,1),(7,0,1),(4,0,2),(2,0,1),(0,0,1),(-1,0,3)]
            return self._secuencia(self._mel(mel, 62, "andina", extender=True), 78)

        if nombre == "caleta":
            mel = [(0,0,1),(2,0,1),(4,0,1),(5,0,1),(4,0,1),(2,0,1),(0,0,2),
                   (4,0,1),(2,0,1),(0,0,1),(-1,0,1),(0,0,2),
                   (2,0,1),(4,0,1),(5,0,1),(7,0,1),(5,0,1),(4,0,1),(2,0,2),
                   (4,0,1),(2,0,1),(4,0,1),(5,0,3)]
            return self._secuencia(self._mel(mel, 64, "mayor", extender=True), 96)

        if nombre == "ruta_costa":
            mel = [(0,0,1),(2,0,1),(4,0,1),(5,0,1),(7,0,1),(5,0,1),(4,0,1),(2,0,1),
                   (0,0,1),(2,0,1),(4,0,2),(2,0,1),(0,0,1),(-1,0,2),
                   (0,0,1),(2,0,1),(4,0,1),(5,0,1),(7,0,1),(9,0,1),(7,0,1),(5,0,1),
                   (4,0,1),(5,0,1),(7,0,3),(4,0,2)]
            return self._secuencia(self._mel(mel, 62, "mayor", extender=True), 108)

        if nombre == "ruta_sierra":
            mel = [(0,0,1),(2,0,1),(3,0,1),(5,0,1),(7,0,2),(5,0,1),(3,0,1),(2,0,2),
                   (0,0,1),(2,0,1),(3,0,1),(5,0,1),(3,0,2),(2,0,2),
                   (0,0,1),(2,0,1),(5,0,1),(7,0,1),(5,0,1),(3,0,1),(2,0,1),(0,0,1),
                   (5,0,1),(7,0,1),(3,0,3),(5,0,2)]
            return self._secuencia(self._mel(mel, 60, "andina", extender=True), 100)

        if nombre == "ruta_selva":
            mel = [(0,0,1),(2,0,1),(0,0,1),(4,0,1),(5,0,1),(4,0,1),(2,0,1),(0,0,1),
                   (0,0,1),(4,0,1),(2,0,1),(0,0,2),
                   (5,0,1),(4,0,1),(2,0,1),(0,0,1),(2,0,1),(4,0,1),(5,0,1),(4,0,1),
                   (2,0,2),(0,0,1),(4,0,1),(2,0,3)]
            return self._secuencia(self._mel(mel, 65, "andina", extender=True), 118)

        if nombre == "pueblo_costa":
            mel = [(0,0,2),(2,0,2),(4,0,2),(2,0,2),(0,0,2),(-1,0,2),
                   (2,0,2),(4,0,2),(5,0,2),(4,0,2),(2,0,2),(0,0,3)]
            return self._secuencia(self._mel(mel, 60, "mayor", extender=True), 84)

        if nombre == "pueblo_sierra":
            mel = [(0,0,2),(3,0,2),(5,0,2),(3,0,2),(2,0,2),(0,0,2),(-1,0,2),
                   (0,0,2),(2,0,2),(3,0,2),(5,0,2),(3,0,2),(2,0,3)]
            return self._secuencia(self._mel(mel, 62, "andina", extender=True), 80)

        if nombre == "pueblo_selva":
            mel = [(0,0,2),(2,0,2),(0,0,1),(4,0,1),(2,0,2),(-1,0,2),
                   (0,0,1),(2,0,1),(4,0,2),(5,0,2),(4,0,1),(2,0,2),(-1,0,2)]
            return self._secuencia(self._mel(mel, 60, "andina", extender=True), 90)

        if nombre == "capital":
            mel = [(0,0,1),(4,0,1),(7,0,1),(4,0,1),(2,0,1),(5,0,1),(4,0,1),(2,0,1),
                   (0,0,2),(7,0,2),
                   (9,0,1),(7,0,1),(4,0,1),(2,0,1),(0,0,2),(4,0,1),(5,0,1),(7,0,1),
                   (4,0,3),(0,0,2)]
            return self._secuencia(self._mel(mel, 65, "mayor", extender=True), 118)

        if nombre == "batalla_salvaje":
            mel = [(0,0,1),(0,0,1),(3,0,1),(0,0,1),(5,0,1),(0,0,1),(3,0,1),(2,0,1),
                   (0,0,1),(0,0,1),(3,0,1),(0,0,1),(7,0,1),(5,0,1),(3,0,1),(2,0,1),
                   (7,0,1),(5,0,1),(3,0,1),(2,0,1),(0,0,1),(3,0,1),(5,0,1),(7,0,1),
                   (5,0,1),(3,0,1),(2,0,1),(0,0,1),(0,0,2)]
            return self._secuencia(self._mel(mel, 65, "menor", extender=True), 130)

        if nombre == "batalla_entrenador":
            mel = [(0,0,1),(2,0,1),(4,0,1),(2,0,1),(5,0,1),(4,0,1),(2,0,1),(0,0,1),
                   (7,0,1),(5,0,1),(4,0,1),(2,0,1),(0,0,2),
                   (7,0,1),(4,0,1),(2,0,1),(0,0,1),(4,0,1),(2,0,1),(7,0,1),(5,0,1),
                   (4,0,1),(2,0,1),(0,0,3)]
            return self._secuencia(self._mel(mel, 60, "menor", extender=True), 125)

        if nombre == "batalla_lider":
            mel = [(0,0,1),(3,0,1),(5,0,1),(7,0,1),(5,0,1),(3,0,1),(0,0,1),(3,0,1),
                   (7,0,1),(5,0,1),(3,0,1),(2,0,1),(0,0,2),
                   (7,0,1),(9,0,1),(7,0,1),(5,0,1),(3,0,1),(2,0,1),(0,0,1),(3,0,1),
                   (5,0,1),(7,0,1),(5,0,2),(0,0,3)]
            return self._secuencia(self._mel(mel, 58, "menor", extender=True), 132)

        if nombre == "batalla_liga":
            mel = [(0,0,1),(7,0,1),(5,0,1),(7,0,1),(0,0,1),(4,0,1),(7,0,1),(4,0,1),
                   (0,0,1),(7,0,1),(5,0,1),(3,0,1),(0,0,2),
                   (9,0,1),(7,0,1),(5,0,1),(4,0,1),(2,0,1),(0,0,1),(7,0,1),(5,0,1),
                   (4,0,1),(2,0,1),(0,0,3)]
            return self._secuencia(self._mel(mel, 62, "menor", extender=True), 135)

        if nombre == "batalla_supay":
            mel = [(0,0,1),(1,0,1),(3,0,1),(1,0,1),(6,0,1),(3,0,1),(1,0,1),(0,0,1),
                   (6,0,1),(3,0,1),(1,0,1),(0,0,1),(-1,0,2),
                   (6,0,1),(5,0,1),(3,0,1),(1,0,1),(0,0,1),(1,0,1),(3,0,1),(6,0,1),
                   (5,0,1),(3,0,1),(1,0,1),(0,0,3)]
            return self._secuencia(self._mel(mel, 55, "menor", extender=True), 122)

        if nombre == "batalla_legendario":
            mel = [(0,0,2),(3,0,2),(7,0,2),(3,0,2),(5,0,2),(3,0,2),(-1,0,2),
                   (7,0,2),(10,0,2),(7,0,2),(3,0,2),(5,0,3),(-1,0,2)]
            return self._secuencia(self._mel(mel, 50, "menor"), 112)

        # El resto igual que antes...
        if nombre == "victoria":
            mel = [(0,0,1),(0,0,1),(0,0,1),(0,0,3),(4,0,1),(2,0,1),(0,0,4),
                   (4,0,1),(4,0,1),(4,0,3),(7,0,2),(0,0,4)]
            return self._secuencia(self._mel(mel, 65, "mayor"), 142)

        if nombre == "derrota":
            mel = [(5,0,2),(4,0,2),(2,0,2),(0,0,4),(-1,0,2),
                   (5,0,2),(4,0,2),(2,0,3),(-1,0,4)]
            return self._secuencia(self._mel(mel, 60, "menor"), 88)

        if nombre == "medalla":
            mel = [(0,0,1),(2,0,1),(4,0,1),(7,0,4),(4,0,1),(7,0,4),
                   (0,0,1),(4,0,1),(7,0,1),(10,0,4),(7,0,3)]
            return self._secuencia(self._mel(mel, 65, "mayor"), 132)

        if nombre == "curacion":
            mel = [(0,0,1),(4,0,1),(7,0,3),(0,0,1),(4,0,1),(7,0,3)]
            return self._secuencia(self._mel(mel, 65, "mayor"), 120)

        if nombre == "evolucion":
            mel = [(0,0,1),(4,0,1),(7,0,1),(9,0,4),(7,0,1),(9,0,1),(12,0,5)]
            return self._secuencia(self._mel(mel, 60, "mayor"), 132)

        return self._secuencia(self._mel([(0,0,2),(4,0,2),(2,0,2),(5,0,3)], 60, "andina"), 110)
    # --------------------------- reproducción ---------------------------
    def _obtener(self, nombre):
        if nombre in self.cache:
            return self.cache[nombre]
        try:
            snd = self._a_sound(self._construir(nombre))
            self.cache[nombre] = snd
            return snd
        except Exception as e:
            print(f"⚠ Música '{nombre}': {e}")
            self.cache[nombre] = None
            return None

    def fondo(self, nombre):
        if not self.activa or self.silenciada:
            return
        if nombre == self.actual:
            return
        snd = self._obtener(nombre)
        if snd is None:
            return
        try:
            import time
            jingle_activo = time.time() < self._jingle_hasta
            self.canal.stop()
            # No revientes el volumen si hay un jingle sonando
            if jingle_activo:
                self.canal.set_volume(self.volumen * 0.25)
            else:
                self.canal.set_volume(self.volumen)
            self.canal.play(snd, loops=-1)
            self.actual = nombre
        except Exception:
            pass

    def jingle(self, nombre):
        if not self.activa or self.silenciada:
            return
        snd = self._obtener(nombre)
        if snd is None:
            return
        try:
            # Bajar música mientras suena el jingle
            if self.canal is not None:
                self.canal.set_volume(self.volumen * 0.25)
            c = pygame.mixer.Channel(6)
            c.set_volume(min(1.0, self.volumen + 0.25))
            c.play(snd, loops=0)
            import time
            self._jingle_hasta = time.time() + snd.get_length() + 0.1
        except Exception:
            pass

    def alternar(self):
        self.silenciada = not self.silenciada
        if self.activa and self.canal is not None:
            self.canal.set_volume(0.0 if self.silenciada else self.volumen)
        return not self.silenciada

    def actualizar(self, dt):
        import time
        if self._jingle_hasta > 0 and time.time() >= self._jingle_hasta:
            self._jingle_hasta = 0.0
            if self.canal is not None:
                self.canal.set_volume(0.0 if self.silenciada else self.volumen)

    def detener(self):
        if self.activa and self.canal is not None:
            self.canal.stop()
            self.actual = None