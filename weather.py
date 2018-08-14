from config import *
from google.appengine.api import urlfetch

def getWeatherURL():
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    return url
