import sys

from datos import nombre_app,version_app

titulo = "Dovakinesapp y su fabulosa gestión de cursos ^^"

def menu_principal():
    print(f"{nombre_app} - {version_app}")
    print("=" * len(f"{nombre_app} - {version_app}"))

    while True:
        for (clave,valor in menu_principal):
            print(f"{clave}. {valor}")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Iniciando gestión de cursos...")
        elif opcion == "2":
            print("Mostrando cursos disponibles...")
        elif opcion == "3":
           print("Saliendo de la aplicación...")
        sys.exit()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.") 