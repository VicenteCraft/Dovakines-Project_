"""Acceso a datos de la tabla 'inscripcion' (relacion estudiante <-> curso)."""

from datos import conexion
from datos.models import Curso, Estudiante, Inscripcion


def guardar(inscripcion, id_estudiante, id_curso):
    """Registro (INSERT) de una inscripcion; devuelve su id."""
    return conexion.ejecutar(
        "INSERT INTO inscripcion "
        "(id_estudiante, id_curso, fecha_inscripcion, porcentaje_avance, estado) "
        "VALUES (%s, %s, %s, %s, %s)",
        (
            id_estudiante,
            id_curso,
            inscripcion.fecha_inscripcion,
            inscripcion.porcentaje_avance,
            inscripcion.estado,
        ),
    )


def existe(id_estudiante, id_curso):
    """Validacion: True si el estudiante ya esta inscrito en ese curso."""
    filas = conexion.consultar(
        "SELECT 1 FROM inscripcion WHERE id_estudiante = %s AND id_curso = %s",
        (id_estudiante, id_curso),
    )
    return bool(filas)


def listar_de_curso(id_curso):
    """Devuelve las inscripciones de un curso como objetos Inscripcion."""
    filas = conexion.consultar(
        "SELECT i.*, u.nombre, u.correo, u.contrasena, e.matricula, "
        "       c.titulo, c.descripcion, c.esta_activo "
        "FROM inscripcion i "
        "INNER JOIN estudiante e ON e.id_usuario = i.id_estudiante "
        "INNER JOIN usuario u ON u.id_usuario = e.id_usuario "
        "INNER JOIN curso c ON c.id_curso = i.id_curso "
        "WHERE i.id_curso = %s "
        "ORDER BY u.nombre",
        (id_curso,),
    )

    inscripciones = []
    for fila in filas:
        estudiante = Estudiante(
            fila["id_estudiante"], fila["nombre"], fila["correo"],
            fila["contrasena"], fila["matricula"],
        )
        curso = Curso(
            id_curso=fila["id_curso"],
            titulo=fila["titulo"],
            descripcion=fila["descripcion"] or "",
            esta_activo=bool(fila["esta_activo"]),
        )
        inscripciones.append(
            Inscripcion(
                estudiante=estudiante,
                curso=curso,
                fecha_inscripcion=fila["fecha_inscripcion"],
                porcentaje_avance=float(fila["porcentaje_avance"]),
                estado=fila["estado"],
            )
        )
    return inscripciones
