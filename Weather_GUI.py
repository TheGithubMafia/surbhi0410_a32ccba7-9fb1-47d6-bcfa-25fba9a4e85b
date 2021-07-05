import tkinter as tk
from tkinter.messagebox import showinfo
import requests
import json


def get_weather_data():
    API_KEY = "0e2087639929997f7b11ae0c30a37cd6"

    city = city_entry.get()
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    res = requests.get(URL)
    json_data = json.loads(res.text)

    weather = json_data["weather"][0]["description"]
    temprature = json_data["main"]["temp"]
    humidity = json_data["main"]["humidity"]
    wind_speed = json_data["wind"]["speed"]

    showinfo(f'{city.title()} Weather',
             f' Weather: {weather} \n Temprature: {temprature} \n Humidity: {humidity} \n Wind Speed: {wind_speed}')


win = tk.Tk()
win.title('Weather App')

app_label = tk.Label(win, text="Weather App", font=('Sans', 25, 'bold'))
app_label.grid(row=0, column=0, columnspan=2)

app_label = tk.Label(win, text="Made by Shubham K Singh", font=('Sans', 10))
app_label.grid(row=1, column=0, columnspan=2)

city_label = tk.Label(win, text='Enter city name: ')
city_label.grid(row=2, column=0, pady=10)

city_entry = tk.Entry(win, width=30)
city_entry.grid(row=2, column=1, pady=10)

btn = tk.Button(win, text='Get Weather', bd=1, command=get_weather_data)
btn.grid(row=4, column=0, columnspan=2, pady=10)

win.mainloop()