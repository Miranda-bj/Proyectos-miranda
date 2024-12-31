'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN JUEGO DE ADIVINANZA CON INTELIGENCIA ARTIFICIAL
'''
# Crea un juego de adivinar un número utilizando un enfoque de inteligencia artificial donde la computadora intenta adivinar el número que el usuario está pensando.

# Pasos
# Paso 1: Define funciones para adivinar y recibir retroalimentación del usuario.
# Paso 2: Implementa un algoritmo que divida el rango y ajuste su búsqueda según la respuesta del usuario.
# Paso 3: Agrega un número de intentos y muestra estadísticas al final.

import random

def juego_adivinanza():
    print("¡Piensa en un número entre 1 y 100 y yo lo adivinaré!")
    rango_inferior = 1
    rango_superior = 100
    intentos = 0

    while True:
        intento = (rango_inferior + rango_superior) // 2
        intentos += 1
        print(f"¿Es {intento}? (introduce 'menor', 'mayor' o 'correcto')")
        respuesta = input().strip().lower()

        if respuesta == 'menor':
            rango_superior = intento - 1
        elif respuesta == 'mayor':
            rango_inferior = intento + 1
        elif respuesta == 'correcto':
            print(f"He adivinado tu número {intento} en {intentos} intentos.")
            break
        else:
            print("Respuesta no válida. Intenta de nuevo.")

if __name__ == '__main__':
    juego_adivinanza()