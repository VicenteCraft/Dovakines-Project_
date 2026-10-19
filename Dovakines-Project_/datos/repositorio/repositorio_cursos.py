from datos.conexion import base_datos
from datos.modelos.curso import Curso
from datos.modelos.instructor import Instructor

database = base_datos()

def listado_cursos():
    cursos = Curso.select(Curso, Instructor).join(Instructor)
    return cursos

def guardar_curso(curso: Curso):
    curso.save()
    return curso
