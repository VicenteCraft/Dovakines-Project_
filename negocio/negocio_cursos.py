from datetime import date

from datos.models import Curso
from datos.repositorio.repositorio_cursos import curso_por_id, guardar_curso, listado_cursos


def cargar_cursos():
    """Devuelve los cursos activos de la plataforma."""
    return listado_cursos()


def crear_curso(nombre, descripcion, fecha_inicio=None, fecha_fin=None):
    """Crea un curso con fechas por defecto (hoy) si no se indican."""
    hoy = date.today()
    curso = Curso()
    curso.nombre = nombre
    curso.descripcion = descripcion
    curso.fecha_inicio = fecha_inicio or hoy
    curso.fecha_fin = fecha_fin or hoy
    guardar_curso(curso)
    return curso


def buscar_curso(curso_id):
    """Devuelve el curso con ese id o None si no existe."""
    return curso_por_id(curso_id)


def actualizar_curso(curso_id, nuevo_nombre, nueva_descripcion):
    """Actualiza nombre y descripción. Devuelve el curso o None si no existe."""
    curso = curso_por_id(curso_id)
    if curso is None:
        return None
    curso.nombre = nuevo_nombre
    curso.descripcion = nueva_descripcion
    guardar_curso(curso)
    return curso


def eliminar_curso(curso_id):
    """Eliminación lógica: marca el curso como inactivo (estado = 0)."""
    curso = curso_por_id(curso_id)
    if curso is None:
        return None
    curso.estado = 0
    guardar_curso(curso)
    return curso
