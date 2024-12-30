'''
EJERCICIO DE LOGICA DE PROGRAMACION
CONTAR CARACTERES UNICOS EN UNA CADENA
'''
def contar_unicos(cadena):
    return len(set(cadena))
print(contar_unicos("programación"))
# Explicación:
# Definimos la función contar_unicos, que recibe una cadena.
# Convertimos la cadena en un conjunto usando set(), eliminando duplicados.
# Retornamos la longitud del conjunto, que representa los caracteres únicos.
# Probamos la función con "programación".