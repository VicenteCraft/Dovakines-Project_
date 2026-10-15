"""Conexion a MySQL usando la libreria oficial mysql-connector-python.

Los parametros (host, puerto, usuario, contrasena y base) se leen del archivo .env
con python-decouple, para no dejar credenciales dentro del codigo fuente.
"""

import mysql.connector
from decouple import UndefinedValueError, config
from mysql.connector import Error


def _valor(clave, por_defecto=None):
    """Lee una variable del .env y le quita comillas o comas de mas."""
    valor = config(clave, default=por_defecto)
    if valor is None:
        return None
    return valor.strip().rstrip(",").strip().strip("'\"").strip()


_conexion = None


def obtener_conexion():
    """Devuelve la conexion a MySQL (se abre una sola vez y se reutiliza)."""
    global _conexion
    if _conexion is None or not _conexion.is_connected():
        _conexion = mysql.connector.connect(
            host=_valor("host"),
            port=int(_valor("port", "3306")),
            user=_valor("user"),
            password=_valor("password"),
            database=_valor("db"),
            charset="utf8mb4",
        )
    return _conexion


def consultar(sql, parametros=()):
    """Ejecuta una consulta SELECT y devuelve una lista de diccionarios.

    Los parametros se envian separados (%s) y nunca se concatenan al texto SQL,
    lo que evita la inyeccion SQL.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    try:
        cursor.execute(sql, parametros)
        return cursor.fetchall()
    finally:
        cursor.close()


def ejecutar(sql, parametros=()):
    """Ejecuta INSERT/UPDATE/DELETE, confirma los cambios y devuelve el id creado."""
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        cursor.execute(sql, parametros)
        conexion.commit()
        return cursor.lastrowid
    except Error:
        conexion.rollback()
        raise
    finally:
        cursor.close()


def probar_conexion():
    """Intenta abrir la conexion y devuelve el servidor consultado."""
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT VERSION()")
        return cursor.fetchone()[0]
    finally:
        cursor.close()


def cerrar_conexion():
    """Cierra la conexion si esta abierta."""
    global _conexion
    if _conexion is not None and _conexion.is_connected():
        _conexion.close()
    _conexion = None
