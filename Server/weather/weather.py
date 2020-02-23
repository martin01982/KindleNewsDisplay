import requests

class Weather:
    def __init__(self, api_key, location):
        self.api_key = api_key
        self.location = location

    def get_weather(self):
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(self.location, self.api_key)
        r = requests.get(url)
        return r.json()

    def get_forecast(self):
        url = "https://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid={}".format(self.location, self.api_key)
        r = requests.get(url)
        return r.json()





