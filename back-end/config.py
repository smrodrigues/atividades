from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import path, remove

#os (operacional system) é mais próximo da linguagem de máquina - path (caminho)

app = Flask(__name__) #instância do flask / define como uma aplicação flask
srcpath = path.dirname(path.abspath(__file__)) #srcpath - caminho da fonte, dirname - caminho do nome do diretório, abspath - caminho absoluto do arquivo.
db_filepath = path.join(srcpath, 'datavase.db') #cainho do arquivo do banco de dados, join - faz junção de dois caminhos (srcpath e datavase)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+db_filepath #conexão do banco de dados para o arquivo datavase.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #retorna as modificações feitas nos bancos de dados, track - rechonhecer as modificações

db = SQLAlchemy(app) #criando uma instância sql com a aplicação flask