from config import *
from models import Paciente

#primeira rota do servidor
@app.route("/")
def index():
    return 'clique <a href="/listar_pacientes">aqui</a> para ver os pacientes cadastrados'
    #link para a próxima rota (listar_pacientes)

@app.route("/listar_pacientes", methods=["GET"]) #retornando dados para o usuário
def listar_pacientes():
    pacientes = db.session.query(Paciente).all()
    pacientes_json = [ _.json() for _ in pacientes ]
    #jsonnamento - traduzindo para json
    resposta = jsonify(pacientes_json)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")

    return resposta