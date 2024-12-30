'''
EJERCICIO DE LOGICA DE PROGRAMACION
CREAR UN DICCIONARIO A PARTIR DE DOS LISTAS
'''
def crear_diccionario(claves, valores):
    return dict(zip(claves, valores))
print(crear_diccionario(['a', 'b', 'c'], [1, 2, 3]))
# Explicación:
# Definimos la función crear_diccionario, que recibe dos listas: claves y valores.
# Usamos zip() para emparejar elementos de ambas listas.
# Convertimos el resultado en un diccionario con dict().
# Probamos la función con listas de claves y valores.