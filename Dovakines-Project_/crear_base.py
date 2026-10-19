"""Crea la base de datos, las tablas (esquema.sql) y datos de ejemplo.

Uso:  python crear_base.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from decouple import UndefinedValueError
from mysql.connector import Error

from datos import conexion


def main():
    # 1) Probar la conexion (manejo de errores del Paso 4)
    try:
        print("Conectando a MySQL... ", end="")
        version = conexion.probar_conexion()
        print(f"OK (servidor MySQL {version})")
    except UndefinedValueError:
        print("\nERROR: falta una variable en el archivo .env (host, port, user, password o db).")
        sys.exit(1)
    except Error as error:
        print("\nERROR: no se pudo conectar a MySQL.")
        print(f"Detalle: {error}")
        print("Revisa que WAMP/MySQL este activo y que el archivo .env tenga los datos correctos.")
        sys.exit(1)

    # 2) Crear las tablas del esquema derivado del UML
    ruta_sql = os.path.join(os.path.dirname(os.path.abspath(__file__)), "datos", "sql", "esquema.sql")
    with open(ruta_sql, encoding="utf-8") as archivo:
        sentencias = [s.strip() for s in archivo.read().split(";") if s.strip()]

    try:
        for sentencia in sentencias:
            conexion.ejecutar(sentencia)
        print(f"Tablas creadas/verificadas: {len(sentencias)}")
    except Error as error:
        print(f"\nERROR al crear las tablas: {error}")
        sys.exit(1)

    # 3) Datos de ejemplo (solo si la base esta vacia)
    if conexion.consultar("SELECT COUNT(*) AS total FROM usuario")[0]["total"] == 0:
        id_ana = conexion.ejecutar(
            "INSERT INTO usuario (nombre, correo, contrasena) VALUES (%s, %s, %s)",
            ("Ana Perez", "ana@demo.cl", "1234"),
        )
        conexion.ejecutar(
            "INSERT INTO estudiante (id_usuario, matricula) VALUES (%s, %s)",
            (id_ana, "2026-001"),
        )
        id_profesor = conexion.ejecutar(
            "INSERT INTO usuario (nombre, correo, contrasena) VALUES (%s, %s, %s)",
            ("Luis Soto", "profe@demo.cl", "1234"),
        )
        conexion.ejecutar(
            "INSERT INTO profesor (id_usuario, especialidad) VALUES (%s, %s)",
            (id_profesor, "Programacion"),
        )
        conexion.ejecutar(
            "INSERT INTO curso (titulo, descripcion, esta_activo, id_profesor) VALUES (%s, %s, TRUE, %s)",
            ("Curso de Python", "Curso basico de Python", id_profesor),
        )
        print("Datos de ejemplo creados: ana@demo.cl / 1234 y profe@demo.cl / 1234")
    else:
        print("La base ya contiene datos: no se crearon datos de ejemplo.")

    conexion.cerrar_conexion()
    print("Listo. Ahora puedes ejecutar:  python main.py")


if __name__ == "__main__":
    main()
