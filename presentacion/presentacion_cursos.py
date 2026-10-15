from prettytable import PrettyTable

from negocio import negocio_cursos as negocio


def mostrar_cursos():
    cursos = negocio.cargar_cursos()
    tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre", "Descripción"]

    for curso in cursos:
        tabla.add_row([curso.id, curso.nombre, curso.descripcion])

    print(tabla)


def datos_curso(curso_id):
    curso = negocio.buscar_curso(curso_id)
    if curso:
        print(f"ID: {curso.id}")
        print(f"Nombre: {curso.nombre}")
        print(f"Descripción: {curso.descripcion}")
        print(f"Inicio: {curso.fecha_inicio}")
        print(f"Fin: {curso.fecha_fin}")
    else:
        print("Curso no encontrado.")


def buscar_curso_nombre(nombre):
    cursos = negocio.cargar_cursos()
    for curso in cursos:
        if curso.nombre.lower() == nombre.lower():
            return curso
    return None


def crear_nuevo_curso(nombre, descripcion):
    nuevo_curso = negocio.crear_curso(nombre, descripcion)
    print(f"Curso '{nuevo_curso.nombre}' creado con éxito con ID: {nuevo_curso.id}")


def actualizar_curso(curso_id, nuevo_nombre, nueva_descripcion):
    curso = negocio.actualizar_curso(curso_id, nuevo_nombre, nueva_descripcion)
    if curso:
        print(f"Curso con ID {curso_id} actualizado con éxito.")
    else:
        print("Curso no encontrado.")


def eliminar_curso(curso_id):
    curso = negocio.eliminar_curso(curso_id)
    if curso:
        print(f"Curso con ID {curso_id} eliminado con éxito.")
    else:
        print("Curso no encontrado.")
