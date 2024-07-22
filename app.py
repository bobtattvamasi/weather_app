from flask import Flask, request, render_template, jsonify, session
import requests
import sqlite3
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Функция для получения прогноза погоды
def get_weather(city):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city)

    # Проверка, удалось ли получить координаты
    if location:
        latitude = location.latitude
        longitude = location.longitude

        # Запрос к Open Meteo API для получения прогноза погоды
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
        response = requests.get(url)
        return response.json()
    else:
        return {"error": "Не удалось найти координаты города"}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
        # Сохранение истории поиска
        save_search_history(city)
        session['last_city'] = city
        return render_template('index.html', weather=weather, city=city, plot_url=create_plot(weather))
    last_city = session.get('last_city')
    return render_template('index.html', last_city=last_city)


def save_search_history(city):
    # Функция для сохранения истории поиска в базе данных
    conn = sqlite3.connect('weather_app.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history (city) VALUES (?)", (city,))
    conn.commit()
    conn.close()


def create_plot(weather):
    times = weather['hourly']['time']
    temperatures = weather['hourly']['temperature_2m']

    plt.figure(figsize=(10, 5))
    plt.plot(times, temperatures, marker='o')
    plt.xticks(rotation=45)
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.title('Hourly Temperature Forecast')
    plt.grid(False)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    return base64.b64encode(buf.getvalue()).decode('utf-8')

# Функция автодополнения
@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('q')
    results = get_city_suggestions(search)
    return jsonify(results)

def get_city_suggestions(query):


# API для истории поиска
@app.route('/api/history', methods=['GET'])
def history():
    history = get_search_history()
    return jsonify(history)

def get_search_history():
    conn = sqlite3.connect('weather_app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT city, COUNT(*) FROM history GROUP BY city")
    result = cursor.fetchall()
    conn.close()
    return result

if __name__ == '__main__':
    app.run(debug=True)