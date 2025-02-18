
def es_par(num):
    """Verifica si un numero es par."""
    return num % 2 == 0
def suma_de_pares(a, b):
    """Verifica si la suma de dos numeros pares es par."""
    if es_par(a) and es_par(b):
        suma = a + b
        return True, suma # Devuelve true si la suma es par, junto con la suma 
    return False, None # Si no son pares, devuelve false 
# Interaccion con el usuario ´
print("Bienvenido a la demostracion del teorema: La suma de dos números pares es siempre es siempre par.")
numero1 = int(input("Introduce el primer número par:"))
numero2 = int(input("Intoduce el segundo número par:"))

# Verificar  si los ingresados son pares 
if es_par(numero1)and es_par(numero2)
es_suma_par, resultado = suma_de_pares(numero1, numero2)
if es_suma_par:
    print (f "La suma de {numero1} y {numero2} es {resultado}, que es un numero par.")
else:
    