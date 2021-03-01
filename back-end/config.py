from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import path, remove

app = Flask(__name__)
srcpath = path.dirname(path.abspath(__file__))
db_filepath = path.join(srcpath, 'datavase.db')

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+db_filepath
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)