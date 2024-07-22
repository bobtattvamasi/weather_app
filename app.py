# app.py
from flask import Flask
from config import Config
from models import db
from flask_migrate import Migrate
from controllers import weather_bp, search_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(weather_bp)
app.register_blueprint(search_bp)

if __name__ == '__main__':
    app.run(debug=True)
