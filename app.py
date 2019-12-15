from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import os

current_file_path = os.path.realpath('models').replace(os.sep, '/')
app = Flask(__name__, instance_relative_config=True)
app.config["TEMPLATES_AUTO_RELOAD"] = True
CORS(app)

port = int(os.getenv("PORT", 9000))

from inspirational_quotes.app import inspirational_quotes_blueprint as inspirational_quotes_bp
from baby_names.app import baby_names_blueprint as baby_names_bp


@app.route("/")
def index():
    return "AYY Y'all wan'ts any of dose models? LoL"


app.register_blueprint(inspirational_quotes_bp)
app.register_blueprint(baby_names_bp)

if __name__ == "__main__":
    app.run(port=port)
