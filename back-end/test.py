from models import *


if __name__ == "__main__":
    if path.exists(db_filepath):
        remove(db_filepath)

    db.create_all()

    p1 = Paciente(nome="Hylson", idade=18, email="hylsinhodograu@gmail.com")
    p2 = Paciente(nome="Riad", idade=78, email="riadteacher@gmail.com")
    p3 = Paciente(nome="Ricardo", idade=22, email="rick@gmail.com")

    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)

    db.session.commit()

    print(p1)
    print(p1.json())