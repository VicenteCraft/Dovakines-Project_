from decouple import config
from peewee import MySQLDatabase


def _valor(clave, por_defecto=None):
    """Lee una variable del .env y le quita comillas o comas de más.

    Así, aunque quede algo como  user='Dovakinesproject',  el programa
    igual entiende que el usuario es:  Dovakinesproject
    """
    valor = config(clave, default=por_defecto)
    if valor is None:
        return None
    return valor.strip().rstrip(",").strip().strip("'\"").strip()


def conectar_db():
    """Crea y retorna la conexión con MySQL (peewee conecta recién al primer uso)."""
    return MySQLDatabase(
        _valor("db"),
        host=_valor("host"),
        port=int(_valor("port", "3306")),
        user=_valor("user"),
        password=_valor("password", ""),
        charset="utf8mb4",
    )
