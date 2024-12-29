'''
EJERCICIO DE LOGICA DE PROGRAMACION:
Crea un programa que pida al usuario tres calificaciones
y calcule si la media de las tres es suficiente para
aprobrar. Considere que la media debe ser 11 o
mas para aprobar
'''

def calcular_media():
    us = input("Escribe tu apellido: ")
    cal1 = int(input("Escribe tu primera calificacion: "))
    cal2 = int(input("Escribe tu segunda calificacion: "))
    cal3 = int(input("Escribe tu tercera calificacion: "))
    
    media = (cal1 + cal2 + cal3) / 3
    media = float(round(media,2))
    
    if media >= 11:
        print(f"{us} has aprobado con una media de calificaciones de: {media}")
    elif media <= 11:
        print(f"{us} has reprobado con una media de calificaciones de: {media}")

calcular_media()