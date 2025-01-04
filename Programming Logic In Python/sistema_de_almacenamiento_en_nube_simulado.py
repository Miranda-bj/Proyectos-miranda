'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN SISTEMA DE ALMACENAMIENTO EN NUBE SIMULADO
'''

# Crea un sistema que permite almacenar y gestionar archivos. Los archivos se representan con nombres y tamaños.

# PASOS
# Paso 1: Define una clase Archivo que contenga atributos como nombre y tamaño.
# Paso 2: Crea una clase AlmacenamientoNube que mantenga una lista de archivos.
# Paso 3: Implementa métodos para agregar, buscar, eliminar y listar archivos.
# Paso 4: Proporciona una interfaz de usuario para interactuar con el sistema.

class Archivo:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano

    def __str__(self):
        return f"{self.nombre} - {self.tamano}KB"

class AlmacenamientoNube:
    def __init__(self):
        self.archivos = []

    def agregar_archivo(self, archivo):
        self.archivos.append(archivo)

    def buscar_archivo(self, nombre):
        for archivo in self.archivos:
            if archivo.nombre == nombre:
                return archivo
        return None

    def eliminar_archivo(self, nombre):
        archivo = self.buscar_archivo(nombre)
        if archivo:
            self.archivos.remove(archivo)
            print(f"Archivo '{nombre}' eliminado.")
        else:
            print("Archivo no encontrado.")

    def listar_archivos(self):
        for archivo in self.archivos:
            print(archivo)

# Uso del sistema de almacenamiento
nube = AlmacenamientoNube()
archivo1 = Archivo("foto.jpg", 150)
archivo2 = Archivo("documento.pdf", 300)

nube.agregar_archivo(archivo1)
nube.agregar_archivo(archivo2)

print("Archivos en la nube:")
nube.listar_archivos()

print("\nBuscando archivo 'foto.jpg':")
archivo_encontrado = nube.buscar_archivo("foto.jpg")
print(archivo_encontrado)

nube.eliminar_archivo("documento.pdf")
print("\nArchivos en la nube después de eliminar:")
nube.listar_archivos()