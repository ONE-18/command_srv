from flask import Flask, jsonify
import subprocess
import json
import os

app = Flask(__name__)

# Carga el diccionario desde un archivo JSON
def load_commands():
    try:
        with open("commands.json", "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error cargando commands.json: {e}")
        return {}

# Ruta para "/"
@app.route('/')
def home():
    return jsonify({
        "message": "Bienvenido al servicio",
        "status": "OK"
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Endpoint no encontrado",
        "status": 404
    }), 404

@app.route('/<key>', methods=['GET'])
def execute_command(key):
    # Recarga los comandos cada vez que se realiza una peticiÃ³n
    commands = load_commands()
    command = commands.get(key)

    if command:
        try:
            # Ejecuta el comando y obtiene la salida
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
            return jsonify({"key": key, "command": command, "output": result}), 200
        except subprocess.CalledProcessError as e:
            return jsonify({"error": f"Error ejecutando el comando '{command}'", "details": e.output}), 500
    else:
        return jsonify({"error": "Clave no encontrada en el diccionario"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
