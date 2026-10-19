"""guardado.py - Save/load JSON compatible con MapaVisual v2 (pos_x/pos_y)."""
import json
import os
from data.pokedex import POKEDEX_COMPLETA
from sistemas.batalla import PokemonBatalla, Movimiento

RUTA_GUARDADOS = "guardados"


def _asegurar():
    if not os.path.exists(RUTA_GUARDADOS):
        os.makedirs(RUTA_GUARDADOS)


def _serializar_pokemon(p):
    return {
        "nombre": p.nombre, "nivel": p.nivel, "ps": p.ps,
        "exp": getattr(p, "exp", 0), "exp_total": getattr(p, "exp_total", 0),
        "movimientos": [
            {"nombre": m.nombre, "tipo": m.tipo, "potencia": m.potencia,
             "precision": m.precision, "categoria": m.categoria,
             "pp": m.pp, "pp_max": m.pp_max}
            for m in p.movimientos
        ],
 "es_shiny": getattr(p, "es_shiny", False),
        "color_shiny": getattr(p, "color_shiny", None),
    }


def _deserializar_pokemon(data):
    datos = POKEDEX_COMPLETA.get(data["nombre"])
    if not datos:
        return None
    p = PokemonBatalla(datos, nivel=data["nivel"])
    p.ps = data.get("ps", p.ps_max)
    p.exp = data.get("exp", 0)
    p.exp_total = data.get("exp_total", 0)
    p.movimientos = []
    for md in data.get("movimientos", []):
        p.movimientos.append(Movimiento(md))
    p.es_shiny = data.get("es_shiny", False)
    p.color_shiny = data.get("color_shiny", None)
    return p


