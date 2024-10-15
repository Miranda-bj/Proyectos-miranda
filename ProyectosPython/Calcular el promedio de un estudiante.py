# codigo para calcular el promedio de un alumno
# \t se usa para hacer una cadena de texto centrada
# \n se usa para hacer un salto de linea
print("\t ==============================")
print("\t Calcular promedio de un alumno")
print("\t ==============================\n")

# input es una funcion para recibir una entrada del usuario
alumno = input("Introduce tu nombre: ")

# int es una funcion de numeros enteros y convierte entradas de usuarios a enteros
# la funcion f-string se utiliza para añadir valores de variables en el codigo
s_d_i = int(input(f"{alumno} Introduce tu nota de seguridad de instalaciones: "))
i_a = int(input(f"{alumno} Introduce tu nota de inteligencia aerea: "))
s_a = int(input(f"{alumno} Introduce tu nota de seguridad aeropertuaria: "))
s_d_a = int(input(f"{alumno} Introduce tu nota de sistema de armamento: "))

# son funciones matematicas +=suma -=resta /=divicion *=multiplicacion **=exponensiacion
promedio = (s_d_i + i_a + s_a + s_d_a) / 4
promedio = int(promedio)

if promedio >= 70:
    print("===========================================================================")
    print(f"Felicidades {alumno} has aprobado el periodo con un promedio de {promedio}")
    print("===========================================================================")
else:
    print("===========================================================================")
    print(f"Mal {alumno} has reprobado el periodo con un promedio de {promedio}")
    print("===========================================================================")

print("\n en el codigo se utilizan comentarios para explicar las funciones que se usan")