
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
        return "N/A"
    else:
        return "Calificación fuera de rango"

# Prueba del código
calificacion = int(input("Ingresa la calificación: "))
mensaje = evaluar_calificacion(calificacion)
print("Resultado:", mensaje)
