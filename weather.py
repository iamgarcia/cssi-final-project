def getWeatherURL():
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    return url

def convertKelvinToFahrenheit(kelvin):
    celcius = kelvin - 273.15
    fahrenheit = 9.0/5.0 * celcius + 32
    return round(fahrenheit)
