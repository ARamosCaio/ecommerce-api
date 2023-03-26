from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE-URI'] = '/db/stock_db.sql'
db = SQLAlchemy(app)

