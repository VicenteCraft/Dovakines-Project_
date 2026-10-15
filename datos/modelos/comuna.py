from peewee import AutoField, CharField, IntegerField

from datos.modelo_base import BaseModel


class Comuna(BaseModel):
    id_comuna = AutoField()
    codigo_comuna = CharField(max_length=5)
    comuna = CharField(max_length=60)

    class Meta:
        table_name = 'comunas'
