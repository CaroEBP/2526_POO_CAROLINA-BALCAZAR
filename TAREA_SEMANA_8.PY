#ASIGNATURA: PROGRAMACION ORIENTADA A OBJETOS
#ESTUDIANTE: CAROLINA ELIZABETH BALCAZAR PARDO 
import os
import subprocess

def mostrar_codigo(ruta_script):
    """
    Muestra el contenido de un script Python en consola.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None


def ejecutar_codigo(ruta_script):
    """
    Ejecuta un script Python en una nueva ventana de consola.
    """
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix/Linux/Mac
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")


def mostrar_menu():
    """
    Muestra el menú principal del Dashboard adaptado.
    Permite seleccionar directamente las carpetas reales del repositorio.
    """
    ruta_base = os.path.dirname(__file__)

    # Carpetas principales de tu repositorio
    unidades = {
        '1': 'EjemplosMundoReal_POO',
        '2': 'SEMANA 3'
    }

    while True:
        print("\n=== Dashboard Personalizado ===")
        for key in unidades:
            print(f"{key} - {unidades[key]}")
        print("0 - Salir")

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")
        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            ruta_unidad = os.path.join(ruta_base, unidades[eleccion_unidad])
            if os.path.exists(ruta_unidad):
                mostrar_scripts(ruta_unidad)
            else:
                print(f"La carpeta {unidades[eleccion_unidad]} no existe en el proyecto.")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


def mostrar_scripts(ruta_unidad):
    """
    Muestra los scripts disponibles directamente en la carpeta seleccionada.
    """
    scripts = [f.name for f in os.scandir(ruta_unidad) if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\n--- Scripts disponibles ---")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al menú principal")

        eleccion_script = input("Elige un script o '0' para regresar: ")
        if eleccion_script == '0':
            break
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_unidad, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("No se ejecutó el script.")
                        else:
                            print("Opción no válida. Regresando al menú de scripts.")
                        input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    print("Bienvenido al Dashboard personalizado de Carolina")
    mostrar_menu()
