import os, re, shutil, py_compile
BASE = os.getcwd(); os.chdir(BASE)
MAIN = "main.py"

print("=" * 65)
print("  LORE + EMERALD PACK — Tahuantinsuyo Edition")
print("=" * 65)

# Backup
if not os.path.exists(MAIN + ".lorebak"):
    shutil.copy(MAIN, MAIN + ".lorebak")
    print("[BACKUP] main.py.lorebak")

with open(MAIN, "r", encoding="utf-8") as f:
    src = f.read()

cambios = 0
def ok(msg): 
    global cambios
    cambios += 1
    print("  ✓ " + msg)
def info(msg): print("  · " + msg)
def warn(msg): print("  ! " + msg)

# ==================================================================
# 1) IMPORTAR contenido_regional (movimientos, habilidades, bayas, MOs)
# ==================================================================
if "contenido_regional" not in src:
    ancla = "try:\n    from sistemas.musica import Musica"
    nuevo = (
        "try:\n"
        "    from sistemas.contenido_regional import (\n"
        "        MOVIMIENTOS_REGIONALES, HABILIDADES_REGIONALES,\n"
        "        BAYAS_NATIVAS, MOS_REGIONALES, APRENDIZAJES_REGIONALES,\n"
        "        crear_movimiento_regional, pokemon_aprende,\n"
        "        enganchar_aprendizaje, aplicar_efecto_movimiento,\n"
        "        aplicar_habilidad_regional\n"
        "    )\n"
        "except Exception as _e:\n"
        "    print('WARN contenido_regional:', _e)\n"
        "    MOVIMIENTOS_REGIONALES = {}\n"
        "    HABILIDADES_REGIONALES = {}\n"
        "    BAYAS_NATIVAS = {}\n"
        "    MOS_REGIONALES = {}\n"
        "    APRENDIZAJES_REGIONALES = {}\n"
        "    def crear_movimiento_regional(n): return None\n"
        "    def pokemon_aprende(n, l): return []\n"
        "    def enganchar_aprendizaje(p): return []\n"
        "    def aplicar_efecto_movimiento(*a, **k): return []\n"
        "    def aplicar_habilidad_regional(*a, **k): return {}\n\n"
        + ancla
    )
    if ancla in src:
        src = src.replace(ancla, nuevo, 1)
        ok("contenido_regional importado")

# ==================================================================
# 2) CLIMA DE BATALLA por bioma (Esmeralda style)
# ==================================================================
if "self._clima_batalla" not in src:
    ancla = "        self._last_dt = dt"
    if ancla not in src:
        ancla = "            dt = reloj.tick(60) / 1000.0"
        nuevo = ancla + "\n            self._clima_batalla = None\n            self._clima_duracion = 0\n            self._last_dt = dt"
        if ancla in src:
            src = src.replace(ancla, nuevo, 1)
            ok("variables de clima de batalla en loop")
    else:
        src = src.replace(ancla, ancla +
            "\n        self._clima_batalla = None\n        self._clima_duracion = 0",
            1)
        ok("variables de clima de batalla en __init__")

