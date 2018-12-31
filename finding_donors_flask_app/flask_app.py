from flask import Flask
from flask import jsonify, request
from flask_cors import CORS
import json
import functools

from .data_bp import data_bp
from .model_bp import model_bp

app = Flask(__name__)
CORS(app, allow_headers=['Content-Type', 'Access-Control-Allow-Origin',
                         'Access-Control-Allow-Headers', 'Access-Control-Allow-Methods'])

app.register_blueprint(data_bp)
app.register_blueprint(model_bp)


@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


# These are just some health/server is up checks

@app.route('/', methods=['GET'])
def enter():
    return jsonify({'status': 'ok'})


@app.route('/health', methods=['POST'])
def health():
    try:
        data = json.loads(request.data.decode('utf-8'))
        return jsonify(data)
    except Exception as e:
        return jsonify({'status': 'ok'})
