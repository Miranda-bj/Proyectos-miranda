'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UN API REST CON FLASK
'''
# Crea una API REST simple para gestionar libros, permitiendo operaciones CRUD (Crear, Leer, Actualizar, Eliminar).

# Pasos
# Paso 1: Instala Flask y configura la aplicación.
# Paso 2: Define un modelo de libro y crea una lista de libros.
# Paso 3: Implementa las rutas para las operaciones CRUD.
# Paso 4: Prueba la API utilizando herramientas como Postman.

from flask import Flask, jsonify, request

app = Flask(__name__)

libros = []

@app.route('/libros', methods=['POST'])
def agregar_libro():
    nuevo_libro = request.get_json()
    libros.append(nuevo_libro)
    return jsonify(nuevo_libro), 201

@app.route('/libros', methods=['GET'])
def listar_libros():
    return jsonify(libros), 200

@app.route('/libros/<int:indice>', methods=['GET'])
def obtener_libro(indice):
    if 0 <= indice < len(libros):
        return jsonify(libros[indice]), 200
    return jsonify({'error': 'Libro no encontrado'}), 404

@app.route('/libros/<int:indice>', methods=['PUT'])
def actualizar_libro(indice):
    if 0 <= indice < len(libros):
        datos_actualizados = request.get_json()
        libros[indice].update(datos_actualizados)
        return jsonify(libros[indice]), 200
    return jsonify({'error': 'Libro no encontrado'}), 404

@app.route('/libros/<int:indice>', methods=['DELETE'])
def eliminar_libro(indice):
    if 0 <= indice < len(libros):
        libros.pop(indice)
        return jsonify({'mensaje': 'Libro eliminado'}), 204
    return jsonify({'error': 'Libro no encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)