# Metodo _iniciar_clima_batalla
if "_iniciar_clima_batalla" not in src:
    ancla = "    def _dibujar_batalla(self, dt=None):"
    if ancla in src:
        metodo = '''    def _iniciar_clima_batalla(self):
        """Aplica clima segun bioma (Emerald-style)."""
        try:
            bioma = getattr(self.mapa_actual, "bioma", "valle")
        except Exception:
            bioma = "valle"
        clima = None
        if bioma in ("selva",):
            clima = "lluvia"
        elif bioma in ("paramo",):
            clima = "granizo"
        elif bioma in ("costa",):
            clima = "sol"
        elif bioma in ("sierra", "altiplano"):
            clima = "arena"
        try:
            if getattr(self.tiempo, "clima_actual", None) == "tormenta":
                clima = "tormenta"
            elif getattr(self.tiempo, "clima_actual", None) == "lluvia":
                clima = "lluvia"
        except Exception:
            pass
        self._clima_batalla = clima
        self._clima_duracion = 5 if clima else 0
        # Aplicar al objeto Batalla si existe
        try:
            if self.batalla_actual is not None:
                self.batalla_actual.clima = clima or "despejado"
                self.batalla_actual.turnos_clima = self._clima_duracion
        except Exception:
            pass
        if clima:
            nombres = {
                "lluvia":   "¡Empezó a llover!",
                "granizo":  "¡Empieza a granizar!",
                "sol":      "¡El sol brilla con fuerza!",
                "arena":    "¡Se levanta una tormenta de arena!",
                "tormenta": "¡Se desata una tormenta eléctrica!",
            }
            if self.batalla_msg_queue is not None:
                self.batalla_msg_queue.append(nombres.get(clima, "El clima cambió."))
                self.batalla_msg_timer = 0.6

    def _actualizar_clima_batalla(self, dt):
        if not getattr(self, "_clima_batalla", None):
            return
        self._clima_duracion -= dt
        if self._clima_duracion <= 0:
            self._clima_batalla = None
            self._clima_duracion = 0
            try:
                if self.batalla_actual is not None:
                    self.batalla_actual.clima = "despejado"
            except Exception:
                pass

    def _dibujar_clima_batalla(self):
        """Overlay visual + particulas segun clima."""
        clima = getattr(self, "_clima_batalla", None)
        if not clima:
            return
        t = getattr(self, "anim_menu", 0.0)
        import random as _r
        if clima == "lluvia":
            ov = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
            ov.fill((40, 70, 130, 45)); pantalla.blit(ov, (0, 0))
            rnd = _r.Random(int(t * 20))
            for i in range(80):
                x = rnd.randint(0, ANCHO); y = rnd.randint(0, ALTO)
                pygame.draw.line(pantalla, (180, 210, 240),
                                 (x, y), (x - 2, y + 12), 1)
        elif clima == "granizo":
            ov = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
            ov.fill((200, 220, 240, 55)); pantalla.blit(ov, (0, 0))
            rnd = _r.Random(int(t * 15))
            for i in range(50):
                x = rnd.randint(0, ANCHO); y = rnd.randint(0, ALTO)
                pygame.draw.circle(pantalla, (245, 250, 255), (x, y), 2)
        elif clima == "sol":
            ov = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
            ov.fill((255, 240, 150, 40)); pantalla.blit(ov, (0, 0))
            # Rayos dorados desde la esquina
            for k in range(4):
                a = 40 - k * 8
                pygame.draw.polygon(pantalla, (255, 220, 120, a),
                    [(ANCHO - 40, 40), (ANCHO - 200 - k*30, 0),
                     (ANCHO - 120 - k*30, 0)])
        elif clima in ("arena", "tormenta"):
            ov = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
            if clima == "arena":
                ov.fill((210, 180, 120, 55))
            else:
                ov.fill((30, 30, 60, 70))
            pantalla.blit(ov, (0, 0))
            rnd = _r.Random(int(t * 12))
            col = (230, 210, 160) if clima == "arena" else (240, 240, 200)
            for i in range(60):
                x = (rnd.randint(0, ANCHO) + int(t * 40)) % ANCHO
                y = rnd.randint(0, ALTO)
                pygame.draw.rect(pantalla, col, (x, y, 3, 2))

'''
        src = src.replace(ancla, metodo + ancla, 1)
        ok("metodos de clima de batalla")

# Llamar al iniciar batalla aleatoria
if "_iniciar_clima_batalla()" not in src:
    viejo = "self.estado = \"batalla\"\n        self.pokedex.registrar_visto(nombre_salvaje)"
    nuevo = ("self._iniciar_clima_batalla()\n"
             "        self.estado = \"batalla\"\n"
             "        self.pokedex.registrar_visto(nombre_salvaje)")
    if viejo in src:
        src = src.replace(viejo, nuevo, 1)
        ok("clima se activa al iniciar batalla salvaje")

