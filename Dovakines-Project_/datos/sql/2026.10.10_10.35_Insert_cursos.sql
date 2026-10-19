USE campus_virtual;

/* Ediciones de los programas académicos */

INSERT INTO ediciones (programa, idioma, edicion, fecha_edicion, codigo) VALUES
(1, (SELECT id_parametro FROM parametros WHERE tipo = 'IDIOMA' AND parametro = 'ES'), '2026-1', STR_TO_DATE('01/03/2026', '%d/%m/%Y'), 'DW-2026-1'),
(1, (SELECT id_parametro FROM parametros WHERE tipo = 'IDIOMA' AND parametro = 'ES'), '2026-2', STR_TO_DATE('01/08/2026', '%d/%m/%Y'), 'DW-2026-2'),
(2, (SELECT id_parametro FROM parametros WHERE tipo = 'IDIOMA' AND parametro = 'ES'), '2026-1', STR_TO_DATE('15/03/2026', '%d/%m/%Y'), 'DS-2026-1'),
(3, (SELECT id_parametro FROM parametros WHERE tipo = 'IDIOMA' AND parametro = 'ES'), '2026-1', STR_TO_DATE('01/04/2026', '%d/%m/%Y'), 'DD-2026-1');

/* Cursos de la plataforma */

INSERT INTO cursos (instructor, categoria, edicion, escuela, titulo, horas) VALUES
((SELECT id_instructor FROM instructores WHERE nombre = 'Juan Pablo Contreras'), (SELECT id_parametro FROM parametros WHERE tipo = 'CATEGORIA' AND parametro = 'PROGRAMACION'), 1, 1, 'Introducción a Python', 40),
((SELECT id_instructor FROM instructores WHERE nombre = 'Valentina Ortiz Rojas'), (SELECT id_parametro FROM parametros WHERE tipo = 'CATEGORIA' AND parametro = 'PROGRAMACION'), 1, 1, 'JavaScript moderno ES6+', 35),
((SELECT id_instructor FROM instructores WHERE nombre = 'Valentina Ortiz Rojas'), (SELECT id_parametro FROM parametros WHERE tipo = 'CATEGORIA' AND parametro = 'PROGRAMACION'), 1, 1, 'React desde cero', 45),
((SELECT id_instructor FROM instructores WHERE nombre = 'Juan Pablo Contreras'), (SELECT id_parametro FROM parametros WHERE tipo = 'CATEGORIA' AND parametro = 'PROGRAMACION'), 1, 1, 'Bases de datos relacionales con SQL', 30),
((SELECT id_instructor FROM instructores WHERE nombre = 'Diego Muñoz Soto'), (SELECT id_parametro FROM parametros WHERE tipo = 'CATEGORIA' AND parametro = 'PROGRAMACION'), 2, 1, 'Docker y Kubernetes en la práctica', 25),
((SELECT id_instructor FROM instructores WHERE nombre = 'Camila Rojas Vargas'), (SELECT id_parametro FROM parametros WHERE tipo = 'CATEGORIA' AND parametro = 'DATOS'), 3, 1, 'Análisis de datos con Pandas', 40),
((SELECT id_instructor FROM instructores WHERE nombre = 'Fernanda Castillo Vidal'), (SELECT id_parametro FROM parametros WHERE tipo = 'CATEGORIA' AND parametro = 'DATOS'), 3, 1, 'Machine Learning con scikit-learn', 50),
((SELECT id_instructor FROM instructores WHERE nombre = 'Rodrigo Salas Pereira'), (SELECT id_parametro FROM parametros WHERE tipo = 'CATEGORIA' AND parametro = 'DISENO'), 4, 2, 'Diseño de interfaces con Figma', 30),
((SELECT id_instructor FROM instructores WHERE nombre = 'Rodrigo Salas Pereira'), (SELECT id_parametro FROM parametros WHERE tipo = 'CATEGORIA' AND parametro = 'DISENO'), 4, 2, 'UX Research aplicado', 20),
((SELECT id_instructor FROM instructores WHERE nombre = 'María Fernanda López'), (SELECT id_parametro FROM parametros WHERE tipo = 'CATEGORIA' AND parametro = 'NEGOCIOS'), 4, 2, 'Gestión ágil de proyectos', 30),
((SELECT id_instructor FROM instructores WHERE nombre = 'Andrés Paredes Gómez'), (SELECT id_parametro FROM parametros WHERE tipo = 'CATEGORIA' AND parametro = 'MARKETING'), 4, 2, 'Estrategia de contenidos y SEO', 25);

/* Comisiones de los cursos */

INSERT INTO comisiones (curso, estado, ubicacion) VALUES
(1, (SELECT id_estado FROM estados WHERE estado = 'ACTIVA'), (SELECT id_ubicacion FROM ubicaciones WHERE ubicacion = 'Virtual')),
(2, (SELECT id_estado FROM estados WHERE estado = 'ACTIVA'), (SELECT id_ubicacion FROM ubicaciones WHERE ubicacion = 'Virtual')),
(3, (SELECT id_estado FROM estados WHERE estado = 'ACTIVA'), (SELECT id_ubicacion FROM ubicaciones WHERE ubicacion = 'Virtual')),
(4, (SELECT id_estado FROM estados WHERE estado = 'ACTIVA'), (SELECT id_ubicacion FROM ubicaciones WHERE ubicacion = 'Virtual')),
(6, (SELECT id_estado FROM estados WHERE estado = 'ACTIVA'), (SELECT id_ubicacion FROM ubicaciones WHERE ubicacion = 'Virtual')),
(8, (SELECT id_estado FROM estados WHERE estado = 'ACTIVA'), (SELECT id_ubicacion FROM ubicaciones WHERE ubicacion = 'Presencial')),
(10, (SELECT id_estado FROM estados WHERE estado = 'CERRADA'), (SELECT id_ubicacion FROM ubicaciones WHERE ubicacion = 'Híbrido')),
(11, (SELECT id_estado FROM estados WHERE estado = 'ACTIVA'), (SELECT id_ubicacion FROM ubicaciones WHERE ubicacion = 'Virtual'));
