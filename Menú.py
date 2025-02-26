import random  
import datetime  

def mostrar_menu():
    print("\n======= MENÚ DE OPCIONES =======")
    print("1. Información Personal")
    print("2. Operaciones Matemáticas")
    print("3. Determinar si un número es Par o Impar")
    print("4. Determinar si un número es mayor a 10")
    print("5. Determinar si un número es positivo o negativo")
    print("6. Adivina el número")
    print("7. Conversión de Calificación a Letra") 
    print("8. Datos de temperatura") 
    print("9. Generar Ticket de Compra")
    print("10. Evaluar Nivel de Calificación")
    print("11. Datos personales")
    print("12. Suma de números")
    print("13. Lista enlazada de nombres")
    print("14. Movimiento de agentes")
    print("15. Verificar suma de números pares")
    print("16. Calcular área de un círculo")
    print("17. Tomar decisión basada en prioridades")
    print("18. Ingresar información académica")
    print("19. Calcular descuento en compra")
    print("0. Realizar operaciones matemáticas")
    print("0. Salir")

def informacion_personal():
    print("\n📌 Información Personal")
    N = input("Ingrese su Nombre Completo: ")
    C = input("Ingrese su Carrera: ")
    S = input("Ingrese su Semestre: ")
    M = input("Ingrese su Materia: ")
    
    print("\n📌 Datos ingresados:")
    print(f"Nombre: {N}")
    print(f"Carrera: {C}")
    print(f"Semestre: {S}")
    print(f"Materia: {M}")

def operaciones_matematicas():
    print("\n📌 Operaciones Matemáticas")
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))
    numero3 = float(input("Introduce el tercer número: "))
    numero4 = float(input("Introduce el cuarto número: "))

    resta = numero1 - numero2
    multiplicacion = numero3 * numero4

    print(f"\nEl resultado de la resta de {numero1} - {numero2} es: {resta}")
    print(f"El resultado de la multiplicación de {numero3} * {numero4} es: {multiplicacion}")

    print("\n¡Realizado por Karina!")

def determinar_paridad():
    print("\n📌 Determinar si un número es Par o Impar")
    num = int(input("Ingresa un número: "))
    print(f"{num} es {'par' if num % 2 == 0 else 'impar'}.")

def determinar_numero():
    print("\n📌 Determinar si un número es mayor a 10")
    num = int(input("Ingresa un número: "))
    print(f"{num} {'es mayor' if num > 10 else 'no es mayor'} que 10.")

def determinar_positivo_negativo():
    print("\n📌 Determinar si un número es positivo, negativo o cero")
    num = int(input("Ingresa un número: "))
    if num > 0:
        print(f"{num} es positivo.")
    elif num < 0:
        print(f"{num} es negativo.")
    else:
        print("El número es cero.")

def numero_aleatorio():
    print("\n📌 Adivina el número")
    numero_secreto = random.randint(1, 10)
    adivina = int(input("Adivina el número entre 1 y 10: "))

    print(f"El número aleatorio era {numero_secreto}")
    if adivina == numero_secreto:
        print("🎉 ¡Correcto! Has adivinado el número.")
    else:
        print("❌ Incorrecto. Inténtalo nuevamente.")

def convertir_calificacion():
    print("\n📌 Conversión de Calificación a Letra")
    nota = int(input("Ingresa tu calificación (0-100): "))

    if 90 <= nota <= 100:
        print("Tu calificación es: 'A'")
    elif 80 <= nota < 90:
        print("Tu calificación es: 'B'")
    elif 70 <= nota < 80:
        print("Tu calificación es: 'C'")
    elif 60 <= nota < 70:
        print("Tu calificación es: 'D'")
    else:
        print("Tu calificación es: 'F'")

