from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
CORS(app)

port = int(os.getenv("PORT", 8000))

@app.route("/")
def index():
  return "AYY Y'all wan'ts any of dose models? LoL"
