from models import *
#pegando a classe pacientes, path, db_filepath, db e remove

if __name__ == "__main__":
    if path.exists(db_filepath): #removendo o banco de dados se ele já existir
        remove(db_filepath)

    db.create_all() #criando o banco de dados

    p1 = Paciente(nome="Hylson", idade=18, email="hylsinhodograu@gmail.com")
    p2 = Paciente(nome="Riad", idade=78, email="riadteacher@gmail.com")
    p3 = Paciente(nome="Ricardo", idade=22, email="rick@gmail.com")

    m1 = Medico(nome="Marcelo", idade=32, email="doutormarcelo@gmail.com", tipo_sanguineo="AB+")
    m2 = Medico(nome="Marcela", idade=23, email="doutoramarcela@gmail.com", tipo_sanguineo="AB-")

    r1 = Receita(codigo="7362", id_paciente=1, paciente=p1, id_medico=1, medico=m1)
    r2 = Receita(codigo="2637", id_paciente=2, paciente=p2, id_medico=2, medico=m2)
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.add(m1)
    db.session.add(m2)
    db.session.add(r1)
    db.session.add(r2)
    #adicionando models no banco
    db.session.commit() #commit para salvar as alterações

    print(m1)
    print(m1.json())
    print(r1.json())