USE campus_virtual;

-- Direcciones de sedes y oficinas
INSERT INTO direcciones (parametro, comuna, calle, numero, departamento) VALUES
((SELECT id_tipo_direccion FROM tipos_direccion WHERE tipo_direccion = 'Sede'), (SELECT id_comuna FROM comunas WHERE comuna = 'Santiago'), 'Avenida Providencia', '1234', NULL),
((SELECT id_tipo_direccion FROM tipos_direccion WHERE tipo_direccion = 'Sede'), (SELECT id_comuna FROM comunas WHERE comuna = 'Providencia'), 'Avenida Manuel Montt', '567', NULL),
((SELECT id_tipo_direccion FROM tipos_direccion WHERE tipo_direccion = 'Oficina'), (SELECT id_comuna FROM comunas WHERE comuna = 'Las Condes'), 'Avenida Apoquindo', '4501', '1201');

-- Escuelas de la plataforma
INSERT INTO escuelas (nombre, web, telefono, correo, direccion) VALUES
('Escuela de Tecnología', 'https://campusvirtual.cl/tecnologia', '+56 2 2345 6789', 'tecnologia@campusvirtual.cl', 1),
('Escuela de Diseño y Creatividad', 'https://campusvirtual.cl/diseno', '+56 2 2345 6790', 'diseno@campusvirtual.cl', 2);

-- Programas académicos
INSERT INTO programas (pais, direccion, programa, telefono, correo) VALUES
((SELECT id_pais FROM paises WHERE nombre = 'Chile'), 3, 'Bootcamp Desarrollo Web', '+56 2 2345 6800', 'web@campusvirtual.cl'),
((SELECT id_pais FROM paises WHERE nombre = 'Chile'), 3, 'Diplomado Ciencia de Datos', '+56 2 2345 6801', 'datos@campusvirtual.cl'),
((SELECT id_pais FROM paises WHERE nombre = 'Chile'), NULL, 'Programa de Diseño Digital', '+56 2 2345 6802', 'diseno@campusvirtual.cl');
