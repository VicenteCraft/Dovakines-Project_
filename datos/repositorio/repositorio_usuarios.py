"""Acceso a datos de las tablas 'usuario', 'estudiante' y 'profesor'."""

from datos import conexion
from datos.models import Estudiante, Profesor, Usuario


def buscar_por_correo(correo):
    """Devuelve un Usuario, Estudiante o Profesor; o None si no existe."""
    filas = conexion.consultar("SELECT * FROM usuario WHERE correo = %s", (correo,))
    if not filas:
        return None
    fila = filas[0]

    estudiante = conexion.consultar(
        "SELECT matricula FROM estudiante WHERE id_usuario = %s", (fila["id_usuario"],)
    )
    if estudiante:
        return Estudiante(
            fila["id_usuario"], fila["nombre"], fila["correo"],
            fila["contrasena"], estudiante[0]["matricula"],
        )

    profesor = conexion.consultar(
        "SELECT especialidad FROM profesor WHERE id_usuario = %s", (fila["id_usuario"],)
    )
    if profesor:
        return Profesor(
            fila["id_usuario"], fila["nombre"], fila["correo"],
            fila["contrasena"], profesor[0]["especialidad"],
        )

    return Usuario(
        fila["id_usuario"], fila["nombre"], fila["correo"], fila["contrasena"]
    )


def buscar_estudiante_por_matricula(matricula):
    """Devuelve un Estudiante o None."""
    filas = conexion.consultar(
        "SELECT u.*, e.matricula FROM usuario u "
        "INNER JOIN estudiante e ON e.id_usuario = u.id_usuario "
        "WHERE e.matricula = %s",
        (matricula,),
    )
    if not filas:
        return None
    fila = filas[0]
    return Estudiante(
        fila["id_usuario"], fila["nombre"], fila["correo"],
        fila["contrasena"], fila["matricula"],
    )


def buscar_profesor(id_profesor):
    """Devuelve un Profesor o None."""
    filas = conexion.consultar(
        "SELECT u.*, p.especialidad FROM usuario u "
        "INNER JOIN profesor p ON p.id_usuario = u.id_usuario "
        "WHERE u.id_usuario = %s",
        (id_profesor,),
    )
    if not filas:
        return None
    fila = filas[0]
    return Profesor(
        fila["id_usuario"], fila["nombre"], fila["correo"],
        fila["contrasena"], fila["especialidad"],
    )


def registrar_estudiante(nombre, correo, contrasena, matricula):
    """Registro (INSERT): crea el usuario y su ficha de estudiante."""
    id_usuario = conexion.ejecutar(
        "INSERT INTO usuario (nombre, correo, contrasena) VALUES (%s, %s, %s)",
        (nombre, correo, contrasena),
    )
    conexion.ejecutar(
        "INSERT INTO estudiante (id_usuario, matricula) VALUES (%s, %s)",
        (id_usuario, matricula),
    )
    return id_usuario
