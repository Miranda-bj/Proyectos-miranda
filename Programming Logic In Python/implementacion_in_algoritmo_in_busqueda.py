'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN ALGORITMO DE BUSQUEDA A*
'''
# Implementa el algoritmo A* para buscar el camino más corto en un grafo, utilizando heurísticas.

# Pasos
# Paso 1: Define una clase Nodo que contenga información sobre el coste y la heurística.
# Paso 2: Define una clase Grafo que contenga los nodos y las conexiones con sus respectivos pesos.
# Paso 3: Implementa el método a_star que utilice una cola de prioridad para encontrar el camino más corto.
# Paso 4: Crea un ejemplo para usar el algoritmo en un grafo dado.

import heapq

class Nodo:
    def __init__(self, nombre, heuristica=0):
        self.nombre = nombre
        self.heuristica = heuristica
        self.gasto = float('inf')  # Coste desde el nodo inicial

    def __lt__(self, other):
        return (self.gasto + self.heuristica) < (other.gasto + other.heuristica)

class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_arista(self, desde, hacia, peso):
        if desde not in self.nodos:
            self.nodos[desde] = []
        self.nodos[desde].append((hacia, peso))

    def a_star(self, inicio, fin, heuristicas):
        nodo_inicial = Nodo(inicio, heuristica=heuristicas[inicio])
        nodo_inicial.gasto = 0
        cola_prioridad = [nodo_inicial]
        visitados = set()

        while cola_prioridad:
            nodo_actual = heapq.heappop(cola_prioridad)

            if nodo_actual.nombre in visitados:
                continue

            visitados.add(nodo_actual.nombre)

            if nodo_actual.nombre == fin:
                return nodo_actual.gasto

            for vecino, peso in self.nodos.get(nodo_actual.nombre, []):
                if vecino in visitados:
                    continue

                nuevo_gasto = nodo_actual.gasto + peso
                nodo_vecino = Nodo(vecino, heuristica=heuristicas[vecino])
                nodo_vecino.gasto = min(nodo_vecino.gasto, nuevo_gasto)

                heapq.heappush(cola_prioridad, nodo_vecino)

        return float("inf")  # Si no se encuentra el destino

heuristicas = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0
}

grafo = Grafo()
grafo.agregar_arista('A', 'B', 2)
grafo.agregar_arista('A', 'C', 4)
grafo.agregar_arista('B', 'C', 1)
grafo.agregar_arista('B', 'D', 5)
grafo.agregar_arista('C', 'D', 1)
grafo.agregar_arista('D', 'E', 1)

print("El coste mínimo desde 'A' hasta 'E' es:", grafo.a_star('A', 'E', heuristicas))