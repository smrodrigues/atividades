from config import *
from models import Paciente

#primeira rota do servidor
@app.route("/")
def index():
    return 'clique <a href="/listar_pacientes">aqui</a> para ver os pacientes cadastrados'
    #link para a próxima rota (listar_pacientes)

@app.route("/listar_pacientes", methods=["get"]) #retornando dados para o usuário
def listar_pacientes():
    pacientes = db.session.query(Paciente).all()
    pacientes_json = [ _.json() for _ in pacientes ]
    #jsonnamento - traduzindo para json
    resposta = jsonify(pacientes_json)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")

    return resposta


@app.route("/incluir_paciente", methods=["post"]) #método post é o método de recebimento do usuário
def incluir_paciente():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})#criando uma resposta padrão sendo bem sucedida
    dados = request.get_json()#pegando os dados que o usuário colocou no html e passou para o javaScript

    try: #tentando criar uma pessoa no banco de dados com os dados que o usuário passou
        paciente = Paciente(**dados)
        db.session.add(paciente)
        db.session.commit()
    except Exception as e: #se não for efetivo retornamos uma resposta de erro
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
    
    resposta.headers.add("Access-Control-Allow-Origin", "*")

    return resposta

@app.route("/excluir_paciente/<int:paciente_id>", methods=['delete'])
def excluir_paciente(paciente_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        Paciente.query.filter(Paciente.id == paciente_id).delete()
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})

    resposta.headers.add("Access-Control-Allow-Origin", "*")

    return resposta
