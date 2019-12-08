from flask import (Flask, jsonify, abort, request,
                   render_template)
from .src.api import get_aurora_power, get_time
import requests

app = Flask(
    __name__,
    static_url_path='',
    static_folder='static',
    template_folder='templates'
)

@app.route("/")
def index():
    time = get_time()
    return(render_template('index.html', time=time))

@app.route("/data")
def serve_data():
    return jsonify(get_aurora_power())

@app.route("/infos")
def infos():
    return(render_template('infos.html'))

if __name__ == "__main__":
    app.run(debug=True)

