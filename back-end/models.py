from config import * #usando apenas o db

class Paciente(db.Model): #herdando da classe da model
    #cada atributo é uma coluna
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(254)) 
    idade = db.Column(db.Integer)
    email = db.Column(db.String(254)) 


    def __str__(self): #método mágico que representa a classe como string
        return f'{self.id}- {self.nome}, {self.idade}, {self.email}'

    #representação da classe em forma de json
    def json(self): 
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "email": self.email
        }

class Medico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    idade = db.Column(db.Integer)
    email = db.Column(db.String(254))
    tipo_sanguineo = db.Column(db.String(3))


    def __str__(self):
        return f'{self.id}. {self.nome}, {self.idade}, {self.email}, {self.tipo_sanguineo}'


    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "email": self.email,
            "tipo_sanguineo": self.tipo_sanguineo 
        }


class Receita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(254))
    id_paciente = db.Column(db.Integer, db.ForeignKey(Paciente.id), nullable=False)
    paciente = db.relationship("Paciente")
    id_medico = db.Column(db.Integer, db.ForeignKey(Medico.id), nullable=False)
    medico = db.relationship("Medico")


    def __str__(self):
        return f'''{self.id}. {self.codigo}
            {self.id_paciente} - {self.paciente.json()};
            {self.id_medico} - {self.medico.json()}'''


    def json(self):
        return {
            "id": self.id,
            "codigo": self.codigo,
            "id_paciente": self.id_paciente,
            "paciente": self.paciente.json(),
            "id_medico": self.id_medico,
            "medico": self.medico.json()
        }
