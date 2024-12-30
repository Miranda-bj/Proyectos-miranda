'''
EJERCICIO DE LOGICA DE PROGRAMACION
COMBINAR DOS LISTAS ALTERNANDO ELEMENTOS
'''
def combinar_listas(lista1, lista2):
    return [elem for pair in zip(lista1, lista2) for elem in pair]
print(combinar_listas([1, 2, 3], ['a', 'b', 'c']))
# Explicación:
# Definimos la función combinar_listas, que recibe dos listas.
# Usamos zip() para combinar las listas en pares.
# Usamos una comprensión de lista para alternar los elementos de ambos pares.
# Retornamos la lista combinada.
# Probamos la función con una lista de números y otra de letras.