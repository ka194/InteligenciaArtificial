import os  # Para manejar archivos y ejecutar comandos del sistema

# Ruta base donde se encuentran los ejercicios
RUTA_BASE = r"C:\Users\karyn\OneDrive\Documentos\IA"

def mostrar_menu():
    """Muestra el menú de opciones en la consola."""
    print("\n======= Menú de Ejercicios de Inteligencia Artificial - Unidad 1 =======")
    print("1. Listar ejercicios disponibles")
    print("2. Ejecutar un ejercicio")
    print("3. Salir")

def listar_ejercicios():
    """Lista los archivos Python disponibles en la carpeta."""
    print("\n📌 Ejercicios disponibles en la carpeta:")
    try:
        archivos = [f for f in os.listdir(RUTA_BASE) if f.endswith(".py")]  # Filtrar solo archivos .py
        if not archivos:
            print("⚠️ No hay ejercicios disponibles.")
        else:
            for idx, archivo in enumerate(archivos, start=1):
                print(f"{idx}. {archivo}")
        return archivos
    except FileNotFoundError:
        print("❌ Error: La ruta especificada no existe.")
        return []

def ejecutar_ejercicio():
    """Permite al usuario seleccionar y ejecutar un ejercicio."""
    archivos = listar_ejercicios()
    if not archivos:
        return

    try:
        seleccion = int(input("\n👉 Selecciona el número del ejercicio a ejecutar: ")) - 1
        if 0 <= seleccion < len(archivos):
            archivo_ejecutar = os.path.join(RUTA_BASE, archivos[seleccion])
            print(f"\n🚀 Ejecutando: {archivo_ejecutar}...\n")
            os.system(f'python "{archivo_ejecutar}"')  # Ejecutar el script seleccionado
        else:
            print("⚠️ Selección fuera de rango. Intenta de nuevo.")
    except ValueError:
        print("❌ Entrada no válida. Ingresa un número.")

def menu_interactivo():
    """Función principal que controla el menú interactivo."""
    while True:
        mostrar_menu()
        opcion = input("👉 Selecciona una opción (1/2/3): ")

        if opcion == "1":
            listar_ejercicios()
        elif opcion == "2":
            ejecutar_ejercicio()
        elif opcion == "3":
            print("👋 Saliendo del menú. ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

# Ejecutar el menú interactivo
if __name__ == "__main__":
    menu_interactivo()
