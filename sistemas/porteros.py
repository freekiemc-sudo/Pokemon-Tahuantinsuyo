# sistemas/porteros.py
"""Sistema de porteros y eventos obligatorios del Team Supay."""
try:
    from data.porteros import obtener_portero, PORTEROS
    from data.eventos_supay import obtener_evento, EVENTOS_SUPAY
except Exception:
    PORTEROS = {}
    EVENTOS_SUPAY = {}
    def obtener_portero(g): return None
    def obtener_evento(c): return None


def gimnasio_bloqueado(gimnasio_id):
    """Devuelve (bloqueado, motivo). Bloqueado si el portero o el evento siguen pendientes."""
    ciudad_evento = None
    for cid, ev in EVENTOS_SUPAY.items():
        if ev.desbloquea_gimnasio == gimnasio_id and not ev.completado:
            ciudad_evento = cid
            return True, f"El Team Supay anda suelto en {cid.replace('_',' ').title()}"
    portero = obtener_portero(gimnasio_id)
    if portero and not portero.derrotado:
        return True, f"{portero.nombre} bloquea la entrada al gimnasio."
    return False, ""


def evento_supay_activo(ciudad_id):
    ev = obtener_evento(ciudad_id)
    if ev and not ev.completado:
        return ev
    return None


def marcar_evento_completado(ciudad_id):
    ev = obtener_evento(ciudad_id)
    if ev:
        ev.completado = True
    return ev