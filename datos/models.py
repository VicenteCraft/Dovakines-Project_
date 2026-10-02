from peewee import CharField, TextField,DateField,AutoField,Charfield,IntergerField,DatetimeField,SQL,Model
from decouple import config

database = conectar_db()
defecto = "DEFAULT 1"

class Curso(BaseModel):
    id = AutoField()
    nombre = CharField(max_length=100)
    descripcion = TextField()
    fecha_inicio = DateField()
    fecha_fin = DateField()
    estado = IntegerField(constraints=[SQL(defecto)])

class Estudiante(BaseModel):
    id = AutoField()
    nombre = CharField(max_length=100)
    apellido = CharField(max_length=100)
    correo_electronico = CharField(max_length=100, unique=True)
    fecha_nacimiento = DateField()
    estado = IntegerField(constraints=[SQL(defecto)])

class Inscripcion(BaseModel):
    id = AutoField()
    estudiante = ForeignKeyField(Estudiante, backref='inscripciones')
    curso = ForeignKeyField(Curso, backref='inscripciones')
    fecha_inscripcion = DateTimeField()
    estado = IntegerField(constraints=[SQL(defecto)])

class Profesor(BaseModel):
    id = AutoField()
    nombre = CharField(max_length=100)
    apellido = CharField(max_length=100)
    correo_electronico = CharField(max_length=100, unique=True)
    fecha_nacimiento = DateField()
    estado = IntegerField(constraints=[SQL(defecto)])

class Asignacion(BaseModel):
    id = AutoField()
    profesor = ForeignKeyField(Profesor, backref='asignaciones')
    curso = ForeignKeyField(Curso, backref='asignaciones')
    fecha_asignacion = DateTimeField()
    estado = IntegerField(constraints=[SQL(defecto)])

class Evaluacion(BaseModel):
    id = AutoField()
    curso = ForeignKeyField(Curso, backref='evaluaciones')
    nombre = CharField(max_length=100)
    descripcion = TextField()
    fecha_evaluacion = DateTimeField()
    estado = IntegerField(constraints=[SQL(defecto)])

class Calificacion(BaseModel):
    id = AutoField()
    estudiante = ForeignKeyField(Estudiante, backref='calificaciones')
    evaluacion = ForeignKeyField(Evaluacion, backref='calificaciones')
    calificacion = IntegerField()
    fecha_calificacion = DateTimeField()
    estado = IntegerField(constraints=[SQL(defecto)])

class Asistencia(BaseModel):
    id = AutoField()
    estudiante = ForeignKeyField(Estudiante, backref='asistencias')
    curso = ForeignKeyField(Curso, backref='asistencias')
    fecha_asistencia = DateTimeField()
    estado = IntegerField(constraints=[SQL(defecto)])

