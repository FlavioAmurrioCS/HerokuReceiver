from flask import Flask, jsonify, request
import json
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route('/elavon', methods=['POST'])
def elavon():
    print(json.dumps(request.form, indent=4))
    return jsonify(request.form)