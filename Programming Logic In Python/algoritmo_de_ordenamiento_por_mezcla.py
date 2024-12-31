'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
ALGORITMO DE ORDENAMIENTO POR MEZCLA (MERGE SORT)
'''
# Implementa el algoritmo de ordenamiento por mezcla (Merge Sort) de manera recursiva.

# Pasos
# Paso 1: Crea una función que divida la lista en dos mitades.
# Paso 2: Crea una función que mezcle dos listas ordenadas.
# Paso 3: Implementa la función principal que llame a las funciones creadas para ordenar la lista.
# Paso 4: Agrega casos de prueba para validar el algoritmo.

def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])

    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado

# Prueba del algoritmo
lista = [38, 27, 43, 3, 9, 82, 10]
print("Lista original:", lista)
lista_ordenada = merge_sort(lista)
print("Lista ordenada:", lista_ordenada)