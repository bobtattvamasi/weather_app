# controllers/weather_controller.py
from flask import request, jsonify
from models import db
from models.search_history import SearchHistory
from utils.weather import get_city_suggestions
import sqlite3
from . import search_bp

# Autocomplete function
@search_bp.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('q')
    results = get_city_suggestions(search)
    return jsonify(results)

# API for search history
@search_bp.route('/api/history', methods=['GET'])
def history():
    history = get_search_history()
    return jsonify(history)

def get_search_history():
    conn = sqlite3.connect('instance/weather_app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT city, COUNT(*) FROM search_history GROUP BY city")
    result = cursor.fetchall()
    conn.close()
    return result

# API for search statistics
@search_bp.route('/api/search_stats', methods=['GET'])
def search_stats():
    stats = db.session.query(SearchHistory.city, db.func.count(SearchHistory.city).label('count')).group_by(SearchHistory.city).all()
    return jsonify({city: count for city, count in stats})
