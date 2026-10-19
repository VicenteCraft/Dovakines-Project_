USE campus_virtual;

/* Instructores de la plataforma */

INSERT INTO instructores (nombre, pseudonimo, pais, fecha_nacimiento, fecha_ingreso, biografia, habilitado) VALUES

('Juan Pablo Contreras', 'JPCode', (SELECT id_pais FROM paises WHERE nombre = 'Chile'), STR_TO_DATE('12/04/1988', '%d/%m/%Y'), STR_TO_DATE('01/03/2020', '%d/%m/%Y'), 'Ingeniero civil informático con más de 10 años de experiencia en desarrollo web.', 1),
('Camila Rojas Vargas', 'CamiData', (SELECT id_pais FROM paises WHERE nombre = 'Chile'), STR_TO_DATE('25/09/1992', '%d/%m/%Y'), STR_TO_DATE('15/08/2021', '%d/%m/%Y'), 'Data Scientist especializada en modelos predictivos y análisis de datos.', 1),
('Rodrigo Salas Pereira', NULL, (SELECT id_pais FROM paises WHERE nombre = 'Argentina'), STR_TO_DATE('03/11/1985', '%d/%m/%Y'), STR_TO_DATE('10/01/2022', '%d/%m/%Y'), 'Diseñador de producto y experto en experiencia de usuario.', 1),
('María Fernanda López', 'MaferPM', (SELECT id_pais FROM paises WHERE nombre = 'Uruguay'), STR_TO_DATE('17/06/1990', '%d/%m/%Y'), STR_TO_DATE('05/04/2021', '%d/%m/%Y'), 'Product Manager con enfoque en gestión ágil de equipos.', 1),
('Diego Muñoz Soto', 'DevOpsDM', (SELECT id_pais FROM paises WHERE nombre = 'Chile'), STR_TO_DATE('22/01/1987', '%d/%m/%Y'), STR_TO_DATE('20/09/2020', '%d/%m/%Y'), 'Ingeniero DevOps especializado en contenedores y despliegue continuo.', 1),
('Valentina Ortiz Rojas', 'ValenDev', (SELECT id_pais FROM paises WHERE nombre = 'Chile'), STR_TO_DATE('09/05/1995', '%d/%m/%Y'), STR_TO_DATE('12/07/2022', '%d/%m/%Y'), 'Desarrolladora frontend apasionada por JavaScript y accesibilidad web.', 1),
('Andrés Paredes Gómez', NULL, (SELECT id_pais FROM paises WHERE nombre = 'Colombia'), STR_TO_DATE('14/08/1989', '%d/%m/%Y'), STR_TO_DATE('03/02/2023', '%d/%m/%Y'), 'Especialista en marketing digital y estrategia de contenidos.', 1),
('Fernanda Castillo Vidal', 'FerCast', (SELECT id_pais FROM paises WHERE nombre = 'Brasil'), STR_TO_DATE('30/12/1991', '%d/%m/%Y'), STR_TO_DATE('18/06/2023', '%d/%m/%Y'), 'Ingeniera de datos con experiencia en pipelines y arquitecturas analíticas.', 1);
