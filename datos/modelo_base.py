from datos.conexion import conectar_db
database = conectar_db()

def modelo_inicial():

class BaseModel(Model):
    class Meta:
        database = database