from app import app, db
from models import Pet

with app.app_context():
    # clear old data
    Pet.query.delete()

    # seed new pets
    pet1 = Pet(name="Buddy", species="Dog", age=3)
    pet2 = Pet(name="Mittens", species="Cat", age=2)
    pet3 = Pet(name="Tweety", species="Bird", age=1)

    db.session.add_all([pet1, pet2, pet3])
    db.session.commit()

    print("Database seeded!")
