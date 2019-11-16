from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
CORS(app)

port = int(os.getenv("PORT", 8000))

# current_file_path = os.path.realpath('/models/inspirational_quotes/tweetManagement')
# print(current_file_path)

@app.route("/")
def index():
  return "AYY Y'all wan'ts any of dose models? LoL"

# @app.route("/test", methods=["GET"])
# def test():
#   return "AYY Y'all wan'ts any of dose models? LoL"

@app.route("/tweet")
def tweet():
  from inspirational_quotes import getTweetThenCombine
  print(getTweetThenCombine)
  return combinedTweet

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=port, debug=True)
    app.run(port=port, debug=True)