# data/tag_team.py
# -*- coding: utf-8 -*-
"""E4: Combates Tag Team - dos entrenadores seguidos sin curar."""

try:
    from data.entrenadores import Entrenador
except Exception:
    Entrenador = None


class TagTeam:
    def __init__(self, ent1, ent2, titulo="Combate Doble", premio_extra=2000):
        self.ent1 = ent1
        self.ent2 = ent2
        self.titulo = titulo
        self.premio_extra = premio_extra
        self.batalla_idx = 0
        self.completado = False

    def siguiente(self):
        """Devuelve (entrenador_actual, es_ultimo)."""
        if self.batalla_idx == 0:
            return self.ent1, False
        elif self.batalla_idx == 1:
            return self.ent2, True
        return None, True

    def avanzar(self):
        self.batalla_idx += 1
        if self.batalla_idx >= 2:
            self.completado = True


# Tags Team predefinidos por zona
TAGS_TEAM = {}


def registrar_tags_team():
    """Registra tags team por zona."""
    if Entrenador is None:
        return
    # Moche
    TAGS_TEAM["ciudad_moche"] = TagTeam(
        Entrenador("Hermano Mayor", "Team Supay", "ciudad_moche", (8, 12),
                   [("Zorrin", 10), ("Tunquid", 11)],
                   ["Hermano del recluta! Te vengare!"],
                   ["No... mi hermano se enojara..."], 400),
        Entrenador("Hermano Menor", "Team Supay", "ciudad_moche", (10, 12),
                   [("Surito", 9), ("Cuy", 11)],
                   ["Mi hermano mayor tambien esta aqui!"],
                   ["Hermano, ayudame!"], 350),
        "Hermanos del Team Supay", 800,
    )
    # Puerto Ancon
    TAGS_TEAM["puerto_ancon"] = TagTeam(
        Entrenador("Pescador Gruñon", "Marino", "puerto_ancon", (30, 15),
                   [("Carachama", 18), ("Piranita", 19)],
                   ["Este puerto tiene duenos!"],
                   ["Bueno... te dejare pasar."], 600),
        Entrenador("Pescador Callado", "Marino", "puerto_ancon", (32, 15),
                   [("Bufeito", 18), ("Tapirex", 20)],
                   ["Mi companero no habla mucho."],
                   ["Venciste a los dos..."], 600),
        "Pescadores del Muelle", 1200,
    )
    # Andahuaylas
    TAGS_TEAM["andahuaylas"] = TagTeam(
        Entrenador("Danzante A", "Danzante", "andahuaylas", (20, 18),
                   [("Cuyver", 22), ("Chinchicab", 23)],
                   ["Solo uno puede pasar el festival!"],
                   ["Buen ritmo, chico."], 700),
        Entrenador("Danzante B", "Danzante", "andahuaylas", (22, 18),
                   [("Simiochuro", 23), ("Colibrindes", 24)],
                   ["Y yo soy el mejor danzante!"],
                   ["Impresionante!"], 700),
        "Dueto de Danzantes", 1400,
    )
    # Ciudad Imperial
    TAGS_TEAM["ciudad_imperial"] = TagTeam(
        Entrenador("Sabio Mayor", "Sabio", "ciudad_imperial", (28, 16),
                   [("Huacotrato", 28), ("Tumito", 29), ("Quipus", 30)],
                   ["La sabiduria no se comparte con extraños."],
                   ["Tu si sabes escuchar."], 1000),
        Entrenador("Sabio Joven", "Sabio", "ciudad_imperial", (30, 16),
                   [("Tumignus", 29), ("Huacok", 30), ("Aurum-Inca", 31)],
                   ["Y yo soy el aprendiz."],
                   ["El maestro estara orgulloso."], 1000),
        "Maestro y Aprendiz", 2000,
    )
    # Puno
    TAGS_TEAM["puno"] = TagTeam(
        Entrenador("Yatiri", "Chamana", "puno", (35, 20),
                   [("Aruy", 33), ("Bufeo Colorado", 34)],
                   ["Los espiritus me acompanan."],
                   ["Los espiritus te aceptan."], 1200),
        Entrenador("Pescador Lago", "Pescador", "puno", (37, 20),
                   [("Carachama", 34), ("Lago-Sagu", 35)],
                   ["Y a mi el lago."],
                   ["El lago te sonrie."], 1200),
        "Guardianes del Lago", 2400,
    )
    # Huaraz
    TAGS_TEAM["huaraz"] = TagTeam(
        Entrenador("Montanista A", "Montanista", "huaraz", (20, 18),
                   [("Papa Chunio", 38), ("Chinchay", 39)],
                   ["Nadie sube sin nuestro permiso."],
                   ["Buen ascenso."], 1500),
        Entrenador("Montanista B", "Montanista", "huaraz", (22, 18),
                   [("Zorro de las Nieves", 39), ("Ursandino", 40)],
                   ["Y nadie baja tampoco!"],
                   ["Gran descenso!"], 1500),
        "Guardianes del Nevado", 3000,
    )
    # Puerto Selva
    TAGS_TEAM["puerto_selva"] = TagTeam(
        Entrenador("Cazador Furtivo", "Team Supay", "puerto_selva", (30, 20),
                   [("Piranatox", 44), ("Mantis-Buho", 45)],
                   ["La selva es nuestra!"],
                   ["La selva nos castiga..."], 2000),
        Entrenador("Guia Traidor", "Team Supay", "puerto_selva", (32, 20),
                   [("Orquidea Negra", 45), ("Chullachaqui", 46)],
                   ["Traicionamos a los guias."],
                   ["Esto no termina aqui!"], 2000),
        "Team Supay - Celula Selva", 4000,
    )
    # Ciudad Capital
    TAGS_TEAM["ciudad_capital"] = TagTeam(
        Entrenador("Guardia A", "Seguridad", "ciudad_capital", (20, 18),
                   [("Tumignus", 50), ("Muquimetal", 51)],
                   ["Acceso restringido a la elite."],
                   ["Tienes credenciales validas."], 3000),
        Entrenador("Guardia B", "Seguridad", "ciudad_capital", (22, 18),
                   [("Wayra-Wind", 51), ("Incaflame", 52)],
                   ["Yo soy la segunda barrera!"],
                   ["Acceso concedido."], 3000),
        "Guardia de Elite", 6000,
    )


registrar_tags_team()


def obtener_tag_team(mapa_id):
    return TAGS_TEAM.get(mapa_id)


print(f"OK data.tag_team ({len(TAGS_TEAM)} tags)")
