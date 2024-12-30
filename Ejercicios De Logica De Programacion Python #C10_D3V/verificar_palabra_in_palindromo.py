'''
EJERCICIO DE LOGICA DE PROGRAMACION
VERIFICAR SI UNA PALABRA ES UN PALINDROMO
'''

def es_palindromo(palabra):
    return palabra == palabra[::-1]
print(es_palindromo("radar"))
# Explicación:
# Definimos la función es_palindromo que recibe una palabra.
# Comparamos la palabra con su inversa usando palabra[::-1].
# Si son iguales, es un palíndromo.
# Probamos la función con "radar".