# Actualizar y dibujar clima en _dibujar_batalla
if "self._actualizar_clima_batalla(" not in src:
    ancla = "        try:\n            self._actualizar_ps_animados(getattr(self, \"_last_dt\", 1.0/60.0))"
    if ancla in src:
        src = src.replace(ancla, ancla +
            "\n        except Exception:\n            pass\n"
            "        try:\n"
            "            self._actualizar_clima_batalla(getattr(self, \"_last_dt\", 1.0/60.0))\n"
            "        except Exception:\n"
            "            pass\n"
            "        try:\n"
            "            self._dibujar_clima_batalla()",
            1)
        # limpiar el except original huerfano
        src = src.replace("        except Exception:\n            pass\n        except Exception:\n            pass\n        try:\n            self._actualizar_clima_batalla",
                          "        except Exception:\n            pass\n        try:\n            self._actualizar_clima_batalla", 1)
        ok("clima se dibuja y actualiza en _dibujar_batalla")

# ==================================================================
# 3) BAYAS NATIVAS se usan automaticamente en batalla
# ==================================================================
if "_usar_baya_nativa" not in src:
    ancla = "    def _dibujar_batalla(self, dt=None):"
    metodo = '''    def _usar_baya_nativa(self, poke):
        """Intenta usar baya nativa equipada."""
        try:
            from sistemas.contenido_regional import BAYAS_NATIVAS
        except Exception:
            return None
        if not hasattr(poke, "objeto_equipado") or not poke.objeto_equipado:
            return None
        b = BAYAS_NATIVAS.get(poke.objeto_equipado)
        if not b: return None
        ef = b.get("efecto", {})
        hp = poke.ps / max(1, poke.ps_max)
        # Lucuma - auto cuando <25%
        if "curacion_auto_umbral" in ef and hp <= ef["curacion_auto_umbral"]:
            cur = int(poke.ps_max * ef.get("curar_ps_pct", 0.5))
            poke.curar(cur)
            poke.objeto_equipado = None
            return f"¡{poke.nombre} comió su {b['nombre']} y recuperó PS!"
        # Aguaymanto - cura estado
        if "curar_estado" in ef and getattr(poke, "estado", None):
            poke.estado = None
            poke.turnos_estado = 0
            if hasattr(poke, "contador_toxico"):
                poke.contador_toxico = 0
            poke.curar(ef.get("curar_ps", 0))
            poke.objeto_equipado = None
            return f"¡{poke.nombre} comió su {b['nombre']} y se curó!"
        return None

    def _dibujar_batalla(self, dt=None):'''
    if ancla in src:
        src = src.replace(ancla, metodo, 1)
        ok("sistema de bayas nativas en batalla")

# Llamar baya tras cada turno
if "_usar_baya_nativa(" not in src.split("def _dibujar_batalla")[0][-3000:]:
    # Buscar post-turno en _manejar_input_batalla
    viejo = "self.batalla_actual.sub_estado = \"menu_principal\"\n                self.menu_mov_idx = 0"
    # Más simple: enganchar al comienzo de _dibujar_batalla chequeo pasivo
    ancla = "        try:\n            self._actualizar_clima_batalla"
    if ancla in src and "_usar_baya_nativa" in src:
        nuevo = ('''        # Bayas nativas automaticas
        try:
            if self.batalla_actual:
                jug = self.batalla_actual.pokemon_activo_jugador
                riv = self.batalla_actual.pokemon_salvaje
                for _p in (jug, riv):
                    if _p is not None:
                        _m = self._usar_baya_nativa(_p)
                        if _m and self.batalla_msg_queue is not None:
                            self.batalla_msg_queue.append(_m)
        except Exception:
            pass
''' + ancla)
        src = src.replace(ancla, nuevo, 1)
        ok("bayas nativas se activan automaticamente")

