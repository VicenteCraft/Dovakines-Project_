from peewee import AutoField, CharField, DateField, IntegerField, TextField

from datos.modelo_base import BaseModel


class Estudiante(BaseModel):
    id = AutoField()
    nombre = CharField(max_length=100)
    apellido = CharField(max_length=100)
    correo_electronico = CharField(max_length=100, unique=True)
    fecha_nacimiento = DateField()
    estado = IntegerField(default=1)

    class Meta:
        table_name = 'estudiantes'
