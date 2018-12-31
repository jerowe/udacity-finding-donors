from flask import Flask
from flask import jsonify, request
from flask_cors import CORS
import json
import functools

app = Flask(__name__)
CORS(app, allow_headers=['Content-Type', 'Access-Control-Allow-Origin', 'Access-Control-Allow-Headers',
                         'Access-Control-Allow-Methods'])


@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@app.route('/health', methods=['POST'])
def hello():
    data = json.loads(request.data.decode('utf-8'))
    return jsonify(data)
