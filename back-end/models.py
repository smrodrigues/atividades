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
