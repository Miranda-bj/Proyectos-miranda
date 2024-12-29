'''
EJERCICIO DE LOGICA DE PROGRAMACION (DE HAORA EN ADELANTE VAN COMENTADOS)
Crea una función que reciba una cadena y devuelva la misma cadena en mayúsculas
'''
# se usa def para crear una funcion
# luego se escriba la funcion que se quiere ejecutar seguida de () y :
def cadena_en_mayusculas():
  # creamos la variable llamda cadena
  # y utilizamos la funcion inpput para recibir la cadena desde el teclado
  cadena = input("Escribe una cadena de texto: ")
  # se usa la funcion .uppper() para convertir la cadena a mayusculas
  # luego imprimimos en pantalla la variable cadena
  print(cadena.upper())
  # al final la llamamos a la funcion para que se ejecute el programa
cadena_en_mayusculas()