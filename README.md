# Dovakinesapp — Plataforma de gestión de cursos online

Programación orientado a objetos IEC-N2-C2 con el profesor Erick Bailey, trabajo hecho por: **Benjamín Monsalve, Cristóbal Vásquez y Vicente Galvez**

Asignatura **TI3021 — Programación Orientada a Objeto Seguro** · Unidad 2 · Evaluación Sumativa ES02.
Sistema desarrollado a partir del **diagrama de clases UML validado en la Unidad 1**
(`trabajos/galvez_vicente.drawio.png`).

---

## 1. Cómo ejecutar el sistema

```bash
pip install -r requirements.txt   # 1) instalar librerías
python crear_base.py              # 2) crear base, tablas y datos de ejemplo
python main.py                    # 3) ejecutar la aplicación
pytest -q                         # 4) (opcional) correr las pruebas
```

Requiere MySQL activo (WAMP). Las credenciales están en el archivo `.env`
(**nunca** se dejan contraseñas dentro del código fuente).

Datos de ejemplo creados por `crear_base.py`:

| Correo | Contraseña | Perfil |
|---|---|---|
| `ana@demo.cl` | `1234` | Estudiante (matrícula 2026-001) |
| `profe@demo.cl` | `1234` | Profesor |
| `juan@demo.cl` | `1234` | Estudiante (creado desde el menú) |

---

## 2. Estructura (arquitectura por capas)

```
Dovakines-Project_-1/
├── main.py                     → punto de entrada: prueba conexión + menú
├── crear_base.py               → crea BD, tablas (esquema.sql) y datos de ejemplo
├── .env                        → datos de conexión (no subir contraseñas al código)
├── requirements.txt            → solo las librerías usadas
├── datos/                      → CAPA DE DATOS
│   ├── conexion.py             → conexión con mysql-connector-python + helpers SQL
│   ├── models.py               → las 11 clases del UML (POO puro, sin BD)
│   ├── auxiliar.py             → menús y datos de la aplicación
│   ├── sql/esquema.sql         → esquema de tablas derivado del UML
│   └── repositorio/            → SQL de cada tabla (CRUD)
│       ├── repositorio_cursos.py
│       ├── repositorio_usuarios.py
│       └── repositorio_inscripciones.py
├── negocio/                    → CAPA DE NEGOCIO (reglas, sin imprimir en pantalla)
│   └── negocio_cursos.py
├── presentacion/               → CAPA DE PRESENTACIÓN
│   ├── menu.py                 → menús + try/except
│   ├── presentacion_cursos.py  → tablas en pantalla
│   └── validaciones.py         → validación de entradas del usuario
├── tests/test_sistema.py       → 14 pruebas automáticas (pytest)
└── trabajos/                   → evidencias (diagrama UML, DDL de la Unidad 1)
```

**Regla de dependencias:** `presentacion → negocio → repositorio → models/conexion`.
Las clases (`models.py`) no importan la base de datos: se pueden probar aisladas.

---

## 3. Coherencia con el diagrama UML (criterio 2.1.1 y 2.1.2)

Las 11 clases del diagrama existen en `datos/models.py` con **atributos, constructor
(`__init__`) y métodos**:

| Clase UML | Herencia / relación | Métodos implementados |
|---|---|---|
| `usuario` | clase base | `iniciar_sesion()`, `actualizar_perfil()` |
| `estudiante` | **hereda** de `usuario` | `inscribirse_curso()`, `ver_avance()` |
| `profesor` | **hereda** de `usuario` | `crear_curso()`, `calificar_entrega()` |
| `inscripcion` | relación estudiante↔curso | `calcular_avance()`, `actualizar_estado()` |
| `curso` | composición con `modulo` | `agregar_modulo()`, `listar_estudiantes()`, `obtener_estadisticas()` |
| `modulo` | composición con contenido/actividad | `agregar_contenido()`, `agregar_actividad()` |
| `contenido` | — | `obtener_detalle()` |
| `actividad` | clase base | `mostrar_instrucciones()` |
| `actividad_evaluada` | **hereda** de `actividad` | `recibir_entrega()` |
| `actividad_formativa` | **hereda** de `actividad` | `mostrar_solucion()` |
| `entrega` | — | `calificar()` |

**Principios de POO aplicados:**

- **Encapsulamiento:** `Usuario.__contrasena` es privada y solo se lee mediante la
  *property* `contrasena` (no existe *setter*: no se puede modificar desde fuera).
  `Curso.modulos` y `Curso.inscripciones` se manipulan solo con los métodos de la clase.
- **Herencia:** `Estudiante(Usuario)`, `Profesor(Usuario)`, `ActividadEvaluada(Actividad)`,
  `ActividadFormativa(Actividad)` → se reutiliza el código de la clase madre con `super()`.
- **Abstracción/métodos:** toda la lógica está en métodos con nombre del UML, no repartida
  en scripts sueltos.
- **Sin duplicación:** una sola clase `Curso` y una sola conexión (`datos/conexion.py`).

---

## 4. Base de datos (criterio 2.1.3)

- **Librería oficial:** `mysql-connector-python` (el conector oficial de MySQL para Python).
- **Conexión:** `datos/conexion.py` lee `.env` con `python-decouple`; expone
  `consultar()` (SELECT) y `ejecutar()` (INSERT/UPDATE/DELETE) que usan **parámetros `%s`**
  → el usuario **nunca** se concatena al SQL (**previene inyección SQL**).
- **Esquema:** `datos/sql/esquema.sql` crea las **11 tablas** del UML con llaves
  foráneas (`FOREIGN KEY`) reales: `usuario, estudiante, profesor, curso, inscripcion,
  modulo, contenido, actividad, actividad_evaluada, actividad_formativa, entrega`.

