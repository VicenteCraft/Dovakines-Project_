from peewee import AutoField, CharField, ForeignKeyField

from datos.modelo_base import BaseModel
from datos.modelos.direccion import Direccion


class Biblioteca(BaseModel):
    id_biblioteca = AutoField()
    nombre = CharField(max_length=30)
    correo = CharField(null=True)
    telefono = CharField(max_length=20, null=True)
    web = CharField(null=True)
    direccion = ForeignKeyField(Direccion)

    class Meta:
        table_name = 'bibliotecas'
