'''
EJERCICIO DE LOGICA DE PROGRAMACION:
Escribe un programa que pida la edad del usuario
y si tiene permiso de los padres (si o no).
Si la edad es mayor de 18, puede acceder,
si es entre 16 y 18, solo puede acceder
si tiene permiso de los padres;
si es menor de 16, no puede acceder.
'''
print("\t*******************************************")
print("\t****Ejercicio de logica de programacion****".upper())
print("\t*******************************************\n")

name = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))

if edad >= 18:
  print(f"Hola {name} puedes acceder, Bienvenido.")

elif edad >= 16 and edad <= 18:
  permiso = str(input("Escribe si tienes permiso (SI o NO): ".lower()))
  if permiso == 'si':
   print(f"Hola {name} puedes acceder, Bienvenido.")
  else:
    permiso == 'no'
    print(f"Lo sentimos {name} no puede acceder.")
else:
  edad <= 16
  print(f"Lo sentimos {name} no puede acceder.")