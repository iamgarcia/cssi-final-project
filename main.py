#
#   main.py
#   WelomeSanDiego
#
#   Created by Alexander Garcia on 8/13/18.
#   Copyright 2018 BreakingCode. All rights reserved.
#

import webapp2
import jinja2
import os
import logging
import json
import urllib
import urllib2
from google.appengine.api import urlfetch
from config import *
from models import *
from weather import *

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomePage(webapp2.RequestHandler):

    def get(self):
        logging.warning('HomePage get(self) working')

        # TODO Refactor this to be a function

        try:
            form_data = urllib.urlencode({'zip': '92104',
                                            'appid': OPENWEATHER_API_KEY})
            result = urlfetch.fetch(getWeatherURL() + form_data)
            if result.status_code == 200:
                content = json.loads(result.content)
                main = content['main']
                temp = main['temp']
                temp = convertKelvinToFahrenheit(temp)
                dict = {"temperature": temp}
                mypage = env.get_template('templates/index.html')
                self.response.write(mypage.render(dict))
            else:
                logging.exception(result)
                self.response.status = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')

    def post(self):
        logging.warning('HomePage post(self) working')

class ExplorationPage(webapp2.RequestHandler):

    def get(self):
        logging.warning('HomePage get(self) working')

        try:
            form_data = urllib.urlencode({'zip': '92104',
                                            'appid': OPENWEATHER_API_KEY})
            result = urlfetch.fetch(getWeatherURL() + form_data)
            if result.status_code == 200:
                content = json.loads(result.content)
                main = content['main']
                temp = main['temp']
                temp = convertKelvinToFahrenheit(temp)
                dict = {"temperature": temp}
                mypage = env.get_template('templates/exploration.html')
                self.response.write(mypage.render(dict))
            else:
                logging.exception(result)
                self.response.status = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')

    def post(self):
        logging.warning('ExplorationPage post(self) working')

class ExplorationHikingPage(webapp2.RequestHandler):

    def get(self):
        logging.warning('HomePage get(self) working')

        try:
            form_data = urllib.urlencode({'zip': '92104',
                                            'appid': OPENWEATHER_API_KEY})
            result = urlfetch.fetch(getWeatherURL() + form_data)
            if result.status_code == 200:
                content = json.loads(result.content)
                main = content['main']
                temp = main['temp']
                temp = convertKelvinToFahrenheit(temp)
                dict = {"temperature": temp}
                mypage = env.get_template('templates/hiking.html')
                self.response.write(mypage.render(dict))
            else:
                logging.exception(result)
                self.response.status = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')

    def post(self):
        logging.warning('ExplorationHikingPage post(self) working')

class ExplorationWineriesPage(webapp2.RequestHandler):

    def get(self):
        logging.warning('HomePage get(self) working')

        try:
            form_data = urllib.urlencode({'zip': '92104',
                                            'appid': OPENWEATHER_API_KEY})
            result = urlfetch.fetch(getWeatherURL() + form_data)
            if result.status_code == 200:
                content = json.loads(result.content)
                main = content['main']
                temp = main['temp']
                temp = convertKelvinToFahrenheit(temp)
                dict = {"temperature": temp}
                mypage = env.get_template('templates/wineries.html')
                self.response.write(mypage.render(dict))
            else:
                logging.exception(result)
                self.response.status = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')

    def post(self):
        logging.warning('ExplorationWineriesPage post(self) working')

class ExplorationParkPage(webapp2.RequestHandler):

    def get(self):
        logging.warning('HomePage get(self) working')

        try:
            form_data = urllib.urlencode({'zip': '92104',
                                            'appid': OPENWEATHER_API_KEY})
            result = urlfetch.fetch(getWeatherURL() + form_data)
            if result.status_code == 200:
                content = json.loads(result.content)
                main = content['main']
                temp = main['temp']
                temp = convertKelvinToFahrenheit(temp)
                dict = {"temperature": temp}
                mypage = env.get_template('templates/park.html')
                self.response.write(mypage.render(dict))
            else:
                logging.exception(result)
                self.response.status = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')

    def post(self):
        logging.warning('ExplorationParkPage post(self) working')

class ExplorationNightlifePage(webapp2.RequestHandler):

    def get(self):
        logging.warning('HomePage get(self) working')

        try:
            form_data = urllib.urlencode({'zip': '92104',
                                            'appid': OPENWEATHER_API_KEY})
            result = urlfetch.fetch(getWeatherURL() + form_data)
            if result.status_code == 200:
                content = json.loads(result.content)
                main = content['main']
                temp = main['temp']
                temp = convertKelvinToFahrenheit(temp)
                dict = {"temperature": temp}
                mypage = env.get_template('templates/nightlife.html')
                self.response.write(mypage.render(dict))
            else:
                logging.exception(result)
                self.response.status = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')

    def post(self):
        logging.warning('ExplorationNightlifePage post(self) working')

class DiningPage(webapp2.RequestHandler):

    def get(self):
        logging.warning('HomePage get(self) working')

        try:
            form_data = urllib.urlencode({'zip': '92104',
                                            'appid': OPENWEATHER_API_KEY})
            result = urlfetch.fetch(getWeatherURL() + form_data)
            if result.status_code == 200:
                content = json.loads(result.content)
                main = content['main']
                temp = main['temp']
                temp = convertKelvinToFahrenheit(temp)
                dict = {"temperature": temp}
                mypage = env.get_template('templates/dining.html')
                self.response.write(mypage.render(dict))
            else:
                logging.exception(result)
                self.response.status = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')

    def post(self):
        logging.warning('DiningPage post(self) working')

