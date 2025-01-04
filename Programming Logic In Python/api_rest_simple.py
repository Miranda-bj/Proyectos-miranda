'''
EJERCICIOS DE LOGICA DE PROGRAMACION NIVEL INTERMEDIO
IMPLEMENTACION DE UNA API REST SIMPLE
'''

# Crea una API REST simple utilizando Flask que permite gestionar una lista de tareas.

# PASOS
# Paso 1: Define el entorno de Flask y crea una lista de tareas en memoria.
# Paso 2: Implementa rutas para crear, listar, actualizar y eliminar tareas.
# Paso 3: Agrega la lógica para manejar las peticiones y respuestas en formato JSON.
# Paso 4: Proporciona un ejemplo de uso de las rutas de la API.

from flask import Flask, jsonify, request

app = Flask(__name__)
tareas = []

@app.route('/tareas', methods=['GET'])
def listar_tareas():
    return jsonify(tareas)

@app.route('/tareas', methods=['POST'])
def agregar_tarea():
    tarea = request.json
    tareas.append(tarea)
    return jsonify(tarea), 201

@app.route('/tareas/<int:id>', methods=['PUT'])
def actualizar_tarea(id):
    if id < len(tareas):
        tareas[id].update(request.json)
        return jsonify(tareas[id])
    return jsonify({"error": "Tarea no encontrada"}), 404

@app.route('/tareas/<int:id>', methods=['DELETE'])
def eliminar_tarea(id):
    if id < len(tareas):
        tarea_eliminada = tareas.pop(id)
        return jsonify(tarea_eliminada)
    return jsonify({"error": "Tarea no encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)