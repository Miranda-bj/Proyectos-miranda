'''
EJERCICIO DE LOGICA DE PROGRAMACION
Crea una función que reciba una lista de números y devuelva la suma de todos sus elementos.
'''

print("\t****************")
print("\tLista de numeros".upper())
print("\t****************\n")

def suma_lista(numeros):
  '''Suma la lista de los numeros'''
  return sum(numeros)

lista = [4,15,20,30,40]
resultado = suma_lista(lista)
print(f"El resulta de la suma de la lista de numeros es: {resultado}")