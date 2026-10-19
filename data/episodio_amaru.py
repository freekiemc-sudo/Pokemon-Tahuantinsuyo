# data/episodio_amaru.py
# -*- coding: utf-8 -*-
"""FASE F: Episodio Amaru - Arco post-game inspirado en el lore oficial.

Basado en la Parte 11 del documento de lore:
- El Despertar del Post-Game (El Mensaje en la Caleta)
- La Caceria de los Pokemon Legendarios
- La Guarida del Amaru (El Combate contra el Mitico)
- El Regalo y la Libertad Definitiva
"""


# Fases del Episodio
FASES_EPISODIO = [
    {
        "id": 1,
        "nombre": "El Mensaje en la Caleta",
        "objetivo": "Regresa a tu casa en Caleta Norte.",
        "descripcion": "Tu mama te tiene algo importante que decir.",
        "ubicacion": "caleta_norte",
        "trigger": "casa_mama",
    },
    {
        "id": 2,
        "nombre": "La Tablilla Antigua",
        "objetivo": "Lee la tablilla que dejo el Profesor Kuntur.",
        "descripcion": "El Profesor Kuntur tiene noticias urgentes.",
        "ubicacion": "caleta_norte",
        "trigger": "profesor",
    },
    {
        "id": 3,
        "nombre": "Los Apus Despiertan",
        "objetivo": "Investiga las senales en la Cordillera Blanca.",
        "descripcion": "Los Apus estan enviando senales de alerta.",
        "ubicacion": "huaraz",
        "trigger": "montana",
    },
    {
        "id": 4,
        "nombre": "El Titicaca Sagrado",
        "objetivo": "Viaja al Lago Titicaca y busca la cueva subacuatica.",
        "descripcion": "El lago guarda el secreto del Yacumama.",
        "ubicacion": "puno",
        "trigger": "lago",
    },
    {
        "id": 5,
        "nombre": "La Grieta del Fin del Mundo",
        "objetivo": "Encuentra la grieta oculta entre los Andes y la selva.",
        "descripcion": "Los ultimos Supay intentan un pacto desesperado.",
        "ubicacion": "selva_profunda",
        "trigger": "grieta",
    },
    {
        "id": 6,
        "nombre": "El Combate contra Yacumama",
        "objetivo": "Purifica a Yacumama en un combate de supervivencia.",
        "descripcion": "El ser mitico debe ser calmado, no capturado.",
        "ubicacion": "selva_profunda",
        "trigger": "yacumama",
    },
    {
        "id": 7,
        "nombre": "El Regalo de los Sabios",
        "objetivo": "Recibe el Orbe del Sol.",
        "descripcion": "Los sabios te recompensan por salvar el Tahuantinsuyo.",
        "ubicacion": "caleta_norte",
        "trigger": "sabios",
    },
]


# Dialogos del Episodio (fieles al lore)
DIALOGOS_EPISODIO = {
    # FASE 1: Mama
    "casa_mama": [
        "!Hola, hijito! Has vuelto a casa!",
        "!Estoy tan orgullosa de ti! Campeon del Tahuantinsuyo...",
        "Pero algo extrano ha pasado esta manana...",
        "Alguien dejo una tablilla de piedra en la puerta.",
        "Dice que es urgente. Ve a verla.",
    ],
    # FASE 2: Profesor Kuntur
    "profesor": [
        "!Ah, has llegado!",
        "El Team Supay, aunque descabezado, intenta un ultimo movimiento desesperado.",
        "Quieren liberar al Amaru definitivo.",
        "Las energias de los Apus se han desestabilizado.",
        "Los guardianes legendarios han despertado en sus habitats naturales.",
        "Necesitamos que recorras nuevamente el Tahuantinsuyo y asegures la paz definitiva.",
        "Empieza por la Cordillera Blanca. Los Apus te llaman.",
    ],
    # FASE 3: Montana
    "montana": [
        "!El hielo de la cumbre brilla con energia extrana!",
        "!Wira-Titan se manifiesta por un instante!",
        "Wira-Titan: Mortal... el equilibrio se quiebra.",
        "Wira-Titan: El Yacumama ha sido alterado por los restos del Team Supay.",
        "Wira-Titan: Busca al Titicaca. Es alli donde debe ser calmado.",
        "!La vision se desvanece!",
    ],
    # FASE 4: Lago
    "lago": [
        "Las aguas del Titicaca estan agitadas.",
        "!Una corriente te arrastra hacia una cueva subacuatica!",
        "Encuentras inscripciones antiguas que hablan del Yacumama.",
        "Descubres un mapa hacia la Grieta del Fin del Mundo.",
        "!El Team Supay debe estar alli!",
    ],
    # FASE 5: Grieta
    "grieta": [
        "!El aire se vuelve pesado con energia cosmica!",
        "Ves a los ultimos restos del Team Supay frente a un altar.",
        "Recluta Supay: !No podras detenernos! !El pacto esta casi sellado!",
        "!Una sombra colosal emerge del altar!",
        "!El Yacumama ha sido invocado en su forma mas pura!",
        "Recluta Supay: !Ahora su furia caera sobre todos ustedes!",
        "!El Team Supay huye despavorido!",
    ],
    # FASE 6: Yacumama (epico)
    "yacumama": [
        "Yacumama: ...",
        "!El ser mitico se retuerce con furia ancestral!",
        "!No responde a la razon. Solo al poder!",
        "!Debes calmarlo con un combate de supervivencia!",
    ],
    "yacumama_fin": [
        "!El Yacumama emite un destello azulado pacifico!",
        "Yacumama: ...gracias...",
        "!Se desliza hacia las profundidades misticas!",
        "!La grieta se sella para siempre!",
        "!El equilibrio de la naturaleza vuelve al Tahuantinsuyo!",
    ],
    # FASE 7: Sabios
    "sabios": [
        "!Los sabios de la region llegan al lugar!",
        "Sabio Mayor: Has purificado al ser mitico.",
        "Sabio Mayor: El Tahuantinsuyo esta en paz.",
        "Sabio Mayor: Como recompensa, te entregamos el Orbe del Sol.",
        "!Obtienes el Orbe del Sol!",
        "!Este objeto te permite retar infinitamente al Alto Mando!",
        "!Felicidades, Campeon! Has completado el Episodio Amaru!",
    ],
}


class EpisodioAmaru:
    def __init__(self):
        self.fase_actual = 0
        self.completado = False
        self.iniciado = False
        self.yacumama_derrotada = False
        self.orbe_obtenido = False

    def iniciar(self):
        if self.completado:
            return False
        self.iniciado = True
        self.fase_actual = 1
        return True

    def avanzar(self):
        if self.fase_actual >= len(FASES_EPISODIO):
            self.completado = True
            return None
        self.fase_actual += 1
        return self.fase_actual

    def fase_info(self):
        if 1 <= self.fase_actual <= len(FASES_EPISODIO):
            return FASES_EPISODIO[self.fase_actual - 1]
        return None

    def dialogo_fase(self, trigger):
        return DIALOGOS_EPISODIO.get(trigger, [])


print(f"OK data.episodio_amaru ({len(FASES_EPISODIO)} fases)")
