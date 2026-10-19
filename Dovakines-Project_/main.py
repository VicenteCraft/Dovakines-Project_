"""Punto de entrada de la aplicacion: gestiona la conexion y el menu principal."""

import sys

from decouple import UndefinedValueError
from mysql.connector import Error

from datos.conexion import cerrar_conexion, probar_conexion
from presentacion import menu_principal


def main():
    # 1) Probar la conexion a la base de datos antes de mostrar el menu
    try:
        version = probar_conexion()
        print(f"Conexion a MySQL establecida (servidor {version}).")
    except UndefinedValueError:
        print("ERROR DE CONFIGURACION: falta una variable en el archivo .env.")
        print("Debe existir: host, port, user, password y db.")
        sys.exit(1)
    except Error as error:
        print("ERROR DE CONEXION: no se pudo conectar a la base de datos.")
        print(f"Detalle: {error}")
        print("Verifica que WAMP/MySQL este activo y que exista la base de datos")
        print("(ejecuta: python crear_base.py).")
        sys.exit(1)

    # 2) Ejecutar el menu; si el usuario cierra la terminal, salir sin error
    try:
        menu_principal()
    except (EOFError, KeyboardInterrupt):
        print("\nHasta luego.")
    finally:
        cerrar_conexion()


if __name__ == "__main__":
    main()
