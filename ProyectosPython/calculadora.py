# PROGRAMA PARA HACER UNA CALCULADORA
print("\t =================================")
print("\t Calculadora para numeros enteros.")
print("\t =================================")

print("1 suma")
print("2 resta")
print("3 multiplicacion")
print("4 division")

numero = int(input("Introduce la opcion deseada: "))

print("Excelente has elegido ", numero)

if numero == 1:
    print("Bien has elegido suma")
    numero = int(input("Introduce el primer numero: "))
    numero += int(input("Introduce el segundo numero: "))
    print("El resultado de la suma es: ", numero)

elif numero == 2:
    print("Bien has elegido resta")
    numero = int(input("Introduce el primer numero: "))
    numero -= int(input("Introduce el segundo numero: "))
    print("El resultado de la resta es: ", numero)

elif numero == 3:
    print("Bien has elegido multiplicacion")
    numero = int(input("Introduce el primer numero: "))
    numero *= int(input("Introduce el segundo numero: "))
    print("El resultado de la multiplicacion es: ", numero)

elif numero == 4:
    print("Bien has elegido divicion")
    numero = int(input("Introduce el primer numero: "))
    numero /= int(input("Introduce el segundo numero: "))
    print("El resultado de la divicion es: ", numero)

else:
    print("la opcion seleccionada no existe")

