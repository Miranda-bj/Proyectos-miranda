'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN SISTEMA DE NOTIFICACION
'''

# Crea un sistema de notificación utilizando el patrón de diseño Observador.

# pasos
# Paso 1: Define una clase Suscriptor que contenga métodos para recibir notificaciones.
# Paso 2: Crea una clase Emisor que mantenga una lista de suscriptores.
# Paso 3: Implementa métodos para suscribirse, desuscribirse y notificar a los suscriptores.
# Paso 4: Simula un escenario de suscripción y notificación.

class Suscriptor:
    def __init__(self, nombre):
        self.nombre = nombre

    def recibir_notificacion(self, mensaje):
        print(f"{self.nombre} ha recibido la notificación: {mensaje}")

class Emisor:
    def __init__(self):
        self.suscriptores = []

    def suscribir(self, suscriptor):
        self.suscriptores.append(suscriptor)

    def desuscribir(self, suscriptor):
        self.suscriptores.remove(suscriptor)

    def notificar(self, mensaje):
        for suscriptor in self.suscriptores:
            suscriptor.recibir_notificacion(mensaje)

# Uso del sistema de notificación
emisor = Emisor()
suscriptor1 = Suscriptor("Alice")
suscriptor2 = Suscriptor("Bob")

emisor.suscribir(suscriptor1)
emisor.suscribir(suscriptor2)

emisor.notificar("¡Nuevo mensaje disponible!")
emisor.notificar("El evento empezará en 10 minutos.")