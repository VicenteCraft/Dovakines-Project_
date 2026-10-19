from datos.conexion import base_datos
from peewee import Model, AutoField, CharField, IntegerField, DateField, TextField

database = base_datos()

class BaseModel(Model):
    class Meta:
        database = database

class Instructor(BaseModel):
    id_instructor = AutoField()
    nombre = CharField(max_length=100,null=True)
    pseudonimo = CharField(max_length=25,null=True)
    pais = IntegerField(index=True,null=True)
    fecha_nacimiento = DateField(null=True)
    fecha_ingreso = DateField(null=True)
    biografia = TextField(null=True)
    habilitado = IntegerField(default=1)

    class Meta:
        table_name = 'instructores'
