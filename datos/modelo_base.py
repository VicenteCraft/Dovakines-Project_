from peewee import Model

from datos.conexion import conectar_db

database = conectar_db()


def modelo_inicial():
    """Crea (si aún no existen) las tablas de la plataforma de cursos."""
    # El import se hace dentro de la función para evitar un import circular
    # (datos.models importa BaseModel desde este módulo).
    from datos import models

    # Muchas instalaciones de WAMP traen MyISAM, que ignora las llaves foráneas.
    # Con esta línea las tablas se crean en InnoDB y las relaciones sí se respetan.
    database.execute_sql("SET default_storage_engine = 'InnoDB'")

    database.create_tables(
        [
            models.Curso,
            models.Estudiante,
            models.Inscripcion,
            models.Profesor,
            models.Asignacion,
            models.Evaluacion,
            models.Calificacion,
            models.Asistencia,
        ],
        safe=True,
    )


class BaseModel(Model):
    class Meta:
        database = database
