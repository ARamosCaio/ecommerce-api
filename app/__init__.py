from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import URL
from sqlalchemy.ext.declarative import as_declarative

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:senha123@localhost/stock'
db = SQLAlchemy(app)



