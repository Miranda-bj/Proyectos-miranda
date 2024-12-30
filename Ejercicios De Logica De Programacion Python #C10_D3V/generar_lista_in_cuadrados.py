'''
EJERCICIO DE LOGICA DE PROGRAMACION
GENERAR UNA LISTA DE CUADRADOS
'''
def lista_cuadrados(n):
  return[i**2 for i in range(1, n+1)]
print(lista_cuadrados(5))
# Explicacion
#1- definimos la funcion que recibe un numero n
#2- Usamos una comprension de lista para generar los cuadrados de los numeros
#3- retornamos la lista de cuadrados
#4- probamos la funcion con n igual a 5, obteniendo [1, 4, 9, 16, 25]