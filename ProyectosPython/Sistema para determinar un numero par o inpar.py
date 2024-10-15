# SISTEMA PARA QUE DETERMINA UN NUMERO PAR O INPAR
print("\t ======================================")
print("\t Determinar si un numero es par o inpar")
print("\t ======================================")

num1 = int(input("Introduzca un numero entero: "))

if num1 % 2 == 0:
    print('el numero ', num1, ' es un numero par')
elif num1 % 2 == 1:
    print(' El numero ', num1, ' es un numero inpar.')

