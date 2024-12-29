'''
EJERCICIO DE LOGICA DE PROGRAMACION
Escribe un programa que imprima todos los números pares del 1 al 50
'''
for i in range(1,51):
  if i % 2 == 0:
    print(f"{i} Es par")
  else:
    print(f"{i} Es impar")