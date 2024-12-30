'''
EJERCICIO DE LOGICA DE PROGRAMACION
FILTRAR NUMEROS PARES DE UNA LISTA
'''
def filtrar_pares(lista):
  return [num for num in lista if num % 2 == 0]
print(filtrar_pares([1, 2, 3, 4, 5, 6]))
# Explicacion
#1- definimos la funcion que recibe una lista de numeros
#2- utilizamos una comprension de lista para filtrar solo los numeros pares
#3- verificamos si cada numero es par usando num % 2 == 0
#4- retornamos la lista de numeros pares
#5- probamos con una lista que contiene numeros del 1 al 6