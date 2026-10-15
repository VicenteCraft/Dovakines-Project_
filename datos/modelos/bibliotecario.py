from peewee import AutoField, CharField, IntegerField, SQL

from datos.modelo_base import BaseModel

defecto = "DEFAULT 1"


class Bibliotecario(BaseModel):
    id_bibliotecario = AutoField()
    usuario = IntegerField(index=True)
    contrasena = CharField(max_length=60)
    tipo_usuario = IntegerField(index=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'bibliotecarios'
