import sys

from datos import nombre_app, version_app, main_menu
from presentacion.presentacion_cursos import (
    actualizar_curso,
    crear_nuevo_curso,
    datos_curso,
    eliminar_curso,
    mostrar_cursos,
)

titulo = "Dovakinesapp y su fabulosa gestión de cursos ^^"

opciones_gestion = {
    "1": "Crear un curso",
    "2": "Ver detalle de un curso",
    "3": "Actualizar un curso",
    "4": "Eliminar un curso",
    "5": "Volver al menú principal",
}


def ejecutar(funcion, *argumentos):
    """Ejecuta una operación evitando que un error de base de datos rompa el menú."""
    try:
        return funcion(*argumentos)
    except Exception as error:
        print(f"Error de base de datos: {error}")
        return None


def pedir_id():
    """Lee un id desde teclado; devuelve None si no es un número."""
    try:
        return int(input("Ingrese el ID del curso: ").strip())
    except ValueError:
        print("El ID debe ser un número.")
        return None


def gestionar_cursos():
    while True:
        print()
        print(titulo)
        for clave, valor in opciones_gestion.items():
            print(f"{clave}. {valor}")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre del curso: ").strip()
            descripcion = input("Descripción del curso: ").strip()
            if not nombre:
                print("El nombre del curso no puede estar vacío.")
                continue
            ejecutar(crear_nuevo_curso, nombre, descripcion)
        elif opcion == "2":
            curso_id = pedir_id()
            if curso_id is not None:
                ejecutar(datos_curso, curso_id)
        elif opcion == "3":
            curso_id = pedir_id()
            if curso_id is not None:
                nuevo_nombre = input("Nuevo nombre: ").strip()
                nueva_descripcion = input("Nueva descripción: ").strip()
                ejecutar(actualizar_curso, curso_id, nuevo_nombre, nueva_descripcion)
        elif opcion == "4":
            curso_id = pedir_id()
            if curso_id is not None:
                ejecutar(eliminar_curso, curso_id)
        elif opcion == "5":
            return
        else:
            print("Opción no válida. Por favor, seleccione una opción que sea válida.")


def menu_principal():
    print(f"{nombre_app} - {version_app}")
    print("=" * len(f"{nombre_app} - {version_app}"))

    while True:
        print()
        for clave, valor in main_menu.items():
            print(f"{clave}. {valor}")

        opcion_usuario = input("Seleccione una opción: ").strip()

        if opcion_usuario == "1":
            print("Iniciando gestión de cursos...")
            gestionar_cursos()
        elif opcion_usuario == "2":
            print("Mostrando cursos disponibles...")
            ejecutar(mostrar_cursos)
        elif opcion_usuario == "3":
            print("Saliendo de la aplicación...")
            sys.exit()
        else:
            print("Opción no válida. Por favor, seleccione una opción que sea válida.")
