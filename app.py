from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all origins by default

@app.route('/')
def home():
    return "Hello from Flask!"

@app.route('/run-script', methods=['POST'])
def run_script():
    data = request.get_json()
    name = data.get('name', 'world')
    return jsonify(message=f"Hello, {name}!")
