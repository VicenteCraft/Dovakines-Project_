"""CRUD de la tabla 'curso' usando SQL parametrizado (%s)."""

from datos import conexion
from datos.models import Curso


def _a_curso(fila):
    """Convierte una fila de la base de datos en un objeto Curso."""
    curso = Curso(
        id_curso=fila["id_curso"],
        titulo=fila["titulo"],
        descripcion=fila["descripcion"] or "",
        esta_activo=bool(fila["esta_activo"]),
    )
    curso.id_profesor = fila.get("id_profesor")
    return curso


def listar_todos(solo_activos=True):
    """Consulta (R del CRUD): lista de cursos."""
    if solo_activos:
        filas = conexion.consultar(
            "SELECT * FROM curso WHERE esta_activo = TRUE ORDER BY id_curso"
        )
    else:
        filas = conexion.consultar("SELECT * FROM curso ORDER BY id_curso")
    return [_a_curso(fila) for fila in filas]


def buscar_por_id(id_curso):
    """Consulta por id; devuelve None si no existe."""
    filas = conexion.consultar("SELECT * FROM curso WHERE id_curso = %s", (id_curso,))
    return _a_curso(filas[0]) if filas else None


def guardar(curso):
    """Registro (INSERT) o actualizacion (UPDATE); devuelve el id del curso."""
    if curso.id_curso is None:
        curso.id_curso = conexion.ejecutar(
            "INSERT INTO curso (titulo, descripcion, esta_activo, id_profesor) "
            "VALUES (%s, %s, %s, %s)",
            (curso.titulo, curso.descripcion, curso.esta_activo, curso.id_profesor),
        )
    else:
        conexion.ejecutar(
            "UPDATE curso SET titulo = %s, descripcion = %s, esta_activo = %s, "
            "id_profesor = %s WHERE id_curso = %s",
            (curso.titulo, curso.descripcion, curso.esta_activo,
             curso.id_profesor, curso.id_curso),
        )
    return curso.id_curso


def eliminar(id_curso):
    """Eliminacion (logica): marca el curso como inactivo (esta_activo = FALSE).

    Se usa eliminacion logica porque el UML contempla el atributo 'esta_activo'
    y asi no se pierden las inscripciones relacionadas (integridad referencial).
    Devuelve True si el curso existia.
    """
    if buscar_por_id(id_curso) is None:
        return False
    conexion.ejecutar(
        "UPDATE curso SET esta_activo = FALSE WHERE id_curso = %s", (id_curso,)
    )
    return True
