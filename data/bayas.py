# data/bayas.py
# -*- coding: utf-8 -*-
"""Bayas nativas de la Region Tahuantinsuyo - held items para combate."""


class Baya:
    def __init__(self, nombre, descripcion, efecto, prioridad=0):
        self.nombre = nombre
        self.descripcion = descripcion
        self.efecto = efecto
        self.prioridad = prioridad  # mas alto = se activa antes


BAYAS = {
    "Aguaymanto": Baya(
        "Aguaymanto",
        "Cura estados alterados y restaura 20 PS.",
        {"curar_estado": True, "curar_ps": 20},
        1,
    ),
    "Lucuma": Baya(
        "Lucuma",
        "Restaura la mitad de los PS cuando el usuario baja del 25%.",
        {"curacion_auto_umbral": 0.25, "curar_ps_pct": 0.50},
        3,  # prioridad alta: se activa antes
    ),
    "Camu Camu": Baya(
        "Camu Camu",
        "Sube la Defensa Especial al recibir un ataque supereficaz.",
        {"subir_stat_al_recibir_supereficaz": ("def_esp", 1)},
        2,
    ),
    "Coca Sagrada": Baya(
        "Coca Sagrada",
        "Evita el cansancio y la perdida de precision.",
        {"inmunidad_cansancio": True, "inmunidad_precision": True},
        0,
    ),
}


def aplicar_baya_held(pokemon, momento, contexto=None):
    """Intenta aplicar la baya equipada. Devuelve lista de mensajes."""
    if not hasattr(pokemon, "objeto_equipado") or not pokemon.objeto_equipado:
        return []
    baya = BAYAS.get(pokemon.objeto_equipado)
    if not baya:
        return []
    msgs = []
    ctx = contexto or {}
    ef = baya.efecto

    # Momento: "inicio_turno", "recibir_danio_supereficaz", "recibir_danio"
    if momento == "recibir_danio":
        hp_pct = pokemon.ps / max(1, pokemon.ps_max)
        # Lucuma: cura si baja del 25%
        if "curacion_auto_umbral" in ef:
            umbral = ef["curacion_auto_umbral"]
            if hp_pct <= umbral and not getattr(pokemon, "_baya_usada_turno", False):
                curado = int(pokemon.ps_max * ef.get("curar_ps_pct", 0.5))
                pokemon.curar(curado)
                msgs.append(f"!{pokemon.nombre} comio su {baya.nombre} y recupero PS!")
                pokemon.objeto_equipado = None
                pokemon._baya_usada_turno = True

    elif momento == "recibir_danio_supereficaz":
        # Camu Camu: sube Def Esp al recibir supereficaz
        if "subir_stat_al_recibir_supereficaz" in ef:
            stat, grados = ef["subir_stat_al_recibir_supereficaz"]
            if hasattr(pokemon, "stages"):
                pokemon.stages[stat] = min(6, pokemon.stages.get(stat, 0) + grados)
                msgs.append(f"!{pokemon.nombre} comio su {baya.nombre} y subio {stat}!")
                pokemon.objeto_equipado = None

    elif momento == "curar_estado":
        # Aguaymanto: cura estados al recibirlos
        if "curar_estado" in ef and pokemon.estado:
            pokemon.estado = None
            pokemon.turnos_estado = 0
            pokemon.contador_toxico = 0
            pokemon.curar(ef.get("curar_ps", 0))
            msgs.append(f"!{pokemon.nombre} comio su {baya.nombre} y se curo!")
            pokemon.objeto_equipado = None

    return msgs


def obtener_bayas_comprables():
    """Devuelve lista de bayas para tiendas."""
    return list(BAYAS.values())


print(f"OK data.bayas ({len(BAYAS)} bayas)")
