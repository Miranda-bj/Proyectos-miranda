'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN MOTOR DE BUSQUEDA SIMPLE
'''

# Crea un motor de búsqueda simple que indexe documentos y permita realizar consultas.

# PASOS
# Paso 1: Define una clase Documento que contenga un título y contenido.
# Paso 2: Crea una clase MotorBusqueda que tenga métodos para agregar documentos e indexarlos.
# Paso 3: Implementa un método de búsqueda que devuelve documentos que contienen la consulta.
# Paso 4: Proporciona un ejemplo de uso.

class Documento:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido

    def __str__(self):
        return f"Título: {self.titulo}, Contenido: {self.contenido[:30]}..."

class MotorBusqueda:
    def __init__(self):
        self.documentos = []

    def agregar_documento(self, documento):
        self.documentos.append(documento)

    def buscar(self, consulta):
        resultados = [doc for doc in self.documentos if consulta.lower() in doc.contenido.lower()]
        return resultados

# Uso del motor de búsqueda
motor = MotorBusqueda()
documento1 = Documento("Document 1", "Este es un documento sobre Python.")
documento2 = Documento("Document 2", "Aquí se habla sobre programación en Java.")
motor.agregar_documento(documento1)
motor.agregar_documento(documento2)

resultados = motor.buscar("Python")
print("Resultados de búsqueda:")
for resultado in resultados:
    print(resultado)