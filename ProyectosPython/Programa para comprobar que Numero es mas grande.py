'''
Programa para calcular cual de los 3 numeros
es el mas grande
'''
print("\t*****************************************************")
print("\t***Calcular cual de los 3 numeros es el mas grande***".upper())
print("\t*****************************************************\n")

n1 = int(input("Introduce el primer numero: "))
n2 = int(input("Introduce el segundo numero: "))
n3 = int(input("Introduce el tercer numero: "))

if n1 > n2 and n1 > n3:
  print(f"El numero {n1} es el mas grande")
elif n2 > n1 and n2 > n3:
  print(f"El numero {n2} es el mas grande")
elif n3 > n1 and n3 > n2:
  print(f"El numero {n3} es el mas grande")