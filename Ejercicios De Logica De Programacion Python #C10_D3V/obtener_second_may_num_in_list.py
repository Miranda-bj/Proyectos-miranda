'''
EJERCICIO DE LOGICA DE PROGRAMACION
OBTENER EL SEGUNDO MAYOR NUMERO DE UNA LISTA
'''
def segundo_mayor(lista):
    return sorted(set(lista))[-2] if len(set(lista)) > 1 else None
print(segundo_mayor([3, 5, 1, 2, 5]))
# Explicación:
# Definimos la función segundo_mayor que recibe una lista.
# Convertimos la lista en un conjunto para eliminar duplicados y luego la ordenamos.
# Retornamos el segundo mayor número, asegurando que haya al menos dos diferentes.
# Probamos la función con una lista de números.