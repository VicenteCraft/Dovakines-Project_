CREATE DATABASE IF NOT EXISTS Curso_online
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE Curso_online;

CREATE TABLE usuario (
    id_usuario     VARCHAR(50)  PRIMARY KEY,
    nombre         VARCHAR(100) NOT NULL,
    correo         VARCHAR(100) NOT NULL UNIQUE,
    contrasenia    VARCHAR(255) NOT NULL,
    iniciar_sesion BOOLEAN      DEFAULT FALSE,
    activo         BOOLEAN      NOT NULL DEFAULT TRUE,
    fecha_registro DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ultimo_acceso  DATETIME
);

CREATE TABLE estudiante (
    id_usuario VARCHAR(50) PRIMARY KEY,
    matricula  VARCHAR(50) NOT NULL UNIQUE,
    CONSTRAINT fk_estudiante_usuario
        FOREIGN KEY (id_usuario)
        REFERENCES usuario(id_usuario)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE profesor (
    id_usuario   VARCHAR(50)  PRIMARY KEY,
    especialidad VARCHAR(100) NOT NULL,
    CONSTRAINT fk_profesor_usuario
        FOREIGN KEY (id_usuario)
        REFERENCES usuario(id_usuario)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE curso (
    id_curso       VARCHAR(50)   PRIMARY KEY,
    id_profesor    VARCHAR(50)   NOT NULL,
    titulo         VARCHAR(150)  NOT NULL,
    descripcion    TEXT,
    categoria      VARCHAR(100),
    precio         DECIMAL(10,2) NOT NULL DEFAULT 0.00 CHECK (precio >= 0),
    nivel          VARCHAR(30)   NOT NULL DEFAULT 'basico'
                   CHECK (nivel IN ('basico', 'intermedio', 'avanzado')),
    esta_activo    BOOLEAN       DEFAULT TRUE,
    fecha_creacion DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_curso_profesor
        FOREIGN KEY (id_profesor)
        REFERENCES profesor(id_usuario)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE inscripcion (
    id_estudiante     VARCHAR(50)  NOT NULL,
    id_curso          VARCHAR(50)  NOT NULL,
    fecha_inscripcion DATE         NOT NULL,
    porcentaje_avance DECIMAL(5,2) NOT NULL DEFAULT 0.00
                      CHECK (porcentaje_avance BETWEEN 0 AND 100),
    estado            VARCHAR(50)  NOT NULL DEFAULT 'activo'
                      CHECK (estado IN ('activo', 'completado', 'cancelado')),
    PRIMARY KEY (id_estudiante, id_curso),
    CONSTRAINT fk_inscripcion_estudiante
        FOREIGN KEY (id_estudiante)
        REFERENCES estudiante(id_usuario)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_inscripcion_curso
        FOREIGN KEY (id_curso)
        REFERENCES curso(id_curso)
        ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE modulo (
    id_modulo   VARCHAR(50)  PRIMARY KEY,
    id_curso    VARCHAR(50)  NOT NULL,
    titulo      VARCHAR(150) NOT NULL,
    descripcion TEXT,
    orden       INT          NOT NULL DEFAULT 1,
    CONSTRAINT fk_modulo_curso
        FOREIGN KEY (id_curso)
        REFERENCES curso(id_curso)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT uq_modulo_orden UNIQUE (id_curso, orden)
);

CREATE TABLE contenido (
    id_contenido VARCHAR(50)  PRIMARY KEY,
    id_modulo    VARCHAR(50)  NOT NULL,
    titulo       VARCHAR(150) NOT NULL,
    tipo         VARCHAR(50)  NOT NULL
                 CHECK (tipo IN ('video', 'texto', 'pdf', 'enlace')),
    url_recurso  VARCHAR(255),
    duracion_min INT,
    orden        INT          NOT NULL DEFAULT 1,
    CONSTRAINT fk_contenido_modulo
        FOREIGN KEY (id_modulo)
        REFERENCES modulo(id_modulo)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT uq_contenido_orden UNIQUE (id_modulo, orden)
);

CREATE TABLE progreso_contenido (
    id_estudiante    VARCHAR(50) NOT NULL,
    id_contenido     VARCHAR(50) NOT NULL,
    completado       BOOLEAN     NOT NULL DEFAULT FALSE,
    fecha_completado DATETIME,
    PRIMARY KEY (id_estudiante, id_contenido),
    CONSTRAINT fk_progreso_estudiante
        FOREIGN KEY (id_estudiante)
        REFERENCES estudiante(id_usuario)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_progreso_contenido
        FOREIGN KEY (id_contenido)
        REFERENCES contenido(id_contenido)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE actividad (
    id_actividad VARCHAR(50)  PRIMARY KEY,
    id_modulo    VARCHAR(50)  NOT NULL,
    titulo       VARCHAR(150) NOT NULL,
    descripcion  TEXT,
    CONSTRAINT fk_actividad_modulo
        FOREIGN KEY (id_modulo)
        REFERENCES modulo(id_modulo)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE actividad_evaluada (
    id_actividad VARCHAR(50)  PRIMARY KEY,
    ponderacion  DECIMAL(5,2) NOT NULL CHECK (ponderacion > 0 AND ponderacion <= 100),
    fecha_limite DATETIME     NOT NULL,
    nota_maxima  DECIMAL(3,1) NOT NULL DEFAULT 7.0,
    CONSTRAINT fk_evaluada_actividad
        FOREIGN KEY (id_actividad)
        REFERENCES actividad(id_actividad)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE actividad_formativa (
    id_actividad      VARCHAR(50) PRIMARY KEY,
    solucion_sugerida TEXT,
    CONSTRAINT fk_formativa_actividad
        FOREIGN KEY (id_actividad)
        REFERENCES actividad(id_actividad)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE entrega (
    id_entrega            VARCHAR(50)  PRIMARY KEY,
    id_actividad_evaluada VARCHAR(50)  NOT NULL,
    id_estudiante         VARCHAR(50)  NOT NULL,
    fecha_envio           DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    archivo_respuesta     VARCHAR(255),
    calificacion          DECIMAL(3,1) CHECK (calificacion >= 0),
    retroalimentacion     TEXT,
    CONSTRAINT fk_entrega_actividad
        FOREIGN KEY (id_actividad_evaluada)
        REFERENCES actividad_evaluada(id_actividad)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_entrega_estudiante
        FOREIGN KEY (id_estudiante)
        REFERENCES estudiante(id_usuario)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT uq_entrega UNIQUE (id_actividad_evaluada, id_estudiante)
);


CREATE TABLE orden (
    id_orden       VARCHAR(50)   PRIMARY KEY,
    id_estudiante  VARCHAR(50)   NOT NULL,
    total          DECIMAL(10,2) NOT NULL CHECK (total >= 0),
    estado         VARCHAR(30)   NOT NULL DEFAULT 'pendiente'
                   CHECK (estado IN ('pendiente', 'pagada', 'cancelada', 'reembolsada')),
    metodo_pago    VARCHAR(30),
    id_transaccion VARCHAR(100)  UNIQUE,
    fecha          DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_orden_estudiante
        FOREIGN KEY (id_estudiante)
        REFERENCES estudiante(id_usuario)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE detalle_orden (
    id_orden        VARCHAR(50)   NOT NULL,
    id_curso        VARCHAR(50)   NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL CHECK (precio_unitario >= 0),
    PRIMARY KEY (id_orden, id_curso),
    CONSTRAINT fk_detalle_orden
        FOREIGN KEY (id_orden)
        REFERENCES orden(id_orden)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_detalle_curso
        FOREIGN KEY (id_curso)
        REFERENCES curso(id_curso)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE resena (
    id_estudiante VARCHAR(50) NOT NULL,
    id_curso      VARCHAR(50) NOT NULL,
    puntuacion    TINYINT     NOT NULL CHECK (puntuacion BETWEEN 1 AND 5),
    comentario    TEXT,
    fecha         DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id_estudiante, id_curso),
    CONSTRAINT fk_resena_inscripcion
        FOREIGN KEY (id_estudiante, id_curso)
        REFERENCES inscripcion(id_estudiante, id_curso)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE certificado (
    id_certificado      VARCHAR(50) PRIMARY KEY,
    id_estudiante       VARCHAR(50) NOT NULL,
    id_curso            VARCHAR(50) NOT NULL,
    fecha_emision       DATE        NOT NULL,
    codigo_verificacion VARCHAR(50) NOT NULL UNIQUE,
    CONSTRAINT uq_certificado UNIQUE (id_estudiante, id_curso),
    CONSTRAINT fk_certificado_inscripcion
        FOREIGN KEY (id_estudiante, id_curso)
        REFERENCES inscripcion(id_estudiante, id_curso)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE INDEX idx_curso_profesor     ON curso(id_profesor);
CREATE INDEX idx_curso_activo       ON curso(esta_activo);
CREATE INDEX idx_inscripcion_curso  ON inscripcion(id_curso);
CREATE INDEX idx_actividad_modulo   ON actividad(id_modulo);
CREATE INDEX idx_entrega_estudiante ON entrega(id_estudiante);
CREATE INDEX idx_orden_estudiante   ON orden(id_estudiante);