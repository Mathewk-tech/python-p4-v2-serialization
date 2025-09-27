from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Create the SQLAlchemy object (no app yet)
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize db with this app
    db.init_app(app)

    # Import models so SQLAlchemy knows them
    from models import Pet

    # Create tables if not exist
    with app.app_context():
        db.create_all()

    # Example route
    @app.route('/pets/<int:id>')
    def get_pet(id):
        pet = Pet.query.get_or_404(id)
        return {
            "id": pet.id,
            "name": pet.name,
            "species": pet.species,
            "age": pet.age
        }

    return app

# This will be imported by seed.py
app = create_app()
