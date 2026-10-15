"""Menu principal de la aplicacion.

En cada operacion se usan bloques try-except (Paso 4 de la pauta):
 - ValueError  -> errores de validacion lanzados por la capa de negocio.
 - Error       -> errores de la base de datos (mysql.connector).
 - EOFError / KeyboardInterrupt -> cierre de la terminal o Ctrl+C.
"""

import sys

from mysql.connector import Error

from datos import main_menu, menu_gestion, menu_inscripciones, nombre_app, version_app
from negocio import negocio_cursos as negocio
from presentacion import presentacion_cursos as pantalla
from presentacion.validaciones import pedir_contrasena, pedir_correo, pedir_entero, pedir_texto


def imprimir_menu(opciones):
    print()
    for clave, valor in opciones.items():
        print(f" {clave}. {valor}")


def gestionar_cursos():
    while True:
        imprimir_menu(menu_gestion)
        opcion = input(" Seleccione una opcion: ").strip()

        try:
            if opcion == "1":
                titulo = pedir_texto("  Titulo del curso: ")
                descripcion = pedir_texto("  Descripcion: ", maximo=200)
                id_profesor = pedir_entero(
                    "  Id del profesor (Enter si no aplica): ",
                    minimo=1, vacio_permitido=True,
                )
                curso = negocio.crear_curso(titulo, descripcion, id_profesor)
                print(f"  Curso '{curso.titulo}' creado con id {curso.id_curso}.")

            elif opcion == "2":
                id_curso = pedir_entero("  Id del curso: ")
                curso = negocio.buscar_curso(id_curso)
                if curso is None:
                    print(f"  No existe un curso con id {id_curso}.")
                else:
                    pantalla.mostrar_detalle(curso)

            elif opcion == "3":
                id_curso = pedir_entero("  Id del curso: ")
                titulo = pedir_texto("  Nuevo titulo: ")
                descripcion = pedir_texto("  Nueva descripcion: ", maximo=200)
                curso = negocio.actualizar_curso(id_curso, titulo, descripcion)
                print(f"  Curso id {curso.id_curso} actualizado.")

            elif opcion == "4":
                id_curso = pedir_entero("  Id del curso: ")
                if negocio.eliminar_curso(id_curso):
                    print(f"  Curso id {id_curso} eliminado (desactivado).")
                else:
                    print(f"  No existe un curso con id {id_curso}.")

            elif opcion == "5":
                return

            else:
                print("  Opcion no valida.")

        except ValueError as error:          # validaciones de la capa de negocio
            print(f"  Error de validacion: {error}")
        except Error as error:               # errores de la base de datos
            print(f"  Error de base de datos: {error}")


def gestionar_inscripciones():
    while True:
        imprimir_menu(menu_inscripciones)
        opcion = input(" Seleccione una opcion: ").strip()

        try:
            if opcion == "1":
                nombre = pedir_texto("  Nombre: ")
                correo = pedir_correo("  Correo: ")
                contrasena = pedir_contrasena("  Contrasena (min. 4): ")
                matricula = pedir_texto("  Matricula: ")
                estudiante = negocio.registrar_estudiante(
                    nombre, correo, contrasena, matricula
                )
                print(f"  Estudiante '{estudiante.nombre}' registrado "
                      f"con matricula {estudiante.matricula}.")

            elif opcion == "2":
                matricula = pedir_texto("  Matricula del estudiante: ")
                id_curso = pedir_entero("  Id del curso: ")
                inscripcion = negocio.inscribir_estudiante(matricula, id_curso)
                print(f"  Inscripcion registrada: {inscripcion}")

            elif opcion == "3":
                id_curso = pedir_entero("  Id del curso: ")
                curso = negocio.inscripciones_de_curso(id_curso)
                print(f"  Curso: {curso.titulo}")
                pantalla.mostrar_inscripciones(curso, curso.inscripciones)

            elif opcion == "4":
                return

            else:
                print("  Opcion no valida.")

        except ValueError as error:
            print(f"  Error de validacion: {error}")
        except Error as error:
            print(f"  Error de base de datos: {error}")


def menu_principal():
    print(f"{nombre_app} - {version_app}")
    print("=" * len(f"{nombre_app} - {version_app}"))
    print("Plataforma de gestion de cursos online")

    while True:
        imprimir_menu(main_menu)
        opcion = input(" Seleccione una opcion: ").strip()

        try:
            if opcion == "1":
                pantalla.mostrar_cursos(negocio.cargar_cursos())

            elif opcion == "2":
                gestionar_cursos()

            elif opcion == "3":
                gestionar_inscripciones()

            elif opcion == "4":
                correo = pedir_correo("  Correo: ")
                contrasena = pedir_contrasena("  Contrasena (min. 4): ")
                usuario = negocio.iniciar_sesion(correo, contrasena)
                print(f"  Bienvenido(a), {usuario.nombre}! "
                      f"({type(usuario).__name__})")

            elif opcion == "5":
                print(" Saliendo de la aplicacion...")
                sys.exit()

            else:
                print("  Opcion no valida.")

        except ValueError as error:
            print(f"  Error de validacion: {error}")
        except Error as error:
            print(f"  Error de base de datos: {error}")
        except (EOFError, KeyboardInterrupt):
            print("\n Hasta luego.")
            sys.exit()