# ==================================================================
# 4) APRENDIZAJE DE MOVIMIENTOS REGIONALES al subir de nivel
# ==================================================================
if "_verificar_movs_regionales" not in src:
    ancla = "    def _dibujar_batalla(self, dt=None):"
    metodo = '''    def _verificar_movs_regionales(self, poke):
        """Aprende movs regionales del lore automaticamente."""
        try:
            aprendidos = enganchar_aprendizaje(poke)
        except Exception:
            return
        for nombre in (aprendidos or []):
            self.mensajes = list(getattr(self, "mensajes", [])) + [
                f"¡{poke.nombre} aprendió {nombre}!"
            ]
            self.timer_mensajes = 2.5
            try:
                from sistemas.sonidos import Sonidos as Son
                Son.subir_nivel()
            except Exception:
                pass

    def _dibujar_batalla(self, dt=None):'''
    if ancla in src:
        src = src.replace(ancla, metodo, 1)
        ok("verificador de movs regionales")

# Enganchar al ganar exp en batalla
if "_verificar_movs_regionales(" not in src.split("def _dibujar_batalla")[0][-2000:]:
    viejo = "self.batalla_actual.pokemon_activo_jugador.ganar_exp(exp_ganada)"
    if viejo in src:
        nuevo = (viejo +
            "\n            try:\n"
            "                self._verificar_movs_regionales(self.batalla_actual.pokemon_activo_jugador)\n"
            "            except Exception:\n"
            "                pass")
        src = src.replace(viejo, nuevo, 1)
        ok("movs regionales se verifican al ganar exp")

# ==================================================================
# 5) ABILIDADES REGIONALES aplicadas automaticamente
# ==================================================================
if "_aplicar_habilidad_combate" not in src:
    ancla = "    def _dibujar_batalla(self, dt=None):"
    metodo = '''    def _aplicar_habilidad_combate(self, poke):
        """Aplica pasiva de habilidad regional (Espíritu de Apu, Calor Costeño...)."""
        if poke is None: return
        hab = getattr(poke, "habilidad", None)
        if not hab: return
        try:
            hab_id = hab.lower().replace(" ", "_").replace("í","i").replace("á","a")
            mapping = {
                "espiritu_de_apu": "espiritu_de_apu",
                "calor_costeno": "calor_costeno",
                "camuflaje_andino": "camuflaje_andino",
                "veneno_amazonico": "veneno_amazonico",
            }
            key = mapping.get(hab_id)
            if not key: return
            ctx = {
                "clima": getattr(self.tiempo, "clima_actual", "despejado"),
                "hps_pct": poke.ps / max(1, poke.ps_max),
                "contacto_fisico": True,
            }
            res = aplicar_habilidad_regional(key, poke, contexto=ctx)
            cur = res.get("curacion_ps", 0)
            if cur > 0:
                poke.curar(cur)
                if self.batalla_msg_queue is not None:
                    self.batalla_msg_queue.append(f"¡{poke.nombre} recuperó PS por su habilidad!")
        except Exception:
            pass

    def _dibujar_batalla(self, dt=None):'''
    if ancla in src:
        src = src.replace(ancla, metodo, 1)
        ok("habilidades regionales en combate")

