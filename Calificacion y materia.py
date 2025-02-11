def evaluar_calificacion(calificacion):
    if 95 <= calificacion <= 100:
        return "Excelente"
    elif 85 <= calificacion <= 94:
        return "Notable"
    elif 75 <= calificacion <= 84:
        return "Buena"
    elif 70 <= calificacion <= 74:
        return "Suficiente"
    elif 60 <= calificacion <= 65:
        return "NA"
    else:
        return "Calificación fuera de rango"

# Solicitar datos al usuario
nombre = input("Ingresa tu nombre: ") 
materia = input("Ingresa la materia: ")
calificacion = int(input("Ingresa la calificación: "))

# Evaluar la calificación
mensaje = evaluar_calificacion(calificacion)

# Mostrar el resultado
print("\n--- RESULTADO ---")
print(f"Nombre: {nombre}")
print(f"Materia: {materia}")
print(f"La calificación ingresada es: {calificacion}")
print(f"Mensaje: {mensaje}")