def guardar_partida(juego, slot=1):
    try:
        _asegurar()
        equipo_data = [_serializar_pokemon(p) for p in juego.equipo.pokemons]
        pc_data = []
        for caja in juego.pc.cajas:
            pc_data.append([_serializar_pokemon(p) for p in caja.pokemons])
        inv_data = {
            "dinero": juego.inventario.dinero,
            "objetos": {n: d["cantidad"] for n, d in juego.inventario.objetos.items()},
        }
        gim = {
            "medallas": list(juego.gimnasios.medallas_obtenidas),
            "derrotados": list(juego.gimnasios.lideres_derrotados),
        }
        hist = {
            "completados": list(getattr(juego.historia, "eventos_completados", [])),
            "capitulo": getattr(juego.historia, "capitulo_actual", 1),
        }
        m = juego.mapa_actual
        mapa_data = {"id": m.id, "pos_x": m.pos_x, "pos_y": m.pos_y,
                     "direccion": m.direccion}
        pokedex_data = {
            "vistos": list(juego.pokedex.vistos),
            "capturados": list(juego.pokedex.capturados),
        }
        datos = {
            "version": "2.0",
            "timestamp": __import__("time").time(),
            "equipo": equipo_data, "pc": pc_data, "inventario": inv_data,
            "gimnasios": gim, "historia": hist, "mapa": mapa_data,
            "pokedex": pokedex_data,
        }
        with open(os.path.join(RUTA_GUARDADOS, f"save_{slot}.json"),
                  "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        import traceback; traceback.print_exc()
        print(f"Error al guardar: {e}")
        return False


def cargar_partida(juego, slot=1):
    try:
        _asegurar()
        ruta = os.path.join(RUTA_GUARDADOS, f"save_{slot}.json")
        if not os.path.exists(ruta):
            return False
        with open(ruta, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Equipo
        juego.equipo.pokemons = []
        for pd in data.get("equipo", []):
            p = _deserializar_pokemon(pd)
            if p:
                juego.equipo.pokemons.append(p)

        # PC
        for i, caja in enumerate(data.get("pc", [])):
            if i < len(juego.pc.cajas):
                juego.pc.cajas[i].pokemons = []
                for pd in caja:
                    p = _deserializar_pokemon(pd)
                    if p:
                        juego.pc.cajas[i].pokemons.append(p)

        # Inventario
        from sistemas.inventario import (CURACIONES, POKEBALLS, BATALLA,
                                          REVIVIRES, EVOLUCION, OBJETOS_CLAVE)
        catalogo = {}
        for d in (CURACIONES, POKEBALLS, BATALLA, REVIVIRES, EVOLUCION, OBJETOS_CLAVE):
            catalogo.update(d)
        inv = data.get("inventario", {})
        juego.inventario.dinero = inv.get("dinero", 3000)
        juego.inventario.objetos = {}
        for nombre, cant in inv.get("objetos", {}).items():
            if nombre in catalogo:
                juego.inventario.agregar(catalogo[nombre], cant)

        # Gimnasios
        g = data.get("gimnasios", {})
        juego.gimnasios.medallas_obtenidas = g.get("medallas", [])
        juego.gimnasios.lideres_derrotados = g.get("derrotados", [])

        # Historia
        h = data.get("historia", {})
        juego.historia.eventos_completados = h.get("completados", [])
        juego.historia.capitulo_actual = h.get("capitulo", 1)

        # Mapa: REGENERAR desde cero (aplica cambios de generacion)
        from sistemas.mapa_visual import MapaVisual
        md = data.get("mapa", {})
        mapa_id = md.get("id", "caleta_norte")
        m = MapaVisual(mapa_id)
        px = float(md.get("pos_x", m.pos_x))
        py = float(md.get("pos_y", m.pos_y))
        try:
            from sistemas.mapa_visual import CAMINABLES
            ix, iy = int(px), int(py)
            es_valido = False
            if 0 <= ix < m.ancho and 0 <= iy < m.alto:
                if m.tiles[iy][ix] in CAMINABLES:
                    es_valido = True
            if not es_valido:
                for radio in range(1, 20):
                    for dy in range(-radio, radio + 1):
                        for dx in range(-radio, radio + 1):
                            if max(abs(dx), abs(dy)) != radio:
                                continue
                            nx, ny = ix + dx, iy + dy
                            if 0 <= nx < m.ancho and 0 <= ny < m.alto:
                                if m.tiles[ny][nx] in CAMINABLES:
                                    px, py = float(nx), float(ny)
                                    es_valido = True
                                    break
                        if es_valido: break
                    if es_valido: break
        except Exception:
            pass
        m.pos_x = px
        m.pos_y = py
        m.destino_x = int(px)
        m.destino_y = int(py)
        m.direccion = md.get("direccion", "abajo")
        juego.mapa_actual = m
        print("[OK] Mapa regenerado con la version actual del juego")

        # Pokédex
        pd = data.get("pokedex", {})
        juego.pokedex.vistos = set(pd.get("vistos", []))
        juego.pokedex.capturados = set(pd.get("capturados", []))

        # Asegurar variables NUEVAS que no existian en saves viejos
        defaults = {
            "_combo_racha": 0,
            "_combo_mejor": 0,
            "_combo_mensaje_t": 0.0,
            "_pokemon_capturados_historial": None,
            "_admin_activo": False,
            "_admin_pwd": "",
            "_admin_pwd_correcta": "1f2r3e4e5k6i7e",
            "_admin_menu_idx": 0,
            "_admin_poke_idx": 0,
            "_admin_poke_lista": None,
            "_admin_nivel": 50,
            "_admin_modo": "lista",
            "_admin_mensaje": "",
            "_admin_msg_t": 0.0,
            "_admin_volver_a": None,
            "_tiempo_juego": 0.0,
            "_stats_partida": None,
            "_mega_usada_batalla": False,
            "_mega_animando": False,
            "_mega_anim_t": 0.0,
            "_anim_ataque_timer": 0.0,
            "_anim_ataque_quien": None,
            "_ps_vis": None,
            "_exp_vis": None,
            "_pausa_anim": 0.0,
            "_screen_shake": 0.0,
            "_vs_intro_timer": 0.0,
            "_vs_intro_datos": None,
            "_vs_intro_siguiente": None,
            "_trans_timer": 0.0,
            "_trans_duracion": 1.6,
            "_fade_alpha": 0.0,
            "_fade_estado": None,
            "_fade_duracion": 0.30,
            "_creditos_t": 0.0,
            "_creditos_activos": False,
            "_seguidor_pos": None,
            "_seguidor_dir": "abajo",
            "_seguidor_cola": None,
            "_seguidor_anim": 0.0,
            "_mega_animando": False,
        }
        for k, v in defaults.items():
            if not hasattr(juego, k):
                if k == "_pokemon_capturados_historial":
                    setattr(juego, k, set())
                elif k in ("_admin_poke_lista", "_seguidor_cola"):
                    setattr(juego, k, [])
                elif k in ("_stats_partida",):
                    setattr(juego, k, {
                        "pasos": 0, "batallas_ganadas": 0, "batallas_perdidas": 0,
                        "capturas": 0, "pokemon_vistos": 0, "dinero_gastado": 0,
                        "dinero_ganado": 0, "medallas": 0, "inicio_ts": 0,
                        "curaciones": 0, "entrenadores_derrotados": 0,
                    })
                elif k in ("_ps_vis", "_exp_vis"):
                    setattr(juego, k, {})
                else:
                    setattr(juego, k, v)
        print("[OK] Variables nuevas inicializadas")

        return True
    except Exception as e:
        import traceback; traceback.print_exc()
        print("Error al cargar: " + str(e))
        return False


def existe_guardado(slot=1):
    _asegurar()
    return os.path.exists(os.path.join(RUTA_GUARDADOS, f"save_{slot}.json"))


def obtener_info_guardado(slot=1):
    try:
        ruta = os.path.join(RUTA_GUARDADOS, f"save_{slot}.json")
        if not os.path.exists(ruta):
            return None
        with open(ruta, "r", encoding="utf-8") as f:
            data = json.load(f)
        import time
        ts = data.get("timestamp", 0)
        equipo = data.get("equipo", [])
        medallas = len(data.get("gimnasios", {}).get("medallas", []))
        # Nombre del primer Pokemon
        primer = equipo[0]["nombre"] if equipo else "?"
        nivel = equipo[0]["nivel"] if equipo else 0
        # Tiempo de juego (si existe)
        t = data.get("tiempo_juego", 0)
        hh = int(t) // 3600
        mm = (int(t) % 3600) // 60
        # Nombre del jugador
        nombre = data.get("nombre_jugador", "Freekie")
        return {
            "fecha": time.strftime("%Y-%m-%d %H:%M", time.localtime(ts)),
            "nombre": nombre,
            "lider": primer,
            "nivel": nivel,
            "medallas": medallas,
            "equipo": equipo[:6],
            "horas": hh, "minutos": mm,
            "mapa": data.get("mapa", {}).get("id", "?"),
        }
    except Exception:
        return None