class DiningFastFoodPage(webapp2.RequestHandler):

    def get(self):
        logging.warning('HomePage get(self) working')

        try:
            form_data = urllib.urlencode({'zip': '92104',
                                            'appid': OPENWEATHER_API_KEY})
            result = urlfetch.fetch(getWeatherURL() + form_data)
            if result.status_code == 200:
                content = json.loads(result.content)
                main = content['main']
                temp = main['temp']
                temp = convertKelvinToFahrenheit(temp)
                dict = {"temperature": temp}
                mypage = env.get_template('templates/fastfood.html')
                self.response.write(mypage.render(dict))
            else:
                logging.exception(result)
                self.response.status = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')

    def post(self):
        logging.warning('DiningFastFoodPage post(self) working')

class DiningMexicanPage(webapp2.RequestHandler):

    def get(self):
        logging.warning('HomePage get(self) working')

        try:
            form_data = urllib.urlencode({'zip': '92104',
                                            'appid': OPENWEATHER_API_KEY})
            result = urlfetch.fetch(getWeatherURL() + form_data)
            if result.status_code == 200:
                content = json.loads(result.content)
                main = content['main']
                temp = main['temp']
                temp = convertKelvinToFahrenheit(temp)
                dict = {"temperature": temp}
                mypage = env.get_template('templates/mexican.html')
                self.response.write(mypage.render(dict))
            else:
                logging.exception(result)
                self.response.status = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')

    def post(self):
        logging.warning('DiningMexicanPage post(self) working')

class DiningAsianPage(webapp2.RequestHandler):

    def get(self):
        logging.warning('HomePage get(self) working')

        try:
            form_data = urllib.urlencode({'zip': '92104',
                                            'appid': OPENWEATHER_API_KEY})
            result = urlfetch.fetch(getWeatherURL() + form_data)
            if result.status_code == 200:
                content = json.loads(result.content)
                main = content['main']
                temp = main['temp']
                temp = convertKelvinToFahrenheit(temp)
                dict = {"temperature": temp}
                mypage = env.get_template('templates/asian.html')
                self.response.write(mypage.render(dict))
            else:
                logging.exception(result)
                self.response.status = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')

    def post(self):
        logging.warning('DiningAsianPage post(self) working')

class DiningItalianPage(webapp2.RequestHandler):

    def get(self):
        logging.warning('HomePage get(self) working')

        try:
            form_data = urllib.urlencode({'zip': '92104',
                                            'appid': OPENWEATHER_API_KEY})
            result = urlfetch.fetch(getWeatherURL() + form_data)
            if result.status_code == 200:
                content = json.loads(result.content)
                main = content['main']
                temp = main['temp']
                temp = convertKelvinToFahrenheit(temp)
                dict = {"temperature": temp}
                mypage = env.get_template('templates/italian.html')
                self.response.write(mypage.render(dict))
            else:
                logging.exception(result)
                self.response.status = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')

    def post(self):
        logging.warning('DiningItalianPage post(self) working')

class AboutPage(webapp2.RequestHandler):

    def get(self):
        logging.warning('HomePage get(self) working')

        try:
            form_data = urllib.urlencode({'zip': '92104',
                                            'appid': OPENWEATHER_API_KEY})
            result = urlfetch.fetch(getWeatherURL() + form_data)
            if result.status_code == 200:
                content = json.loads(result.content)
                main = content['main']
                temp = main['temp']
                temp = convertKelvinToFahrenheit(temp)
                dict = {"temperature": temp}
                mypage = env.get_template('templates/about.html')
                self.response.write(mypage.render(dict))
            else:
                logging.exception(result)
                self.response.status = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')

    def post(self):
        logging.warning('AboutPage post(self) working')

class WeatherPage(webapp2.RequestHandler):

    def get(self):
        logging.warning('WeatherPage get(self) working')

        try:
            form_data = urllib.urlencode({'zip': '92104',
                                            'appid': OPENWEATHER_API_KEY})
            result = urlfetch.fetch(getWeatherURL() + form_data)
            if result.status_code == 200:
                content = json.loads(result.content)
                main = content['main']
                temp = main['temp']
                logging.info(temp)
                self.response.write(convertKelvinToFahrenheit(temp))
            else:
                logging.exception(result)
                self.response.status = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')

    def post(self):
        logging.warning('WeatherPage post(self) working')

# The app configuration section
app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/exploration', ExplorationPage),
    ('/exploration/hiking', ExplorationHikingPage),
    ('/exploration/wineries', ExplorationWineriesPage),
    ('/exploration/parks', ExplorationParkPage),
    ('/exploration/nightlife', ExplorationNightlifePage),
    ('/dining', DiningPage),
    ('/dining/fastfood', DiningFastFoodPage),
    ('/dining/mexican', DiningMexicanPage),
    ('/dining/asian', DiningAsianPage),
    ('/dining/italian', DiningItalianPage),
    ('/about', AboutPage),
    ('/weather', WeatherPage)
], debug=True)
