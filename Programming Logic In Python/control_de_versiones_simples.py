'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN SISTEMA DE CONTROL DE VERSIONES SIMPLES
'''

# Crea un sistema que simula un control de versiones usando un historial de cambios para diferentes archivos.

# PASOS
# Paso 1: Define una clase Archivo que tiene un nombre y un contenido, y un historial de versiones.
# Paso 2: Crea métodos para commit (guardar cambios), revertir a una versión anterior y listar_versiones.
# Paso 3: Utiliza un identificador de versión para acceder a las distintas versiones del archivo.
# Paso 4: Proporciona un ejemplo de uso.

class Archivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.contenido = ""
        self.historial = []

    def commit(self, nuevo_contenido):
        self.historial.append(self.contenido)  # Guarda la versión anterior
        self.contenido = nuevo_contenido

    def revertir(self, version_id):
        if version_id < len(self.historial):
            self.contenido = self.historial[version_id]
        else:
            print("Version ID no válido.")

    def listar_versiones(self):
        for index, version in enumerate(self.historial):
            print(f"Versión {index}: {version}")

# Uso del sistema de control de versiones
archivo = Archivo("ejemplo.txt")
archivo.commit("Contenido de la versión 1.")
archivo.commit("Contenido de la versión 2.")
archivo.commit("Contenido de la versión 3.")

print(f"Contenido actual: {archivo.contenido}")

archivo.listar_versiones()

archivo.revertir(1)
print(f"Contenido después de revertir: {archivo.contenido}")