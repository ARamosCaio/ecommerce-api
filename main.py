import mysql.connector
from flask import Flask

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "rootpassword",
    database = "stock"
)

app = Flask(__name__)