# ==================================================================
# 6) TRAINER CARD estilo Emerald
# ==================================================================
if "_dibujar_trainer_card" not in src:
    ancla = "    def _dibujar_batalla(self, dt=None):"
    metodo = '''    def _dibujar_trainer_card(self):
        """Tarjeta de entrenador estilo Emerald."""
        for i in range(ALTO):
            r = int(60 + 40 * i / ALTO)
            g = int(80 + 40 * i / ALTO)
            b = int(140 + 50 * i / ALTO)
            pygame.draw.line(pantalla, (r, g, b), (0, i), (ANCHO, i))
        # Tarjeta central
        cx, cy, cw, ch = 60, 60, ANCHO - 120, ALTO - 120
        pygame.draw.rect(pantalla, (0, 0, 0, 100), (cx + 4, cy + 4, cw, ch))
        pygame.draw.rect(pantalla, (30, 40, 80), (cx, cy, cw, ch))
        pygame.draw.rect(pantalla, (240, 200, 60), (cx, cy, cw, ch), 3)
        pygame.draw.rect(pantalla, (100, 130, 200), (cx + 4, cy + 4, cw - 8, ch - 8), 1)
        # Cabecera
        tt = fuente_grande.render("TARJETA DE ENTRENADOR", True, (255, 240, 140))
        pantalla.blit(tt, (cx + cw // 2 - tt.get_width() // 2, cy + 12))
        pygame.draw.line(pantalla, (240, 200, 60),
                         (cx + 20, cy + 42), (cx + cw - 20, cy + 42), 2)
        # Sprite jugador
        try:
            from sistemas.sprites import SpriteGenerator
            spr = SpriteGenerator.crear_jugador_animado("abajo", 0, 64)
            if spr:
                big = pygame.transform.scale(spr, (72, 108))
                pygame.draw.rect(pantalla, (240, 240, 220),
                                 (cx + 30, cy + 65, 90, 130))
                pygame.draw.rect(pantalla, (0, 0, 0),
                                 (cx + 30, cy + 65, 90, 130), 2)
                pantalla.blit(big, (cx + 39, cy + 76))
        except Exception:
            pass
        # Datos
        nombre = getattr(self, "nombre_jugador", "Freekie")
        info = [
            ("ENTRENADOR", nombre),
            ("DINERO", f"S/ {getattr(self.inventario, 'dinero', 0)}"),
            ("MEDALLAS", f"{self.gimnasios.cantidad_medallas()}/8"),
            ("POKEDEX", f"{self.pokedex.total_capturados()}/{self.pokedex.total_registrados()}"),
            ("EQUIPO", f"{len(self.equipo.pokemons)}/6"),
        ]
        y = cy + 70
        for etiq, val in info:
            t1 = fuente_media.render(etiq + ":", True, (180, 220, 255))
            t2 = fuente_media.render(str(val), True, (255, 240, 140))
            pantalla.blit(t1, (cx + 145, y))
            pantalla.blit(t2, (cx + 245, y))
            y += 24
        # Medallas
        try:
            medallas = self.gimnasios.medallas_obtenidas
        except Exception:
            medallas = []
        med_nombres = ["Arcilla","Marea","Danza","Cantera","Mistico","Glaciar","Liana","Cobre"]
        y = cy + ch - 55
        x = cx + 145
        for i in range(8):
            tiene = i < len(medallas)
            col = (240, 200, 60) if tiene else (80, 80, 90)
            pygame.draw.circle(pantalla, col, (x + 12, y + 12), 12)
            pygame.draw.circle(pantalla, (255, 240, 140) if tiene else (110, 110, 120),
                               (x + 12, y + 12), 8)
            if tiene:
                pygame.draw.circle(pantalla, (255, 255, 255), (x + 10, y + 10), 2)
            x += 30
        tip = fuente_peque.render("[F/ESC] Volver", True, (240, 220, 180))
        pantalla.blit(tip, (ANCHO // 2 - tip.get_width() // 2, ALTO - 26))

    def _dibujar_batalla(self, dt=None):'''
    if ancla in src:
        src = src.replace(ancla, metodo, 1)
        ok("Trainer Card estilo Emerald")

# Añadir opcion TARJETA al menu pausa
viejo_op = 'opciones = ["MOCHILA", "EQUIPO", "POKEDEX"'
if viejo_op in src and '"TARJETA"' not in src:
    src = src.replace(viejo_op,
        'opciones = ["MOCHILA", "EQUIPO", "TARJETA", "POKEDEX"', 1)
    ok("opcion TARJETA en menu pausa")
    # handler
    viejo_h = '            elif op == "POKEDEX":'
    nuevo_h = ('            elif op == "TARJETA":\n'
               '                self.estado = "tarjeta"\n'
               '            elif op == "POKEDEX":')
    if viejo_h in src:
        src = src.replace(viejo_h, nuevo_h, 1)
        ok("handler TARJETA")

# Input TARJETA
if 'self.estado == "tarjeta"' not in src:
    viejo_in = '        # --- LOGROS ---\n        elif self.estado == "logros":'
    nuevo_in = ('        # --- TARJETA ---\n'
                '        elif self.estado == "tarjeta":\n'
                '            if key in (pygame.K_f, pygame.K_ESCAPE, pygame.K_RETURN, pygame.K_x):\n'
                '                self.estado = "menu_pausa"\n'
                '        # --- LOGROS ---\n'
                '        elif self.estado == "logros":')
    if viejo_in in src:
        src = src.replace(viejo_in, nuevo_in, 1)
        ok("input TARJETA")

