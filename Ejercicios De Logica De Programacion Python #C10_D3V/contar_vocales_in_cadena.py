'''
EJERCICIO DE LOGICA DE PROGRAMACION
CONTAR VOCALES EN UNA CADENA
'''
def contar_vocales(cadena):
  return sum(cadena.lower().count(v) for v in 'aeiou')
print(contar_vocales("miranda josue"))

# Explicacion
#1- definimos la funcion que recibe la cadena
#2- convertimos la cadena a minusculas
#3- Usamos una comprension de lista para contar las vocales
#4- sumamos todo para obtener el total
#5- probamos la funcion con cualquier string