def determinar_temperatura():
    print("\n📌 Datos de temperatura")
    datos_temperatura = {  
        "México": 25,  
        "Oaxaca": 28,  
        "Guadalajara": 22,  
        "Puebla": 20,  
        "Querétaro": 23  
    }  

    temperatura = float(input("Ingrese la temperatura en °C: "))
    
    ciudad_encontrada = None
    for ciudad, temp in datos_temperatura.items():
        if temperatura == temp:
            ciudad_encontrada = ciudad
            break

    if ciudad_encontrada:
        print(f"La ciudad con una temperatura de {temperatura}°C es {ciudad_encontrada}.")
    else:
        print("Temperatura no encontrada en la base de datos.")

def generar_ticket_compra():
    print("\n📌 Generar Ticket de Compra")
    nombre = input("Ingresa tu nombre: ")
    producto = input("Ingresa el nombre del producto: ")
    precio = float(input("Ingresa el precio del producto: "))
    cantidad = int(input("Ingresa la cantidad: "))

    total_compra = precio * cantidad
    descuento = total_compra * 0.10 if total_compra > 100 else 0
    total_final = total_compra - descuento

    folio = random.randint(1000, 9999)
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"""
==========================================
               TICKET DE COMPRA           
==========================================
Tienda: Tienda XYZ
Folio: {folio}
Fecha y hora: {fecha_hora}
------------------------------------------
Cliente: {nombre}
Producto: {producto}
Precio unitario: ${precio:.2f}
Cantidad: {cantidad}
Total de la compra: ${total_compra:.2f}
Descuento aplicado: ${descuento:.2f}
Total a pagar: ${total_final:.2f}
------------------------------------------
¡Gracias por tu compra! ¡Vuelve pronto!
==========================================
""")

def evaluar_calificacion_nivel():
    print("\n📌 Evaluar Nivel de Calificación")
    calificacion = int(input("Ingresa la calificación: "))
    
    if 95 <= calificacion <= 100:
        mensaje = "Excelente"
    elif 85 <= calificacion <= 94:
        mensaje = "Notable"
    elif 75 <= calificacion <= 84:
        mensaje = "Buena"
    elif 70 <= calificacion <= 74:
        mensaje = "Suficiente"
    else:
        mensaje = "Calificación fuera de rango"

    print(f"Mensaje: {mensaje}")
def datos_personales():
    print("\n📌 Datos Personales")
    nombre = input("¿Cuál es tu nombre? ")
    edad = int(input("¿Cuántos años tienes? "))
    altura = float(input("¿Cuánto mides? (en metros) "))
    print(f"Hola {nombre}, tienes {edad} años y mides {altura} metros.")

def suma_numeros():
    print("\n📌 Suma de los primeros N números")
    n = int(input("Ingrese un número: "))
    suma = sum(range(1, n + 1))
    print(f"La suma de los primeros {n} números es: {suma}")

def lista_enlazada():
    class Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.siguiente = None
    
    print("\n📌 Lista enlazada de nombres")
    nodo1 = Nodo(input("Introduce el primer nombre: "))
    nodo2 = Nodo(input("Introduce el segundo nombre: "))
    nodo3 = Nodo(input("Introduce el tercer nombre: "))
    nodo4 = Nodo(input("Introduce el cuarto nombre: "))
    
    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3
    nodo3.siguiente = nodo4
    
    print("\nNombres de la lista enlazada:")
    print(f"{nodo1.valor} -> {nodo2.valor} -> {nodo3.valor} -> {nodo4.valor}")

def movimiento_agentes():
    class Agente:
        def __init__(self, nombre, ubicacion):
            self.nombre = nombre
            self.ubicacion = ubicacion 
    
        def mover(self, nueva_ubicacion):
            self.ubicacion = nueva_ubicacion
            print(f"{self.nombre} se movió a {self.ubicacion}")
    
    print("\n📌 Movimiento de Agentes")
    agente1 = Agente("Agente 1", "A")
    agente2 = Agente("Agente 2", "B")
    
    agente1.mover("C")
    agente2.mover("C")
    
    if agente1.ubicacion == agente2.ubicacion:
        print("Los agentes se han encontrado en el punto C")
    else:
        print("Los agentes no se han encontrado")
