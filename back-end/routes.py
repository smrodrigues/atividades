from config import *
from models import Paciente


@app.route("/")
def index():
    return 'clique <a href="/listar_pacientes">aqui</a> para ver os pacientes cadastrados'


@app.route("/listar_pacientes", methods=["get"])
def listar_pacientes():
    pacientes = db.session.query(Paciente).all()
    pacientes_json = [ _.json() for _ in pacientes ]

    return jsonify(pacientes_json)