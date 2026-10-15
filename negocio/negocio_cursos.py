"""Capa de negocio: contiene las reglas del sistema de gestion de cursos."""

from datos.models import Curso, Estudiante
from datos.repositorio import (
    repositorio_cursos,
    repositorio_inscripciones,
    repositorio_usuarios,
)


def cargar_cursos(solo_activos=True):
    """Devuelve la lista de cursos."""
    return repositorio_cursos.listar_todos(solo_activos=solo_activos)


def buscar_curso(id_curso):
    """Devuelve el curso o None."""
    return repositorio_cursos.buscar_por_id(id_curso)


def crear_curso(titulo, descripcion, id_profesor=None):
    """Crea y guarda un curso. Si se indica profesor, lo crea con su metodo UML."""
    if id_profesor is not None:
        profesor = repositorio_usuarios.buscar_profesor(id_profesor)
        if profesor is None:
            raise ValueError(f"No existe un profesor con id {id_profesor}.")
        curso = profesor.crear_curso(titulo, descripcion)   # UML: crear_curso()
        curso.id_profesor = profesor.id_usuario
    else:
        curso = Curso(id_curso=None, titulo=titulo, descripcion=descripcion)

    repositorio_cursos.guardar(curso)
    return curso


def actualizar_curso(id_curso, titulo, descripcion):
    """Actualiza titulo y descripcion de un curso existente."""
    curso = repositorio_cursos.buscar_por_id(id_curso)
    if curso is None:
        raise ValueError(f"No existe un curso con id {id_curso}.")
    curso.titulo = titulo.strip()
    curso.descripcion = descripcion
    repositorio_cursos.guardar(curso)
    return curso


def eliminar_curso(id_curso):
    """Elimina (desactiva) un curso. Devuelve False si no existia."""
    return repositorio_cursos.eliminar(id_curso)


def registrar_estudiante(nombre, correo, contrasena, matricula):
    """Registra un usuario y su ficha de estudiante, validando duplicados."""
    if repositorio_usuarios.buscar_por_correo(correo) is not None:
        raise ValueError(f"Ya existe un usuario registrado con el correo '{correo}'.")
    if repositorio_usuarios.buscar_estudiante_por_matricula(matricula) is not None:
        raise ValueError(f"La matricula '{matricula}' ya esta registrada.")

    repositorio_usuarios.registrar_estudiante(nombre, correo, contrasena, matricula)
    return repositorio_usuarios.buscar_estudiante_por_matricula(matricula)


def inscribir_estudiante(matricula, id_curso):
    """Inscribe a un estudiante en un curso (UML: inscribirse_curso())."""
    curso = repositorio_cursos.buscar_por_id(id_curso)
    if curso is None:
        raise ValueError(f"No existe un curso con id {id_curso}.")
    if not curso.esta_activo:
        raise ValueError(f"El curso '{curso.titulo}' esta inactivo.")

    estudiante = repositorio_usuarios.buscar_estudiante_por_matricula(matricula)
    if estudiante is None:
        raise ValueError(f"No existe un estudiante con la matricula '{matricula}'.")

    if repositorio_inscripciones.existe(estudiante.id_usuario, curso.id_curso):
        raise ValueError("El estudiante ya esta inscrito en ese curso.")

    inscripcion = estudiante.inscribirse_curso(curso)   # UML: inscribirse_curso()
    repositorio_inscripciones.guardar(
        inscripcion, estudiante.id_usuario, curso.id_curso
    )
    return inscripcion


def inscripciones_de_curso(id_curso):
    """Devuelve el curso con sus inscripciones cargadas."""
    curso = repositorio_cursos.buscar_por_id(id_curso)
    if curso is None:
        raise ValueError(f"No existe un curso con id {id_curso}.")
    curso.inscripciones = repositorio_inscripciones.listar_de_curso(curso.id_curso)
    return curso


def iniciar_sesion(correo, contrasena):
    """Valida las credenciales con el metodo UML iniciar_sesion()."""
    usuario = repositorio_usuarios.buscar_por_correo(correo)
    if usuario is None:
        raise ValueError("No existe un usuario con ese correo.")
    if not usuario.iniciar_sesion(contrasena):   # UML: iniciar_sesion()
        raise ValueError("La contrasena es incorrecta.")
    return usuario
