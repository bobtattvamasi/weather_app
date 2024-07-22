

# create_all_db.py
from flask import Flask
from models import db
from models.user import User
from models.search_history import SearchHistory
from config import Config

def create_database():
    # Create a Flask app instance
    app = Flask(__name__)
    app.config.from_object(Config)

    # Bind SQLAlchemy to the Flask app
    db.init_app(app)

    # Create all tables defined in the models
    with app.app_context():
        print("Application context is active.")
        db.create_all()
        print("Tables should be created.")

    print("Database and tables created successfully.")

if __name__ == "__main__":
    create_database()