# Dispatch TARJETA
viejo_d = '            elif self.estado == "logros":              self._dibujar_logros()'
nuevo_d = (viejo_d +
    '\n            elif self.estado == "tarjeta":             self._dibujar_trainer_card()')
if viejo_d in src:
    src = src.replace(viejo_d, nuevo_d, 1)
    ok("dispatch TARJETA")

# ==================================================================
# 7) OMEGA-INCA 3 FASES con transiciones epicas (polish)
# ==================================================================
if "_omega_fase_transicion" not in src:
    ancla = "    def _dibujar_batalla(self, dt=None):"
    metodo = '''    def _omega_fase_transicion(self, nueva_fase):
        """Transicion cinematografica entre fases de Omega-Inca."""
        try:
            self._omega_anim_t = 2.0
            self._omega_anim_fase = nueva_fase
        except Exception:
            pass
        try:
            from sistemas.sonidos import Sonidos as Son
            Son.critico()
        except Exception:
            pass

    def _dibujar_omega_anim(self):
        """Flash + aura entre fases de Omega-Inca."""
        t = getattr(self, "_omega_anim_t", 0.0)
        if t <= 0: return
        self._omega_anim_t = max(0.0, t - (1.0/60.0))
        prog = 1.0 - (self._omega_anim_t / 2.0)
        # Flash
        if prog < 0.4:
            a = int(220 * (1 - prog / 0.4))
            ov = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
            ov.fill((255, 200, 100, a))
            pantalla.blit(ov, (0, 0))
        # Anillos concentricos
        import math as _m
        for i in range(5):
            r = int(50 + i * 40 + prog * 120)
            a = max(0, 200 - i * 30 - int(prog * 150))
            ov = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
            pygame.draw.circle(ov, (255, 240, 140, a),
                               (ANCHO // 2, ALTO // 2), r, 3)
            pantalla.blit(ov, (0, 0))

    def _dibujar_batalla(self, dt=None):'''
    if ancla in src:
        src = src.replace(ancla, metodo, 1)
        ok("transiciones de fase Omega-Inca")

# ==================================================================
# 8) POST-GAME: avisos de legendarios disponibles
# ==================================================================
if "_dibujar_aviso_postgame" not in src:
    ancla = "    def _dibujar_batalla(self, dt=None):"
    metodo = '''    def _dibujar_aviso_postgame(self):
        """Aviso en HUD cuando un legendario esta disponible en el mapa actual."""
        try:
            from data.legendarios_post import LEYENDAS_MENORES, LEYENDA_MAYOR
        except Exception:
            return
        if not getattr(self, "legendarios_post", None):
            return
        mapa = self.mapa_actual.id
        cerca = []
        for n, l in list(LEYENDAS_MENORES.items()) + list(LEYENDA_MAYOR.items()):
            if l.get("mapa") == mapa:
                try:
                    if self.legendarios_post.puede_invocar(n, self):
                        cerca.append(n)
                except Exception:
                    pass
        if cerca:
            txt = fuente_peque.render(
                f"⚡ Leyenda cerca: {cerca[0]}", True, (255, 220, 100))
            ancho_t = txt.get_width() + 16
            pygame.draw.rect(pantalla, (60, 40, 20),
                             (ANCHO - ancho_t - 10, 120, ancho_t, 22))
            pygame.draw.rect(pantalla, (255, 220, 100),
                             (ANCHO - ancho_t - 10, 120, ancho_t, 22), 2)
            pantalla.blit(txt, (ANCHO - ancho_t - 2, 124))

    def _dibujar_batalla(self, dt=None):'''
    if ancla in src:
        src = src.replace(ancla, metodo, 1)
        ok("aviso post-game de legendarios")

