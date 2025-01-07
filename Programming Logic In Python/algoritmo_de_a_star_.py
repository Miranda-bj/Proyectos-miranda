'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN ALGORITMO DE A (A STAR*)
'''

# Implementa el algoritmo A* para encontrar el camino más corto en un grafo con pesos, usando heurísticas.

# PASOS
# Paso 1: Define una clase Nodo que contenga atributos como nombre, g (costo desde el inicio), h (heurística) y f (costo total).
# Paso 2: Crea una clase Grafo que contenga un diccionario para los nodos y un método para agregar aristas.
# Paso 3: Implementa un método a_star que inicialice las listas de nodos abiertos y cerrados, y calcule las rutas.
# Paso 4: Durante la búsqueda, actualiza los costos y la heurística hasta encontrar la ruta óptima.

import heapq

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.g = float('inf')  # Costo desde el nodo inicial
        self.h = 0              # Heurística
        self.f = float('inf')   # Costo total
        self.padre = None

class Grafo:
    def __init__(self):
        self.nodos = {}
        self.aristas = {}

    def agregar_nodo(self, nombre):
        nodo = Nodo(nombre)
        self.nodos[nombre] = nodo

    def agregar_arista(self, desde, hacia, costo):
        if desde not in self.aristas:
            self.aristas[desde] = []
        self.aristas[desde].append((hacia, costo))

    def a_star(self, inicio, objetivo):
        nodos_abiertos = []
        self.nodos[inicio].g = 0
        self.nodos[inicio].f = self.nodos[inicio].h
        heapq.heappush(nodos_abiertos, (self.nodos[inicio].f, self.nodos[inicio]))

        while nodos_abiertos:
            _, nodo_actual = heapq.heappop(nodos_abiertos)

            if nodo_actual.nombre == objetivo:
                ruta = []
                while nodo_actual:
                    ruta.append(nodo_actual.nombre)
                    nodo_actual = nodo_actual.padre
                return ruta[::-1]

            for vecino, costo in self.aristas.get(nodo_actual.nombre, []):
                tentative_g_score = nodo_actual.g + costo
                nodo_vecino = self.nodos[vecino]

                if tentative_g_score < nodo_vecino.g:
                    nodo_vecino.padre = nodo_actual
                    nodo_vecino.g = tentative_g_score
                    nodo_vecino.f = nodo_vecino.g + nodo_vecino.h
                    if all(nodo[1] != nodo_vecino for nodo in nodos_abiertos):
                        heapq.heappush(nodos_abiertos, (nodo_vecino.f, nodo_vecino))

        return []

# Uso del grafo
grafo = Grafo()
for nodo in ['A', 'B', 'C', 'D', 'E']:
    grafo.agregar_nodo(nodo)

grafo.agregar_arista('A', 'B', 1)
grafo.agregar_arista('A', 'C', 4)
grafo.agregar_arista('B', 'C', 2)
grafo.agregar_arista('B', 'D', 5)
grafo.agregar_arista('C', 'D', 1)
grafo.agregar_arista('D', 'E', 3)

# Establecer heurísticas
grafo.nodos['A'].h = 7
grafo.nodos['B'].h = 6
grafo.nodos['C'].h = 2
grafo.nodos['D'].h = 1
grafo.nodos['E'].h = 0

print(grafo.a_star('A', 'E'))