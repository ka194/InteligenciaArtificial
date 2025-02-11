
total_compra = float("ingresa el total de tu compra:"))
if total_compra > 100:
    descuento = total_compra * 0.10
    total_final = total_compra - descuento
print(f" ¡Felicidades! Tienes un descuento del 10%. El total a pagar es: {total_final}  ")
else:
    print(f"El total a pagar es: {total_compra}")