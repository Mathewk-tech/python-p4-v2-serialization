from app import db

class Pet(db.Model):
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Pet {self.name} ({self.species}), {self.age} yrs>"
