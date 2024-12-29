'''
EJERCICIO DE LOGICA DE PROGRAMACION
crea la sucecion Fibonacci hasta el numero 1597
'''
a = 0
b = 1
while b <= 1597:
  print(a, b, end = ' ')
  a = a + b
  b = b + a