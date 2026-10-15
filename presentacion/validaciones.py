"""Validacion de las entradas del usuario (Paso 4 de la pauta).

Las funciones 'validar_*' no leen el teclado: revisan un valor y devuelven
un mensaje de error (o None si el dato esta bien). Por eso se pueden probar
con pytest sin necesidad de base de datos.
"""


def validar_texto(valor, minimo=1, maximo=100):
    """Devuelve un mensaje de error o None si el texto es valido."""
    if valor is None:
        return "El dato no puede ser nulo."
    texto = str(valor).strip()
    if len(texto) < minimo:
        return f"Debe tener al menos {minimo} caracteres."
    if len(texto) > maximo:
        return f"Como maximo puede tener {maximo} caracteres."
    return None


def validar_correo(valor):
    """Valida el formato basico de un correo: usuario@dominio."""
    texto = (str(valor) if valor is not None else "").strip()
    if "@" not in texto:
        return "Debe contener '@'."
    dominio = texto.split("@")[-1]
    if "." not in dominio or dominio.startswith(".") or dominio.endswith("."):
        return "Debe tener formato usuario@dominio (ej: ana@correo.cl)."
    return None


def validar_entero(valor, minimo=None, maximo=None):
    """Valida que el valor sea un entero dentro del rango.

    Devuelve la tupla (numero, mensaje_de_error). Si el dato esta bien,
    el mensaje es None; si no, el numero es None.
    """
    try:
        numero = int(str(valor).strip())
    except (TypeError, ValueError):
        return None, "Debe ser un numero entero."
    if minimo is not None and numero < minimo:
        return None, f"Debe ser mayor o igual a {minimo}."
    if maximo is not None and numero > maximo:
        return None, f"Debe ser menor o igual a {maximo}."
    return numero, None


# ---------------------------------------------------------------------------
# Lectura desde teclado: repite la pregunta mientras el dato no sea valido.
# ---------------------------------------------------------------------------

def pedir_texto(mensaje, minimo=1, maximo=100):
    while True:
        entrada = input(mensaje)
        error = validar_texto(entrada, minimo, maximo)
        if error is None:
            return entrada.strip()
        print(f"   Dato invalido: {error}")


def pedir_correo(mensaje):
    while True:
        entrada = input(mensaje).strip()
        error = validar_correo(entrada)
        if error is None:
            return entrada
        print(f"   Dato invalido: {error}")


def pedir_entero(mensaje, minimo=1, maximo=None, vacio_permitido=False):
    """Lee un entero; con vacio_permitido=True devuelve None si se presiona Enter."""
    while True:
        entrada = input(mensaje).strip()
        if vacio_permitido and entrada == "":
            return None
        numero, error = validar_entero(entrada, minimo, maximo)
        if error is None:
            return numero
        print(f"   Dato invalido: {error}")


def pedir_contrasena(mensaje):
    """Lee una contrasena minima de 4 caracteres."""
    return pedir_texto(mensaje, minimo=4, maximo=100)
