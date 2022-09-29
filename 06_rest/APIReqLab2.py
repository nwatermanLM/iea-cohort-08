#!/usr/bin/python3

import requests
import datetime

if __name__ == "__main__":
    SECRET_KEY = '1d8c58ed1d54f96f939e706c788650f1'
    lat, long = (43.1927,-70.8706)  
    url = 'https://api.darksky.net/forecast/{key}/{lat},{long}'.format(
    key=SECRET_KEY, lat=lat, long=long)

    response = requests.get(url)
    forecast_data = response.json()
    time = forecast_data['currently']['time']
    temp = forecast_data['currently']['temperature']
    today = forecast_data['daily']['data'][0]
    print('Today - High: {high} F, Low: {low} F'.format(
        high=today['temperatureHigh'], low=today['temperatureLow']), 'Currently:', temp, 'F', 
        datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d %I:%M %p'))