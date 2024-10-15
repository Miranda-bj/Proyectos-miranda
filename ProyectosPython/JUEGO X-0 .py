import random

def jugar_x_o():
    """
    Juego de X-O con rival automático.
    """
    tablero = [" " for _ in range(9)]
    turno = "X"
    juego_terminado = False

    def mostrar_tablero():
        """Muestra el tablero de juego."""
        print("-------------")
        for i in range(3):
            print("|", tablero[i * 3], "|", tablero[i * 3 + 1], "|", tablero[i * 3 + 2], "|")
            print("-------------")

    def obtener_posicion_jugador():
        """Obtiene la posición del jugador."""
        while True:
            try:
                posicion = int(input(f"Turno de {turno}. Elige una posición (1-9): "))
                if 1 <= posicion <= 9 and tablero[posicion - 1] == " ":
                    return posicion - 1
                else:
                    print("Posición inválida. Intenta de nuevo.")
            except ValueError:
                print("Entrada inválida. Intenta de nuevo.")

    def obtener_posicion_rival():
        """Obtiene una posición aleatoria para el rival."""
        posiciones_disponibles = [i for i in range(9) if tablero[i] == " "]
        return random.choice(posiciones_disponibles)

    def verificar_victoria():
        """Verifica si hay un ganador."""
        ganador = None
        ganadores = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
                     [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
                     [0, 4, 8], [2, 4, 6]]  # Diagonales
        for ganador in ganadores:
            if tablero[ganador[0]] == tablero[ganador[1]] == tablero[ganador[2]] and tablero[ganador[0]] != " ":
                return tablero[ganador[0]]
        if " " not in tablero:
            return "Empate"
        return None

    while not juego_terminado:
        mostrar_tablero()
        if turno == "X":
            posicion = obtener_posicion_jugador()
        else:
            posicion = obtener_posicion_rival()
        tablero[posicion] = turno
        ganador = verificar_victoria()
        if ganador:
            juego_terminado = True
            mostrar_tablero()
            if ganador == "Empate":
                print("¡Empate!")
            else:
                print(f"¡{ganador} gana!")
        else:
            turno = "O" if turno == "X" else "X"

    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ")
    if jugar_de_nuevo.lower() == "s":
        jugar_x_o()

if __name__ == "__main__":
    jugar_x_o()