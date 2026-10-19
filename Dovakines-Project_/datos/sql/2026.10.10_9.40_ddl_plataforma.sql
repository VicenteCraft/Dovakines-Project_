CREATE DATABASE campus_virtual CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE campus_virtual;

CREATE TABLE tipos_direccion(
    id_tipo_direccion INTEGER AUTO_INCREMENT,
    tipo_direccion VARCHAR(20) NOT NULL,
    descripcion VARCHAR(100) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_tiposdireccion PRIMARY KEY (id_tipo_direccion)
) COMMENT = 'Tipos de dirección: sede, oficina y particular';

CREATE TABLE parametros(
    id_parametro INTEGER AUTO_INCREMENT,
    tipo VARCHAR(20) NOT NULL,
    parametro VARCHAR(50) NOT NULL,
    descripcion VARCHAR(100) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_parametros PRIMARY KEY (id_parametro)
) COMMENT = 'Parámetros de sistema. Categorías y niveles de cursos, idiomas de las ediciones, tipos de usuario, planes de estudiante';

CREATE TABLE estados(
    id_estado INTEGER AUTO_INCREMENT,
    estado VARCHAR(20) NOT NULL,
    descripcion VARCHAR(100) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_estados PRIMARY KEY (id_estado)
) COMMENT = 'Tabla de listado de estados de comisiones de curso';

CREATE TABLE ubicaciones(
    id_ubicacion INTEGER AUTO_INCREMENT,
    ubicacion VARCHAR(20) NOT NULL,
    detalles VARCHAR(100) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_ubicaciones PRIMARY KEY (id_ubicacion)
) COMMENT = 'Tabla de modalidad de las comisiones: virtual, presencial o híbrida';

CREATE TABLE paises(
    id_pais INTEGER AUTO_INCREMENT,
    nombre VARCHAR(60) NOT NULL,
    nacionalidad VARCHAR(50) NULL,
    iso_2 CHAR(2) NULL,
    iso_3 CHAR(3) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_paises PRIMARY KEY (id_pais)
) COMMENT = 'Tabla de paises y nacionalidades para asociar a instructor, programa y personas';

CREATE TABLE comunas(
    id_comuna INTEGER AUTO_INCREMENT,
    codigo_comuna CHAR(5) NOT NULL,
    comuna VARCHAR(60) NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_comunas PRIMARY KEY (id_comuna)
) COMMENT = 'Tabla de comunas de Chile de acuerdo a SUBDERE para asociar a direccion';

CREATE TABLE direcciones(
    id_direccion INTEGER AUTO_INCREMENT,
    parametro INTEGER NULL,
    comuna INTEGER NULL,
    calle VARCHAR(50) NULL,
    numero VARCHAR(5) NULL,
    departamento VARCHAR(5) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_direcciones PRIMARY KEY (id_direccion),
    CONSTRAINT fk_direcciones_tiposdireccion FOREIGN KEY (parametro) REFERENCES tipos_direccion(id_tipo_direccion),
    CONSTRAINT fk_direcciones_comunas FOREIGN KEY (comuna) REFERENCES comunas(id_comuna)
) COMMENT = 'Tabla de direcciones físicas de escuelas, programas y usuarios';

CREATE TABLE escuelas(
    id_escuela INTEGER AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    web VARCHAR(255) NULL,
    telefono VARCHAR(15) NULL,
    correo VARCHAR(255) NULL,
    direccion INTEGER NULL,

    CONSTRAINT pk_escuelas PRIMARY KEY (id_escuela),
    CONSTRAINT fk_escuelas_direcciones FOREIGN KEY (direccion) REFERENCES direcciones(id_direccion)
) COMMENT = 'Tabla de escuelas de la plataforma que agrupan cursos';

CREATE TABLE programas(
    id_programa INTEGER AUTO_INCREMENT,
    pais INTEGER NOT NULL,
    direccion INTEGER NULL,
    programa VARCHAR(100) NOT NULL,
    telefono VARCHAR(15) NULL,
    correo VARCHAR(255) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_programas PRIMARY KEY (id_programa),
    CONSTRAINT fk_programas_paises FOREIGN KEY (pais) REFERENCES paises(id_pais),
    CONSTRAINT fk_programas_direcciones FOREIGN KEY (direccion) REFERENCES direcciones(id_direccion)
) COMMENT = 'Tabla de programas académicos que publican ediciones de cursos';

CREATE TABLE instructores(
    id_instructor INTEGER AUTO_INCREMENT,
    pais INTEGER NULL,
    nombre VARCHAR(100) NULL,
    pseudonimo VARCHAR(25) NULL,
    fecha_nacimiento DATE NULL,
    fecha_ingreso DATE NULL,
    biografia TEXT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_instructores PRIMARY KEY (id_instructor),
    CONSTRAINT fk_instructores_paises FOREIGN KEY (pais) REFERENCES paises(id_pais)
) COMMENT = 'Tabla de instructores de la plataforma, crean y dictan cursos';

CREATE TABLE ediciones(
    id_edicion INTEGER AUTO_INCREMENT,
    programa INTEGER NULL,
    idioma INTEGER NULL,
    edicion VARCHAR(25) NULL,
    fecha_edicion DATE NULL,
    codigo VARCHAR(20) NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_ediciones PRIMARY KEY (id_edicion),
    CONSTRAINT fk_ediciones_programas FOREIGN KEY (programa) REFERENCES programas(id_programa),
    CONSTRAINT fk_ediciones_parametros FOREIGN KEY (idioma) REFERENCES parametros(id_parametro)
) COMMENT = 'Tabla de ediciones de los programas académicos, cada curso pertenece a una edición';

