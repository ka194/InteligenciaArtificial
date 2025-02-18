# Ejemplo simple de adquisición de conocimiento a través de la observación  

# El sistema aprenderá la relación entre las horas del día y la temperatura promedio  
datos_temperatura = {  
    "mañana": 20,  
    "tarde": 25,  
    "noche": 18,  
    "amanecer": 22,  
    "anochecer": 21  
}  

# El sistema hace predicciones de temperatura basándose en la observación  
def predecir_temperatura(hora):  
    hora = hora.strip().lower()  # Limpia espacios y convierte a minúsculas
    if hora in datos_temperatura:
        return datos_temperatura[hora]
    else:
        return "Hora no válida"  

# Ejemplo de uso    
hora = input("Ingrese la hora (mañana, tarde, noche, amanecer, anochecer): ").strip().lower()
print(f"La temperatura promedio en la {hora} es: {predecir_temperatura(hora)}°C")
 