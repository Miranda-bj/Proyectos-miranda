print("\t=================================")
print("\tSistema vacacional compañia RAPPI".upper())
print("\t=================================\n")

nombre = input("Porfavor escriba su nombre: ")
print("CLAVE #1 = 'Atencion al cliente'")
print("CLAVE #2 = 'Logistica'")
print("CLAVE #3 = 'Gerencia'")
clave = int(input("Porfavor escriba su CLAVE en 'numeros': "))
tiempo = int(input("Porfavor escriba sus años de servicio: "))

if clave == 1:
  print(f"\nBien {nombre} tu clave es #1 'ATENCION AL CLIENTE'")
  print(f"Tu {nombre} tienes {tiempo} años de servicio en la empresa")
  if tiempo == 1:
    print(f"Tu {nombre} tienes derecho a 6 dias de vacaciones.")
  elif tiempo == 2 or tiempo <= 6:
    print(f"Tu {nombre} tienes derecho a 14 dias de vacaciones.")
  elif tiempo >= 7:
    print(f"Tu {nombre} tienes derecho a 20 dias de vacaciones.")
  else:
    print(f"Aun no {nombre}, no tienes derecho a vacaciones.")

elif clave == 2:
  print(f"\nBien {nombre} tu clave es #2 'LOGISTICA'")
  print(f"Tu {nombre} tienes {tiempo} años de servicio en la empresa")
  if tiempo == 1:
    print(f"Tu {nombre} tienes derecho a 7 dias de vacaciones.")
  elif tiempo == 2 or tiempo <= 6:
    print(f"Tu {nombre} tienes derecho a 15 dias de vacaciones.")
  elif tiempo >= 7:
    print(f"Tu {nombre} tienes derecho a 22 dias de vacaciones.")
  else:
    print(f"Aun no {nombre}, no tienes derecho a vacaciones.")

if clave == 3:
  print(f"\nBien {nombre} tu clave es #3 'GERENCIA'")
  print(f"Tu {nombre} tienes {tiempo} años de servicio en la empresa")
  if tiempo == 1:
    print(f"Tu {nombre} tienes derecho a 10 dias de vacaciones.")
  elif tiempo == 2 or tiempo <= 6:
    print(f"Tu {nombre} tienes derecho a 20 dias de vacaciones.")
  elif tiempo >= 7:
    print(f"Tu {nombre} tienes derecho a 30 dias de vacaciones.")
  else:
    print(f"Aun no {nombre}, no tienes derecho a vacaciones.")

print(f"Disfruta tus vacaciones {nombre} ;)".upper())