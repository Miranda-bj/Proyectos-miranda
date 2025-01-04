'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
SISTEMA DE GESTION DE LIBROS
'''

# Crea un sistema que gestiona una colección de libros, permitiendo agregar, buscar, eliminar y mostrar libros.

# PASOS
# Paso 1: Define una clase Libro que contenga atributos como titulo, autor, anio y ISBN.
# Paso 2: Crea una clase Biblioteca que mantenga una lista de libros.
# Paso 3: Implementa métodos para agregar, buscar, eliminar y listar libros.
# Paso 4: Proporciona una interfaz de usuario para interactuar con el sistema.

class Libro:
    def __init__(self, titulo, autor, anio, isbn):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} por {self.autor} ({self.anio}) - ISBN: {self.isbn}"

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def eliminar_libro(self, isbn):
        libro = self.buscar_libro(isbn)
        if libro:
            self.libros.remove(libro)
            print(f"Libro '{libro.titulo}' eliminado.")
        else:
            print("Libro no encontrado.")

    def listar_libros(self):
        for libro in self.libros:
            print(libro)

# Uso de la Biblioteca
biblioteca = Biblioteca()
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, "978-3-16-148410-0")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, "978-3-16-148410-1")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

print("Libros en la biblioteca:")
biblioteca.listar_libros()

print("\nBuscando libro con ISBN 978-3-16-148410-0:")
libro_encontrado = biblioteca.buscar_libro("978-3-16-148410-0")
print(libro_encontrado)

biblioteca.eliminar_libro("978-3-16-148410-1")
print("\nLibros en la biblioteca después de eliminar:")
biblioteca.listar_libros()