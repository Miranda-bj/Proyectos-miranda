'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN ALGORITMO DE BUSCA DE PATRON (KMP)
'''

# Implementa el algoritmo de KMP para buscar un patrón en una cadena de texto.

# PASOS
# Paso 1: Define una función que construya la tabla de prefijos del patrón.
# Paso 2: Implementa la función principal que utiliza esta tabla para buscar el patrón en el texto.
# Paso 3: Maneja los casos en los que no se encuentra el patrón.
# Paso 4: Proporciona un ejemplo de uso.

def construir_tabla(patron):
    tabla = [0] * len(patron)
    longitud = 0
    i = 1

    while i < len(patron):
        if patron[i] == patron[length]:
            longitud += 1
            tabla[i] = longitud
            i += 1
        else:
            if longitud != 0:
                longitud = tabla[length - 1]
            else:
                tabla[i] = 0
                i += 1
    return tabla

def kmp_buscar(texto, patron):
    tabla = construir_tabla(patron)
    i = j = 0

    while i < len(texto):
        if patron[j] == texto[i]:
            i += 1
            j += 1

        if j == len(patron):
            print(f"Patrón encontrado en el índice {i - j}")
            j = tabla[j - 1]
        elif i < len(texto) and patron[j] != texto[i]:
            if j != 0:
                j = tabla[j - 1]
            else:
                i += 1

# Uso del algoritmo
texto = "abcabcabcd"
patron = "abc"
kmp_buscar(texto, patron)