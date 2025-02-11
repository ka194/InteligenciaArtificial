
import datetime

nombre = input ("ingresa tu nombre")

fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%5")
print("Nombre del cliente: {nombre} y la fecha y hora: {fecha}")
