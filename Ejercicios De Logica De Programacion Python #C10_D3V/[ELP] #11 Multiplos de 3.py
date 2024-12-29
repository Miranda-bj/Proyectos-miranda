'''
EJERCICIO DE LOGICA DE PROGRAMACION
Escribe un programa en python que imprima los numeros del 1 al 30 e indique si son multiplos de 3
'''

def multiplos3():
  for i in range(1,31):
    if i % 3 == 0:
      print(f'{i} es multiplo de 3')
    else:
      print(f'{i} no es multiplo de 3')
multiplos3()