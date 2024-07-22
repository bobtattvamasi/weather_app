# controllers/__init__.py
from flask import Blueprint

weather_bp = Blueprint('weather', __name__)
search_bp = Blueprint('search', __name__)

from . import weather_controller, search_controller
