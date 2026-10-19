"""Pruebas automaticas del sistema (etapa 'Pruebas y validacion' de la pauta).

Se ejecutan con:  pytest -q
No necesitan base de datos: prueban las clases del UML y las validaciones.
"""

import os
import sys
from datetime import date

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datos.models import (
    Actividad,
    ActividadEvaluada,
    ActividadFormativa,
    Contenido,
    Curso,
    Entrega,
    Estudiante,
    Inscripcion,
    Modulo,
    Profesor,
    Usuario,
)
from presentacion.validaciones import validar_correo, validar_entero, validar_texto


# ---------------------------------------------------------------------------
# Herencia y encapsulamiento (Paso 2 de la pauta)
# ---------------------------------------------------------------------------

def test_estudiante_y_profesor_hereda_de_usuario():
    estudiante = Estudiante(1, "Ana", "ana@demo.cl", "1234", "2026-001")
    profesor = Profesor(2, "Luis", "luis@demo.cl", "1234", "Programacion")
    assert isinstance(estudiante, Usuario)
    assert isinstance(profesor, Usuario)


def test_contrasena_es_privada_no_se_puede_modificar_desde_fuera():
    usuario = Usuario(1, "Ana", "ana@demo.cl", "1234")
    assert usuario.contrasena == "1234"          # lectura por property
    with pytest.raises(AttributeError):          # no existe setter
        usuario.contrasena = "otra"


# ---------------------------------------------------------------------------
# Metodos definidos en el diagrama UML (Paso 1 de la pauta)
# ---------------------------------------------------------------------------

def test_iniciar_sesion_valida_contrasena():
    usuario = Usuario(1, "Ana", "ana@demo.cl", "1234")
    assert usuario.iniciar_sesion("1234") is True
    assert usuario.iniciar_sesion("9999") is False


def test_actualizar_perfil_valida_entradas():
    usuario = Usuario(1, "Ana", "ana@demo.cl", "1234")
    usuario.actualizar_perfil("Ana Perez", "ana@duoc.cl")
    assert usuario.nombre == "Ana Perez"
    with pytest.raises(ValueError):
        usuario.actualizar_perfil("", "nuevo@correo.cl")
    with pytest.raises(ValueError):
        usuario.actualizar_perfil("Ana", "correo-sin-arroba")


def test_profesor_crear_curso_asigna_al_profesor():
    profesor = Profesor(2, "Luis", "luis@demo.cl", "1234", "Programacion")
    curso = profesor.crear_curso("Base de datos", "Unidad de tablas")
    assert isinstance(curso, Curso)
    assert curso.profesor is profesor


def test_curso_metodos_del_uml():
    curso = Curso(id_curso=1, titulo="Python", descripcion="Basico")
    estudiante = Estudiante(1, "Ana", "ana@demo.cl", "1234", "2026-001")
    inscripcion = estudiante.inscribirse_curso(curso)
    curso.inscripciones.append(inscripcion)

    modulo = Modulo(id_modulo=None, titulo="Unidad 1", orden=1)
    modulo.agregar_contenido(Contenido(None, "Video 1", "video", "http://video"))
    modulo.agregar_actividad(ActividadEvaluada(None, "Tarea 1", "Ejercicios",
                                               25, date(2026, 11, 1), 7.0))
    curso.agregar_modulo(modulo)

    assert curso.listar_estudiantes() == [estudiante]     # UML: listar_estudiantes()
    assert "Modulos: 1" in curso.obtener_estadisticas()   # UML: obtener_estadisticas()
    assert "Inscripciones: 1" in curso.obtener_estadisticas()


def test_curso_rechaza_titulo_vacio():
    with pytest.raises(ValueError):
        Curso(id_curso=None, titulo="   ", descripcion="x")


def test_inscripcion_calculo_y_estados():
    estudiante = Estudiante(1, "Ana", "ana@demo.cl", "1234", "2026-001")
    curso = Curso(id_curso=1, titulo="Python", descripcion="Basico")
    inscripcion = Inscripcion(estudiante, curso, porcentaje_avance=80.5)

    assert inscripcion.calcular_avance() == 80.5          # UML: calcularAvance()
    inscripcion.actualizar_estado("completada")
    assert inscripcion.estado == "completada"
    with pytest.raises(ValueError):
        inscripcion.actualizar_estado("inventado")


def test_estudiante_ver_avance_promedia_sus_inscripciones():
    estudiante = Estudiante(1, "Ana", "ana@demo.cl", "1234", "2026-001")
    curso = Curso(id_curso=1, titulo="Python", descripcion="Basico")
    estudiante.inscripciones.append(Inscripcion(estudiante, curso, porcentaje_avance=50))
    estudiante.inscripciones.append(Inscripcion(estudiante, curso, porcentaje_avance=100))
    assert estudiante.ver_avance() == 75.0                # UML: ver_avance()


def test_entrega_calificar_respeta_rango_de_notas():
    entrega = Entrega(id_entrega=None, archivo_respuesta="tarea.zip")
    assert entrega.calificar(5.5, "Buen trabajo") == 5.5
    with pytest.raises(ValueError):
        entrega.calificar(9.0, "fuera de rango")


def test_actividades_heran_de_actividad_y_muestran_contenido():
    evaluada = ActividadEvaluada(None, "Tarea 1", "Ejercicios", 25, date(2026, 11, 1), 7.0)
    formativa = ActividadFormativa(None, "Foro 1", "Comenta", "Respuesta sugerida")
    entrega = Entrega(id_entrega=None)

    evaluada.recibir_entrega(entrega)                      # UML: recibir_entrega()
    assert evaluada.entregas == [entrega]
    assert "Tarea 1" in evaluada.mostrar_instrucciones()
    assert formativa.mostrar_solucion().startswith("Solucion sugerida")
    assert isinstance(evaluada, Actividad)                 # herencia UML
    assert isinstance(formativa, Actividad)


# ---------------------------------------------------------------------------
# Validaciones de entradas (Paso 4 de la pauta)
# ---------------------------------------------------------------------------

def test_validar_texto():
    assert validar_texto("Curso de Python") is None
    assert validar_texto("") is not None
    assert validar_texto("   ") is not None
    assert validar_texto("x" * 101, maximo=100) is not None


def test_validar_correo():
    assert validar_correo("ana@duoc.cl") is None
    assert validar_correo("ana") is not None
    assert validar_correo("ana@dominio") is not None


def test_validar_entero():
    assert validar_entero("12", minimo=1) == (12, None)
    assert validar_entero("abc") == (None, "Debe ser un numero entero.")
    assert validar_entero("0", minimo=1) == (None, "Debe ser mayor o igual a 1.")
