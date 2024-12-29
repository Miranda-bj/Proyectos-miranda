print("\t*********************")
print("\t*****Calculadora*****".upper())
print("\t*********************\n")

print('''Seleccione la operacion que desee ejecutar:
#1 SUMA
#2 RESTA
#3 MULTIPLICACION
#4 DIVISION
#5 EXPONENTE''')

numero = int(input("Introduzca la opcion deseada: "))

if numero == 1:
  print("Has seleccionado 'SUMA'")
  numero = int(input("Introduca el primer digito: "))
  numero += int(input("Introduca el segundo digito: "))
  print(f"total de la suma es : {numero}")

elif numero == 2:
  print("Has seleccionado 'RESTA'")
  numero = int(input("Introduca el primer digito: "))
  numero -= int(input("Introduca el segundo digito: "))
  print(f"total de la resta es : {numero}")

elif numero == 3:
  print("Has seleccionado 'MULTIPLICACION'")
  numero = int(input("Introduca el primer digito: "))
  numero *= int(input("Introduca el segundo digito: "))
  print(f"total de la multiplicacion es : {numero}")

elif numero == 4:
  print("Has seleccionado 'DIVISION'")
  numero = int(input("Introduca el primer digito: "))
  numero /= int(input("Introduca el segundo digito: "))
  print(f"total de la division es : {numero}")

elif numero == 5:
  print("Has seleccionado 'EXPONENTE'")
  numero = int(input("Introduca el primer digito: "))
  numero **= int(input("Introduca el segundo digito: "))
  print(f"total de la exponensiacion es : {numero}")

else:
  print("Esta operacion no existe en este programa")