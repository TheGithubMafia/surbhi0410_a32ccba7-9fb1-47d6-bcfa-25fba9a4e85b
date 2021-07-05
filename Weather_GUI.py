#Libraries

import tkinter as tk
from tkinter.messagebox import showinfo
import requests
import json

def get_weather():
    API_Key = "0e2087639929997f7b11ae0c30a37cd6"

    City = city_entry.get()
    URL= f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}&untts=mctric"
    
    res = requests.get(URL)

    json_data= json.loads(res, text)

    weather = json_data["weather"][0]["description"]

    temprature= json_data["main" ["temp"]

    humidity = json catal["main"]["humdity"]

    wind speed json_datal "wind" ["speed"

    showinfo('{city.titl Weather.

    f Weather: {weather}\n
    Temprature: {temprature) in

    Humidity: humidity) in
    Wind Speed: (wind speed}')