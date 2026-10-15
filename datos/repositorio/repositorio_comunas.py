from datos.modelos.comuna import Comuna


def listado_comunas():
    """Devuelve todas las comunas ordenadas por id."""
    return list(Comuna.select().order_by(Comuna.id_comuna))


def guardar_comuna(comuna):
    """Guarda la comuna y devuelve la cantidad de filas afectadas (1 = ok)."""
    return comuna.save()


def comuna_por_nombre(nombre):
    """Devuelve las comunas cuyo nombre contenga el texto recibido."""
    return list(Comuna.select().where(Comuna.comuna.contains(nombre)))
