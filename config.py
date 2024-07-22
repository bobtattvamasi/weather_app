# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///weather_app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GEOAPIFY_API_KEY = '9791aa8b7c5343979031e58bdab06571'
