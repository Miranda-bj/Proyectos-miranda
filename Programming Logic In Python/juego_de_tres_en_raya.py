'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN JUEGO DE TRES EN RAYA
'''

# Crea un juego de Tres en Raya (Tic-Tac-Toe) que permita a dos jugadores jugar en la consola.

# PASOS
# Paso 1: Define una clase Juego que tenga una matriz para representar el tablero.
# Paso 2: Crea métodos para mostrar el tablero y realizar movimientos.
# Paso 3: Implementa la lógica para verificar si hay un ganador o un empate.
# Paso 4: Proporciona un ciclo de juego que permita a los jugadores alternar turnos

class Juego:
    def __init__(self):
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]
        self.turno = "X"

    def mostrar_tablero(self):
        for fila in self.tablero:
            print("|".join(fila))
            print("-" * 5)

    def realizar_movimiento(self, fila, columna):
        if self.tablero[fila][columna] == " ":
            self.tablero[fila][columna] = self.turno
            return True
        return False

    def verificar_ganador(self):
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != " ":
                return True
        for col in range(3):
            if self.tablero[0][col] == self.tablero[1][col] == self.tablero[2][col] != " ":
                return True
        if (self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != " ") or \
           (self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != " "):
            return True
        return False

    def jugar(self):
        for _ in range(9):
            self.mostrar_tablero()
            fila = int(input(f"Jugador {self.turno}, elige fila (0-2): "))
            columna = int(input(f"Jugador {self.turno}, elige columna (0-2): "))
            if self.realizar_movimiento(fila, columna):
                if self.verificar_ganador():
                    self.mostrar_tablero()
                    print(f"¡Jugador {self.turno} gana!")
                    return
                self.turno = "O" if self.turno == "X" else "X"
            else:
                print("Movimiento inválido. Intenta de nuevo.")
        self.mostrar_tablero()
        print("¡Es un empate!")

# Uso del juego
juego = Juego()
juego.jugar()