"""Clases del sistema de gestion de cursos online.

Coherentes con el diagrama de clases UML validado en la Unidad 1
(archivo: trabajos/galvez_vicente.drawio.png).

Decisiones de implementacion respecto al UML (ver README, seccion de validacion):
 - Los identificadores se implementan como enteros con autoincremento en la base
   de datos (el UML los muestra como String) para simplificar su generacion.
 - El metodo iniciar_sesion() del UML recibe la contrasena como parametro, ya que
   sin parametro no seria posible compararla.
 - Las relaciones se representan como atributos (asociacion/composicion) y como
   herencia de clases (Estudiante y Profesor heredan de Usuario).
"""

from datetime import date


class Usuario:
    """Clase base del UML 'usuario'."""

    def __init__(self, id_usuario, nombre, correo, contrasena):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.__contrasena = contrasena  # atributo privado (encapsulamiento)

    @property
    def contrasena(self):
        """Lectura unica de la contrasena (no existe setter: no se puede modificar desde fuera)."""
        return self.__contrasena

    def iniciar_sesion(self, contrasena):
        """UML: iniciar_sesion(): bool - valida la contrasena ingresada."""
        return self.__contrasena == contrasena

    def actualizar_perfil(self, nombre, correo):
        """UML: actualizar_perfil(nombre:string, email:string)."""
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacio.")
        if not correo or "@" not in correo:
            raise ValueError("El correo debe contener '@'.")
        self.nombre = nombre.strip()
        self.correo = correo.strip()

    def __str__(self):
        return f"{self.nombre} <{self.correo}>"


class Estudiante(Usuario):
    """UML: 'estudiante' hereda de 'usuario'."""

    def __init__(self, id_usuario, nombre, correo, contrasena, matricula):
        super().__init__(id_usuario, nombre, correo, contrasena)
        self.matricula = matricula
        self.inscripciones = []

    def inscribirse_curso(self, curso):
        """UML: inscribirse_curso() - crea su inscripcion en el curso indicado."""
        inscripcion = Inscripcion(estudiante=self, curso=curso)
        self.inscripciones.append(inscripcion)
        return inscripcion

    def ver_avance(self):
        """UML: ver_avance(): float - promedio de avance de sus inscripciones."""
        if not self.inscripciones:
            return 0.0
        total = sum(inscripcion.calcular_avance() for inscripcion in self.inscripciones)
        return round(total / len(self.inscripciones), 2)


class Inscripcion:
    """UML: 'inscripcion' - relacion estudiante <-> curso."""

    ESTADOS_VALIDOS = ("activa", "completada", "cancelada")

    def __init__(self, estudiante, curso, fecha_inscripcion=None,
                 porcentaje_avance=0.0, estado="activa"):
        self.estudiante = estudiante
        self.curso = curso
        self.fecha_inscripcion = fecha_inscripcion or date.today()
        self.porcentaje_avance = float(porcentaje_avance)
        self.estado = estado

    def calcular_avance(self):
        """UML: calcularAvance(): float."""
        return round(self.porcentaje_avance, 2)

    def actualizar_estado(self, nuevo_estado):
        """UML: actualizar_estado(nuevoEstado: string)."""
        if nuevo_estado not in self.ESTADOS_VALIDOS:
            raise ValueError(
                f"Estado invalido: '{nuevo_estado}'. "
                f"Debe ser uno de: {', '.join(self.ESTADOS_VALIDOS)}"
            )
        self.estado = nuevo_estado

    def __str__(self):
        return f"{self.estudiante.matricula} -> {self.curso.titulo} ({self.estado})"


class Profesor(Usuario):
    """UML: 'profesor' hereda de 'usuario'."""

    def __init__(self, id_usuario, nombre, correo, contrasena, especialidad):
        super().__init__(id_usuario, nombre, correo, contrasena)
        self.especialidad = especialidad

    def crear_curso(self, titulo, descripcion):
        """UML: crear_curso() - el profesor es dueno de sus cursos (composicion)."""
        curso = Curso(id_curso=None, titulo=titulo, descripcion=descripcion)
        curso.profesor = self
        return curso

    def calificar_entrega(self, entrega, nota, observacion):
        """UML: calificar_entrega() - delega en la entrega."""
        return entrega.calificar(nota, observacion)


