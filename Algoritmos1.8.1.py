
from collections import deque

grafos = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'A': [],
} 

def bfs(grafo, inicio):
    visitados = set()
    cola = deque([inicio])

    while cola:
        nodo = cola.popleft()
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino in grafo [nodo]:
            if vecino not in visitados:
                cola.append(vecino)
    return visitados

resultado = bfs(grafos, 'A')
print(f"Nodos visitados por BFS: {resultado}")