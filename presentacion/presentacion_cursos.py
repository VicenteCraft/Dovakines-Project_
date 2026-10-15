"""Funciones que muestran informacion en pantalla (solo presentacion, sin reglas)."""

from prettytable import PrettyTable


def mostrar_cursos(cursos):
    """Lista los cursos en una tabla."""
    tabla = PrettyTable()
    tabla.field_names = ["ID", "Titulo", "Descripcion", "Estado"]
    for curso in cursos:
        estado = "activo" if curso.esta_activo else "inactivo"
        tabla.add_row([curso.id_curso, curso.titulo, curso.descripcion, estado])
    print(tabla)
    if not cursos:
        print("   No hay cursos para mostrar.")


def mostrar_detalle(curso):
    """Muestra un curso en particular, con sus estadisticas (metodo del UML)."""
    print(f"   ID:          {curso.id_curso}")
    print(f"   Titulo:      {curso.titulo}")
    print(f"   Descripcion: {curso.descripcion}")
    print(f"   Estado:      {'activo' if curso.esta_activo else 'inactivo'}")
    print(f"   Estadisticas: {curso.obtener_estadisticas()}")


def mostrar_inscripciones(curso, inscripciones):
    """Muestra las inscripciones de un curso."""
    tabla = PrettyTable()
    tabla.field_names = ["Matricula", "Estudiante", "Avance %", "Estado"]
    for inscripcion in inscripciones:
        tabla.add_row([
            inscripcion.estudiante.matricula,
            inscripcion.estudiante.nombre,
            inscripcion.calcular_avance(),   # UML: calcularAvance()
            inscripcion.estado,
        ])
    print(tabla)
    print(f"   Estadisticas: {curso.obtener_estadisticas()}")
    if not inscripciones:
        print("   El curso aun no tiene inscripciones.")
