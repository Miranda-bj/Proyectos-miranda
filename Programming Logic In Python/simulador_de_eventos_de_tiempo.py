'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN SIMULADOR DE EVENTOS DE TIEMPO
'''

# Crea un simulador donde se puede programar eventos futuros y ejecutar acciones en el tiempo especificado.

# PASOS
# Paso 1: Define una clase Evento que contenga detalles sobre el evento y su tiempo.
# Paso 2: Crea una clase Simulador que pueda agregar eventos a un calendario y ejecutarlos en secuencia.
# Paso 3: Implementa la lógica para simular el paso del tiempo y ejecutar eventos.
# Paso 4: Proporciona un ejemplo de uso.

class Evento:
    def __init__(self, tiempo, accion):
        self.tiempo = tiempo
        self.accion = accion

    def ejecutar(self):
        self.accion()

class Simulador:
    def __init__(self):
        self.eventos = []

    def agregar_evento(self, evento):
        self.eventos.append(evento)

    def ejecutar_eventos(self):
        for evento in sorted(self.eventos, key=lambda x: x.tiempo):
            evento.ejecutar()

# Uso del simulador
simulador = Simulador()
simulador.agregar_evento(Evento(1, lambda: print("Evento 1: Acción a las 1.")))
simulador.agregar_evento(Evento(3, lambda: print("Evento 2: Acción a las 3.")))
simulador.agregar_evento(Evento(2, lambda: print("Evento 3: Acción a las 2.")))

print("Ejecutando eventos en orden:")
simulador.ejecutar_eventos()