'''
EJERCICIO DE LOGICA DE PROGRAMACION
CALCULAR EL PROMEDIO DE UNA LISTA DE NUMEROS
'''
def promedio(lista):
    return sum(lista) / len(lista) if lista else 0
print(promedio([10, 20, 30]))
# Explicación:
# Definimos la función promedio, que toma una lista de números.
# Usamos sum() para obtener la suma y len() para contar los elementos.
# Retornamos el promedio, asegurando que la lista no esté vacía.
# Probamos la función con una lista de números.