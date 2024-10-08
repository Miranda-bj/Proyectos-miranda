# SENTENCIA CONDICIONAL MULTIPLE ELIF
print("=============================")
print("Convertir un numero en letras")
print("=============================")

while True:

      num1 = int(input("ingrese un numero del 1 al 5: "))
      if num1 == 1:
           print("el numero es 'UNO'")
      elif num1 == 2:
           print("el numero es 'DOS'")
      elif num1 == 3:
           print("el numero es 'TRES'")
      elif num1 == 4:
           print("el numero es 'CUATRO'")
      elif num1 == 5:
           print("el numero es 'CINCO'")
      else:
           print("este sistema solo convierte numeros hasta el 5")
           break
print("Fin del programa.")