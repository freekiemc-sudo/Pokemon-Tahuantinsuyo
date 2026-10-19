"""
Sistema de misiones secundarias
"""


class Mision:
    def __init__(self, mid, nombre, descripcion, npc_origen, objetivo,
                 cantidad=1, recompensa_dinero=0, recompensa_objeto=None, cantidad_obj=1):
        self.id = mid
        self.nombre = nombre
        self.descripcion = descripcion
        self.npc_origen = npc_origen
        self.objetivo = objetivo
        self.cantidad = cantidad
        self.recompensa_dinero = recompensa_dinero
        self.recompensa_objeto = recompensa_objeto
        self.cantidad_obj = cantidad_obj
        self.estado = "disponible"
        self.progreso = 0

    def aceptar(self):
        if self.estado == "disponible":
            self.estado = "activa"; return True
        return False

    def avanzar(self, n=1):
        if self.estado == "activa":
            self.progreso += n
            if self.progreso >= self.cantidad:
                self.estado = "completada"
                return True
        return False

    def reclamar(self, jugador):
        if self.estado != "completada": return False
        jugador.inventario.dinero += self.recompensa_dinero
        if self.recompensa_objeto:
            try:
                from sistemas.inventario import CURACIONES, POKEBALLS, BATALLA, REVIVIRES, EVOLUCION, OBJETOS_CLAVE
                cat = {}
                for d in (CURACIONES, POKEBALLS, BATALLA, REVIVIRES, EVOLUCION, OBJETOS_CLAVE):
                    cat.update(d)
                if self.recompensa_objeto in cat:
                    jugador.inventario.agregar(cat[self.recompensa_objeto], self.cantidad_obj)
            except Exception:
                pass
        self.estado = "reclamada"
        return True


MISIONES_INICIALES = [
    Mision("m1_cuy", "Plaga de Cuyes",
           "Captura 3 cuyes para el granjero Ramón de la Caleta.",
           "Granjero Ramón", "capturar_cuy", cantidad=3,
           recompensa_dinero=400, recompensa_objeto="Pocion", cantidad_obj=3),
    Mision("m2_quipu", "Mensaje del Chasqui",
           "Lleva el quipu de la alcaldesa al Profesor Kuntur.",
           "Alcaldesa de la Caleta", "entregar_quipu", cantidad=1,
           recompensa_dinero=600, recompensa_objeto="Freekie Ball", cantidad_obj=5),
    Mision("m3_huaca", "Ruidos en la Huaca",
           "Investiga los ruidos extraños al este de Ciudad Moche.",
           "Curaca de Moche", "investigar_huaca", cantidad=1,
           recompensa_dinero=800, recompensa_objeto="Super Ball", cantidad_obj=3),
]


class SistemaMisiones:
    def __init__(self):
        self.misiones = {m.id: Mision(m.id, m.nombre, m.descripcion,
                                       m.npc_origen, m.objetivo, m.cantidad,
                                       m.recompensa_dinero, m.recompensa_objeto,
                                       m.cantidad_obj)
                         for m in MISIONES_INICIALES}
    def obtener(self, mid): return self.misiones.get(mid)
    def disponibles(self): return [m for m in self.misiones.values() if m.estado == "disponible"]
    def activas(self):     return [m for m in self.misiones.values() if m.estado == "activa"]
    def completadas(self): return [m for m in self.misiones.values() if m.estado == "completada"]
    def aceptar(self, mid):
        m = self.obtener(mid)
        return m.aceptar() if m else False
    def avanzar_objetivo(self, objetivo, n=1):
        for m in self.activas():
            if m.objetivo == objetivo: m.avanzar(n)
    def reclamar(self, mid, jugador):
        m = self.obtener(mid)
        return m.reclamar(jugador) if m else False