def verificar_suma_pares():
    def es_par(num):
        return num % 2 == 0
    
    def suma_de_pares(a, b):
        if es_par(a) and es_par(b):
            suma = a + b
            return True, suma
        return False, None
    
    print("\n📌 Verificar suma de números pares")
    numero1 = int(input("Introduce el primer número par: "))
    numero2 = int(input("Introduce el segundo número par: "))
    
    if es_par(numero1) and es_par(numero2):
        es_suma_par, resultado = suma_de_pares(numero1, numero2)
        print(f"La suma de {numero1} y {numero2} es {resultado}, que es un número par.")
    else:
        print("Ambos números deben ser pares.")

def calcular_area_circulo():
    print("\n📌 Calcular área de un círculo")
    radio = float(input("Introduce el radio del círculo en metros: "))
    area = math.pi * (radio ** 2)
    print(f"\nEl área del círculo con radio {radio:.2f} metros es: {area:.2f} metros cuadrados.")

def tomar_decision():
    print("\n📌 Tomar decisión basada en prioridades")
    opciones = ["ir al cine", "estudiar", "hacer ejercicio"]
    prioridades = input("Introduce tus prioridades separadas por coma: ").split(",")
    
    for opcion in opciones:
        if opcion in prioridades:
            print(f"El agente decide: {opcion}")
            return
    print("El agente no decide nada")

def datos_academicos():
    print("\n📌 Ingresar Información Académica")
    nombre = input("Ingresa tu nombre: ")
    carrera = input("Ingresa tu carrera: ")
    semestre = int(input("Ingresa tu semestre: "))
    print(f"Nombre: {nombre}, Carrera: {carrera}, Semestre: {semestre}")

def calcular_descuento():
    print("\n📌 Calcular Descuento en Compra")
    total_compra = float(input("Ingresa el total de tu compra: "))
    if total_compra > 100:
        descuento = total_compra * 0.10
        total_final = total_compra - descuento
        print(f"¡Felicidades! Tienes un descuento del 10%. El total a pagar es: {total_final}")
    else:
        print(f"El total a pagar es: {total_compra}")

def operaciones_mate():
    print("\n📌 Realizar Operaciones Matemáticas")
    numero1 = int(input("Ingresa el primer número: "))
    numero2 = int(input("Ingresa el segundo número: "))
    resultado1 = numero1 - numero2
    print(f"El resultado de la resta es: {resultado1}")
    resultado2 = numero1 * numero2
    print(f"El resultado de la multiplicación es: {resultado2}")


# Bucle del menú
while True:
    mostrar_menu()
    opcion = input("👉 Ingrese el número del ejercicio que desea ejecutar: ")

    if opcion == "1":
        informacion_personal()
    elif opcion == "2":
        operaciones_matematicas()
    elif opcion == "3":
        determinar_paridad()
    elif opcion == "4":
        determinar_numero()
    elif opcion == "5":
        determinar_positivo_negativo()
    elif opcion == "6":
        numero_aleatorio()
    elif opcion == "7":
        convertir_calificacion() 
    elif opcion == "8":
        determinar_temperatura() 
    elif opcion == "9":
        generar_ticket_compra()
    elif opcion == "10": 
        evaluar_calificacion_nivel()
    elif opcion == "11":
        datos_personales()
    elif opcion == "12":
        suma_numeros()
    elif opcion == "13":
        lista_enlazada()
    elif opcion == "14":
        movimiento_agentes()
    elif opcion == "15":
        verificar_suma_pares()
    elif opcion == "16":
        calcular_area_circulo()
    elif opcion == "17":
        tomar_decision()
    elif opcion == "18":
        datos_academicos()
    elif opcion == "19":
        calcular_descuento()
    elif opcion == "20":
        operaciones_mate()
    elif opcion == "0":
        print("👋 Saliendo del programa... ¡Hasta luego!")
        break
    else:
        print("⚠ Opción no válida, intenta de nuevo.")
