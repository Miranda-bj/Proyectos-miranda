'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN SISTEMA DE GESTION DE TAREAS
'''
# Crea una aplicación de consola para gestionar tareas, permitiendo al usuario agregar, eliminar, actualizar y listar tareas.

# Pasos:
# Paso 1: Define una clase Tarea que contenga atributos como titulo, descripcion y completada.
# Paso 2: Crea una clase GestorTareas que mantenga una lista de tareas y contenga métodos para añadir, eliminar, actualizar y listar tareas.
# Paso 3: Implementa la funcionalidad de la aplicación a través de un menú interactivo en la consola.
# Paso 4: Maneja la persistencia de datos mediante el almacenamiento de tareas en un archivo JSON

import json

class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False

    def completar(self):
        self.completada = True

    def __repr__(self):
        return f'{self.titulo} - {"✓" if self.completada else "✗"}: {self.descripcion}'

class GestorTareas:
    def __init__(self):
        self.tareas = []
        self.cargar_tareas()

    def agregar_tarea(self, titulo, descripcion):
        tarea = Tarea(titulo, descripcion)
        self.tareas.append(tarea)
        self.guardar_tareas()

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
            self.guardar_tareas()

    def listar_tareas(self):
        for i, tarea in enumerate(self.tareas):
            print(f"{i}. {tarea}")

    def completar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completar()
            self.guardar_tareas()

    def guardar_tareas(self):
        with open('tareas.json', 'w') as f:
            json.dump([t.__dict__ for t in self.tareas], f)

    def cargar_tareas(self):
        try:
            with open('tareas.json', 'r') as f:
                tareas_data = json.load(f)
                self.tareas = [Tarea(d['titulo'], d['descripcion']) for d in tareas_data]
                for i, t in enumerate(self.tareas):
                    t.completada = d.get('completada', False)
        except FileNotFoundError:
            self.tareas = []

def menu():
    gestor = GestorTareas()
    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            titulo = input("Título de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            gestor.agregar_tarea(titulo, descripcion)
        elif opcion == 2:
            gestor.listar_tareas()
        elif opcion == 3:
            gestor.listar_tareas()
            indice = int(input("Selecciona el índice de la tarea a completar: "))
            gestor.completar_tarea(indice)
        elif opcion == 4:
            gestor.listar_tareas()
            indice = int(input("Selecciona el índice de la tarea a eliminar: "))
            gestor.eliminar_tarea(indice)
        elif opcion == 5:
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()