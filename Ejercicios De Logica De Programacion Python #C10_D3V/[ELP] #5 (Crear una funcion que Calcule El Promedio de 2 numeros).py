'''
EJERCICIO DE LOGICA DE PROGRAMACION
Desarrolla un programa que pida al usuario dos números y muestre su promedio.
'''

def calcular_promedio():
  num1 = float(input("Introduzca el primer numero: "))
  num2 = float(input("Introduzca el segundo numero: "))

  promedio = (num1 + num2) / 2
  print(f"El promedio de {num1} y {num2} es: {promedio}")

calcular_promedio()