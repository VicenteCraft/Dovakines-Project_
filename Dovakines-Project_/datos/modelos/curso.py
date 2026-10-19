from datos.conexion import base_datos
from datos.modelos.instructor import Instructor
from peewee import Model, AutoField, CharField, IntegerField, ForeignKeyField, SQL

database = base_datos()
defecto = "DEFAULT 1"

class BaseModel(Model):
    class Meta:
        database = database

class Curso(BaseModel):
    id_curso = AutoField()
    instructor = ForeignKeyField(Instructor, column_name='instructor')
    categoria = IntegerField(index=True)
    edicion = IntegerField(index=True)
    escuela = IntegerField(index=True)
    titulo = CharField(max_length=100,null=True)
    horas = IntegerField(null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'cursos'
