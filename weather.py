
import requests
from pprint import pprint

API_key = '976e0f765fe7e4f1088fd8f67dd3f59f'

city = input("Enter a city: ")
base_URL = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_key +"&q=" + city
#print(base_URL)
weather_data = requests.get (base_URL).json()
#print(weather_data)
pprint (weather_data)
