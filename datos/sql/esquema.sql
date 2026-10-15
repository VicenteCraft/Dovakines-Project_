-- Esquema de la base de datos "Curso_online"
-- Derivado del diagrama de clases UML validado en la Unidad 1.
-- Se ejecuta con: python crear_base.py

CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre     VARCHAR(100) NOT NULL,
    correo     VARCHAR(100) NOT NULL UNIQUE,
    contrasena VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS estudiante (
    id_usuario INT PRIMARY KEY,
    matricula  VARCHAR(50) NOT NULL UNIQUE,
    CONSTRAINT fk_estudiante_usuario
        FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS profesor (
    id_usuario   INT PRIMARY KEY,
    especialidad VARCHAR(100) NOT NULL,
    CONSTRAINT fk_profesor_usuario
        FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS curso (
    id_curso    INT AUTO_INCREMENT PRIMARY KEY,
    titulo      VARCHAR(150) NOT NULL,
    descripcion TEXT,
    esta_activo BOOLEAN NOT NULL DEFAULT TRUE,
    id_profesor INT NULL,
    CONSTRAINT fk_curso_profesor
        FOREIGN KEY (id_profesor) REFERENCES profesor (id_usuario)
        ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS inscripcion (
    id_inscripcion     INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante      INT NOT NULL,
    id_curso           INT NOT NULL,
    fecha_inscripcion  DATE NOT NULL,
    porcentaje_avance  DECIMAL(5,2) NOT NULL DEFAULT 0,
    estado             VARCHAR(20) NOT NULL DEFAULT 'activa',
    CONSTRAINT fk_inscripcion_estudiante
        FOREIGN KEY (id_estudiante) REFERENCES estudiante (id_usuario)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_inscripcion_curso
        FOREIGN KEY (id_curso) REFERENCES curso (id_curso)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS modulo (
    id_modulo INT AUTO_INCREMENT PRIMARY KEY,
    id_curso  INT NOT NULL,
    titulo    VARCHAR(150) NOT NULL,
    orden     INT NOT NULL DEFAULT 1,
    CONSTRAINT fk_modulo_curso
        FOREIGN KEY (id_curso) REFERENCES curso (id_curso)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS contenido (
    id_contenido INT AUTO_INCREMENT PRIMARY KEY,
    id_modulo    INT NOT NULL,
    titulo       VARCHAR(150) NOT NULL,
    tipo         VARCHAR(30) NOT NULL,
    url_recurso  VARCHAR(255),
    CONSTRAINT fk_contenido_modulo
        FOREIGN KEY (id_modulo) REFERENCES modulo (id_modulo)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS actividad (
    id_actividad INT AUTO_INCREMENT PRIMARY KEY,
    id_modulo    INT NOT NULL,
    titulo       VARCHAR(150) NOT NULL,
    descripcion  TEXT,
    CONSTRAINT fk_actividad_modulo
        FOREIGN KEY (id_modulo) REFERENCES modulo (id_modulo)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS actividad_evaluada (
    id_actividad INT PRIMARY KEY,
    ponderacion  DECIMAL(5,2) NOT NULL,
    fecha_limite DATE NOT NULL,
    nota_maxima  FLOAT NOT NULL DEFAULT 7.0,
    CONSTRAINT fk_evaluada_actividad
        FOREIGN KEY (id_actividad) REFERENCES actividad (id_actividad)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS actividad_formativa (
    id_actividad       INT PRIMARY KEY,
    solucion_sugerida  TEXT,
    CONSTRAINT fk_formativa_actividad
        FOREIGN KEY (id_actividad) REFERENCES actividad (id_actividad)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS entrega (
    id_entrega             INT AUTO_INCREMENT PRIMARY KEY,
    id_actividad_evaluada  INT NOT NULL,
    fecha_envio            DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    archivo_respuesta      VARCHAR(255),
    calificacion           FLOAT NULL,
    CONSTRAINT fk_entrega_actividad
        FOREIGN KEY (id_actividad_evaluada) REFERENCES actividad_evaluada (id_actividad)
        ON DELETE CASCADE ON UPDATE CASCADE
);