CREATE TABLE cursos(
    id_curso INTEGER AUTO_INCREMENT,
    instructor INTEGER NOT NULL,
    categoria INTEGER NOT NULL,
    edicion INTEGER NOT NULL,
    escuela INTEGER NOT NULL,
    titulo VARCHAR(100) NULL,
    horas INTEGER NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_cursos PRIMARY KEY (id_curso),
    CONSTRAINT fk_cursos_instructores FOREIGN KEY (instructor) REFERENCES instructores(id_instructor),
    CONSTRAINT fk_cursos_parametros FOREIGN KEY (categoria) REFERENCES parametros(id_parametro),
    CONSTRAINT fk_cursos_ediciones FOREIGN KEY (edicion) REFERENCES ediciones(id_edicion),
    CONSTRAINT fk_cursos_escuelas FOREIGN KEY (escuela) REFERENCES escuelas(id_escuela)
) COMMENT = 'Tabla de cursos de la plataforma';

CREATE TABLE usuarios(
    id_usuario INTEGER AUTO_INCREMENT,
    rut VARCHAR(11) NULL,
    nombre VARCHAR(25) NOT NULL,
    apellido VARCHAR(25) NOT NULL,
    correo VARCHAR(255) NOT NULL,
    pais INTEGER NULL,
    fecha_nacimiento DATE NULL,
    genero INTEGER NOT NULL,
    fecha_incorporacion DATE NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_usuarios PRIMARY KEY (id_usuario),
    CONSTRAINT fk_usuarios_paises FOREIGN KEY (pais) REFERENCES paises(id_pais)
) COMMENT = 'Tabla de usuarios de sistema. Administradores, instructores y estudiantes';

CREATE TABLE direcciones_usuarios(
    id_direccion_usuario INTEGER AUTO_INCREMENT,
    direccion INTEGER NOT NULL,
    usuario INTEGER NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_direccionesusuarios PRIMARY KEY (id_direccion_usuario),
    CONSTRAINT fk_direccionesusuarios_direcciones FOREIGN KEY (direccion) REFERENCES direcciones(id_direccion),
    CONSTRAINT fk_direccionesusuarios_usuarios FOREIGN KEY (usuario) REFERENCES usuarios(id_usuario)
) COMMENT = 'Tabla auxiliar de direcciones de usuarios';

CREATE TABLE administradores(
    id_administrador INTEGER AUTO_INCREMENT,
    usuario INTEGER NOT NULL,
    tipo_usuario INTEGER NOT NULL,
    contrasena CHAR(60) NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_administradores PRIMARY KEY (id_administrador),
    CONSTRAINT fk_administradores_usuarios FOREIGN KEY (usuario) REFERENCES usuarios(id_usuario),
    CONSTRAINT fk_administradores_parametros FOREIGN KEY (tipo_usuario) REFERENCES parametros(id_parametro)
) COMMENT = 'Tabla de usuarios de tipo administrador, gestionan cursos, instructores y matrículas de la plataforma';

CREATE TABLE estudiantes(
    id_estudiante INTEGER AUTO_INCREMENT,
    usuario INTEGER NOT NULL,
    categoria INTEGER NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_estudiantes PRIMARY KEY (id_estudiante),
    CONSTRAINT fk_estudiantes_usuarios FOREIGN KEY (usuario) REFERENCES usuarios(id_usuario),
    CONSTRAINT fk_estudiantes_parametros FOREIGN KEY (categoria) REFERENCES parametros(id_parametro)
) COMMENT = 'Tabla de usuarios de tipo estudiante, pueden matricularse en comisiones de cursos';

CREATE TABLE comisiones(
    id_comision INTEGER AUTO_INCREMENT,
    curso INTEGER NOT NULL,
    estado INTEGER NOT NULL,
    ubicacion INTEGER NOT NULL,

    CONSTRAINT pk_comisiones PRIMARY KEY (id_comision),
    CONSTRAINT fk_comisiones_cursos FOREIGN KEY (curso) REFERENCES cursos(id_curso),
    CONSTRAINT fk_comisiones_estados FOREIGN KEY (estado) REFERENCES estados(id_estado),
    CONSTRAINT fk_comisiones_ubicaciones FOREIGN KEY (ubicacion) REFERENCES ubicaciones(id_ubicacion)
) COMMENT = 'Registro de comisiones o grupos de cursos con su modalidad';

CREATE TABLE matriculas(
    id_matricula INTEGER AUTO_INCREMENT,
    comision INTEGER NOT NULL,
    estudiante INTEGER NOT NULL,
    fecha_matricula DATETIME NOT NULL DEFAULT NOW(),
    fecha_limite DATETIME NOT NULL,
    fecha_certificacion DATETIME NULL,

    CONSTRAINT pk_matriculas PRIMARY KEY (id_matricula),
    CONSTRAINT fk_matriculas_comisiones FOREIGN KEY (comision) REFERENCES comisiones(id_comision),
    CONSTRAINT fk_matriculas_estudiantes FOREIGN KEY (estudiante) REFERENCES estudiantes(id_estudiante)
) COMMENT = 'Registro de matrículas y certificaciones de estudiantes en comisiones';
