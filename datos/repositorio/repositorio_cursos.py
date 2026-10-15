from datos.models import Curso


def listado_cursos():
    """Devuelve la lista de cursos activos (estado = 1)."""
    return list(Curso.select().where(Curso.estado == 1).order_by(Curso.id))


def curso_por_id(curso_id):
    """Devuelve el curso con ese id o None si no existe."""
    try:
        return Curso.get(Curso.id == curso_id)
    except Curso.DoesNotExist:
        return None


def guardar_curso(curso):
    """Inserta el curso si es nuevo o lo actualiza si ya existía."""
    curso.save()
    return curso
