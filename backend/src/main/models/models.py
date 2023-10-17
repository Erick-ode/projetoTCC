from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    confidence_level  = db.Column(db.Float)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"), unique=True)
    answers = db.Column(db.JSON)

    def __init__(self, name, coherence, answers, person_id):
        self.name = name
        self.confidence_level  = coherence
        self.answers = answers
        self.person_id = person_id

    def __repr__(self):
        return f"Name <{self.name}>; Coherence <{self.confidence_level :.2f}>"
    

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(100))
    experience = db.Column(db.String(100))
    chosen_technic = db.Column(db.String(50))
    technic = db.relationship("Result", backref="person", uselist=False, lazy=True)



    def __repr__(self):
        return f"Experience <{self.experience}>"
