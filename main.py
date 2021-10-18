import requests
from pprint import pprint

API_KEY = '8ee1f2c55e9e5d9d3c15ec4269302963'

# city = input('Enter a city:  ')

base_url = "https://api.openweathermap.org/data/2.5/weather?q={London}&appid={API_KEY}"

weather_data = requests.get(base_url).json()

print(weather_data)