from datos.conexion import base_datos
from datos.modelos.direccion import Direccion
from peewee import Model, AutoField, CharField, IntegerField, ForeignKeyField

database = base_datos()

class BaseModel(Model):
    class Meta:
        database = database

class Escuela(BaseModel):
    id_escuela = AutoField()
    nombre = CharField(max_length=100)
    correo = CharField(null=True)
    telefono = CharField(max_length=15,null=True)
    web = CharField(null=True)
    direccion = ForeignKeyField(Direccion, column_name='direccion', null=True)

    class Meta:
        table_name = 'escuelas'
