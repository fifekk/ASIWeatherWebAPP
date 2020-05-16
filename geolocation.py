import requests
import json
from flask import jsonify

from app import simple_geoip


def getGeoLocation():
    r = requests.get('https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey=at_UvMGkFW6X5HCQUsi7aBIXab0n7nqH')
    data = r.content.strip()
    jsonData = json.loads(data)
    lat = jsonData['location']['lat']
    lng = jsonData['location']['lng']
    city = jsonData['location']['city']
    return lat, lng, city