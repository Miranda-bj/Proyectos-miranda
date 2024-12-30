'''
EJERCICIO DE LOGICA DE PROGRAMACION
ENCONTRAR NUMEROS REPETIDOS EN UNA LISTA
'''
def encontrar_repetidos(lista):
    return set(x for x in lista if lista.count(x) > 1)
print(encontrar_repetidos([1, 2, 3, 1, 2, 4]))
# Explicación:
# Definimos la función encontrar_repetidos que toma una lista.
# Usamos una comprensión de conjunto para identificar elementos cuyo conteo es mayor que 1.
# Retornamos el conjunto de números repetidos.
# Probamos la función con una lista que incluye duplicados.