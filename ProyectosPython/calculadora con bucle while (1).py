# CALCULADORA CON BUCLE WHILE
print("\t =============================")
print("\t Calculdora de numeros enteros")
print("\t ============================= \n")

print("1 suma")
print("2 resta")
print("3 multiplicacion")
print("4 division \n ")

while True:
    num1 = int(input("Elije una funcion: "))
    print("OK has elegido", num1, "\n")
    
    if num1 == 1:
        print("Bien has elegido suma")
        num1 = int(input("Introduce el primer digito: "))
        num1 += int(input("Introduce el segundo digito: "))
        print("total es: ", num1) 
        
    elif num1 == 2:
        print("Bien has elegido resta")
        num1 = int(input("Introduce el primer digito: "))
        num1 -= int(input("Introduce el segundo digito: "))
        print("total es: ", num1)  
        
    elif num1 == 3:
        print("Bien has elegido multiplicacion")
        num1 = int(input("Introduce el primer digito: "))
        num1 *= int(input("Introduce el segundo digito: "))
        print("total es: ", num1)  
        
    elif num1 == 4:
        print("Bien has elegido divicion")
        num1 = int(input("Introduce el primer digito: "))
        num1 /= int(input("Introduce el segundo digito: "))
        print("total es: ", num1)
        
    else:
        print("La funcion que has ingresado no existe")
        break
  