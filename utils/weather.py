# utils/weather.py
import requests
from geopy.geocoders import Nominatim
from config import Config

def get_weather(city):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city)

    if location:
        latitude = location.latitude
        longitude = location.longitude

        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
        response = requests.get(url)
        return response.json()
    else:
        return {"error": "Не удалось найти координаты города"}

def get_city_suggestions(query):
    url = f"https://api.geoapify.com/v1/geocode/autocomplete?text={query}&apiKey={Config.GEOAPIFY_API_KEY}&"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()
        suggestions = [feature['properties'].get('city') for feature in results['features']]
        return [city for city in suggestions if city]
    return []
