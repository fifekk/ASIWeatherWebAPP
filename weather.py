import requests
import json
from decimal import Decimal


def getWeatherData(city):
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?q={}&appid=36e1555b9828764965dd60b0976e0eda'.format(city))
    loc_weather = r.content.strip()
    jsonData = json.loads(loc_weather)
    clouds = jsonData['clouds']['all']
    icon = jsonData['weather'][0]['icon']
    icon = "http://openweathermap.org/img/wn/{}@2x.png".format(icon)
    currentTemp = round((jsonData['main']['temp']) - 273)
    feelsLike = round(Decimal(jsonData['main']['feels_like']) - 273)
    temp_min = round(Decimal(jsonData['main']['temp_min']) - 273)
    temp_max = round(Decimal(jsonData['main']['temp_max']) - 273)
    pressure = jsonData['main']['pressure']
    humidity =jsonData['main']['humidity']
    return clouds, icon, currentTemp, feelsLike, temp_min, temp_max, pressure, humidity
