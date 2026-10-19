from datos.modelos.instructor import Instructor
from datos.conexion import base_datos

def listado_instructores():
    instructores = Instructor.select()
    return instructores

def guardar_instructor(instructor: Instructor):
    db = base_datos()
    db.connect()
    instructor.save()
    db.close()
    return instructor
