print("Calculadora\n".upper())

print('''Elije una funcion\n
#1 suma
#2 resta
#3 multiplicacion
#4 division
#5 Exponente
''')

num1 = int(input(""))

if num1 == 1:
    print("Bien has elejido #1 Suma")
    num1 = int(input("Introduce el primer digito: \n"))
    num1 += int(input("Introduce el segundo digito: \n"))
    print(f"El total de la suma es:  {num1}")

elif num1 == 2:
    print("Bien has elejido #2 Resta")
    num1 = int(input("Introduce el primer digito: \n"))
    num1 -= int(input("Introduce el segundo digito: \n"))
    print(f"El total de la resta es:  {num1}")

elif num1 == 3:
    print("Bien has elejido #3 Multiplicacion")
    num1 = int(input("Introduce el primer digito: \n"))
    num1 *= int(input("Introduce el segundo digito: \n"))
    print(f"El total de la Multiplicacion es:  {num1}")

elif num1 == 4:
    print("Bien has elejido #4 Division")
    num1 = int(input("Introduce el primer digito: \n"))
    num1 /= int(input("Introduce el segundo digito: \n"))
    print(f"El total de la Division es:  {num1}")

elif num1 == 5:
    print("Bien has elejido #5 Exponente")
    num1 = int(input("Introduce el primer digito: \n"))
    num1 **= int(input("Introduce el segundo digito: \n"))
    print(f"El total del Exponente es:  {num1}")

else:
    print("Esta funcion no exise")