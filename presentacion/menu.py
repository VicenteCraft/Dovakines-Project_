import sys
from datos import nombre_app,version_app,main_menu

titulo = "Dovakinesapp y su fabulosa gestión de cursos ^^"

def menu_principal():
    print(f"{nombre_app} - {version_app}")
    print("=" * len(f"{nombre_app} - {version_app}"))

    while True:
        for clave,valor in main_menu.items():
            print(f"{clave}. {valor}")
        
        opcion_usuario = input("Seleccione una opción: ")

        if opcion_usuario == "1":
            print("Iniciando gestión de cursos...")
        elif opcion_usuario == "2":
            print("Mostrando cursos disponibles...")
        elif opcion_usuario == "3":
           print("Saliendo de la aplicación...")
        sys.exit()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.") 