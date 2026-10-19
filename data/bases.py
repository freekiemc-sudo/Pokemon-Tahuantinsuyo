# data/bases.py
# -*- coding: utf-8 -*-
"""E5: Bases secretas en huacas - personalizacion."""


class ObjetoDecorativo:
    def __init__(self, id, nombre, precio, categoria, icono="[]"):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria  # mueble, alfombra, cuadro, planta, pokemon
        self.icono = icono


DECORACIONES = {
    # Muebles
    "alfombra_moche": ObjetoDecorativo("alfombra_moche", "Alfombra Moche", 1500, "mueble", "="),
    "mesa_piedra": ObjetoDecorativo("mesa_piedra", "Mesa de Piedra", 2000, "mueble", "#"),
    "silla_totora": ObjetoDecorativo("silla_totora", "Silla de Totora", 1200, "mueble", "T"),
    "cama_llama": ObjetoDecorativo("cama_llama", "Cama de Lana", 3500, "mueble", "C"),
    "baul_inca": ObjetoDecorativo("baul_inca", "Baul Inca", 4000, "mueble", "B"),

    # Alfombras
    "alfombra_andina": ObjetoDecorativo("alfombra_andina", "Alfombra Andina", 800, "alfombra", "a"),
    "tapete_selva": ObjetoDecorativo("tapete_selva", "Tapete de la Selva", 900, "alfombra", "t"),

    # Cuadros
    "cuadro_nasca": ObjetoDecorativo("cuadro_nasca", "Cuadro Nasca", 2500, "cuadro", "N"),
    "cuadro_inti": ObjetoDecorativo("cuadro_inti", "Cuadro del Sol", 3000, "cuadro", "I"),
    "cuadro_killa": ObjetoDecorativo("cuadro_killa", "Cuadro de la Luna", 3000, "cuadro", "K"),

    # Plantas
    "orquidea_maceta": ObjetoDecorativo("orquidea_maceta", "Orquidea en Maceta", 1800, "planta", "O"),
    "cactus_maceta": ObjetoDecorativo("cactus_maceta", "Cactus en Maceta", 1000, "planta", "c"),
    "papa_sagrada": ObjetoDecorativo("papa_sagrada", "Papa Sagrada", 2200, "planta", "P"),

    # Objetos especiales
    "estatua_amaru": ObjetoDecorativo("estatua_amaru", "Estatua del Amaru", 15000, "especial", "A"),
    "fuente_titicaca": ObjetoDecorativo("fuente_titicaca", "Fuente del Titicaca", 8000, "especial", "F"),
    "antorcha_sagrada": ObjetoDecorativo("antorcha_sagrada", "Antorcha Sagrada", 5000, "especial", "!"),
    "totem_apu": ObjetoDecorativo("totem_apu", "Totem del Apu", 10000, "especial", "T"),
}


class BaseSecreta:
    def __init__(self, mapa_id, x, y):
        self.mapa_id = mapa_id
        self.x = x
        self.y = y
        self.decoraciones = []  # [(objeto_id, pos_x, pos_y)]
        self.visitas = []       # IDs de NPCs que la han visitado
        self.nombre = "Mi Huaca"
        self.bandera = "amaru"  # amaru, condor, puma
        self.compartida = False

    def decorar(self, obj_id, px, py):
        # Verificar que no haya otra decoracion en la misma posicion
        for (oid, ox, oy) in self.decoraciones:
            if ox == px and oy == py:
                return False, "Ya hay algo aqui."
        self.decoraciones.append((obj_id, px, py))
        return True, f"Colocaste {obj_id}."

    def quitar(self, px, py):
        for i, (oid, ox, oy) in enumerate(self.decoraciones):
            if ox == px and oy == py:
                self.decoraciones.pop(i)
                return True, f"Quitaste {oid}."
        return False, "No hay nada aqui."

    def contar(self):
        return len(self.decoraciones)


class SistemaBases:
    def __init__(self):
        self.bases = {}  # {mapa_id: BaseSecreta}
        self.base_actual = None

    def crear_base(self, mapa_id, x, y):
        if mapa_id in self.bases:
            return self.bases[mapa_id], False
        b = BaseSecreta(mapa_id, x, y)
        self.bases[mapa_id] = b
        return b, True

    def obtener(self, mapa_id):
        return self.bases.get(mapa_id)

    def total_decoraciones(self):
        return sum(b.contar() for b in self.bases.values())


print(f"OK data.bases ({len(DECORACIONES)} decoraciones)")
