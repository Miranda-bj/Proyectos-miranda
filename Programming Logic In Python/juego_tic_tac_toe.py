'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN JUEGO DE TIC TAC TOE
'''

#  Crea un juego de Tic Tac Toe que permita a dos usuarios jugar entre sí.

# PASOS
# Paso 1: Define una clase Tablero que represente el estado del juego y valide las jugadas.
# Paso 2: Implementa métodos para mostrar el tablero y verificar condiciones de victoria.
# Paso 3: Crea una clase Juego que gestione el flujo de juego y la interacción de los jugadores.
# Paso 4: Proporciona una interfaz de consola para los jugadores.

class Tablero:
    def __init__(self):
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]

    def mostrar(self):
        for fila in self.tablero:
            print('|'.join(fila))
            print('-' * 5)

    def realizar_jugada(self, fila, columna, jugador):
        if self.tablero[fila][columna] == ' ':
            self.tablero[fila][columna] = jugador
            return True
        return False

    def verificar_victoria(self, jugador):
        # Verificar filas, columnas y diagonales
        for fila in self.tablero:
            if all([celda == jugador for celda in fila]):
                return True
        for col in range(3):
            if all([self.tablero[fila][col] == jugador for fila in range(3)]):
                return True
        if all([self.tablero[i][i] == jugador for i in range(3)]) or all([self.tablero[i][2 - i] == jugador for i in range(3)]):
            return True
        return False

class Juego:
    def __init__(self):
        self.tablero = Tablero()
        self.turno = 'X'

    def jugar(self):
        for _ in range(9):
            self.tablero.mostrar()
            print(f"Turno de {self.turno}. Introduce fila y columna (0-2):")
            fila, col = map(int, input().split())
            if self.tablero.realizar_jugada(fila, col, self.turno):
                if self.tablero.verificar_victoria(self.turno):
                    print(f"{self.turno} ha ganado!")
                    self.tablero.mostrar()
                    return
                self.turno = 'O' if self.turno == 'X' else 'X'
            else:
                print("Movimiento inválido, intenta de nuevo.")
        print("¡Es un empate!")
        self.tablero.mostrar()

# Iniciar el juego
juego = Juego()
juego.jugar()