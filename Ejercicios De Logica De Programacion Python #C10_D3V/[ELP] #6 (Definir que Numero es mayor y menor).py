'''
EJERCICIO DE LOGICA DE PROGRAMACION
Escribe un programa que pida al usuario tres numeros distintos y determine cual es el mayor y cual es el menor. Ademas, si los tres numeros son mayores de 50, imprime "todos los numeros son altos"
'''

def numero_mayor_y_menor():

  num1 = int(input("Introduzca el primer numero: "))
  num2 = int(input("Introduzca el segundo numero: "))
  num3 = int(input("Introduzca el tercer numero: "))

  if num1 == num2 or num1 == num3 or num2 == num3:
    print("Todos los numeros deben de ser distintos!!!!!")

  else:
    mayor = max(num1, num2, num3)
    menor = min(num1, num2, num3)

    print(f"El numero mayor es el {mayor}")
    print(f"El numero menor es el {menor}")

    if num1 > 50 and num2 > 50 and num3 > 50:
      print("Todos los numeros son altos")

numero_mayor_y_menor()