'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
SIMULACION DE UN SITEMA DE NOTIFICACION USANDO DISEÑO DE OBSERVADOR
'''
# Implementa un sistema de notificación donde los suscriptores pueden registrarse para recibir actualizaciones de un emisor.

# Pasos
# Paso 1: Define una clase Emisor que gestione la lista de suscriptores.
# Paso 2: Implementa métodos para suscribir y notificar a los suscriptores.
# Paso 3: Crea una clase Suscriptor que reciba notificaciones y pueda reaccionar a ellas.
# Paso 4: Simula diferentes eventos y notificaciones.

class Suscriptor:
    def __init__(self, nombre):
        self.nombre = nombre

    def recibir_notificacion(self, mensaje):
        print(f'{self.nombre} ha recibido una notificación: {mensaje}')

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

def simulacion():
    emisor = Emisor()
    suscriptor1 = Suscriptor('Alice')
    suscriptor2 = Suscriptor('Bob')

    emisor.suscribir(suscriptor1)
    emisor.suscribir(suscriptor2)

    emisor.notificar('¡Nueva oferta disponible!')
    emisor.notificar('El evento comenzará en 30 minutos.')

    emisor.desuscribir(suscriptor1)
    emisor.notificar('Último recordatorio para el evento.')

if __name__ == '__main__':
    simulacion()