create database Curso_online;

CREATE TABLE usuario(
    id_usuario VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    contrasenia VARCHAR(255) NOT NULLM
    iniciar_sesion BOOLEAN DEFAULT FALSE
);

CREATE TABLE estudiante (
    id_usuario VARCHAR(50) PRIMARY KEY,
    matricula VARCHAR(50) NOT NULL UNIQUE,
    CONSTRAINT fk_estudiante_usuario
        FOREING KEY (id_usuario)
        REFERECES usuario(id_usuario)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE profesor (
    id_usuario VARCHAR(50) PRIMARY KEY,
    especialidad VARCHAR(100) NOT NULL,
    CONSTRAINT fk_profesor_usuario
        FOREIGN KEY (id_usuario)
        REFERECES usuario(id_usuario)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE curso(
    id_curso VARCHAR(50) PRIMARY KEY,
    id_profesor VARCHAR(50) NOT NULL,
    titulo VARCHAR(150) NOT NULL,
    descripcion TEXT,
    esta_activo BOOLEAN DEFAULT TRUE,
    CONSTRAINT fk_curso_profesor
        FOREIGN KEY(id_profesor)
        REFERECES profesor (id_usuario)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE inscripcion (
    id_estudiante VARCHAR(50) NOT NULL,
    id_curso VARCHAR(50) NOT NULL,
    fecha_inscripcion DATE NOT NULL,
    porcentaje_avance FLOAT DEFAULT 0.0,
    estado VARCHAR(50) NOT NULL DEFAULT 'activo',
    PRIMARY KEY (id_estudiante, id_curso),
    CONSTRAINT fk_inscripcion_estudiante
        FOREIGN KEY (id_estudiante)
        REFERECES estudiante(id_usuario)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_inscripcion_curso
        FOREING KEY (id_curso)
        REFERECES curso(id_curso)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE modulo(
    id_modulo VARCHAR(50) PRIMARY KEY,
    id_curso VARCHAR(50) NOT NULL,
    titulo VARCHAR(150) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    url_recurso VARCHAR(255),
    CONSTRAINT fk_contenido_modulo
        FOREIGN KEY (id_curso)
        REFERECES curso(id_curso)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE contenido (
    id_contenido VARCHAR(50) PRIMARY KEY,
    id_modulo VARCHAR(50) NOT NULL,
    titulo VARCHAR(150) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    url_recurso VARHCAR(255),
    CONSTRAINT fk_contenido_modulo
        FOREIGN KEY (ide_modulo)
        REFERECES modulo(id_modulo)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE actividad_evaluada (
    id_actividad VARCHAR(50) PRIMARY KEY,
    ponderacion FLOAT NOT NULL,
    fecha_limite DATE NOT NULL,
    nota_maxima FLOAT NOT NULL DEFAULT 7.0,
    CONSTRAINT fk_evaluada_actividad
        FOREIGN KEY (id_actividad)
        REFERECES actividad(id_actividad)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE actividad_formativa (
    id_actividad VARCHAR(50) PRIMARY KEY,
    solucion_sugerida TEXT,
    CONSTRAINT fk_formativa_actividad
        FOREIGN KEY (id_actividad)
        REFERECES actividad (id_actividad)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE entrega (
    id_entrega VARCHAR(50) PRIMARY KEY,
    id_actividad_evaluada VARCHAR(50) NOT NULL,
    id_estudiante VARCHAR(50) NOT NULL,
    fecha_envio DATE NOT NULL,
    archivo_respuesta VARCHAR(255),
    calificacion FLOAT,
    CONSTRAINT fk_entrega_actividad
        FOREIGN KEY (id_actividad_evaluada)
        REFERECES actividad_evaluada(id_actividad)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_entrega_estudiante
        FOREIGN KEY (id_estudiante)
        REFERENCES estudiante(id_usuario)
        ON DELETE CASCADE ON UPDATE CASCADE
);