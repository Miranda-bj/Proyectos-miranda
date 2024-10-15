import random

def jugar_piedra_papel_tijera():
    """
    Juego de Piedra, Papel o Tijera con selección de botón y 5 rondas.
    """
    opciones = ["piedra", "papel", "tijera"]
    puntuacion_jugador = 0
    puntuacion_maquina = 0

    for ronda in range(1, 6):
        print(f"\nRonda {ronda}:")
        eleccion_jugador = input("Elige: piedra, papel o tijera: ").lower()
        while eleccion_jugador not in opciones:
            print("Opción inválida. Elige piedra, papel o tijera.")
            eleccion_jugador = input("Elige: piedra, papel o tijera: ").lower()

        eleccion_maquina = random.choice(opciones)
        print(f"La máquina eligió: {eleccion_maquina}")

        if eleccion_jugador == eleccion_maquina:
            print("¡Empate!")
        elif (eleccion_jugador == "piedra" and eleccion_maquina == "tijera") or \
             (eleccion_jugador == "papel" and eleccion_maquina == "piedra") or \
             (eleccion_jugador == "tijera" and eleccion_maquina == "papel"):
            print("¡Ganaste!")
            puntuacion_jugador += 1
        else:
            print("¡Perdiste!")
            puntuacion_maquina += 1

    print(f"\nResultados finales:")
    print(f"Jugador: {puntuacion_jugador} puntos")
    print(f"Máquina: {puntuacion_maquina} puntos")

    if puntuacion_jugador > puntuacion_maquina:
        print("¡Felicidades! Ganaste el juego.")
    elif puntuacion_jugador < puntuacion_maquina:
        print("Lo siento, perdiste el juego.")
    else:
        print("¡Empate en el juego!")

jugar_piedra_papel_tijera()