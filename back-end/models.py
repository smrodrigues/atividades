from config import *

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(254)) 
    idade = db.Column(db.Integer)
    email = db.Column(db.String(254)) 


    def __str__(self):
        return f'{self.id}- {self.nome}, {self.idade}, {self.email}'


    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "email": self.email
        }
