from models import *
#pegando a classe pacientes, path, db_filepath, db e remove

if __name__ == "__main__":
    if path.exists(db_filepath): #removendo o banco de dados se ele já existir
        remove(db_filepath)

    db.create_all() #criando o banco de dados

    p1 = Paciente(nome="Hylson", idade=18, email="hylsinhodograu@gmail.com")
    p2 = Paciente(nome="Riad", idade=78, email="riadteacher@gmail.com")
    p3 = Paciente(nome="Ricardo", idade=22, email="rick@gmail.com")

    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    #adicionando models no banco
    db.session.commit() #commit para salvar as alterações