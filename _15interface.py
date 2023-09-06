
import requests
import pickle
import os

API_URL = "https://api.open-meteo.com/v1/forecast"
folder = "weather_data_folder"
file_path = os.path.join(folder)

class WeatherForecast:
    def __init__(self, date, weather):
        self.date = date
        self.weather = weather
        self.forecast = {}
    
    def get_from_api(self):
        params = {
            "daily":"precipitation_sum",  
            "latitude":"51.50853",
            "longitude":"-0.12574",  
            "timezone":"Europe/London",
        }

        resp = requests.get(API_URL, params=params)

        if resp.ok:
            data = resp.json() 
            with open(file_path, "wb") as f:
                pickle.dump(data,f)
        else:
            data = {}
            print(f"Request was not successful: {resp.text}")
  
    def __setitem__(self, date, weather):
        self.forecast[date] = weather

    def __getitem__(self, date):
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                return pickle.load(f)
        else:
            return self.get_from_api[date]
    
    def __iter__(self):
        folder = "weather_data_folder"
        for file_name in os.listdir(folder):
            yield file_name.split('-')[0]
            
    def items(self):
        folder = "weather_data_folder"
        file_path = os.path.join(folder)
        precip = data.get("daily",{}).get("precipitation_sum",[-1])[0]

        for file_name in os.listdir(folder):
            if os.path.exists(file_path):
                print("Date present in history, getting from cache...")
            with open(file_path, "rb") as f:
                data = pickle.load(f)
        else:
            yield (file_name.split('-')[0], precip)
        
        if precip > 0:
            print("It will rain")
        elif precip == 0:
            print("It will not rain")
        else:
            print("I don't know")
         