### Operaciones CRUD

| Operación | Menú | Función | SQL |
|---|---|---|---|
| **Registro** | 2.1 Crear curso | `negocio.crear_curso()` → `repositorio_cursos.guardar()` | `INSERT INTO curso ...` |
| **Consulta** | 1 Ver cursos / 2.2 Detalle | `negocio.cargar_cursos()` → `listar_todos()` | `SELECT * FROM curso ...` |
| **Actualización** | 2.3 Actualizar | `negocio.actualizar_curso()` → `guardar()` | `UPDATE curso SET ...` |
| **Eliminación** | 2.4 Eliminar | `negocio.eliminar_curso()` → `eliminar()` | `UPDATE curso SET esta_activo = FALSE` |

Extras: registro e inscripción de estudiantes (`INSERT INTO usuario/estudiante/inscripcion`,
`SELECT` con `INNER JOIN`) y login (`SELECT ... WHERE correo = %s`).

---

## 5. Manejo de errores y validaciones (criterio 2.1.4)

| Tipo de error | Excepción capturada | Dónde |
|---|---|---|
| Dato malo del usuario (texto vacío, correo inválido, id no numérico) | validaciones en `presentacion/validaciones.py` (pregunta **hasta** que el dato sea válido) | antes de llegar a la BD |
| Regla de negocio violada (curso inexistente, matrícula duplicada, nota fuera de rango…) | `ValueError` → mensaje `Error de validacion: ...` | `try/except ValueError` en `menu.py` |
| Falla de la base de datos (servidor caído, tabla inexistente, dato duplicado) | `mysql.connector.Error` → mensaje `Error de base de datos: ...` | `try/except Error` en `menu.py` |
| Archivo `.env` incompleto | `decouple.UndefinedValueError` | `main.py` y `crear_base.py` |
| Cierre con Ctrl+C o terminal cerrada | `EOFError`, `KeyboardInterrupt` → `Hasta luego.` | `main.py` y `menu.py` |

El sistema **no se interrumpe** por un error: lo informa y sigue en el menú.
Las clases también validan (`Curso` exige título; `Entrega.calificar()` acepta notas
entre 0 y 7; `Inscripcion.actualizar_estado()` solo acepta estados conocidos).

---

## 6. Decisiones de implementación respecto al UML

| Punto | UML | Implementación | Justificación |
|---|---|---|---|
| Identificadores (`id_curso`, `id_usuario`…) | `String` | `INT AUTO_INCREMENT` | Evita inventar códigos en Python; la base de datos los genera y son claves primarias nativas. |
| `iniciar_sesion()` | sin parámetros | `iniciar_sesion(contrasena)` | Sin la contraseña a comparar el método no podría validar nada. |
| `profesor ◆ curso` (composición) | asociación | atributo `id_profesor` con `FOREIGN KEY` | Relación persistida entre tablas; en la clase, `curso.profesor`. |
| Eliminación de cursos | `esta_activo: bool` | eliminación **lógica** (`esta_activo = FALSE`) | Respetar el atributo del UML y no perder inscripciones referenciadas. |
| Contraseñas | `contraseña: string` | texto plano en `.env`/tabla | Fuera de alcance de la Unidad 2; mejora futura: `hashlib`/`bcrypt`. |

---

## 7. Validación crítica del código generado con IA (criterio 2.1.5)

> ⚠️ **Este apartado es una base que deben revisar, adaptar con sus propias palabras
> y estudiar antes de la defensa oral.** No se puede leer tal cual: el profesor
> preguntará *por qué* se tomó cada decisión.

| Fragmento / decisión asistida por IA | Acción (adoptar / modificar / descartar) | Justificación técnica |
|---|---|---|
| Estructura de las 11 clases del UML (`models.py`) | **Adoptar** | Coincide atributo por atributo con el diagrama validado; se revisó que cada método tenga sentido de primer año. |
| Uso de `mysql-connector-python` con SQL parametrizado | **Adoptar** | Es la librería oficial de MySQL y los parámetros `%s` evitan la inyección SQL. |
| Reemplazo de la capa ORM (peewee) por SQL explícito | **Modificar** | Se descarta la magia del ORM: en el curso se pide comprender la conexión y las operaciones; el SQL queda visible para poder explicarlo en la defensa. |
| `iniciar_sesion()` con parámetro | **Modificar** | Corrige una falencia del diseño original (ver tabla anterior). |
| Almacenar contraseñas en claro | **Descartar como solución definitiva** | Es inseguro; se documenta como mejora futura con hash, fuera del alcance de esta entrega. |
| Eliminar las clases `Asignacion`, `Evaluacion`, `Calificacion`, `Asistencia` y las capas de comunas/bibliotecas | **Descartar** | No existen en el diagrama UML: rompían la coherencia con el modelo validado. |
| Pruebas automatizadas (`tests/test_sistema.py`) | **Adoptar** | Permiten comprobar herencia, encapsulamiento, métodos del UML y validaciones sin necesitar la base. |

**Recomendación de uso responsable de IA:** todo código generado se revisó, se ejecutó
(`pytest -q` + pruebas manuales del menú) y se ajustó al modelo; la responsabilidad del
funcionamiento y de la defensa es del equipo.

---

## 8. Pruebas automáticas

```bash
pytest -q        # 14 pruebas
```

Cubren: herencia (`Estudiante`/`Profesor` → `Usuario`), encapsulamiento de la contraseña,
todos los métodos del UML (`iniciar_sesion`, `crear_curso`, `agregar_modulo`,
`listar_estudiantes`, `obtener_estadisticas`, `calcular_avance`, `ver_avance`,
`calificar`, `recibir_entrega`, `mostrar_solucion`…) y las validaciones de entrada.
