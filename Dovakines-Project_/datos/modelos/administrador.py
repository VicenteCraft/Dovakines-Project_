from datos.conexion import base_datos
from peewee import Model, AutoField, CharField, IntegerField, SQL

database = base_datos()
defecto = "DEFAULT 1"

class BaseModel(Model):
    class Meta:
        database = database

class Administrador(BaseModel):
    id_administrador = AutoField()
    usuario = IntegerField(index=True)
    contrasena = CharField(max_length=60)
    tipo_usuario = IntegerField(index=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'administradores'
.