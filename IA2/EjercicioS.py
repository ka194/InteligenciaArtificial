class Agente:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion 
    
    def mover(self, nueva_ubicacion):
        self.ubicacion = nueva_ubicacion
        print(f"{self.nombre} se movió a {self.ubicacion}")

agente1 = Agente("Agente 1", "A")
agente2 = Agente("Agente 2", "B")

agente1.mover("C")
agente2.mover("C")

if agente1.ubicacion == agente2.ubicacion:
    print("Los agentes se han encontrado en el punto C")
else:
    print("Los agentes no se han encontrado")