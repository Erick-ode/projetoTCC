from app import db


class Technic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    coherence = db.Column(db.Float)

    def __repr__(self):
        return f'Name <{self.name}>; Coherence <{self.coherence:.2f}>'
