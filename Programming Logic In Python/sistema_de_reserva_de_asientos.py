'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN SISTEMA DE RESERVA DE ASIENTOS
'''

# Crea un sistema que permite reservar asientos en un teatro.

# PASOS
# Paso 1: Define una clase Asiento que tenga un número y un estado (reservado o no).
# Paso 2: Crea una clase Teatro que mantenga una lista de asientos.
# Paso 3: Implementa métodos para reservar y liberar asientos.
# Paso 4: Proporciona una interfaz de consola para el usuario, mostrando el estado de los asientos.

class Asiento:
    def __init__(self, numero):
        self.numero = numero
        self.reservado = False

    def reservar(self):
        if not self.reservado:
            self.reservado = True
            return True
        return False

    def liberar(self):
        if self.reservado:
            self.reservado = False
            return True
        return False

class Teatro:
    def __init__(self, num_asientos):
        self.asientos = [Asiento(i) for i in range(1, num_asientos + 1)]

    def mostrar_asientos(self):
        for asiento in self.asientos:
            estado = "Reservado" if asiento.reservado else "Libre"
            print(f"Asiento {asiento.numero}: {estado}")

    def reservar_asiento(self, numero):
        if 1 <= numero <= len(self.asientos):
            if self.asientos[numero - 1].reservar():
                print(f"Asiento {numero} reservado.")
            else:
                print(f"Asiento {numero} ya está reservado.")
        else:
            print("Número de asiento no válido.")

    def liberar_asiento(self, numero):
        if 1 <= numero <= len(self.asientos):
            if self.asientos[numero - 1].liberar():
                print(f"Asiento {numero} liberado.")
            else:
                print(f"Asiento {numero} no estaba reservado.")
        else:
            print("Número de asiento no válido.")

# Uso del sistema de teatro
teatro = Teatro(5)
teatro.mostrar_asientos()
teatro.reservar_asiento(2)
teatro.reservar_asiento(2)
teatro.mostrar_asientos()
teatro.liberar_asiento(2)
teatro.mostrar_asientos()