'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN SISTEMA DE NOTAS
'''

# Crea un sistema para gestionar notas de los estudiantes con funcionalidades para agregar, eliminar y listar notas.

# PASOS
# Paso 1: Define una clase Estudiante que tenga un identificador y una lista de notas.
# Paso 2: Crea una clase GestorNotas que almacene estudiantes y permite gestionar sus notas.
# Paso 3: Implementa métodos para agregar, eliminar y listar las notas de un estudiante.
# Paso 4: Proporciona una interfaz de consola para interactuar con el sistema.

class Estudiante:
    def __init__(self, id_estudiante):
        self.id_estudiante = id_estudiante
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def eliminar_nota(self, nota):
        self.notas.remove(nota)

    def listar_notas(self):
        return self.notas

class GestorNotas:
    def __init__(self):
        self.estudiantes = {}

    def agregar_estudiante(self, id_estudiante):
        self.estudiantes[id_estudiante] = Estudiante(id_estudiante)

    def agregar_nota(self, id_estudiante, nota):
        if id_estudiante in self.estudiantes:
            self.estudiantes[id_estudiante].agregar_nota(nota)
        else:
            print("Estudiante no encontrado.")

    def listar_notas(self, id_estudiante):
        if id_estudiante in self.estudiantes:
            return self.estudiantes[id_estudiante].listar_notas()
        return "Estudiante no encontrado."

# Uso del sistema de notas
gestor = GestorNotas()
gestor.agregar_estudiante("123")
gestor.agregar_nota("123", 8.5)
gestor.agregar_nota("123", 9.0)

print("Notas del estudiante 123:", gestor.listar_notas("123"))
gestor.agregar_nota("124", 5.0)  # Estudiante no encontrado