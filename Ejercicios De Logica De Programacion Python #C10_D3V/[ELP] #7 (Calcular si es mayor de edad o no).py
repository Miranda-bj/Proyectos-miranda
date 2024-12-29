'''
EJERCICIO DE LOGICA DE PROGRAMACION
Escribir un programa que pregunte al usuario su edad 
y muestre por pantalla si es mayor de edad o no
'''

edad = int(input("Escriba su edad: "))

if edad <= 18:
    print("Aun eres menor de edad")
elif edad >= 18 and edad <= 30:
    print("Eres una persona con edad joven")
elif edad > 30:
    print("Eres mayor de edad")
