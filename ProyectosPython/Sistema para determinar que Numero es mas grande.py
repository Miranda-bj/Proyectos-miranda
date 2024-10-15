# SISTEMA PARA DETERMINAR EL NUMERO MAS GRANDE
print('\t ===========================================================')
print('\t Programa para determinar que numero de los 3 es mas grande.')
print('\t ===========================================================')

num1 = int(input('Introduce el primer numero: '))
num2 = int(input('Introduce el segundo numero: '))
num3 = int(input('Introduce el tercer numero: '))

if num1 > num2 and num1 > num3:
    print('El numero ', num1, ' es el numero mas grande.')
else:
    if num2 > num3:
        print('El numero ', num2, ' es el numero mas grande.')
    else:
        print('El numero', num3, ' es el numero mas grande.')

