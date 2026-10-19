USE campus_virtual;

-- Estados de comisiones de curso
INSERT INTO estados (estado, descripcion) VALUES
('ACTIVA', 'Comisión en curso, admite nuevas matrículas'),
('CERRADA', 'Comisión cerrada, sin nuevos estudiantes'),
('SUSPENDIDA', 'Comisión suspendida temporalmente'),
('FINALIZADA', 'Comisión finalizada y certificada');

-- Modalidades de las comisiones
INSERT INTO ubicaciones (ubicacion, detalles) VALUES
('Virtual', 'Clases en línea por videollamada'),
('Presencial', 'Clases en sede física de la escuela'),
('Híbrido', 'Combinación de clases virtuales y presenciales');

-- Tipos de dirección
INSERT INTO tipos_direccion (tipo_direccion, descripcion) VALUES
('Sede', 'Sede física de una escuela o programa'),
('Oficina', 'Oficina administrativa de la plataforma'),
('Casa', 'Dirección particular de un usuario');
