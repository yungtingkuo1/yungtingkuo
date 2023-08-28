
import requests

class WeatherForecast:
    def __init__(self, date, weather):
        self.date = date
        self.weather = weather
        self.forecast = {}
    
    def __setitem__(self, date, weather):
        self.forecast[date] = weather

    def __getitem__(self, date):
        return self.forecast[date]
    
    def __iter__(self):
        for weather in self.forecast:
            yield weather
    
    def items(self):
        for date, weather in wf.items():
            print({date}, {weather})

wf = WeatherForecast()

def create_forecast():
        resp = requests.get("https://api.open-meteo.com/v1/forecast")
        if not resp.ok:
            return None
        resp = resp.json()["results"][0]
        forcast = forcast(
        forcast = resp["precipitation_sum"]
        date = resp["date"],)
        return True, forcast
    