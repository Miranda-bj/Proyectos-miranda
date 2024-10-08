# sistema para determinar vacaciones de empleados de google
print("===========================")
print("=sistema vacacional google=")
print("===========================")

nombre_empleado = input("Ingrese el nombre del empleado: ")
clave_departamento = int(input("Ingrese la clave del departamento: "))
antiguedad_empleado = int(input("Ingrese los años laborados del empleado: "))

if clave_departamento == 1:

    if antiguedad_empleado == 1 and antiguedad_empleado < 2:
        print("el empleado ", nombre_empleado, " tiene derecho a 6 dias de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("el empleado ", nombre_empleado, " tiene derecho a 14 dias de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("el empleado ", nombre_empleado, " tiene derecho a 20 dias de vacaciones.")
    else:
        print("el empleado ", nombre_empleado, " aun no tiene derecho a vacaciones.")

elif clave_departamento == 2:

    if antiguedad_empleado == 1 and antiguedad_empleado < 2:
        print("el empleado ", nombre_empleado, " tiene derecho a 7 dias de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("el empleado ", nombre_empleado, " tiene derecho a 15 dias de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("el empleado ", nombre_empleado, " tiene derecho a 22 dias de vacaciones")
    else:
        print("el empleado ", nombre_empleado, " aun no tiene derecho a vacaciones.")

elif clave_departamento == 3:

    if antiguedad_empleado == 1 and antiguedad_empleado < 2:
        print("el empleado ", nombre_empleado, " tiene derecho a 10 dias de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("el empleado ", nombre_empleado, " tiene derecho a 20 dias de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("el empleado ", nombre_empleado, " tiene derecho a 30 dias de vacaciones")
    else:
        print("el empleado ", nombre_empleado, " aun no tiene derecho a vacaciones.")

else:
    ("La clave de departamento aun no existe.")

