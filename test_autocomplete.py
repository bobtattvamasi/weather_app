
import requests

OPENWEATHERMAP_API_KEY = 'fb3775b2c33abbccecbb83b2af58e056'

search = "Tbil"

# url = f"http://api.geonames.org/searchJSON?name_startsWith={search}&maxRows=5&username={GEONAMES_USERNAME}"
url = f"http://api.openweathermap.org/data/2.5/find?q={search}&type=like&sort=population&cnt=5&appid={OPENWEATHERMAP_API_KEY}"

response = requests.get(url)

print(response)

results = response.json().get('geonames', [])
