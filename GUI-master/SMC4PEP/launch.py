import random
import json
import glob, os
import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

from email import message
from urllib import response
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS


bot_name = "Cubot"

app = Flask(__name__)
CORS(app)



@app.get("/")
def index_get():
    return render_template("basen.html")

@app.post("/upload_static_file")
def upload_static_file():
 print("Got request in static files")
 print(request.files)
 f = request.files['static_file']
 f.save(f.filename)
 print(f.filename)
 resp = {"success": True, "response": "file saved!"}
 return jsonify(resp), 200


@app.post("/predict")
def predict():
 
    rep = "a"
    mes = {"answer": rep}
    return jsonify(mes)


if __name__ == "__main__":
    app.run(debug=True)