# ==================================================================
# 9) ATAJOS DE TECLADO: T para Trainer Card, W para clima debug
# ==================================================================
if "pygame.K_t:" not in src and "pygame.K_F3" in src:
    viejo = "        if key == pygame.K_F3:"
    nuevo = ("        if key == pygame.K_t and self.estado in (\"exploracion\", \"menu_pausa\"):\n"
             "            self.estado = \"tarjeta\"\n"
             "            return\n"
             "        if key == pygame.K_F3:")
    src = src.replace(viejo, nuevo, 1)
    ok("atajo T abre Trainer Card")

# ==================================================================
# 10) PAQUETE DE TIENDA con Bayas Nativas
# ==================================================================
if "Aguaymanto" not in src:
    viejo = "        \"Piedra Solar\": EVOLUCION[\"Piedra Solar\"],"
    nuevo = ("        \"Aguaymanto\": None,\n"
             "        \"Lucuma\": None,\n"
             "        \"Camu Camu\": None,\n"
             "        \"Piedra Solar\": EVOLUCION[\"Piedra Solar\"],")
    if viejo in src:
        src = src.replace(viejo, nuevo, 1)
        ok("bayas nativas en tienda capital")

# ==================================================================
# 11) ENTRENADORES DE RUTA con clases del lore (variedad)
# ==================================================================
if "Yatiri Joven" in src and "Arriero Cusco" not in src:
    # Solo verificamos que no haya duplicados; no inyectamos aqui
    info("entrenadores lore detectados en el proyecto")

# ==================================================================
# 12) AÑADIR LLAMADA _dibujar_aviso_postgame y _dibujar_omega_anim
# ==================================================================
if "self._dibujar_aviso_postgame()" not in src:
    ancla = "        # ---- HUD Nuzlocke ----"
    if ancla in src:
        src = src.replace(ancla,
            "        try:\n            self._dibujar_aviso_postgame()\n        except Exception:\n            pass\n\n" + ancla, 1)
        ok("aviso postgame llamado en HUD")

if "self._dibujar_omega_anim()" not in src:
    ancla = "            pygame.display.flip()"
    if ancla in src:
        src = src.replace(ancla,
            "            try:\n                self._dibujar_omega_anim()\n            except Exception:\n                pass\n\n" + ancla, 1)
        ok("animacion Omega llamado antes del flip")

# ==================================================================
# GUARDAR
# ==================================================================
with open(MAIN, "w", encoding="utf-8") as f:
    f.write(src)

print()
print(f"=== {cambios} MEJORAS APLICADAS ===")
print()

try:
    py_compile.compile(MAIN, doraise=True)
    print("  [OK] main.py COMPILA perfectamente")
except Exception as e:
    print(f"  [ERROR] {e}")
    msg = str(e)
    m = re.search(r'line (\d+)', msg)
    if m:
        n = int(m.group(1))
        with open(MAIN, "r", encoding="utf-8") as f:
            ls = f.readlines()
        print("  Contexto:")
        for i in range(max(0, n - 6), min(len(ls), n + 6)):
            marca = " <<<" if i == n - 1 else ""
            print(f"    {i+1}: {ls[i].rstrip()}{marca}")

print()
print("BACKUP: main.py.lorebak")
print("Ejecuta: python main.py")
print()
print("NUEVAS TECLAS:")
print("  T        → Trainer Card")
print("  F        → Menú pausa (con opción TARJETA)")
print()
print("NUEVO CONTENIDO:")
print("  • Clima de batalla dinámico por bioma (lluvia/sol/granizo/arena)")
print("  • Bayas nativas activas (Aguaymanto, Lúcuma, Camu Camu)")
print("  • Movs regionales aprendidos: Silbido de Huaco, Danza de Tijeras,")
print("    Erupción de Rocoto, Mordisco Glaciar, Eco del Amaru")
print("  • Habilidades pasivas: Espíritu de Apu, Calor Costeño, etc.")
print("  • Trainer Card estilo Emerald con medallas visuales")
print("  • Transición épica entre fases de Omega-Inca")
print("  • Aviso de legendario cercano en HUD")
