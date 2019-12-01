from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import os

current_file_path = os.path.realpath('models').replace(os.sep, '/')
app = Flask(__name__, instance_relative_config=True)
app.config["TEMPLATES_AUTO_RELOAD"] = True
from inspirational_quotes.app import inspirational_quotes_blueprint as inspirational_quotes_bp
print(current_file_path)
# app.config.from_object(current_file_path + '/config')
# app.config.from_pyfile(current_file_path + '/instsance/config.py')
# Now we can access the configuration variables via app.config["VAR_NAME"].
CORS(app)

port = int(os.getenv("PORT", 9000))

# current_file_path = os.path.realpath('/models/inspirational_quotes/tweetManagement')
# print(current_file_path)


@app.route("/")
def index():
    return "AYY Y'all wan'ts any of dose models? LoL"

# @app.route("/test", methods=["GET"])
# def test():
#   return "AYY Y'all wan'ts any of dose models? LoL"

# @app.route("/tweet")
# def tweet():
#   from inspirational_quotes import getTweetThenCombine
#   print(getTweetThenCombine)
#   return combinedTweet


app.register_blueprint(inspirational_quotes_bp)

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=port, debug=True)
    app.run(port=port)
