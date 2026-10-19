from peewee import TextField,DateField,AutoField,CharField,IntegerField,DateTimeField,SQL,Model
from datos.conexion import base_datos

database = base_datos()
defecto = "DEFAULT 1"

class BaseModel(Model):
    class Meta:
        database = database

class Administradores(BaseModel):
    contrasena = CharField(max_length=60)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_administrador = AutoField()
    tipo_usuario = IntegerField(index=True)
    usuario = IntegerField(index=True)

    class Meta:
        table_name = 'administradores'

class Comisiones(BaseModel):
    curso = IntegerField(index=True)
    estado = IntegerField(index=True)
    id_comision = AutoField()
    ubicacion = IntegerField(index=True)

    class Meta:
        table_name = 'comisiones'

class Comunas(BaseModel):
    codigo_comuna = CharField(max_length=5)
    comuna = CharField(max_length=60)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_comuna = AutoField()

    class Meta:
        table_name = 'comunas'

class Cursos(BaseModel):
    categoria = IntegerField(index=True)
    edicion = IntegerField(index=True)
    escuela = IntegerField(index=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    horas = IntegerField(null=True)
    id_curso = AutoField()
    instructor = IntegerField(index=True)
    titulo = CharField(max_length=100, null=True)

    class Meta:
        table_name = 'cursos'

class Direcciones(BaseModel):
    calle = CharField(max_length=50, null=True)
    comuna = IntegerField(index=True, null=True)
    departamento = CharField(max_length=5, null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_direccion = AutoField()
    numero = CharField(max_length=5, null=True)
    parametro = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'direcciones'

class DireccionesUsuarios(BaseModel):
    direccion = IntegerField(index=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_direccion_usuario = AutoField()
    usuario = IntegerField(index=True)

    class Meta:
        table_name = 'direcciones_usuarios'

class Ediciones(BaseModel):
    codigo = CharField(max_length=20)
    edicion = CharField(max_length=25, null=True)
    fecha_edicion = DateField(null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_edicion = AutoField()
    idioma = IntegerField(index=True, null=True)
    programa = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'ediciones'

class Escuelas(BaseModel):
    correo = CharField(null=True)
    direccion = IntegerField(index=True, null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_escuela = AutoField()
    nombre = CharField(max_length=100)
    telefono = CharField(max_length=15, null=True)
    web = CharField(null=True)

    class Meta:
        table_name = 'escuelas'

class Estados(BaseModel):
    descripcion = CharField(max_length=100, null=True)
    estado = CharField(max_length=20)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_estado = AutoField()

    class Meta:
        table_name = 'estados'

class Estudiantes(BaseModel):
    categoria = IntegerField(index=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_estudiante = AutoField()
    usuario = IntegerField(index=True)

    class Meta:
        table_name = 'estudiantes'

class Instructores(BaseModel):
    biografia = TextField(null=True)
    fecha_ingreso = DateField(null=True)
    fecha_nacimiento = DateField(null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_instructor = AutoField()
    nombre = CharField(max_length=100, null=True)
    pais = IntegerField(index=True, null=True)
    pseudonimo = CharField(max_length=25, null=True)

    class Meta:
        table_name = 'instructores'

class Matriculas(BaseModel):
    comision = IntegerField(index=True)
    estudiante = IntegerField(index=True)
    fecha_certificacion = DateTimeField(null=True)
    fecha_limite = DateTimeField()
    fecha_matricula = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id_matricula = AutoField()

    class Meta:
        table_name = 'matriculas'

class Parametros(BaseModel):
    descripcion = CharField(max_length=100, null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_parametro = AutoField()
    parametro = CharField(max_length=50)
    tipo = CharField(max_length=20)

    class Meta:
        table_name = 'parametros'

class Programas(BaseModel):
    correo = CharField(null=True)
    direccion = IntegerField(index=True, null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_programa = AutoField()
    pais = IntegerField(index=True)
    programa = CharField(max_length=100)
    telefono = CharField(max_length=15, null=True)

    class Meta:
        table_name = 'programas'

class TiposDireccion(BaseModel):
    descripcion = CharField(max_length=100, null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_tipo_direccion = AutoField()
    tipo_direccion = CharField(max_length=20)

    class Meta:
        table_name = 'tipos_direccion'

class Ubicaciones(BaseModel):
    detalles = CharField(max_length=100, null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_ubicacion = AutoField()
    ubicacion = CharField(max_length=20)

    class Meta:
        table_name = 'ubicaciones'

class Usuarios(BaseModel):
    apellido = CharField(max_length=25)
    correo = CharField()
    fecha_incorporacion = DateField()
    fecha_nacimiento = DateField(null=True)
    genero = IntegerField()
    habilitado = IntegerField(constraints=[SQL(defecto)])
    id_usuario = AutoField()
    nombre = CharField(max_length=25)
    pais = IntegerField(index=True, null=True)
    rut = CharField(max_length=11, null=True)

    class Meta:
        table_name = 'usuarios'
