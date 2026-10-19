# data/pokedex_ext.py
"""
Pokémon 019-103 de la Región Tahuantinsuyo (los 18 primeros están en data/pokedex.py).
Se fusionan automáticamente en POKEDEX_COMPLETA. Todos los números (stats, movimientos, niveles)
son editables: ajusta lo que quieras para balancear.

Notas:
 - "evolucion" = evolución por nivel (como en tu pokedex.py).
 - "evoluciones_especiales" = piedras / intercambio / felicidad / movimiento (según el lore).
   Tu sistemas/evoluciones.py debe leerlo para activarlas; el resto del juego lo ignora sin problema.
 - Tipo "Sonido" (Pututos) es propio de la región: añádelo a tu tabla de tipos si usas una.
"""

POKEDEX_EXT = {
    "Orugüeta": {
        "id": 19,
        "nombre": "Orugüeta",
        "tipos": [
            "Bicho"
        ],
        "categoria": "Oruga",
        "altura": 0.4,
        "peso": 6.0,
        "stats_base": {
            "ps": 40,
            "atq": 40,
            "def": 40,
            "atq_esp": 40,
            "def_esp": 40,
            "vel": 40
        },
        "descripcion": "Oruga andina que se camufla entre las hojas y roe todo lo que encuentra.",
        "evolucion": {
            "nivel": 7,
            "evoluciona_a": "Crisálida Selva"
        },
        "movimientos_iniciales": [
            {
                "nombre": "Placaje",
                "tipo": "Normal",
                "potencia": 40,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Picadura",
                "tipo": "Bicho",
                "potencia": 40,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 8,
                "movimiento": {
                    "nombre": "Corte Cruzado",
                    "tipo": "Bicho",
                    "potencia": 60,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 20
                }
            }
        ],
        "tasa_captura": 255,
        "exp_base": 55,
        "grupo_huevo": "Bicho"
    },
    "Crisálida Selva": {
        "id": 20,
        "nombre": "Crisálida Selva",
        "tipos": [
            "Bicho",
            "Planta"
        ],
        "categoria": "Capullo",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 70,
            "atq": 50,
            "def": 70,
            "atq_esp": 40,
            "def_esp": 65,
            "vel": 35
        },
        "descripcion": "Envuelta en un capullo de lianas, espera inmóvil la hora de transformarse.",
        "evolucion": {
            "nivel": 28,
            "evoluciona_a": "Mantis-Búho"
        },
        "movimientos_iniciales": [
            {
                "nombre": "Picadura",
                "tipo": "Bicho",
                "potencia": 40,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Corte Cruzado",
                "tipo": "Bicho",
                "potencia": 60,
                "precision": 100,
                "categoria": "Físico",
                "pp": 20
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 10,
                "movimiento": {
                    "nombre": "Hoja Afilada",
                    "tipo": "Planta",
                    "potencia": 55,
                    "precision": 95,
                    "categoria": "Físico",
                    "pp": 25
                }
            },
            {
                "nivel": 18,
                "movimiento": {
                    "nombre": "Zumbido",
                    "tipo": "Bicho",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 28,
                "movimiento": {
                    "nombre": "Energibola",
                    "tipo": "Planta",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            }
        ],
        "tasa_captura": 120,
        "exp_base": 120,
        "grupo_huevo": "Bicho"
    },
    "Mantis-Búho": {
        "id": 21,
        "nombre": "Mantis-Búho",
        "tipos": [
            "Bicho",
            "Siniestro"
        ],
        "categoria": "Acechador",
        "altura": 1.5,
        "peso": 70.0,
        "stats_base": {
            "ps": 70,
            "atq": 80,
            "def": 65,
            "atq_esp": 80,
            "def_esp": 65,
            "vel": 120
        },
        "descripcion": "Sus alas tienen patrones de ojos de búho que paralizan de miedo a sus presas.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Corte Cruzado",
                "tipo": "Bicho",
                "potencia": 60,
                "precision": 100,
                "categoria": "Físico",
                "pp": 20
            },
            {
                "nombre": "Triturar",
                "tipo": "Siniestro",
                "potencia": 80,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Zumbido",
                    "tipo": "Bicho",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Pulso Umbrío",
                    "tipo": "Siniestro",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            },
            {
                "nivel": 34,
                "movimiento": {
                    "nombre": "Tijera Letal",
                    "tipo": "Bicho",
                    "potencia": 110,
                    "precision": 90,
                    "categoria": "Físico",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 180,
        "grupo_huevo": "Bicho"
    },
    "Tunquirex": {
        "id": 22,
        "nombre": "Tunquirex",
        "tipos": [
            "Volador",
            "Fuego"
        ],
        "categoria": "Gallito",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 65,
            "atq": 85,
            "def": 65,
            "atq_esp": 45,
            "def_esp": 55,
            "vel": 65
        },
        "descripcion": "Su copete arde cuando se enfurece; defiende su territorio a picotazos.",
        "evolucion": {
            "nivel": 36,
            "evoluciona_a": "Tunquialt"
        },
        "movimientos_iniciales": [
            {
                "nombre": "Picotazo",
                "tipo": "Volador",
                "potencia": 35,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Ataque Ala",
                "tipo": "Volador",
                "potencia": 60,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 10,
                "movimiento": {
                    "nombre": "Llamarada",
                    "tipo": "Fuego",
                    "potencia": 70,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 15
                }
            },
            {
                "nivel": 18,
                "movimiento": {
                    "nombre": "Tajo Aéreo",
                    "tipo": "Volador",
                    "potencia": 75,
                    "precision": 95,
                    "categoria": "Especial",
                    "pp": 15
                }
            },
            {
                "nivel": 28,
                "movimiento": {
                    "nombre": "Lanzallamas",
                    "tipo": "Fuego",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            }
        ],
        "tasa_captura": 120,
        "exp_base": 120,
        "grupo_huevo": "Volador"
    },
    "Tunquialt": {
        "id": 23,
        "nombre": "Tunquialt",
        "tipos": [
            "Volador",
            "Fuego"
        ],
        "categoria": "Gallito de las Rocas",
        "altura": 1.5,
        "peso": 70.0,
        "stats_base": {
            "ps": 85,
            "atq": 110,
            "def": 85,
            "atq_esp": 60,
            "def_esp": 70,
            "vel": 85
        },
        "descripcion": "El gallito de las rocas: su plumaje carmesí brilla entre la neblina del bosque.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Ataque Ala",
                "tipo": "Volador",
                "potencia": 60,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Llamarada",
                "tipo": "Fuego",
                "potencia": 70,
                "precision": 90,
                "categoria": "Especial",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Tajo Aéreo",
                    "tipo": "Volador",
                    "potencia": 75,
                    "precision": 95,
                    "categoria": "Especial",
                    "pp": 15
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Lanzallamas",
                    "tipo": "Fuego",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            },
            {
                "nivel": 34,
                "movimiento": {
                    "nombre": "Pájaro Osado",
                    "tipo": "Volador",
                    "potencia": 120,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 180,
        "grupo_huevo": "Volador"
    },
    "Monito": {
        "id": 24,
        "nombre": "Monito",
        "tipos": [
            "Planta"
        ],
        "categoria": "Mono Churo",
        "altura": 0.4,
        "peso": 6.0,
        "stats_base": {
            "ps": 40,
            "atq": 45,
            "def": 35,
            "atq_esp": 45,
            "def_esp": 35,
            "vel": 65
        },
        "descripcion": "Pequeño mono que se cuelga de las ramas con su cola prensil.",
        "evolucion": {
            "nivel": 16,
            "evoluciona_a": "Churotail"
        },
        "movimientos_iniciales": [
            {
                "nombre": "Placaje",
                "tipo": "Normal",
                "potencia": 40,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Látigo Cepa",
                "tipo": "Planta",
                "potencia": 45,
                "precision": 100,
                "categoria": "Físico",
                "pp": 25
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 8,
                "movimiento": {
                    "nombre": "Hoja Afilada",
                    "tipo": "Planta",
                    "potencia": 55,
                    "precision": 95,
                    "categoria": "Físico",
                    "pp": 25
                }
            }
        ],
        "tasa_captura": 255,
        "exp_base": 55,
        "grupo_huevo": "Planta"
    },
    "Churotail": {
        "id": 25,
        "nombre": "Churotail",
        "tipos": [
            "Planta",
            "Normal"
        ],
        "categoria": "Mono Churo",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 50,
            "atq": 60,
            "def": 50,
            "atq_esp": 60,
            "def_esp": 50,
            "vel": 90
        },
        "descripcion": "Su cola enroscada como un churo le sirve de quinto brazo.",
        "evolucion": {
            "nivel": 32,
            "evoluciona_a": "Simiochuro"
        },
        "movimientos_iniciales": [
            {
                "nombre": "Látigo Cepa",
                "tipo": "Planta",
                "potencia": 45,
                "precision": 100,
                "categoria": "Físico",
                "pp": 25
            },
            {
                "nombre": "Hoja Afilada",
                "tipo": "Planta",
                "potencia": 55,
                "precision": 95,
                "categoria": "Físico",
                "pp": 25
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 10,
                "movimiento": {
                    "nombre": "Impulso Andino",
                    "tipo": "Normal",
                    "potencia": 60,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 20
                }
            },
            {
                "nivel": 18,
                "movimiento": {
                    "nombre": "Energibola",
                    "tipo": "Planta",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 28,
                "movimiento": {
                    "nombre": "Golpe Cuerpo",
                    "tipo": "Normal",
                    "potencia": 85,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            }
        ],
        "tasa_captura": 120,
        "exp_base": 120,
        "grupo_huevo": "Planta"
    },
    "Simiochuro": {
        "id": 26,
        "nombre": "Simiochuro",
        "tipos": [
            "Planta",
            "Lucha"
        ],
        "categoria": "Mono Churo",
        "altura": 1.5,
        "peso": 70.0,
        "stats_base": {
            "ps": 85,
            "atq": 115,
            "def": 85,
            "atq_esp": 60,
            "def_esp": 70,
            "vel": 85
        },
        "descripcion": "Salta entre los árboles a tal velocidad que parece volar.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Hoja Afilada",
                "tipo": "Planta",
                "potencia": 55,
                "precision": 95,
                "categoria": "Físico",
                "pp": 25
            },
            {
                "nombre": "Patada Salto",
                "tipo": "Lucha",
                "potencia": 85,
                "precision": 90,
                "categoria": "Físico",
                "pp": 25
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Energibola",
                    "tipo": "Planta",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Puño Dinámico",
                    "tipo": "Lucha",
                    "potencia": 100,
                    "precision": 50,
                    "categoria": "Físico",
                    "pp": 5
                }
            },
            {
                "nivel": 34,
                "movimiento": {
                    "nombre": "Lluvia Solar",
                    "tipo": "Planta",
                    "potencia": 120,
                    "precision": 85,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 180,
        "grupo_huevo": "Planta"
    },
    "Sachavacuna": {
        "id": 27,
        "nombre": "Sachavacuna",
        "tipos": [
            "Normal"
        ],
        "categoria": "Tapir",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 60,
            "atq": 40,
            "def": 60,
            "atq_esp": 30,
            "def_esp": 55,
            "vel": 30
        },
        "descripcion": "Cría de tapir que husmea en la espesura con su trompita curiosa.",
        "evolucion": {
            "nivel": 18,
            "evoluciona_a": "Tapirex"
        },
        "movimientos_iniciales": [
            {
                "nombre": "Placaje",
                "tipo": "Normal",
                "potencia": 40,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Impulso Andino",
                "tipo": "Normal",
                "potencia": 60,
                "precision": 100,
                "categoria": "Físico",
                "pp": 20
            }
        ],
        "aprendizajes_por_nivel": [],
        "tasa_captura": 255,
        "exp_base": 55,
        "grupo_huevo": "Campo"
    },
    "Tapirex": {
        "id": 28,
        "nombre": "Tapirex",
        "tipos": [
            "Normal",
            "Agua"
        ],
        "categoria": "Tapir",
        "altura": 1.5,
        "peso": 70.0,
        "stats_base": {
            "ps": 80,
            "atq": 55,
            "def": 80,
            "atq_esp": 45,
            "def_esp": 75,
            "vel": 35
        },
        "descripcion": "Se zambulle en los ríos y puede caminar por el fondo respirando por la trompa.",
        "evolucion": {
            "nivel": 36,
            "evoluciona_a": "Sachavaca Titán"
        },
        "movimientos_iniciales": [
            {
                "nombre": "Placaje",
                "tipo": "Normal",
                "potencia": 40,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Impulso Andino",
                "tipo": "Normal",
                "potencia": 60,
                "precision": 100,
                "categoria": "Físico",
                "pp": 20
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 10,
                "movimiento": {
                    "nombre": "Hidropulso",
                    "tipo": "Agua",
                    "potencia": 65,
                    "precision": 95,
                    "categoria": "Especial",
                    "pp": 20
                }
            },
            {
                "nivel": 18,
                "movimiento": {
                    "nombre": "Golpe Cuerpo",
                    "tipo": "Normal",
                    "potencia": 85,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            },
            {
                "nivel": 28,
                "movimiento": {
                    "nombre": "Cascada Andina",
                    "tipo": "Agua",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            }
        ],
        "tasa_captura": 120,
        "exp_base": 120,
        "grupo_huevo": "Campo"
    },
    "Sachavaca Titán": {
        "id": 29,
        "nombre": "Sachavaca Titán",
        "tipos": [
            "Agua",
            "Tierra"
        ],
        "categoria": "Tapir Amazónico",
        "altura": 2.2,
        "peso": 180.0,
        "stats_base": {
            "ps": 105,
            "atq": 75,
            "def": 110,
            "atq_esp": 60,
            "def_esp": 100,
            "vel": 50
        },
        "descripcion": "Colosal tapir amazónico; su paso hace temblar el barro de la selva.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Hidropulso",
                "tipo": "Agua",
                "potencia": 65,
                "precision": 95,
                "categoria": "Especial",
                "pp": 20
            },
            {
                "nombre": "Excavar",
                "tipo": "Tierra",
                "potencia": 80,
                "precision": 100,
                "categoria": "Físico",
                "pp": 10
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Cascada Andina",
                    "tipo": "Agua",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Terremoto",
                    "tipo": "Tierra",
                    "potencia": 100,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 10
                }
            },
            {
                "nivel": 34,
                "movimiento": {
                    "nombre": "Hidrobomba Mística",
                    "tipo": "Agua",
                    "potencia": 120,
                    "precision": 80,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 180,
        "grupo_huevo": "Agua"
    },
    "Vizcachin": {
        "id": 30,
        "nombre": "Vizcachin",
        "tipos": [
            "Roca"
        ],
        "categoria": "Vizcacha",
        "altura": 0.4,
        "peso": 6.0,
        "stats_base": {
            "ps": 60,
            "atq": 45,
            "def": 60,
            "atq_esp": 35,
            "def_esp": 55,
            "vel": 30
        },
        "descripcion": "Vizcacha de los peñascos que vigila desde lo alto de las rocas.",
        "evolucion": {
            "nivel": 24,
            "evoluciona_a": "Montazcach"
        },
        "movimientos_iniciales": [
            {
                "nombre": "Placaje",
                "tipo": "Normal",
                "potencia": 40,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Lanzarrocas",
                "tipo": "Roca",
                "potencia": 50,
                "precision": 90,
                "categoria": "Físico",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 8,
                "movimiento": {
                    "nombre": "Avalancha",
                    "tipo": "Roca",
                    "potencia": 75,
                    "precision": 90,
                    "categoria": "Físico",
                    "pp": 10
                }
            }
        ],
        "tasa_captura": 255,
        "exp_base": 55,
        "grupo_huevo": "Mineral"
    },
    "Montazcach": {
        "id": 31,
        "nombre": "Montazcach",
        "tipos": [
            "Roca",
            "Normal"
        ],
        "categoria": "Vizcacha Andina",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 95,
            "atq": 65,
            "def": 95,
            "atq_esp": 50,
            "def_esp": 90,
            "vel": 45
        },
        "descripcion": "Su pelaje se endurece como piedra con el frío de la cordillera.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Avalancha",
                "tipo": "Roca",
                "potencia": 75,
                "precision": 90,
                "categoria": "Físico",
                "pp": 10
            },
            {
                "nombre": "Impulso Andino",
                "tipo": "Normal",
                "potencia": 60,
                "precision": 100,
                "categoria": "Físico",
                "pp": 20
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Roca Afilada",
                    "tipo": "Roca",
                    "potencia": 100,
                    "precision": 80,
                    "categoria": "Físico",
                    "pp": 5
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Golpe Cuerpo",
                    "tipo": "Normal",
                    "potencia": 85,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 180,
        "grupo_huevo": "Mineral"
    },
    "Picaflor": {
        "id": 32,
        "nombre": "Picaflor",
        "tipos": [
            "Volador"
        ],
        "categoria": "Colibrí",
        "altura": 0.4,
        "peso": 6.0,
        "stats_base": {
            "ps": 40,
            "atq": 45,
            "def": 35,
            "atq_esp": 45,
            "def_esp": 35,
            "vel": 70
        },
        "descripcion": "Se detiene en el aire y liba las flores con un aleteo imposible de seguir.",
        "evolucion": {
            "nivel": 22,
            "evoluciona_a": "Colibrindes"
        },
        "movimientos_iniciales": [
            {
                "nombre": "Placaje",
                "tipo": "Normal",
                "potencia": 40,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Picotazo",
                "tipo": "Volador",
                "potencia": 35,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 8,
                "movimiento": {
                    "nombre": "Ataque Ala",
                    "tipo": "Volador",
                    "potencia": 60,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 35
                }
            }
        ],
        "tasa_captura": 255,
        "exp_base": 55,
        "grupo_huevo": "Volador"
    },
    "Colibrindes": {
        "id": 33,
        "nombre": "Colibrindes",
        "tipos": [
            "Volador",
            "Psíquico"
        ],
        "categoria": "Picaflor de los Andes",
        "altura": 0.4,
        "peso": 6.0,
        "stats_base": {
            "ps": 65,
            "atq": 75,
            "def": 60,
            "atq_esp": 75,
            "def_esp": 60,
            "vel": 110
        },
        "descripcion": "Dicen que su vuelo traza las mismas figuras que las líneas de Nasca.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Ataque Ala",
                "tipo": "Volador",
                "potencia": 60,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Psicorrayo",
                "tipo": "Psíquico",
                "potencia": 65,
                "precision": 100,
                "categoria": "Especial",
                "pp": 20
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Tajo Aéreo",
                    "tipo": "Volador",
                    "potencia": 75,
                    "precision": 95,
                    "categoria": "Especial",
                    "pp": 15
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Psíquico",
                    "tipo": "Psíquico",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 180,
        "grupo_huevo": "Volador"
    },
    "Tumito": {
        "id": 34,
        "nombre": "Tumito",
        "tipos": [
            "Acero"
        ],
        "categoria": "Tumi Menor",
        "altura": 0.4,
        "peso": 6.0,
        "stats_base": {
            "ps": 50,
            "atq": 65,
            "def": 50,
            "atq_esp": 35,
            "def_esp": 40,
            "vel": 50
        },
        "descripcion": "Pequeño tumi vivo que custodia los tesoros de los antiguos templos.",
        "evolucion": {
            "nivel": 30,
            "evoluciona_a": "Tumignus"
        },
        "movimientos_iniciales": [
            {
                "nombre": "Placaje",
                "tipo": "Normal",
                "potencia": 40,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Garra Metal",
                "tipo": "Acero",
                "potencia": 50,
                "precision": 95,
                "categoria": "Físico",
                "pp": 35
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 8,
                "movimiento": {
                    "nombre": "Cabeza de Hierro",
                    "tipo": "Acero",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            },
            {
                "nivel": 18,
                "movimiento": {
                    "nombre": "Foco Resplandor",
                    "tipo": "Acero",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            }
        ],
        "tasa_captura": 120,
        "exp_base": 120,
        "grupo_huevo": "Mineral"
    },
    "Tumignus": {
        "id": 35,
        "nombre": "Tumignus",
        "tipos": [
            "Acero",
            "Psíquico"
        ],
        "categoria": "Tumi",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 75,
            "atq": 90,
            "def": 70,
            "atq_esp": 90,
            "def_esp": 70,
            "vel": 75
        },
        "descripcion": "Forjado por antiguos orfebres, corta con el filo y con la mente.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Cabeza de Hierro",
                "tipo": "Acero",
                "potencia": 80,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            },
            {
                "nombre": "Psicorrayo",
                "tipo": "Psíquico",
                "potencia": 65,
                "precision": 100,
                "categoria": "Especial",
                "pp": 20
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Foco Resplandor",
                    "tipo": "Acero",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Psíquico",
                    "tipo": "Psíquico",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 180,
        "grupo_huevo": "Mineral"
    },
    "Huacok": {
        "id": 36,
        "nombre": "Huacok",
        "tipos": [
            "Roca"
        ],
        "categoria": "Huaco",
        "altura": 0.4,
        "peso": 6.0,
        "stats_base": {
            "ps": 60,
            "atq": 45,
            "def": 60,
            "atq_esp": 35,
            "def_esp": 55,
            "vel": 30
        },
        "descripcion": "Una vasija de arcilla que cobró vida al ser enterrada con ofrendas.",
        "evolucion": {
            "nivel": 28,
            "evoluciona_a": "Huacotrato"
        },
        "movimientos_iniciales": [
            {
                "nombre": "Placaje",
                "tipo": "Normal",
                "potencia": 40,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Lanzarrocas",
                "tipo": "Roca",
                "potencia": 50,
                "precision": 90,
                "categoria": "Físico",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 8,
                "movimiento": {
                    "nombre": "Avalancha",
                    "tipo": "Roca",
                    "potencia": 75,
                    "precision": 90,
                    "categoria": "Físico",
                    "pp": 10
                }
            }
        ],
        "tasa_captura": 255,
        "exp_base": 55,
        "grupo_huevo": "Mineral"
    },
    "Huacotrato": {
        "id": 37,
        "nombre": "Huacotrato",
        "tipos": [
            "Roca",
            "Fantasma"
        ],
        "categoria": "Huaco Retrato",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 75,
            "atq": 55,
            "def": 65,
            "atq_esp": 105,
            "def_esp": 75,
            "vel": 75
        },
        "descripcion": "El rostro pintado en su cerámica guarda el espíritu de un noble olvidado.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Avalancha",
                "tipo": "Roca",
                "potencia": 75,
                "precision": 90,
                "categoria": "Físico",
                "pp": 10
            },
            {
                "nombre": "Garra Sombra",
                "tipo": "Fantasma",
                "potencia": 70,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Roca Afilada",
                    "tipo": "Roca",
                    "potencia": 100,
                    "precision": 80,
                    "categoria": "Físico",
                    "pp": 5
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Bola Sombra",
                    "tipo": "Fantasma",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 180,
        "grupo_huevo": "Mineral"
    },
    "Ajito": {
        "id": 38,
        "nombre": "Ajito",
        "tipos": [
            "Planta"
        ],
        "categoria": "Ají",
        "altura": 0.4,
        "peso": 6.0,
        "stats_base": {
            "ps": 45,
            "atq": 35,
            "def": 40,
            "atq_esp": 65,
            "def_esp": 45,
            "vel": 45
        },
        "descripcion": "Pequeña ají que pica con solo mirarla; crece en las chacras abandonadas.",
        "evolucion": {
            "nivel": 20,
            "evoluciona_a": "Picantox"
        },
        "movimientos_iniciales": [
            {
                "nombre": "Placaje",
                "tipo": "Normal",
                "potencia": 40,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Látigo Cepa",
                "tipo": "Planta",
                "potencia": 45,
                "precision": 100,
                "categoria": "Físico",
                "pp": 25
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 8,
                "movimiento": {
                    "nombre": "Hoja Afilada",
                    "tipo": "Planta",
                    "potencia": 55,
                    "precision": 95,
                    "categoria": "Físico",
                    "pp": 25
                }
            }
        ],
        "tasa_captura": 255,
        "exp_base": 55,
        "grupo_huevo": "Planta"
    },
    "Picantox": {
        "id": 39,
        "nombre": "Picantox",
        "tipos": [
            "Fuego",
            "Planta"
        ],
        "categoria": "Ají Limo y Rocoto",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 75,
            "atq": 55,
            "def": 65,
            "atq_esp": 105,
            "def_esp": 75,
            "vel": 75
        },
        "descripcion": "Mezcla la picardía del ají limo con el fuego del rocoto.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Llamarada",
                "tipo": "Fuego",
                "potencia": 70,
                "precision": 90,
                "categoria": "Especial",
                "pp": 15
            },
            {
                "nombre": "Hoja Afilada",
                "tipo": "Planta",
                "potencia": 55,
                "precision": 95,
                "categoria": "Físico",
                "pp": 25
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Lanzallamas",
                    "tipo": "Fuego",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Energibola",
                    "tipo": "Planta",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 180,
        "grupo_huevo": "Campo"
    },
    "Condorito": {
        "id": 40,
        "nombre": "Condorito",
        "tipos": [
            "Volador"
        ],
        "categoria": "Cóndor Joven",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 50,
            "atq": 65,
            "def": 50,
            "atq_esp": 35,
            "def_esp": 40,
            "vel": 50
        },
        "descripcion": "Joven cóndor que practica planear en las corrientes de aire de la cordillera.",
        "evolucion": {
            "nivel": 33,
            "evoluciona_a": "Apucondor"
        },
        "movimientos_iniciales": [
            {
                "nombre": "Placaje",
                "tipo": "Normal",
                "potencia": 40,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Picotazo",
                "tipo": "Volador",
                "potencia": 35,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 8,
                "movimiento": {
                    "nombre": "Ataque Ala",
                    "tipo": "Volador",
                    "potencia": 60,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 35
                }
            },
            {
                "nivel": 18,
                "movimiento": {
                    "nombre": "Tajo Aéreo",
                    "tipo": "Volador",
                    "potencia": 75,
                    "precision": 95,
                    "categoria": "Especial",
                    "pp": 15
                }
            }
        ],
        "tasa_captura": 255,
        "exp_base": 55,
        "grupo_huevo": "Volador"
    },
    "Apucondor": {
        "id": 41,
        "nombre": "Apucondor",
        "tipos": [
            "Volador",
            "Siniestro"
        ],
        "categoria": "Cóndor Andino",
        "altura": 2.2,
        "peso": 180.0,
        "stats_base": {
            "ps": 80,
            "atq": 110,
            "def": 80,
            "atq_esp": 60,
            "def_esp": 70,
            "vel": 80
        },
        "descripcion": "Señor de los cielos: los Apus le confían la vigilancia de las cumbres.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Ataque Ala",
                "tipo": "Volador",
                "potencia": 60,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Triturar",
                "tipo": "Siniestro",
                "potencia": 80,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Tajo Aéreo",
                    "tipo": "Volador",
                    "potencia": 75,
                    "precision": 95,
                    "categoria": "Especial",
                    "pp": 15
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Pulso Umbrío",
                    "tipo": "Siniestro",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            },
            {
                "nivel": 34,
                "movimiento": {
                    "nombre": "Pájaro Osado",
                    "tipo": "Volador",
                    "potencia": 120,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 180,
        "grupo_huevo": "Volador"
    },
    "Tremarcto": {
        "id": 42,
        "nombre": "Tremarcto",
        "tipos": [
            "Lucha"
        ],
        "categoria": "Oso de Anteojos",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 50,
            "atq": 70,
            "def": 50,
            "atq_esp": 35,
            "def_esp": 45,
            "vel": 50
        },
        "descripcion": "Cachorro de oso con manchas blancas alrededor de los ojos; muy juguetón.",
        "evolucion": {
            "nivel": 30,
            "evoluciona_a": "Ursandino"
        },
        "movimientos_iniciales": [
            {
                "nombre": "Placaje",
                "tipo": "Normal",
                "potencia": 40,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Golpe Karate",
                "tipo": "Lucha",
                "potencia": 50,
                "precision": 100,
                "categoria": "Físico",
                "pp": 25
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 8,
                "movimiento": {
                    "nombre": "Patada Salto",
                    "tipo": "Lucha",
                    "potencia": 85,
                    "precision": 90,
                    "categoria": "Físico",
                    "pp": 25
                }
            },
            {
                "nivel": 18,
                "movimiento": {
                    "nombre": "Puño Dinámico",
                    "tipo": "Lucha",
                    "potencia": 100,
                    "precision": 50,
                    "categoria": "Físico",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 255,
        "exp_base": 55,
        "grupo_huevo": "Campo"
    },
    "Ursandino": {
        "id": 43,
        "nombre": "Ursandino",
        "tipos": [
            "Lucha",
            "Tierra"
        ],
        "categoria": "Oso de Anteojos",
        "altura": 2.2,
        "peso": 180.0,
        "stats_base": {
            "ps": 85,
            "atq": 110,
            "def": 85,
            "atq_esp": 60,
            "def_esp": 70,
            "vel": 85
        },
        "descripcion": "Fuerza descomunal en un cuerpo tranquilo; protege los bosques nublados.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Patada Salto",
                "tipo": "Lucha",
                "potencia": 85,
                "precision": 90,
                "categoria": "Físico",
                "pp": 25
            },
            {
                "nombre": "Excavar",
                "tipo": "Tierra",
                "potencia": 80,
                "precision": 100,
                "categoria": "Físico",
                "pp": 10
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Puño Dinámico",
                    "tipo": "Lucha",
                    "potencia": 100,
                    "precision": 50,
                    "categoria": "Físico",
                    "pp": 5
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Terremoto",
                    "tipo": "Tierra",
                    "potencia": 100,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 10
                }
            },
            {
                "nivel": 34,
                "movimiento": {
                    "nombre": "A Bocajarro",
                    "tipo": "Lucha",
                    "potencia": 120,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 180,
        "grupo_huevo": "Campo"
    },
    "Pirañita": {
        "id": 44,
        "nombre": "Pirañita",
        "tipos": [
            "Agua"
        ],
        "categoria": "Piraña",
        "altura": 0.4,
        "peso": 6.0,
        "stats_base": {
            "ps": 45,
            "atq": 65,
            "def": 45,
            "atq_esp": 35,
            "def_esp": 40,
            "vel": 45
        },
        "descripcion": "Pececillo de dientes afilados que caza en cardúmenes del Amazonas.",
        "evolucion": {
            "nivel": 26,
            "evoluciona_a": "Pirañatox"
        },
        "movimientos_iniciales": [
            {
                "nombre": "Placaje",
                "tipo": "Normal",
                "potencia": 40,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Pistola Agua",
                "tipo": "Agua",
                "potencia": 40,
                "precision": 100,
                "categoria": "Especial",
                "pp": 25
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 8,
                "movimiento": {
                    "nombre": "Hidropulso",
                    "tipo": "Agua",
                    "potencia": 65,
                    "precision": 95,
                    "categoria": "Especial",
                    "pp": 20
                }
            }
        ],
        "tasa_captura": 255,
        "exp_base": 55,
        "grupo_huevo": "Agua"
    },
    "Pirañatox": {
        "id": 45,
        "nombre": "Pirañatox",
        "tipos": [
            "Agua",
            "Veneno"
        ],
        "categoria": "Piraña Amazónica",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 80,
            "atq": 105,
            "def": 80,
            "atq_esp": 55,
            "def_esp": 65,
            "vel": 80
        },
        "descripcion": "Sus colmillos inyectan un veneno que adormece a las presas en segundos.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Hidropulso",
                "tipo": "Agua",
                "potencia": 65,
                "precision": 95,
                "categoria": "Especial",
                "pp": 20
            },
            {
                "nombre": "Residuos",
                "tipo": "Veneno",
                "potencia": 65,
                "precision": 100,
                "categoria": "Especial",
                "pp": 20
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Cascada Andina",
                    "tipo": "Agua",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Bomba Lodo",
                    "tipo": "Veneno",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 180,
        "grupo_huevo": "Agua"
    },
    "Papa Nativa": {
        "id": 46,
        "nombre": "Papa Nativa",
        "tipos": [
            "Planta",
            "Tierra"
        ],
        "categoria": "Tubérculo",
        "altura": 0.4,
        "peso": 6.0,
        "stats_base": {
            "ps": 70,
            "atq": 50,
            "def": 70,
            "atq_esp": 40,
            "def_esp": 65,
            "vel": 35
        },
        "descripcion": "Papa de mil colores: según el suelo y la piedra que toque, cambia de forma.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Látigo Cepa",
                "tipo": "Planta",
                "potencia": 45,
                "precision": 100,
                "categoria": "Físico",
                "pp": 25
            },
            {
                "nombre": "Hoja Afilada",
                "tipo": "Planta",
                "potencia": 55,
                "precision": 95,
                "categoria": "Físico",
                "pp": 25
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 10,
                "movimiento": {
                    "nombre": "Excavar",
                    "tipo": "Tierra",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 10
                }
            },
            {
                "nivel": 18,
                "movimiento": {
                    "nombre": "Energibola",
                    "tipo": "Planta",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 28,
                "movimiento": {
                    "nombre": "Terremoto",
                    "tipo": "Tierra",
                    "potencia": 100,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 10
                }
            }
        ],
        "tasa_captura": 120,
        "exp_base": 120,
        "grupo_huevo": "Planta",
        "evoluciones_especiales": [
            {
                "metodo": "piedra",
                "objeto": "Piedra Hielo",
                "evoluciona_a": "Papa Chuño"
            },
            {
                "metodo": "piedra",
                "objeto": "Piedra Dura",
                "evoluciona_a": "Papa Desértica"
            },
            {
                "metodo": "piedra",
                "objeto": "Piedra Furia",
                "evoluciona_a": "Papa Selvática"
            }
        ]
    },
    "Papa Chuño": {
        "id": 47,
        "nombre": "Papa Chuño",
        "tipos": [
            "Planta",
            "Hielo"
        ],
        "categoria": "Chuño",
        "altura": 0.4,
        "peso": 6.0,
        "stats_base": {
            "ps": 100,
            "atq": 70,
            "def": 105,
            "atq_esp": 55,
            "def_esp": 95,
            "vel": 45
        },
        "descripcion": "Liofilizada por las heladas, es dura como roca y fría como el nevado.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Hoja Afilada",
                "tipo": "Planta",
                "potencia": 55,
                "precision": 95,
                "categoria": "Físico",
                "pp": 25
            },
            {
                "nombre": "Mordisco Glaciar",
                "tipo": "Hielo",
                "potencia": 65,
                "precision": 95,
                "categoria": "Físico",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Energibola",
                    "tipo": "Planta",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Rayo Hielo",
                    "tipo": "Hielo",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 180,
        "grupo_huevo": "Planta"
    },
    "Papa Desértica": {
        "id": 48,
        "nombre": "Papa Desértica",
        "tipos": [
            "Planta",
            "Roca"
        ],
        "categoria": "Tubérculo Seco",
        "altura": 0.4,
        "peso": 6.0,
        "stats_base": {
            "ps": 100,
            "atq": 70,
            "def": 105,
            "atq_esp": 55,
            "def_esp": 95,
            "vel": 45
        },
        "descripcion": "Su piel agrietada guarda agua para años de sequía.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Hoja Afilada",
                "tipo": "Planta",
                "potencia": 55,
                "precision": 95,
                "categoria": "Físico",
                "pp": 25
            },
            {
                "nombre": "Avalancha",
                "tipo": "Roca",
                "potencia": 75,
                "precision": 90,
                "categoria": "Físico",
                "pp": 10
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Energibola",
                    "tipo": "Planta",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Roca Afilada",
                    "tipo": "Roca",
                    "potencia": 100,
                    "precision": 80,
                    "categoria": "Físico",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 180,
        "grupo_huevo": "Planta"
    },
    "Papa Selvática": {
        "id": 49,
        "nombre": "Papa Selvática",
        "tipos": [
            "Planta",
            "Veneno"
        ],
        "categoria": "Tubérculo Salvaje",
        "altura": 0.4,
        "peso": 6.0,
        "stats_base": {
            "ps": 80,
            "atq": 55,
            "def": 70,
            "atq_esp": 110,
            "def_esp": 80,
            "vel": 80
        },
        "descripcion": "Crece bajo los árboles de la selva y rezuma esporas tóxicas.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Hoja Afilada",
                "tipo": "Planta",
                "potencia": 55,
                "precision": 95,
                "categoria": "Físico",
                "pp": 25
            },
            {
                "nombre": "Residuos",
                "tipo": "Veneno",
                "potencia": 65,
                "precision": 100,
                "categoria": "Especial",
                "pp": 20
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Energibola",
                    "tipo": "Planta",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Bomba Lodo",
                    "tipo": "Veneno",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 180,
        "grupo_huevo": "Planta"
    },
    "Aruy": {
        "id": 50,
        "nombre": "Aruy",
        "tipos": [
            "Normal",
            "Fantasma"
        ],
        "categoria": "Espíritu Camélido",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 60,
            "atq": 60,
            "def": 60,
            "atq_esp": 60,
            "def_esp": 60,
            "vel": 60
        },
        "descripcion": "Espíritu de llama que vaga entre mundos; cambia según la luz que lo toque.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Placaje",
                "tipo": "Normal",
                "potencia": 40,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Impulso Andino",
                "tipo": "Normal",
                "potencia": 60,
                "precision": 100,
                "categoria": "Físico",
                "pp": 20
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 10,
                "movimiento": {
                    "nombre": "Garra Sombra",
                    "tipo": "Fantasma",
                    "potencia": 70,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            },
            {
                "nivel": 18,
                "movimiento": {
                    "nombre": "Golpe Cuerpo",
                    "tipo": "Normal",
                    "potencia": 85,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            },
            {
                "nivel": 28,
                "movimiento": {
                    "nombre": "Bola Sombra",
                    "tipo": "Fantasma",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            }
        ],
        "tasa_captura": 120,
        "exp_base": 120,
        "grupo_huevo": "Campo",
        "evoluciones_especiales": [
            {
                "metodo": "felicidad_dia",
                "objeto": "Felicidad (de día)",
                "evoluciona_a": "Llama Solar"
            },
            {
                "metodo": "felicidad_noche",
                "objeto": "Felicidad (de noche)",
                "evoluciona_a": "Llama Lunar"
            },
            {
                "metodo": "movimiento",
                "objeto": "Subir nivel con movimiento Fantasma",
                "evoluciona_a": "Llama Espectral"
            }
        ]
    },
    "Llama Solar": {
        "id": 51,
        "nombre": "Llama Solar",
        "tipos": [
            "Normal",
            "Fuego"
        ],
        "categoria": "Llama del Sol",
        "altura": 1.5,
        "peso": 70.0,
        "stats_base": {
            "ps": 80,
            "atq": 110,
            "def": 80,
            "atq_esp": 55,
            "def_esp": 70,
            "vel": 80
        },
        "descripcion": "Su lana irradia el calor del sol del mediodía.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Impulso Andino",
                "tipo": "Normal",
                "potencia": 60,
                "precision": 100,
                "categoria": "Físico",
                "pp": 20
            },
            {
                "nombre": "Llamarada",
                "tipo": "Fuego",
                "potencia": 70,
                "precision": 90,
                "categoria": "Especial",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Golpe Cuerpo",
                    "tipo": "Normal",
                    "potencia": 85,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Lanzallamas",
                    "tipo": "Fuego",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            },
            {
                "nivel": 34,
                "movimiento": {
                    "nombre": "Hiperrayo",
                    "tipo": "Normal",
                    "potencia": 150,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 180,
        "grupo_huevo": "Campo"
    },
    "Llama Lunar": {
        "id": 52,
        "nombre": "Llama Lunar",
        "tipos": [
            "Normal",
            "Siniestro"
        ],
        "categoria": "Llama de la Luna",
        "altura": 1.5,
        "peso": 70.0,
        "stats_base": {
            "ps": 75,
            "atq": 95,
            "def": 70,
            "atq_esp": 95,
            "def_esp": 70,
            "vel": 75
        },
        "descripcion": "Camina de noche, guiada por la luz plateada de Killa.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Impulso Andino",
                "tipo": "Normal",
                "potencia": 60,
                "precision": 100,
                "categoria": "Físico",
                "pp": 20
            },
            {
                "nombre": "Triturar",
                "tipo": "Siniestro",
                "potencia": 80,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Golpe Cuerpo",
                    "tipo": "Normal",
                    "potencia": 85,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Pulso Umbrío",
                    "tipo": "Siniestro",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            },
            {
                "nivel": 34,
                "movimiento": {
                    "nombre": "Hiperrayo",
                    "tipo": "Normal",
                    "potencia": 150,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 180,
        "grupo_huevo": "Campo"
    },
    "Llama Espectral": {
        "id": 53,
        "nombre": "Llama Espectral",
        "tipos": [
            "Fantasma"
        ],
        "categoria": "Llama Espectral",
        "altura": 1.5,
        "peso": 70.0,
        "stats_base": {
            "ps": 80,
            "atq": 55,
            "def": 70,
            "atq_esp": 110,
            "def_esp": 80,
            "vel": 80
        },
        "descripcion": "Ha perdido el cuerpo; solo queda su espíritu con forma de llama.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Garra Sombra",
                "tipo": "Fantasma",
                "potencia": 70,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            },
            {
                "nombre": "Impulso Andino",
                "tipo": "Normal",
                "potencia": 60,
                "precision": 100,
                "categoria": "Físico",
                "pp": 20
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Bola Sombra",
                    "tipo": "Fantasma",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Golpe Cuerpo",
                    "tipo": "Normal",
                    "potencia": 85,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            },
            {
                "nivel": 34,
                "movimiento": {
                    "nombre": "Silbido de Huaco",
                    "tipo": "Fantasma",
                    "potencia": 100,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 10
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 180,
        "grupo_huevo": "Amorfo"
    },
    "Zorrín": {
        "id": 54,
        "nombre": "Zorrín",
        "tipos": [
            "Siniestro"
        ],
        "categoria": "Zorro",
        "altura": 0.4,
        "peso": 6.0,
        "stats_base": {
            "ps": 40,
            "atq": 50,
            "def": 40,
            "atq_esp": 50,
            "def_esp": 40,
            "vel": 70
        },
        "descripcion": "Zorrito que husmea en las laderas rocosas sin hacer ruido.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Placaje",
                "tipo": "Normal",
                "potencia": 40,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Mordisco",
                "tipo": "Siniestro",
                "potencia": 60,
                "precision": 100,
                "categoria": "Físico",
                "pp": 25
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 8,
                "movimiento": {
                    "nombre": "Triturar",
                    "tipo": "Siniestro",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            }
        ],
        "tasa_captura": 255,
        "exp_base": 55,
        "grupo_huevo": "Campo",
        "evoluciones_especiales": [
            {
                "metodo": "piedra",
                "objeto": "Piedra Costa",
                "evoluciona_a": "Sechurax"
            }
        ]
    },
    "Sechurax": {
        "id": 55,
        "nombre": "Sechurax",
        "tipos": [
            "Siniestro",
            "Tierra"
        ],
        "categoria": "Zorro del Desierto",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 65,
            "atq": 80,
            "def": 65,
            "atq_esp": 80,
            "def_esp": 65,
            "vel": 115
        },
        "descripcion": "El zorro de Sechura: sobrevive entre dunas sin beber agua.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Triturar",
                "tipo": "Siniestro",
                "potencia": 80,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            },
            {
                "nombre": "Excavar",
                "tipo": "Tierra",
                "potencia": 80,
                "precision": 100,
                "categoria": "Físico",
                "pp": 10
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Pulso Umbrío",
                    "tipo": "Siniestro",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Terremoto",
                    "tipo": "Tierra",
                    "potencia": 100,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 10
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 180,
        "grupo_huevo": "Campo"
    },
    "Culpeito": {
        "id": 56,
        "nombre": "Culpeito",
        "tipos": [
            "Fuego"
        ],
        "categoria": "Zorro Culpeo",
        "altura": 0.4,
        "peso": 6.0,
        "stats_base": {
            "ps": 50,
            "atq": 35,
            "def": 40,
            "atq_esp": 65,
            "def_esp": 50,
            "vel": 50
        },
        "descripcion": "Zorro de pelaje rojizo que se camufla entre arbustos secos.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Placaje",
                "tipo": "Normal",
                "potencia": 40,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Ascuas",
                "tipo": "Fuego",
                "potencia": 40,
                "precision": 100,
                "categoria": "Especial",
                "pp": 25
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 8,
                "movimiento": {
                    "nombre": "Llamarada",
                    "tipo": "Fuego",
                    "potencia": 70,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 15
                }
            },
            {
                "nivel": 18,
                "movimiento": {
                    "nombre": "Lanzallamas",
                    "tipo": "Fuego",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            }
        ],
        "tasa_captura": 255,
        "exp_base": 55,
        "grupo_huevo": "Campo",
        "evoluciones_especiales": [
            {
                "metodo": "piedra",
                "objeto": "Piedra Sol",
                "evoluciona_a": "Vulandino"
            }
        ]
    },
    "Vulandino": {
        "id": 57,
        "nombre": "Vulandino",
        "tipos": [
            "Fuego",
            "Siniestro"
        ],
        "categoria": "Zorro Volcánico",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 70,
            "atq": 80,
            "def": 65,
            "atq_esp": 80,
            "def_esp": 65,
            "vel": 115
        },
        "descripcion": "Una llama negra recorre su cola cuando caza de noche.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Llamarada",
                "tipo": "Fuego",
                "potencia": 70,
                "precision": 90,
                "categoria": "Especial",
                "pp": 15
            },
            {
                "nombre": "Triturar",
                "tipo": "Siniestro",
                "potencia": 80,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Lanzallamas",
                    "tipo": "Fuego",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Pulso Umbrío",
                    "tipo": "Siniestro",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 180,
        "grupo_huevo": "Campo"
    },
    "Muquitox": {
        "id": 58,
        "nombre": "Muquitox",
        "tipos": [
            "Tierra"
        ],
        "categoria": "Mineral",
        "altura": 0.4,
        "peso": 6.0,
        "stats_base": {
            "ps": 60,
            "atq": 45,
            "def": 65,
            "atq_esp": 35,
            "def_esp": 60,
            "vel": 30
        },
        "descripcion": "Bulto de tierra con vetas de mineral; vive bajo las minas abandonadas.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Placaje",
                "tipo": "Normal",
                "potencia": 40,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Disparo Lodo",
                "tipo": "Tierra",
                "potencia": 55,
                "precision": 95,
                "categoria": "Especial",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 8,
                "movimiento": {
                    "nombre": "Excavar",
                    "tipo": "Tierra",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 10
                }
            },
            {
                "nivel": 18,
                "movimiento": {
                    "nombre": "Terremoto",
                    "tipo": "Tierra",
                    "potencia": 100,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 10
                }
            }
        ],
        "tasa_captura": 255,
        "exp_base": 55,
        "grupo_huevo": "Mineral",
        "evoluciones_especiales": [
            {
                "metodo": "intercambio",
                "objeto": "Cobre (intercambio)",
                "evoluciona_a": "Muquimetal"
            }
        ]
    },
    "Muquimetal": {
        "id": 59,
        "nombre": "Muquimetal",
        "tipos": [
            "Tierra",
            "Acero"
        ],
        "categoria": "Mineral de Cobre",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 100,
            "atq": 70,
            "def": 105,
            "atq_esp": 55,
            "def_esp": 95,
            "vel": 45
        },
        "descripcion": "El cobre fundido corre por sus venas y lo hace casi indestructible.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Excavar",
                "tipo": "Tierra",
                "potencia": 80,
                "precision": 100,
                "categoria": "Físico",
                "pp": 10
            },
            {
                "nombre": "Cabeza de Hierro",
                "tipo": "Acero",
                "potencia": 80,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Terremoto",
                    "tipo": "Tierra",
                    "potencia": 100,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 10
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Foco Resplandor",
                    "tipo": "Acero",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 180,
        "grupo_huevo": "Mineral"
    },
    "Tigrillo": {
        "id": 60,
        "nombre": "Tigrillo",
        "tipos": [
            "Fuego"
        ],
        "categoria": "Gatito Montés",
        "altura": 0.4,
        "peso": 6.0,
        "stats_base": {
            "ps": 50,
            "atq": 70,
            "def": 50,
            "atq_esp": 35,
            "def_esp": 40,
            "vel": 50
        },
        "descripcion": "Gato montés cuyas manchas arden cuando se emociona.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Placaje",
                "tipo": "Normal",
                "potencia": 40,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Ascuas",
                "tipo": "Fuego",
                "potencia": 40,
                "precision": 100,
                "categoria": "Especial",
                "pp": 25
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 8,
                "movimiento": {
                    "nombre": "Llamarada",
                    "tipo": "Fuego",
                    "potencia": 70,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 15
                }
            },
            {
                "nivel": 18,
                "movimiento": {
                    "nombre": "Lanzallamas",
                    "tipo": "Fuego",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            }
        ],
        "tasa_captura": 255,
        "exp_base": 55,
        "grupo_huevo": "Campo",
        "evoluciones_especiales": [
            {
                "metodo": "nivel_nieve",
                "objeto": "Garra Ardiente (subir nivel en nieve)",
                "evoluciona_a": "Chinchay"
            }
        ]
    },
    "Chinchay": {
        "id": 61,
        "nombre": "Chinchay",
        "tipos": [
            "Fuego",
            "Lucha"
        ],
        "categoria": "Felino de Fuego",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 80,
            "atq": 110,
            "def": 80,
            "atq_esp": 55,
            "def_esp": 70,
            "vel": 80
        },
        "descripcion": "Combina la fuerza de un luchador con garras al rojo vivo.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Llamarada",
                "tipo": "Fuego",
                "potencia": 70,
                "precision": 90,
                "categoria": "Especial",
                "pp": 15
            },
            {
                "nombre": "Patada Salto",
                "tipo": "Lucha",
                "potencia": 85,
                "precision": 90,
                "categoria": "Físico",
                "pp": 25
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Lanzallamas",
                    "tipo": "Fuego",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Puño Dinámico",
                    "tipo": "Lucha",
                    "potencia": 100,
                    "precision": 50,
                    "categoria": "Físico",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 180,
        "grupo_huevo": "Campo"
    },
    "Tarasquito": {
        "id": 62,
        "nombre": "Tarasquito",
        "tipos": [
            "Dragón"
        ],
        "categoria": "Dragoncito",
        "altura": 0.4,
        "peso": 6.0,
        "stats_base": {
            "ps": 50,
            "atq": 50,
            "def": 50,
            "atq_esp": 50,
            "def_esp": 50,
            "vel": 50
        },
        "descripcion": "Pequeño dragón nacido en las ruinas; sus cuernos sueñan con ser Amaru.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Placaje",
                "tipo": "Normal",
                "potencia": 40,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Aliento Dragón",
                "tipo": "Dragón",
                "potencia": 60,
                "precision": 100,
                "categoria": "Especial",
                "pp": 20
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 8,
                "movimiento": {
                    "nombre": "Garra Dragón",
                    "tipo": "Dragón",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            },
            {
                "nivel": 18,
                "movimiento": {
                    "nombre": "Pulso Dragón",
                    "tipo": "Dragón",
                    "potencia": 85,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            }
        ],
        "tasa_captura": 120,
        "exp_base": 120,
        "grupo_huevo": "Dragón",
        "evoluciones_especiales": [
            {
                "metodo": "piedra",
                "objeto": "Piedra Cobre",
                "evoluciona_a": "Tarascom"
            }
        ]
    },
    "Tarascom": {
        "id": 63,
        "nombre": "Tarascom",
        "tipos": [
            "Dragón",
            "Roca"
        ],
        "categoria": "Dragón de Piedra",
        "altura": 1.5,
        "peso": 70.0,
        "stats_base": {
            "ps": 105,
            "atq": 75,
            "def": 105,
            "atq_esp": 60,
            "def_esp": 100,
            "vel": 50
        },
        "descripcion": "Su coraza de roca resiste cualquier ataque, hasta los de otros dragones.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Garra Dragón",
                "tipo": "Dragón",
                "potencia": 80,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            },
            {
                "nombre": "Avalancha",
                "tipo": "Roca",
                "potencia": 75,
                "precision": 90,
                "categoria": "Físico",
                "pp": 10
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Pulso Dragón",
                    "tipo": "Dragón",
                    "potencia": 85,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Roca Afilada",
                    "tipo": "Roca",
                    "potencia": 100,
                    "precision": 80,
                    "categoria": "Físico",
                    "pp": 5
                }
            },
            {
                "nivel": 34,
                "movimiento": {
                    "nombre": "Eco del Amaru",
                    "tipo": "Dragón",
                    "potencia": 130,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 180,
        "grupo_huevo": "Dragón"
    },
    "Pishtaco": {
        "id": 64,
        "nombre": "Pishtaco",
        "tipos": [
            "Siniestro",
            "Fantasma"
        ],
        "categoria": "Leyenda",
        "altura": 1.5,
        "peso": 70.0,
        "stats_base": {
            "ps": 75,
            "atq": 90,
            "def": 65,
            "atq_esp": 90,
            "def_esp": 65,
            "vel": 75
        },
        "descripcion": "Cuentan que roba la grasa de los viajeros solitarios en la oscuridad.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Triturar",
                "tipo": "Siniestro",
                "potencia": 80,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            },
            {
                "nombre": "Garra Sombra",
                "tipo": "Fantasma",
                "potencia": 70,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Pulso Umbrío",
                    "tipo": "Siniestro",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Bola Sombra",
                    "tipo": "Fantasma",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 175,
        "grupo_huevo": "Campo"
    },
    "Jarjacha": {
        "id": 65,
        "nombre": "Jarjacha",
        "tipos": [
            "Normal",
            "Fantasma"
        ],
        "categoria": "Espíritu Maldito",
        "altura": 1.5,
        "peso": 70.0,
        "stats_base": {
            "ps": 80,
            "atq": 55,
            "def": 70,
            "atq_esp": 110,
            "def_esp": 80,
            "vel": 80
        },
        "descripcion": "Llama de dos cabezas que castiga a los infieles en la noche.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Impulso Andino",
                "tipo": "Normal",
                "potencia": 60,
                "precision": 100,
                "categoria": "Físico",
                "pp": 20
            },
            {
                "nombre": "Garra Sombra",
                "tipo": "Fantasma",
                "potencia": 70,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Golpe Cuerpo",
                    "tipo": "Normal",
                    "potencia": 85,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Bola Sombra",
                    "tipo": "Fantasma",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 175,
        "grupo_huevo": "Campo"
    },
    "Pututos": {
        "id": 66,
        "nombre": "Pututos",
        "tipos": [
            "Agua",
            "Sonido"
        ],
        "categoria": "Caracola",
        "altura": 0.4,
        "peso": 6.0,
        "stats_base": {
            "ps": 75,
            "atq": 50,
            "def": 65,
            "atq_esp": 100,
            "def_esp": 75,
            "vel": 75
        },
        "descripcion": "Su llamado atraviesa los valles y alerta a los Pokémon cercanos.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Hidropulso",
                "tipo": "Agua",
                "potencia": 65,
                "precision": 95,
                "categoria": "Especial",
                "pp": 20
            },
            {
                "nombre": "Llamado Ancestral",
                "tipo": "Sonido",
                "potencia": 80,
                "precision": 100,
                "categoria": "Especial",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Cascada Andina",
                    "tipo": "Agua",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Alarido Andino",
                    "tipo": "Sonido",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 175,
        "grupo_huevo": "Agua"
    },
    "Quipus": {
        "id": 67,
        "nombre": "Quipus",
        "tipos": [
            "Fantasma",
            "Normal"
        ],
        "categoria": "Registro",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 75,
            "atq": 50,
            "def": 65,
            "atq_esp": 100,
            "def_esp": 75,
            "vel": 75
        },
        "descripcion": "Sus cuerdas de colores guardan la memoria de un imperio entero.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Garra Sombra",
                "tipo": "Fantasma",
                "potencia": 70,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            },
            {
                "nombre": "Impulso Andino",
                "tipo": "Normal",
                "potencia": 60,
                "precision": 100,
                "categoria": "Físico",
                "pp": 20
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Bola Sombra",
                    "tipo": "Fantasma",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Golpe Cuerpo",
                    "tipo": "Normal",
                    "potencia": 85,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 175,
        "grupo_huevo": "Amorfo"
    },
    "Ceviche": {
        "id": 68,
        "nombre": "Ceviche",
        "tipos": [
            "Agua",
            "Veneno"
        ],
        "categoria": "Plato Vivo",
        "altura": 0.4,
        "peso": 6.0,
        "stats_base": {
            "ps": 75,
            "atq": 50,
            "def": 60,
            "atq_esp": 100,
            "def_esp": 75,
            "vel": 75
        },
        "descripcion": "Un plato que cobró vida; es mejor no probarlo si sus ojos te miran.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Hidropulso",
                "tipo": "Agua",
                "potencia": 65,
                "precision": 95,
                "categoria": "Especial",
                "pp": 20
            },
            {
                "nombre": "Residuos",
                "tipo": "Veneno",
                "potencia": 65,
                "precision": 100,
                "categoria": "Especial",
                "pp": 20
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Cascada Andina",
                    "tipo": "Agua",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Bomba Lodo",
                    "tipo": "Veneno",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 175,
        "grupo_huevo": "Agua"
    },
    "Maíz Morado": {
        "id": 69,
        "nombre": "Maíz Morado",
        "tipos": [
            "Planta"
        ],
        "categoria": "Maíz",
        "altura": 0.4,
        "peso": 6.0,
        "stats_base": {
            "ps": 90,
            "atq": 65,
            "def": 90,
            "atq_esp": 50,
            "def_esp": 85,
            "vel": 40
        },
        "descripcion": "Grano púrpura lleno de energía; se dice que su jugo cura cualquier mal.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Hoja Afilada",
                "tipo": "Planta",
                "potencia": 55,
                "precision": 95,
                "categoria": "Físico",
                "pp": 25
            },
            {
                "nombre": "Impulso Andino",
                "tipo": "Normal",
                "potencia": 60,
                "precision": 100,
                "categoria": "Físico",
                "pp": 20
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Energibola",
                    "tipo": "Planta",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Golpe Cuerpo",
                    "tipo": "Normal",
                    "potencia": 85,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 175,
        "grupo_huevo": "Planta"
    },
    "Colibrí Nasca": {
        "id": 70,
        "nombre": "Colibrí Nasca",
        "tipos": [
            "Roca",
            "Psíquico"
        ],
        "categoria": "Geoglifo",
        "altura": 1.5,
        "peso": 70.0,
        "stats_base": {
            "ps": 80,
            "atq": 55,
            "def": 70,
            "atq_esp": 110,
            "def_esp": 80,
            "vel": 80
        },
        "descripcion": "Figura de las líneas de Nasca que despierta a la luz de los eclipses.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Avalancha",
                "tipo": "Roca",
                "potencia": 75,
                "precision": 90,
                "categoria": "Físico",
                "pp": 10
            },
            {
                "nombre": "Psicorrayo",
                "tipo": "Psíquico",
                "potencia": 65,
                "precision": 100,
                "categoria": "Especial",
                "pp": 20
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Roca Afilada",
                    "tipo": "Roca",
                    "potencia": 100,
                    "precision": 80,
                    "categoria": "Físico",
                    "pp": 5
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Psíquico",
                    "tipo": "Psíquico",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 175,
        "grupo_huevo": "Mineral"
    },
    "Araña Nasca": {
        "id": 71,
        "nombre": "Araña Nasca",
        "tipos": [
            "Roca",
            "Veneno"
        ],
        "categoria": "Geoglifo",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 80,
            "atq": 110,
            "def": 80,
            "atq_esp": 55,
            "def_esp": 70,
            "vel": 80
        },
        "descripcion": "Teje redes sobre el desierto que guían a los espíritus.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Avalancha",
                "tipo": "Roca",
                "potencia": 75,
                "precision": 90,
                "categoria": "Físico",
                "pp": 10
            },
            {
                "nombre": "Residuos",
                "tipo": "Veneno",
                "potencia": 65,
                "precision": 100,
                "categoria": "Especial",
                "pp": 20
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Roca Afilada",
                    "tipo": "Roca",
                    "potencia": 100,
                    "precision": 80,
                    "categoria": "Físico",
                    "pp": 5
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Bomba Lodo",
                    "tipo": "Veneno",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 175,
        "grupo_huevo": "Mineral"
    },
    "Tunche": {
        "id": 72,
        "nombre": "Tunche",
        "tipos": [
            "Fantasma",
            "Siniestro"
        ],
        "categoria": "Silbido",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 75,
            "atq": 90,
            "def": 70,
            "atq_esp": 90,
            "def_esp": 70,
            "vel": 75
        },
        "descripcion": "Anuncia la muerte con un silbido que se oye en la selva profunda.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Garra Sombra",
                "tipo": "Fantasma",
                "potencia": 70,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            },
            {
                "nombre": "Triturar",
                "tipo": "Siniestro",
                "potencia": 80,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Bola Sombra",
                    "tipo": "Fantasma",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Pulso Umbrío",
                    "tipo": "Siniestro",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 175,
        "grupo_huevo": "Amorfo"
    },
    "Carachama": {
        "id": 73,
        "nombre": "Carachama",
        "tipos": [
            "Agua",
            "Roca"
        ],
        "categoria": "Pez Acorazado",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 95,
            "atq": 70,
            "def": 100,
            "atq_esp": 55,
            "def_esp": 90,
            "vel": 45
        },
        "descripcion": "Un tanque defensivo con escamas durísimas.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Hidropulso",
                "tipo": "Agua",
                "potencia": 65,
                "precision": 95,
                "categoria": "Especial",
                "pp": 20
            },
            {
                "nombre": "Avalancha",
                "tipo": "Roca",
                "potencia": 75,
                "precision": 90,
                "categoria": "Físico",
                "pp": 10
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Cascada Andina",
                    "tipo": "Agua",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Roca Afilada",
                    "tipo": "Roca",
                    "potencia": 100,
                    "precision": 80,
                    "categoria": "Físico",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 175,
        "grupo_huevo": "Agua"
    },
    "Bufeo Colorado": {
        "id": 74,
        "nombre": "Bufeo Colorado",
        "tipos": [
            "Agua",
            "Psíquico"
        ],
        "categoria": "Delfín Rosado",
        "altura": 2.2,
        "peso": 180.0,
        "stats_base": {
            "ps": 70,
            "atq": 85,
            "def": 70,
            "atq_esp": 85,
            "def_esp": 70,
            "vel": 125
        },
        "descripcion": "Dicen que seduce a los ribereños y los lleva a su palacio bajo el río.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Hidropulso",
                "tipo": "Agua",
                "potencia": 65,
                "precision": 95,
                "categoria": "Especial",
                "pp": 20
            },
            {
                "nombre": "Psicorrayo",
                "tipo": "Psíquico",
                "potencia": 65,
                "precision": 100,
                "categoria": "Especial",
                "pp": 20
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Cascada Andina",
                    "tipo": "Agua",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Psíquico",
                    "tipo": "Psíquico",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 34,
                "movimiento": {
                    "nombre": "Hidrobomba Mística",
                    "tipo": "Agua",
                    "potencia": 120,
                    "precision": 80,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 175,
        "grupo_huevo": "Agua"
    },
    "Chullachaqui": {
        "id": 75,
        "nombre": "Chullachaqui",
        "tipos": [
            "Planta",
            "Fantasma"
        ],
        "categoria": "Guardián de la Selva",
        "altura": 1.5,
        "peso": 70.0,
        "stats_base": {
            "ps": 75,
            "atq": 95,
            "def": 70,
            "atq_esp": 95,
            "def_esp": 70,
            "vel": 75
        },
        "descripcion": "Guardián con un pie de hoja: toma la forma de tus seres queridos para perderte.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Hoja Afilada",
                "tipo": "Planta",
                "potencia": 55,
                "precision": 95,
                "categoria": "Físico",
                "pp": 25
            },
            {
                "nombre": "Garra Sombra",
                "tipo": "Fantasma",
                "potencia": 70,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Energibola",
                    "tipo": "Planta",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Bola Sombra",
                    "tipo": "Fantasma",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            },
            {
                "nivel": 34,
                "movimiento": {
                    "nombre": "Lluvia Solar",
                    "tipo": "Planta",
                    "potencia": 120,
                    "precision": 85,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 175,
        "grupo_huevo": "Planta"
    },
    "Muki-Muki": {
        "id": 76,
        "nombre": "Muki-Muki",
        "tipos": [
            "Tierra",
            "Hada"
        ],
        "categoria": "Duende Minero",
        "altura": 0.4,
        "peso": 6.0,
        "stats_base": {
            "ps": 75,
            "atq": 50,
            "def": 65,
            "atq_esp": 100,
            "def_esp": 75,
            "vel": 75
        },
        "descripcion": "Duende de las minas que premia a los que respetan la montaña.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Excavar",
                "tipo": "Tierra",
                "potencia": 80,
                "precision": 100,
                "categoria": "Físico",
                "pp": 10
            },
            {
                "nombre": "Brillo Mágico",
                "tipo": "Hada",
                "potencia": 80,
                "precision": 100,
                "categoria": "Especial",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Terremoto",
                    "tipo": "Tierra",
                    "potencia": 100,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 10
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Fuerza Lunar",
                    "tipo": "Hada",
                    "potencia": 95,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 175,
        "grupo_huevo": "Mineral"
    },
    "Tunante": {
        "id": 77,
        "nombre": "Tunante",
        "tipos": [
            "Normal",
            "Psíquico"
        ],
        "categoria": "Bailarín",
        "altura": 1.5,
        "peso": 70.0,
        "stats_base": {
            "ps": 75,
            "atq": 55,
            "def": 65,
            "atq_esp": 105,
            "def_esp": 75,
            "vel": 75
        },
        "descripcion": "Elegante bailarín de sombrero que hechiza con sus pasos.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Impulso Andino",
                "tipo": "Normal",
                "potencia": 60,
                "precision": 100,
                "categoria": "Físico",
                "pp": 20
            },
            {
                "nombre": "Psicorrayo",
                "tipo": "Psíquico",
                "potencia": 65,
                "precision": 100,
                "categoria": "Especial",
                "pp": 20
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Golpe Cuerpo",
                    "tipo": "Normal",
                    "potencia": 85,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Psíquico",
                    "tipo": "Psíquico",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 175,
        "grupo_huevo": "Campo"
    },
    "Danza de Tijeras": {
        "id": 78,
        "nombre": "Danza de Tijeras",
        "tipos": [
            "Lucha",
            "Psíquico"
        ],
        "categoria": "Danzante",
        "altura": 1.5,
        "peso": 70.0,
        "stats_base": {
            "ps": 85,
            "atq": 110,
            "def": 85,
            "atq_esp": 60,
            "def_esp": 70,
            "vel": 85
        },
        "descripcion": "Baila con tijeras de acero en una competencia contra sus propios fantasmas.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Patada Salto",
                "tipo": "Lucha",
                "potencia": 85,
                "precision": 90,
                "categoria": "Físico",
                "pp": 25
            },
            {
                "nombre": "Psicorrayo",
                "tipo": "Psíquico",
                "potencia": 65,
                "precision": 100,
                "categoria": "Especial",
                "pp": 20
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Puño Dinámico",
                    "tipo": "Lucha",
                    "potencia": 100,
                    "precision": 50,
                    "categoria": "Físico",
                    "pp": 5
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Psíquico",
                    "tipo": "Psíquico",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 34,
                "movimiento": {
                    "nombre": "A Bocajarro",
                    "tipo": "Lucha",
                    "potencia": 120,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 175,
        "grupo_huevo": "Campo"
    },
    "Orquídea Negra": {
        "id": 79,
        "nombre": "Orquídea Negra",
        "tipos": [
            "Planta",
            "Siniestro"
        ],
        "categoria": "Flor Carnívora",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 80,
            "atq": 55,
            "def": 70,
            "atq_esp": 110,
            "def_esp": 80,
            "vel": 80
        },
        "descripcion": "Planta carnívora singular: su perfume atrae y adormece a sus víctimas.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Hoja Afilada",
                "tipo": "Planta",
                "potencia": 55,
                "precision": 95,
                "categoria": "Físico",
                "pp": 25
            },
            {
                "nombre": "Triturar",
                "tipo": "Siniestro",
                "potencia": 80,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Energibola",
                    "tipo": "Planta",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Pulso Umbrío",
                    "tipo": "Siniestro",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            },
            {
                "nivel": 34,
                "movimiento": {
                    "nombre": "Lluvia Solar",
                    "tipo": "Planta",
                    "potencia": 120,
                    "precision": 85,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 175,
        "grupo_huevo": "Planta"
    },
    "Torito de Pucará": {
        "id": 80,
        "nombre": "Torito de Pucará",
        "tipos": [
            "Roca",
            "Fuego"
        ],
        "categoria": "Toro de Cerámica",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 95,
            "atq": 70,
            "def": 100,
            "atq_esp": 55,
            "def_esp": 95,
            "vel": 45
        },
        "descripcion": "Amuleto de cerámica que protege los techos de las casas.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Avalancha",
                "tipo": "Roca",
                "potencia": 75,
                "precision": 90,
                "categoria": "Físico",
                "pp": 10
            },
            {
                "nombre": "Llamarada",
                "tipo": "Fuego",
                "potencia": 70,
                "precision": 90,
                "categoria": "Especial",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Roca Afilada",
                    "tipo": "Roca",
                    "potencia": 100,
                    "precision": 80,
                    "categoria": "Físico",
                    "pp": 5
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Lanzallamas",
                    "tipo": "Fuego",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 15
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 175,
        "grupo_huevo": "Mineral"
    },
    "Dracuy": {
        "id": 81,
        "nombre": "Dracuy",
        "tipos": [
            "Dragón"
        ],
        "categoria": "Cuy Dragón",
        "altura": 0.4,
        "peso": 6.0,
        "stats_base": {
            "ps": 50,
            "atq": 50,
            "def": 50,
            "atq_esp": 50,
            "def_esp": 50,
            "vel": 50
        },
        "descripcion": "Pequeña criatura que parece un cuy con diminutas escamas.",
        "evolucion": {
            "nivel": 30,
            "evoluciona_a": "Serpior"
        },
        "movimientos_iniciales": [
            {
                "nombre": "Placaje",
                "tipo": "Normal",
                "potencia": 40,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            },
            {
                "nombre": "Aliento Dragón",
                "tipo": "Dragón",
                "potencia": 60,
                "precision": 100,
                "categoria": "Especial",
                "pp": 20
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 8,
                "movimiento": {
                    "nombre": "Garra Dragón",
                    "tipo": "Dragón",
                    "potencia": 80,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            },
            {
                "nivel": 18,
                "movimiento": {
                    "nombre": "Pulso Dragón",
                    "tipo": "Dragón",
                    "potencia": 85,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            }
        ],
        "tasa_captura": 120,
        "exp_base": 120,
        "grupo_huevo": "Dragón"
    },
    "Serpior": {
        "id": 82,
        "nombre": "Serpior",
        "tipos": [
            "Dragón",
            "Volador"
        ],
        "categoria": "Serpiente Alada",
        "altura": 1.5,
        "peso": 70.0,
        "stats_base": {
            "ps": 70,
            "atq": 70,
            "def": 70,
            "atq_esp": 70,
            "def_esp": 70,
            "vel": 70
        },
        "descripcion": "Despliega alas diminutas mientras se enrosca en los riscos.",
        "evolucion": {
            "nivel": 55,
            "evoluciona_a": "Amaru"
        },
        "movimientos_iniciales": [
            {
                "nombre": "Garra Dragón",
                "tipo": "Dragón",
                "potencia": 80,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            },
            {
                "nombre": "Ataque Ala",
                "tipo": "Volador",
                "potencia": 60,
                "precision": 100,
                "categoria": "Físico",
                "pp": 35
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 14,
                "movimiento": {
                    "nombre": "Pulso Dragón",
                    "tipo": "Dragón",
                    "potencia": 85,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 24,
                "movimiento": {
                    "nombre": "Tajo Aéreo",
                    "tipo": "Volador",
                    "potencia": 75,
                    "precision": 95,
                    "categoria": "Especial",
                    "pp": 15
                }
            }
        ],
        "tasa_captura": 120,
        "exp_base": 120,
        "grupo_huevo": "Dragón"
    },
    "Amaru": {
        "id": 83,
        "nombre": "Amaru",
        "tipos": [
            "Dragón",
            "Volador"
        ],
        "categoria": "Dragón Celestial",
        "altura": 3.5,
        "peso": 420.0,
        "stats_base": {
            "ps": 100,
            "atq": 100,
            "def": 100,
            "atq_esp": 100,
            "def_esp": 100,
            "vel": 100
        },
        "descripcion": "El dragón celestial primordial: sus escamas canalizan los vientos de la región.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Pulso Dragón",
                "tipo": "Dragón",
                "potencia": 85,
                "precision": 100,
                "categoria": "Especial",
                "pp": 10
            },
            {
                "nombre": "Tajo Aéreo",
                "tipo": "Volador",
                "potencia": 75,
                "precision": 95,
                "categoria": "Especial",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 30,
                "movimiento": {
                    "nombre": "Eco del Amaru",
                    "tipo": "Dragón",
                    "potencia": 130,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            },
            {
                "nivel": 40,
                "movimiento": {
                    "nombre": "Psíquico",
                    "tipo": "Psíquico",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 50,
                "movimiento": {
                    "nombre": "Pájaro Osado",
                    "tipo": "Volador",
                    "potencia": 120,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            },
            {
                "nivel": 60,
                "movimiento": {
                    "nombre": "Hiperrayo",
                    "tipo": "Normal",
                    "potencia": 150,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 45,
        "exp_base": 300,
        "grupo_huevo": "Dragón"
    },
    "Yacumama": {
        "id": 84,
        "nombre": "Yacumama",
        "tipos": [
            "Agua",
            "Dragón"
        ],
        "categoria": "Madre de las Aguas",
        "altura": 3.5,
        "peso": 420.0,
        "stats_base": {
            "ps": 100,
            "atq": 70,
            "def": 85,
            "atq_esp": 135,
            "def_esp": 100,
            "vel": 100
        },
        "descripcion": "La madre de las aguas, que descansa en los abismos del Amazonas y el Titicaca.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Cascada Andina",
                "tipo": "Agua",
                "potencia": 80,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            },
            {
                "nombre": "Pulso Dragón",
                "tipo": "Dragón",
                "potencia": 85,
                "precision": 100,
                "categoria": "Especial",
                "pp": 10
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 30,
                "movimiento": {
                    "nombre": "Hidrobomba Mística",
                    "tipo": "Agua",
                    "potencia": 120,
                    "precision": 80,
                    "categoria": "Especial",
                    "pp": 5
                }
            },
            {
                "nivel": 40,
                "movimiento": {
                    "nombre": "Psíquico",
                    "tipo": "Psíquico",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 50,
                "movimiento": {
                    "nombre": "Eco del Amaru",
                    "tipo": "Dragón",
                    "potencia": 130,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            },
            {
                "nivel": 60,
                "movimiento": {
                    "nombre": "Hiperrayo",
                    "tipo": "Normal",
                    "potencia": 150,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 3,
        "exp_base": 330,
        "grupo_huevo": "Desconocido"
    },
    "Inti-Can": {
        "id": 85,
        "nombre": "Inti-Can",
        "tipos": [
            "Fuego",
            "Psíquico"
        ],
        "categoria": "Guardián Solar",
        "altura": 1.5,
        "peso": 70.0,
        "stats_base": {
            "ps": 100,
            "atq": 70,
            "def": 85,
            "atq_esp": 135,
            "def_esp": 100,
            "vel": 100
        },
        "descripcion": "Guardián elemental del sol: sus ojos reflejan el amanecer.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Lanzallamas",
                "tipo": "Fuego",
                "potencia": 90,
                "precision": 100,
                "categoria": "Especial",
                "pp": 15
            },
            {
                "nombre": "Psíquico",
                "tipo": "Psíquico",
                "potencia": 90,
                "precision": 100,
                "categoria": "Especial",
                "pp": 10
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 50,
                "movimiento": {
                    "nombre": "Psicocorte",
                    "tipo": "Psíquico",
                    "potencia": 120,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            },
            {
                "nivel": 60,
                "movimiento": {
                    "nombre": "Hiperrayo",
                    "tipo": "Normal",
                    "potencia": 150,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 3,
        "exp_base": 290,
        "grupo_huevo": "Desconocido"
    },
    "Killa-Puma": {
        "id": 86,
        "nombre": "Killa-Puma",
        "tipos": [
            "Hielo",
            "Fantasma"
        ],
        "categoria": "Guardián Lunar",
        "altura": 1.5,
        "peso": 70.0,
        "stats_base": {
            "ps": 85,
            "atq": 100,
            "def": 80,
            "atq_esp": 100,
            "def_esp": 80,
            "vel": 145
        },
        "descripcion": "Guardián de la luna: su rastro congela el aire de la noche.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Rayo Hielo",
                "tipo": "Hielo",
                "potencia": 90,
                "precision": 100,
                "categoria": "Especial",
                "pp": 10
            },
            {
                "nombre": "Bola Sombra",
                "tipo": "Fantasma",
                "potencia": 80,
                "precision": 100,
                "categoria": "Especial",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 40,
                "movimiento": {
                    "nombre": "Psíquico",
                    "tipo": "Psíquico",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 50,
                "movimiento": {
                    "nombre": "Silbido de Huaco",
                    "tipo": "Fantasma",
                    "potencia": 100,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 60,
                "movimiento": {
                    "nombre": "Hiperrayo",
                    "tipo": "Normal",
                    "potencia": 150,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 3,
        "exp_base": 290,
        "grupo_huevo": "Desconocido"
    },
    "Pach-Avis": {
        "id": 87,
        "nombre": "Pach-Avis",
        "tipos": [
            "Planta",
            "Tierra"
        ],
        "categoria": "Guardián Alado",
        "altura": 1.5,
        "peso": 70.0,
        "stats_base": {
            "ps": 120,
            "atq": 90,
            "def": 125,
            "atq_esp": 70,
            "def_esp": 115,
            "vel": 60
        },
        "descripcion": "Guardián alado de los bosques; sus plumas brotan en semillas.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Energibola",
                "tipo": "Planta",
                "potencia": 90,
                "precision": 100,
                "categoria": "Especial",
                "pp": 10
            },
            {
                "nombre": "Terremoto",
                "tipo": "Tierra",
                "potencia": 100,
                "precision": 100,
                "categoria": "Físico",
                "pp": 10
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 40,
                "movimiento": {
                    "nombre": "Psíquico",
                    "tipo": "Psíquico",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 50,
                "movimiento": {
                    "nombre": "Fisura",
                    "tipo": "Tierra",
                    "potencia": 120,
                    "precision": 80,
                    "categoria": "Físico",
                    "pp": 5
                }
            },
            {
                "nivel": 60,
                "movimiento": {
                    "nombre": "Hiperrayo",
                    "tipo": "Normal",
                    "potencia": 150,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 3,
        "exp_base": 290,
        "grupo_huevo": "Desconocido"
    },
    "Wira-Titan": {
        "id": 88,
        "nombre": "Wira-Titan",
        "tipos": [
            "Psíquico",
            "Roca"
        ],
        "categoria": "Arquitecto del Orden",
        "altura": 3.5,
        "peso": 420.0,
        "stats_base": {
            "ps": 140,
            "atq": 100,
            "def": 145,
            "atq_esp": 80,
            "def_esp": 135,
            "vel": 70
        },
        "descripcion": "Arquitecto del orden, la tierra y la mente. Deidad colosal de piedra.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Psíquico",
                "tipo": "Psíquico",
                "potencia": 90,
                "precision": 100,
                "categoria": "Especial",
                "pp": 10
            },
            {
                "nombre": "Roca Afilada",
                "tipo": "Roca",
                "potencia": 100,
                "precision": 80,
                "categoria": "Físico",
                "pp": 5
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 30,
                "movimiento": {
                    "nombre": "Psicocorte",
                    "tipo": "Psíquico",
                    "potencia": 120,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            },
            {
                "nivel": 40,
                "movimiento": {
                    "nombre": "Golpe Cuerpo",
                    "tipo": "Normal",
                    "potencia": 85,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            },
            {
                "nivel": 50,
                "movimiento": {
                    "nombre": "Alud Andino",
                    "tipo": "Roca",
                    "potencia": 120,
                    "precision": 85,
                    "categoria": "Físico",
                    "pp": 5
                }
            },
            {
                "nivel": 60,
                "movimiento": {
                    "nombre": "Hiperrayo",
                    "tipo": "Normal",
                    "potencia": 150,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 3,
        "exp_base": 340,
        "grupo_huevo": "Desconocido"
    },
    "Supay-Dread": {
        "id": 89,
        "nombre": "Supay-Dread",
        "tipos": [
            "Siniestro",
            "Fantasma"
        ],
        "categoria": "Guardián de las Pruebas",
        "altura": 3.5,
        "peso": 420.0,
        "stats_base": {
            "ps": 110,
            "atq": 130,
            "def": 95,
            "atq_esp": 130,
            "def_esp": 95,
            "vel": 110
        },
        "descripcion": "Guardián de las sombras y las pruebas del destino.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Pulso Umbrío",
                "tipo": "Siniestro",
                "potencia": 80,
                "precision": 100,
                "categoria": "Especial",
                "pp": 15
            },
            {
                "nombre": "Bola Sombra",
                "tipo": "Fantasma",
                "potencia": 80,
                "precision": 100,
                "categoria": "Especial",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 30,
                "movimiento": {
                    "nombre": "Juego Sucio",
                    "tipo": "Siniestro",
                    "potencia": 95,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            },
            {
                "nivel": 40,
                "movimiento": {
                    "nombre": "Psíquico",
                    "tipo": "Psíquico",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 50,
                "movimiento": {
                    "nombre": "Silbido de Huaco",
                    "tipo": "Fantasma",
                    "potencia": 100,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 60,
                "movimiento": {
                    "nombre": "Hiperrayo",
                    "tipo": "Normal",
                    "potencia": 150,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 3,
        "exp_base": 340,
        "grupo_huevo": "Desconocido"
    },
    "Pachamama-Prime": {
        "id": 90,
        "nombre": "Pachamama-Prime",
        "tipos": [
            "Planta",
            "Hada"
        ],
        "categoria": "Madre Naturaleza",
        "altura": 3.5,
        "peso": 420.0,
        "stats_base": {
            "ps": 115,
            "atq": 80,
            "def": 95,
            "atq_esp": 155,
            "def_esp": 115,
            "vel": 115
        },
        "descripcion": "La madre de la naturaleza, la vida vegetal y las hadas.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Energibola",
                "tipo": "Planta",
                "potencia": 90,
                "precision": 100,
                "categoria": "Especial",
                "pp": 10
            },
            {
                "nombre": "Fuerza Lunar",
                "tipo": "Hada",
                "potencia": 95,
                "precision": 100,
                "categoria": "Especial",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 30,
                "movimiento": {
                    "nombre": "Lluvia Solar",
                    "tipo": "Planta",
                    "potencia": 120,
                    "precision": 85,
                    "categoria": "Especial",
                    "pp": 5
                }
            },
            {
                "nivel": 40,
                "movimiento": {
                    "nombre": "Psíquico",
                    "tipo": "Psíquico",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 50,
                "movimiento": {
                    "nombre": "Voz Cautivadora",
                    "tipo": "Hada",
                    "potencia": 110,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            },
            {
                "nivel": 60,
                "movimiento": {
                    "nombre": "Hiperrayo",
                    "tipo": "Normal",
                    "potencia": 150,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 3,
        "exp_base": 340,
        "grupo_huevo": "Desconocido"
    },
    "Perro Sin Pelo": {
        "id": 91,
        "nombre": "Perro Sin Pelo",
        "tipos": [
            "Fantasma",
            "Psíquico"
        ],
        "categoria": "Guía de Almas",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 90,
            "atq": 60,
            "def": 75,
            "atq_esp": 120,
            "def_esp": 90,
            "vel": 90
        },
        "descripcion": "Forma guía: acompaña a las almas en su tránsito por el más allá.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Bola Sombra",
                "tipo": "Fantasma",
                "potencia": 80,
                "precision": 100,
                "categoria": "Especial",
                "pp": 15
            },
            {
                "nombre": "Psíquico",
                "tipo": "Psíquico",
                "potencia": 90,
                "precision": 100,
                "categoria": "Especial",
                "pp": 10
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 50,
                "movimiento": {
                    "nombre": "Psicocorte",
                    "tipo": "Psíquico",
                    "potencia": 120,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            },
            {
                "nivel": 60,
                "movimiento": {
                    "nombre": "Hiperrayo",
                    "tipo": "Normal",
                    "potencia": 150,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 3,
        "exp_base": 290,
        "grupo_huevo": "Desconocido"
    },
    "Zorro de las Nieves Altas": {
        "id": 92,
        "nombre": "Zorro de las Nieves Altas",
        "tipos": [
            "Hielo",
            "Siniestro"
        ],
        "categoria": "Zorro Glacial",
        "altura": 0.9,
        "peso": 28.0,
        "stats_base": {
            "ps": 75,
            "atq": 90,
            "def": 70,
            "atq_esp": 90,
            "def_esp": 70,
            "vel": 130
        },
        "descripcion": "Habita las cumbres más altas; su aullido congela el viento.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Rayo Hielo",
                "tipo": "Hielo",
                "potencia": 90,
                "precision": 100,
                "categoria": "Especial",
                "pp": 10
            },
            {
                "nombre": "Pulso Umbrío",
                "tipo": "Siniestro",
                "potencia": 80,
                "precision": 100,
                "categoria": "Especial",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 40,
                "movimiento": {
                    "nombre": "Psíquico",
                    "tipo": "Psíquico",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 50,
                "movimiento": {
                    "nombre": "Juego Sucio",
                    "tipo": "Siniestro",
                    "potencia": 95,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            },
            {
                "nivel": 60,
                "movimiento": {
                    "nombre": "Hiperrayo",
                    "tipo": "Normal",
                    "potencia": 150,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 3,
        "exp_base": 290,
        "grupo_huevo": "Desconocido"
    },
    "Aurum-Inca": {
        "id": 93,
        "nombre": "Aurum-Inca",
        "tipos": [
            "Acero",
            "Psíquico"
        ],
        "categoria": "Guerrero de Oro",
        "altura": 2.2,
        "peso": 180.0,
        "stats_base": {
            "ps": 90,
            "atq": 110,
            "def": 85,
            "atq_esp": 110,
            "def_esp": 85,
            "vel": 90
        },
        "descripcion": "Guerrero antiguo de oro puro que custodia los tesoros del sol.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Foco Resplandor",
                "tipo": "Acero",
                "potencia": 80,
                "precision": 100,
                "categoria": "Especial",
                "pp": 10
            },
            {
                "nombre": "Psíquico",
                "tipo": "Psíquico",
                "potencia": 90,
                "precision": 100,
                "categoria": "Especial",
                "pp": 10
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 50,
                "movimiento": {
                    "nombre": "Psicocorte",
                    "tipo": "Psíquico",
                    "potencia": 120,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            },
            {
                "nivel": 60,
                "movimiento": {
                    "nombre": "Hiperrayo",
                    "tipo": "Normal",
                    "potencia": 150,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 3,
        "exp_base": 290,
        "grupo_huevo": "Desconocido"
    },
    "Argentum-Moon": {
        "id": 94,
        "nombre": "Argentum-Moon",
        "tipos": [
            "Acero",
            "Hada"
        ],
        "categoria": "Guardián de Plata",
        "altura": 2.2,
        "peso": 180.0,
        "stats_base": {
            "ps": 95,
            "atq": 70,
            "def": 80,
            "atq_esp": 130,
            "def_esp": 95,
            "vel": 95
        },
        "descripcion": "Guardián de plata de los tesoros de la luna.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Foco Resplandor",
                "tipo": "Acero",
                "potencia": 80,
                "precision": 100,
                "categoria": "Especial",
                "pp": 10
            },
            {
                "nombre": "Fuerza Lunar",
                "tipo": "Hada",
                "potencia": 95,
                "precision": 100,
                "categoria": "Especial",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 40,
                "movimiento": {
                    "nombre": "Psíquico",
                    "tipo": "Psíquico",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 50,
                "movimiento": {
                    "nombre": "Voz Cautivadora",
                    "tipo": "Hada",
                    "potencia": 110,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            },
            {
                "nivel": 60,
                "movimiento": {
                    "nombre": "Hiperrayo",
                    "tipo": "Normal",
                    "potencia": 150,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 3,
        "exp_base": 290,
        "grupo_huevo": "Desconocido"
    },
    "Bronce-Tari": {
        "id": 95,
        "nombre": "Bronce-Tari",
        "tipos": [
            "Acero",
            "Lucha"
        ],
        "categoria": "Guardián de Bronce",
        "altura": 2.2,
        "peso": 180.0,
        "stats_base": {
            "ps": 95,
            "atq": 130,
            "def": 95,
            "atq_esp": 70,
            "def_esp": 80,
            "vel": 95
        },
        "descripcion": "Su armadura de bronce resiste incluso el fuego de los volcanes.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Foco Resplandor",
                "tipo": "Acero",
                "potencia": 80,
                "precision": 100,
                "categoria": "Especial",
                "pp": 10
            },
            {
                "nombre": "Puño Dinámico",
                "tipo": "Lucha",
                "potencia": 100,
                "precision": 50,
                "categoria": "Físico",
                "pp": 5
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 40,
                "movimiento": {
                    "nombre": "Psíquico",
                    "tipo": "Psíquico",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 50,
                "movimiento": {
                    "nombre": "A Bocajarro",
                    "tipo": "Lucha",
                    "potencia": 120,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 5
                }
            },
            {
                "nivel": 60,
                "movimiento": {
                    "nombre": "Hiperrayo",
                    "tipo": "Normal",
                    "potencia": 150,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 3,
        "exp_base": 290,
        "grupo_huevo": "Desconocido"
    },
    "Wayra-Wind": {
        "id": 96,
        "nombre": "Wayra-Wind",
        "tipos": [
            "Volador",
            "Eléctrico"
        ],
        "categoria": "Espíritu del Viento",
        "altura": 1.5,
        "peso": 70.0,
        "stats_base": {
            "ps": 80,
            "atq": 95,
            "def": 75,
            "atq_esp": 95,
            "def_esp": 75,
            "vel": 140
        },
        "descripcion": "Entidad atmosférica de viento que recorre la cordillera.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Tajo Aéreo",
                "tipo": "Volador",
                "potencia": 75,
                "precision": 95,
                "categoria": "Especial",
                "pp": 15
            },
            {
                "nombre": "Rayo",
                "tipo": "Eléctrico",
                "potencia": 90,
                "precision": 100,
                "categoria": "Especial",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 40,
                "movimiento": {
                    "nombre": "Psíquico",
                    "tipo": "Psíquico",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 50,
                "movimiento": {
                    "nombre": "Trueno",
                    "tipo": "Eléctrico",
                    "potencia": 110,
                    "precision": 70,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 60,
                "movimiento": {
                    "nombre": "Hiperrayo",
                    "tipo": "Normal",
                    "potencia": 150,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 3,
        "exp_base": 290,
        "grupo_huevo": "Desconocido"
    },
    "Paria-Rain": {
        "id": 97,
        "nombre": "Paria-Rain",
        "tipos": [
            "Agua",
            "Eléctrico"
        ],
        "categoria": "Espíritu de la Lluvia",
        "altura": 1.5,
        "peso": 70.0,
        "stats_base": {
            "ps": 95,
            "atq": 65,
            "def": 80,
            "atq_esp": 130,
            "def_esp": 95,
            "vel": 95
        },
        "descripcion": "Trae las tormentas que riegan las chacras de los Andes.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Cascada Andina",
                "tipo": "Agua",
                "potencia": 80,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            },
            {
                "nombre": "Rayo",
                "tipo": "Eléctrico",
                "potencia": 90,
                "precision": 100,
                "categoria": "Especial",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 40,
                "movimiento": {
                    "nombre": "Psíquico",
                    "tipo": "Psíquico",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 50,
                "movimiento": {
                    "nombre": "Trueno",
                    "tipo": "Eléctrico",
                    "potencia": 110,
                    "precision": 70,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 60,
                "movimiento": {
                    "nombre": "Hiperrayo",
                    "tipo": "Normal",
                    "potencia": 150,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 3,
        "exp_base": 290,
        "grupo_huevo": "Desconocido"
    },
    "Khamuy-Mist": {
        "id": 98,
        "nombre": "Khamuy-Mist",
        "tipos": [
            "Fantasma",
            "Veneno"
        ],
        "categoria": "Espíritu de la Neblina",
        "altura": 1.5,
        "peso": 70.0,
        "stats_base": {
            "ps": 95,
            "atq": 65,
            "def": 80,
            "atq_esp": 130,
            "def_esp": 95,
            "vel": 95
        },
        "descripcion": "Neblina viviente que desorienta a los viajeros de la ceja de selva.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Bola Sombra",
                "tipo": "Fantasma",
                "potencia": 80,
                "precision": 100,
                "categoria": "Especial",
                "pp": 15
            },
            {
                "nombre": "Bomba Lodo",
                "tipo": "Veneno",
                "potencia": 90,
                "precision": 100,
                "categoria": "Especial",
                "pp": 10
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 40,
                "movimiento": {
                    "nombre": "Psíquico",
                    "tipo": "Psíquico",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 50,
                "movimiento": {
                    "nombre": "Carga Tóxica",
                    "tipo": "Veneno",
                    "potencia": 120,
                    "precision": 85,
                    "categoria": "Físico",
                    "pp": 5
                }
            },
            {
                "nivel": 60,
                "movimiento": {
                    "nombre": "Hiperrayo",
                    "tipo": "Normal",
                    "potencia": 150,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 3,
        "exp_base": 290,
        "grupo_huevo": "Desconocido"
    },
    "Constelación Sur": {
        "id": 99,
        "nombre": "Constelación Sur",
        "tipos": [
            "Psíquico",
            "Normal"
        ],
        "categoria": "Estrella Viva",
        "altura": 2.2,
        "peso": 180.0,
        "stats_base": {
            "ps": 100,
            "atq": 70,
            "def": 85,
            "atq_esp": 135,
            "def_esp": 100,
            "vel": 100
        },
        "descripcion": "Constelación que bajó a la tierra para observar a los humanos.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Psíquico",
                "tipo": "Psíquico",
                "potencia": 90,
                "precision": 100,
                "categoria": "Especial",
                "pp": 10
            },
            {
                "nombre": "Golpe Cuerpo",
                "tipo": "Normal",
                "potencia": 85,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 50,
                "movimiento": {
                    "nombre": "Hiperrayo",
                    "tipo": "Normal",
                    "potencia": 150,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 3,
        "exp_base": 290,
        "grupo_huevo": "Desconocido"
    },
    "Apu-Cerro": {
        "id": 100,
        "nombre": "Apu-Cerro",
        "tipos": [
            "Roca",
            "Tierra"
        ],
        "categoria": "Montaña Viva",
        "altura": 3.5,
        "peso": 420.0,
        "stats_base": {
            "ps": 125,
            "atq": 90,
            "def": 130,
            "atq_esp": 70,
            "def_esp": 120,
            "vel": 60
        },
        "descripcion": "El espíritu de una montaña sagrada.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Roca Afilada",
                "tipo": "Roca",
                "potencia": 100,
                "precision": 80,
                "categoria": "Físico",
                "pp": 5
            },
            {
                "nombre": "Terremoto",
                "tipo": "Tierra",
                "potencia": 100,
                "precision": 100,
                "categoria": "Físico",
                "pp": 10
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 40,
                "movimiento": {
                    "nombre": "Psíquico",
                    "tipo": "Psíquico",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 50,
                "movimiento": {
                    "nombre": "Fisura",
                    "tipo": "Tierra",
                    "potencia": 120,
                    "precision": 80,
                    "categoria": "Físico",
                    "pp": 5
                }
            },
            {
                "nivel": 60,
                "movimiento": {
                    "nombre": "Hiperrayo",
                    "tipo": "Normal",
                    "potencia": 150,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 3,
        "exp_base": 290,
        "grupo_huevo": "Desconocido"
    },
    "Lago-Sagu": {
        "id": 101,
        "nombre": "Lago-Sagu",
        "tipos": [
            "Agua",
            "Hada"
        ],
        "categoria": "Espíritu del Lago",
        "altura": 3.5,
        "peso": 420.0,
        "stats_base": {
            "ps": 100,
            "atq": 70,
            "def": 85,
            "atq_esp": 135,
            "def_esp": 100,
            "vel": 100
        },
        "descripcion": "El espíritu del lago sagrado, que vive en las islas flotantes.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Cascada Andina",
                "tipo": "Agua",
                "potencia": 80,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            },
            {
                "nombre": "Fuerza Lunar",
                "tipo": "Hada",
                "potencia": 95,
                "precision": 100,
                "categoria": "Especial",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 40,
                "movimiento": {
                    "nombre": "Psíquico",
                    "tipo": "Psíquico",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 50,
                "movimiento": {
                    "nombre": "Voz Cautivadora",
                    "tipo": "Hada",
                    "potencia": 110,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            },
            {
                "nivel": 60,
                "movimiento": {
                    "nombre": "Hiperrayo",
                    "tipo": "Normal",
                    "potencia": 150,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 3,
        "exp_base": 290,
        "grupo_huevo": "Desconocido"
    },
    "Chask-Messenger": {
        "id": 102,
        "nombre": "Chask-Messenger",
        "tipos": [
            "Normal",
            "Volador"
        ],
        "categoria": "Mensajero Estelar",
        "altura": 1.5,
        "peso": 70.0,
        "stats_base": {
            "ps": 85,
            "atq": 100,
            "def": 80,
            "atq_esp": 100,
            "def_esp": 80,
            "vel": 145
        },
        "descripcion": "Mensajero de los dioses: cruza el cielo como una estrella fugaz.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Golpe Cuerpo",
                "tipo": "Normal",
                "potencia": 85,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            },
            {
                "nombre": "Tajo Aéreo",
                "tipo": "Volador",
                "potencia": 75,
                "precision": 95,
                "categoria": "Especial",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 40,
                "movimiento": {
                    "nombre": "Psíquico",
                    "tipo": "Psíquico",
                    "potencia": 90,
                    "precision": 100,
                    "categoria": "Especial",
                    "pp": 10
                }
            },
            {
                "nivel": 50,
                "movimiento": {
                    "nombre": "Pájaro Osado",
                    "tipo": "Volador",
                    "potencia": 120,
                    "precision": 100,
                    "categoria": "Físico",
                    "pp": 15
                }
            },
            {
                "nivel": 60,
                "movimiento": {
                    "nombre": "Hiperrayo",
                    "tipo": "Normal",
                    "potencia": 150,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 3,
        "exp_base": 290,
        "grupo_huevo": "Desconocido"
    },
    "Omega-Inca": {
        "id": 103,
        "nombre": "Omega-Inca",
        "tipos": [
            "Psíquico"
        ],
        "categoria": "Origen de Todo",
        "altura": 3.5,
        "peso": 420.0,
        "stats_base": {
            "ps": 120,
            "atq": 120,
            "def": 120,
            "atq_esp": 120,
            "def_esp": 120,
            "vel": 120
        },
        "descripcion": "Núcleo del cual brotó toda la vida y la energía de los Pokémon.",
        "evolucion": None,
        "movimientos_iniciales": [
            {
                "nombre": "Psíquico",
                "tipo": "Psíquico",
                "potencia": 90,
                "precision": 100,
                "categoria": "Especial",
                "pp": 10
            },
            {
                "nombre": "Golpe Cuerpo",
                "tipo": "Normal",
                "potencia": 85,
                "precision": 100,
                "categoria": "Físico",
                "pp": 15
            }
        ],
        "aprendizajes_por_nivel": [
            {
                "nivel": 30,
                "movimiento": {
                    "nombre": "Psicocorte",
                    "tipo": "Psíquico",
                    "potencia": 120,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            },
            {
                "nivel": 50,
                "movimiento": {
                    "nombre": "Hiperrayo",
                    "tipo": "Normal",
                    "potencia": 150,
                    "precision": 90,
                    "categoria": "Especial",
                    "pp": 5
                }
            }
        ],
        "tasa_captura": 3,
        "exp_base": 330,
        "grupo_huevo": "Desconocido"
    }
}