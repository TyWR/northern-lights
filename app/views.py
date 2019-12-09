from flask import (Flask, jsonify, abort, request,
                   render_template)
from .api import get_aurora_power, get_time
from app import app

@app.route("/")
def index():
    time = get_time()
    return(render_template('index.html', time=time))

@app.route("/data")
def serve_data():
    return jsonify(get_aurora_power())
