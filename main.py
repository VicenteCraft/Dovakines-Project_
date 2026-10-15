from datos.modelo_base import modelo_inicial
from presentacion import menu_principal

try:
    modelo_inicial()
    print("Base de datos lista: tablas verificadas/creadas.\n")
except Exception as error:
    print("Aviso: no se pudo conectar a MySQL (¿está activo el servidor?).")
    print(f"Detalle del error: {error}\n")

try:
    menu_principal()
except (EOFError, KeyboardInterrupt):
    print("\nHasta luego.")
