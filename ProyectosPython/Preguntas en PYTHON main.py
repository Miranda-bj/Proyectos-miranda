
preguntas = {
     "1 ¿cual es el mejor equipo del mundo?": "ajax",
     "2 ¿quien es el mejor jugador del mundo?": "cristiano",
     "3 ¿quien es la mejor atleta del mundo?": "femke bol",
     "4 ¿que ingenieria es mejor?": "ingenieria en computacion",
     "5 ¿cual es el mejor pais de centroamerica?": "honduras",
     "6 ¿matematica mas dificl?": "algebra",
}

puntos = 0

for pregunta, respuesta in preguntas.items():
    print(pregunta)
    respuesta_usuario = input("Tu respuesta: ")

    if respuesta_usuario.lower() == respuesta.lower():
        print("Correcto!")
        puntos += 1
    else:
        print("Incorrecto la rspuesta correcta es: ",respuesta)
print(f"ha terminado el juego, sacastes {puntos} puntos")