from peewee import AutoField, CharField

from datos.modelo_base import BaseModel


class Pais(BaseModel):
    id_pais = AutoField()
    nombre = CharField(max_length=60)
    nacionalidad = CharField(max_length=30)
    iso_2 = CharField(max_length=2, null=True)
    iso_3 = CharField(max_length=3, null=True)

    class Meta:
        table_name = 'paises'
