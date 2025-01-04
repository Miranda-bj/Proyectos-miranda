'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN JUEGO DE ADIVINANZA DE NUMEROS
'''

# Crea un juego donde el usuario debe adivinar un número entre 1 y 100.

# PASOS
# Paso 1: Usa la biblioteca random para generar un número aleatorio.
# Paso 2: Crea un bucle que permita al usuario realizar intentos.
# Paso 3: Proporciona retroalimentación sobre si el número es demasiado alto o bajo.
# Paso 4: Termina el juego cuando el número es adivinado. Muestra el número de intentos realizados.

import random

class JuegoAdivinanza:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

    def adivinar(self, intento):
        self.intentos += 1
        if intento < self.numero_secreto:
            return "Demasiado bajo!"
        elif intento > self.numero_secreto:
            return "Demasiado alto!"
        else:
            return "¡Felicidades! has adivinado el número."

# Uso del juego
juego = JuegoAdivinanza()
while True:
    try:
        intento = int(input("Adivina el número entre 1 y 100: "))
        resultado = juego.adivinar(intento)
        print(resultado)
        if intento == juego.numero_secreto:
            print(f"Total de intentos: {juego.intentos}")
            break
    except ValueError:
        print("Por favor, introduce un número válido.")