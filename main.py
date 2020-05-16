from flask import Blueprint, render_template, request
from app import db
from geolocation import getGeoLocation
from weather import getWeatherData, getWeatherDataByCoords

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
def profile():
    lat, lng, city = getGeoLocation()
    clouds, icon, currentTemp, feelsLike, temp_min, temp_max, pressure, humidity = getWeatherDataByCoords(lat, lng)
    return render_template('profile.html', clouds=clouds, icon=icon, currentTemp=currentTemp,
                           feelsLike=feelsLike, temp_min=temp_min, temp_max=temp_max, pressure=pressure,
                           humidity=humidity, city=city)


@main.route('/weather')
def weather():
    return render_template('weather.html', showInput=True)


@main.route('/weather', methods=['POST'])
def weather_post():
    city = request.form.get('city')
    clouds, icon, currentTemp, feelsLike, temp_min, temp_max, pressure, humidity = getWeatherData(city)
    return render_template('weather.html', showInput=False, clouds=clouds, icon=icon, currentTemp=currentTemp, feelsLike=feelsLike, temp_min=temp_min, temp_max=temp_max, pressure=pressure, humidity=humidity, city=city)
