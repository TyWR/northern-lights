from flask import (Flask, jsonify, abort, request,
                   render_template)
from .src.api import get_aurora_power
import geopandas as gpd
from .src.map import plot_all

app = Flask(
    __name__,
    static_url_path='',
    static_folder='static',
    template_folder='templates'
)

@app.route("/")
def hello():
    return(render_template('index.html', title='Home'))


if __name__ == "__main__":
    plot_map()
    app.run(debug=True)

