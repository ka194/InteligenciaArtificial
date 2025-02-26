import datetime
import random


nombre = input("Ingresa tu nombre: ")
producto = input("Ingresa el nombre del producto: ")
precio = float(input("Ingresa el precio del producto: "))
cantidad = int(input("Ingresa la cantidad: "))


total_compra = precio * cantidad

descuento = 0

if total_compra > 100:
    descuento = total_compra * 0.10

total_final = total_compra - descuento


folio = random.randint(1000, 9999)
fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


ticket = f"""
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
"""

print(ticket)
