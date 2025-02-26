datos_temperatura = {
    "mexico": 20,
    "oaxaca": 25,
    "guadalajara": 18,
    "puebla": 22,
    "queretaro": 15
}

def predecir_ciudad(temperatura):
    if temperatura == datos_temperatura["mexico"]:
        return "mexico"
    elif temperatura == datos_temperatura["oaxaca"]:
        return "oaxaca"
    elif temperatura == datos_temperatura["guadalajara"]:
        return "guadalajara"
    elif temperatura == datos_temperatura["puebla"]:
        return "puebla"
    elif temperatura == datos_temperatura["queretaro"]:
        return "queretaro"
    else:
        return "Temperatura no encontrada"

temperatura = float(input("Ingrese la temperatura en °C: "))

ciudad = predecir_ciudad(temperatura)

if ciudad != "Temperatura no encontrada":
    print(f"La ciudad con una temperatura de {temperatura}°C es {ciudad.capitalize()}.")
else:
    print(ciudad)