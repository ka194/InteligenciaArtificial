class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

nodo1 = Nodo(input("Introduce el primer nombre: "))
nodo2 = Nodo(input("Introduce el segundo nombre: "))
nodo3 = Nodo(input("Introduce el tercer nombre: "))
nodo4 = Nodo(input("Introduce el cuarto nombre: "))

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4

print("\nNombres de la lista enlazada:")
print(nodo1.valor, "->", nodo1.siguiente.valor, "->", nodo1.siguiente.siguiente.valor, "->", nodo1.siguiente.siguiente.siguiente.valor)
