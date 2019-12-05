from flask import (Flask, jsonify, abort, request,
                   render_template)
from .src.api import get_aurora_power
import geopandas as gpd

app = Flask(
    __name__,
    static_url_path='',
    static_folder='static',
    template_folder='templates'
)

@app.route("/")
def index():
    return(render_template('index.html', title='Home'))

@app.route("/data")
def serve_data():
    return jsonify(get_aurora_power())

if __name__ == "__main__":
    app.run(debug=True)

