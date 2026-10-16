from datos.repositorio.repositorio_cursos import listado_cursos,guardar_curso
from prettytable import PrettyTable
from datos.modelos.curso import Curso

def cargar_cursos(tabla: PrettyTable):
    cursos = listado_cursos()
    tabla.field_names = ['Id','Título','Instructor','Horas']

    if cursos:
        for curso in cursos:
            tabla.add_row([curso.id_curso, curso.titulo, curso.instructor.nombre, curso.horas])

    return tabla

def crear_curso(titulo,horas,instructor):
    nuevo_curso = Curso()
    nuevo_curso.titulo = titulo
    nuevo_curso.horas = horas
    nuevo_curso.instructor = instructor
    curso = guardar_curso(nuevo_curso)
    print(f'Se ha guardado el curso {curso.titulo}')
