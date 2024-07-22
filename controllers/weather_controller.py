# controllers/weather_controller.py
from flask import request, render_template, session
from . import weather_bp
from models.user import User
from models.search_history import SearchHistory
from utils.weather import get_weather
from utils.plot import create_plot
from models import db

@weather_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)

        ip_address = request.remote_addr
        user = User.query.filter_by(ip_address=ip_address).first()

        if not user:
            user = User(ip_address=ip_address)
            db.session.add(user)
            db.session.commit()

        save_search_history(city, user.id)
        session['last_city'] = city
        return render_template('index.html', weather=weather, city=city, plot_url=create_plot(weather))
    last_city = session.get('last_city')
    return render_template('index.html', last_city=last_city)

def save_search_history(city, user_id):
    search_history = SearchHistory(city=city, user_id=user_id)
    db.session.add(search_history)
    db.session.commit()
