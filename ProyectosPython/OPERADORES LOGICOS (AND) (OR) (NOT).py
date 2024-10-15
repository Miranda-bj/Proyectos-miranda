# OPERADORES LOGICOS AND OR NOT
# CONJUCION AND
print("===============")
print("Conjucion (and)")
print("===============")

num1 = int(input("Escribe un numero mayor a 4 y menor a 15: "))

if num1 > 4 and num1 < 15:
    print("El numero ", num1, " Cumple con la condicion.")
else:
    print("El numero ", num1, " No cumple con la condicion")
    
# DISYUNCION OR
print("===============")
print("Disyuncion (or)")
print("===============")

palabra = input("para cumplir con la condicion escribe 'ajax' o 'amsterdam': ")

if palabra == "ajax" or palabra == "amsterdam":
    print("La condicion se ha cumplido")
else:
    print("La condicion no se ha cumplido")


# NEGACION NOT
print("==============")
print("Negacion (not)")
print("==============")

num_uno = int(input("Escibe un numero igual a 15: "))

if not num_uno == 15:
    print("El numero es diferente de 15 y si cumple con la condicion.")
else:
    print("El numero es igual a 15 y no cumple con la condicion.")
