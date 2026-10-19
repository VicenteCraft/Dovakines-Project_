USE campus_virtual;

/* Parámetros de la plataforma: categorías y niveles de cursos, tipos de usuario y planes de estudiante */

INSERT INTO parametros (tipo, parametro, descripcion) VALUES
('CATEGORIA', 'PROGRAMACION', 'Programación y Desarrollo'),
('CATEGORIA', 'DISENO', 'Diseño y Creatividad'),
('CATEGORIA', 'DATOS', 'Ciencia de Datos e Inteligencia Artificial'),
('CATEGORIA', 'NEGOCIOS', 'Negocios y Gestión'),
('CATEGORIA', 'MARKETING', 'Marketing Digital'),
('NIVEL', 'BASICO', 'Nivel Básico'),
('NIVEL', 'INTERMEDIO', 'Nivel Intermedio'),
('NIVEL', 'AVANZADO', 'Nivel Avanzado'),
('TIPO_USUARIO', 'ADMIN', 'Administrador de plataforma'),
('TIPO_USUARIO', 'INSTRUCTOR', 'Instructor o creador de cursos'),
('TIPO_USUARIO', 'ESTUDIANTE', 'Estudiante de la plataforma'),
('ESTUDIANTE', 'GRATUITO', 'Plan gratuito con acceso limitado'),
('ESTUDIANTE', 'PREMIUM', 'Plan premium con acceso completo'),
('ESTUDIANTE', 'EMPRESA', 'Cuenta corporativa de empresa');
