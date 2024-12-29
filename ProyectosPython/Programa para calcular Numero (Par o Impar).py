'''
Comprobar si un numero es par o impar
'''
print("\t***********************************************************")
print("\t****Programa para comprobar si un numero es par o impar****".upper())
print("\t***********************************************************\n")

n1 = int(input("Escribe el numero que deseas comprobar: "))

if n1 % 2 == 0:
  print(f"el numero {n1} es par")
elif n1 % 2 == 1:
  print(f"el numero {n1} es impar")