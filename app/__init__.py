from flask import Flask, request, jsonify
from app.db import db
from flask_migrate import Migrate
import app.models 


app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/beds", methods=['GET'])
def get_beds():
    return jsonify({"beds-sucess"})

@app.route("/wardrobe", methods=['GET'])
def get_wardrobes():
    return jsonify({"wardrobe-sucess": "item"})

@app.route("/couches", methods=['GET'])
def get_couches():
    return jsonify({"couches-sucess"})
