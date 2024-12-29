'''
EJERCICIO PRACTICO DE PYTHON
Crear una calculadora con una unica variable llamada NUMERO
'''
print('''\tCalculadora
\n#1 suma
#2 resta
#3 multiplicacion
#4 division
#5 division entera
#6 exponente
''')

numero = int(input("Elije una funcion: "))

if numero == 1:
  print("Bien has elejido #1 suma")
  numero = int(input("Escribe el primer digito: "))
  numero += int(input("Escribe el segundo digito: "))
  print(f"El total de la suma es {numero}")

elif numero == 2:
  print("Bien has elejido #2 resta")
  numero = int(input("Escribe el primer digito: "))
  numero -= int(input("Escribe el segundo digito: "))
  print(f"El total de la resta es {numero}")

elif numero == 3:
  print("Bien has elejido #3 multiplicacion")
  numero = int(input("Escribe el primer digito: "))
  numero *= int(input("Escribe el segundo digito: "))
  print(f"El total de la multiplicacion es {numero}")

elif numero == 4:
  print("Bien has elejido #4 division")
  numero = int(input("Escribe el primer digito: "))
  numero /= int(input("Escribe el segundo digito: "))
  print(f"El total de la division es", round(numero, 2))

elif numero == 5:
  print("Bien has elejido #5 division entera")
  numero = int(input("Escribe el primer digito: "))
  numero //= int(input("Escribe el segundo digito: "))
  print(f"El total de la division entera es {numero}")

elif numero == 6:
  print("Bien has elejido #6 exponente")
  numero = int(input("Escribe el primer digito: "))
  numero **= int(input("Escribe el segundo digito: "))
  print(f"El total del exponente es {numero}")

else:
  print("Esta funcion aun no existe;(")