class Curso:
    """UML: 'curso'."""

    def __init__(self, id_curso, titulo, descripcion, esta_activo=True):
        if not titulo or not titulo.strip():
            raise ValueError("El titulo del curso no puede estar vacio.")
        self.id_curso = id_curso
        self.titulo = titulo.strip()
        self.descripcion = descripcion
        self.esta_activo = esta_activo
        self.profesor = None           # asociacion con 'profesor'
        self.modulos = []              # composicion curso (1) <-> modulo (1..*)
        self.inscripciones = []        # relacion con 'inscripcion'

    def agregar_modulo(self, modulo):
        """UML: agregar_modulo(modulo: Modulo)."""
        self.modulos.append(modulo)

    def listar_estudiantes(self):
        """UML: listar_estudiantes(): List<Estudiante>."""
        return [inscripcion.estudiante for inscripcion in self.inscripciones]

    def obtener_estadisticas(self):
        """UML: obtener_estadisticas(): string."""
        activos = sum(1 for i in self.inscripciones if i.estado == "activa")
        return (
            f"Modulos: {len(self.modulos)} | "
            f"Inscripciones: {len(self.inscripciones)} | "
            f"Activas: {activos}"
        )

    def __str__(self):
        estado = "activo" if self.esta_activo else "inactivo"
        return f"[{self.id_curso}] {self.titulo} ({estado})"


class Modulo:
    """UML: 'modulo' - contenido propio de un curso (composicion)."""

    def __init__(self, id_modulo, titulo, orden):
        self.id_modulo = id_modulo
        self.titulo = titulo
        self.orden = orden
        self.contenidos = []
        self.actividades = []

    def agregar_contenido(self, contenido):
        """UML: agregar_contenido(contenido: Contenido)."""
        self.contenidos.append(contenido)

    def agregar_actividad(self, actividad):
        """UML: agregar_actividad(actividad: Actividad)."""
        self.actividades.append(actividad)

    def __str__(self):
        return f"{self.orden}. {self.titulo}"


class Contenido:
    """UML: 'contenido'."""

    def __init__(self, id_contenido, titulo, tipo, url_recurso=""):
        self.id_contenido = id_contenido
        self.titulo = titulo
        self.tipo = tipo
        self.url_recurso = url_recurso

    def obtener_detalle(self):
        """UML: obtener_detalle(): string."""
        return f"{self.titulo} ({self.tipo}) - {self.url_recurso or 'sin enlace'}"


class Actividad:
    """UML: 'actividad' - clase base de las actividades."""

    def __init__(self, id_actividad, titulo, descripcion):
        self.id_actividad = id_actividad
        self.titulo = titulo
        self.descripcion = descripcion

    def mostrar_instrucciones(self):
        """UML: mostrar_instrucciones()."""
        return f"{self.titulo}: {self.descripcion}"

    def __str__(self):
        return self.titulo


class ActividadEvaluada(Actividad):
    """UML: 'actividad_evaluada' hereda de 'actividad'."""

    def __init__(self, id_actividad, titulo, descripcion, ponderacion,
                 fecha_limite, nota_maxima):
        super().__init__(id_actividad, titulo, descripcion)
        self.ponderacion = ponderacion
        self.fecha_limite = fecha_limite
        self.nota_maxima = nota_maxima
        self.entregas = []

    def recibir_entrega(self, entrega):
        """UML: recibir_entrega(entrega: Entrega)."""
        self.entregas.append(entrega)
        return entrega


class ActividadFormativa(Actividad):
    """UML: 'actividad_formativa' hereda de 'actividad'."""

    def __init__(self, id_actividad, titulo, descripcion, solucion_sugerida):
        super().__init__(id_actividad, titulo, descripcion)
        self.solucion_sugerida = solucion_sugerida

    def mostrar_solucion(self):
        """UML: mostrarSolucion()."""
        return f"Solucion sugerida: {self.solucion_sugerida}"


class Entrega:
    """UML: 'entrega' - trabajos entregados por un estudiante."""

    def __init__(self, id_entrega, fecha_envio=None, archivo_respuesta="", calificacion=None):
        self.id_entrega = id_entrega
        self.fecha_envio = fecha_envio or date.today()
        self.archivo_respuesta = archivo_respuesta
        self.calificacion = calificacion
        self.observacion = ""

    def calificar(self, nota, observacion):
        """UML: calificar(nota: float, obs: string)."""
        if nota < 0 or nota > 7:
            raise ValueError("La nota debe estar entre 0.0 y 7.0.")
        self.calificacion = float(nota)
        self.observacion = observacion
        return self.calificacion

    def __str__(self):
        return f"Entrega {self.id_entrega}: {self.calificacion}"
