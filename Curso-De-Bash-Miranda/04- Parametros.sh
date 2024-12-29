#!/bin/bash

# Esto sirve para comentar

$n # La informacion de un parametro en concreto, siendo n un numero de parametro

$* # Todos los parametros se presentan es una sola cadena de caracteres

$@ # Todos los parametros en una lista con un elemento por cada parametro recibido

$# # EL numero de parametros con los que se a invocado al script. Sera una cifra

#!/bin/bash

echo El primer parametro es $1 # Cuando se ejecute en la terminal debes escribir el paremetro de cada uno
echo EL numero de parametros ha sido $#
echo Todos los parametros son: $*
