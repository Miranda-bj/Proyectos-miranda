'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN ALGORITMO DE BUSQUEDA BINARIA
'''

# Implementa un algoritmo de búsqueda binaria para encontrar elementos en una lista ordenada.

# PASOS
# Paso 1: Define una función que realice la búsqueda binaria.
# Paso 2: Implementa un método para recibir la lista y el valor a buscar.
# Paso 3: Agrega manejo de excepciones para valores no presentes en la lista.
# Paso 4: Proporciona un menú para probar el algoritmo.

def busqueda_binaria(lista, valor):
    bajo = 0
    alto = len(lista) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio] < valor:
            bajo = medio + 1
        elif lista[medio] > valor:
            alto = medio - 1
        else:
            return medio
    return -1  # Valor no encontrado

def menu():
    lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print("Lista ordenada:", lista)
    valor = int(input("Introduce el valor a buscar: "))
    resultado = busqueda_binaria(lista, valor)
    if resultado != -1:
        print(f"Valor encontrado en el índice: {resultado}")
    else:
        print("Valor no encontrado.")

# Ejecutar el menú
menu()