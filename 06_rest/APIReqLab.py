#!/usr/bin/python3
# Using the `requests` package, and the API key above, write a function 
# that makes a request for your own location 43.19276223284654, -70.87064642315792 to the DarkSky API, 
# and print out the response data.

import requests
import json
from urllib.request import urlopen
SECRET_KEY = '1d8c58ed1d54f96f939e706c788650f1'

lat, long = (43.1927,-70.8706)  

url = 'https://api.darksky.net/forecast/{key}/{lat},{long}'.format(
    key=SECRET_KEY, lat=lat, long=long)
response = urlopen(url)  # Defaults to a GET request
# Returns a file-like Response object, so we can read it just like File I/O

forecast_data = response.read()
forecast = json.loads(forecast_data)
print(type(forecast))
time = forecast['currently']['time']
temp = forecast['currently']['temperature']
print(time, temp)
today = forecast['daily']['data'][0]
print('Today - High: {high}, Low: {low}'.format(
    high=today['temperatureHigh'], low=today['temperatureLow']))