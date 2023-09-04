
import requests
import pickle
import os

percip = []

with open("_13pip.py") as f:
    for percip in f:
         if "percip" in percip:
            percip.append(percip)

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
        
        for percip in f:
            print(percip)
    
    def items(self):
        for date, weather in percip.items():
            print({date}, {weather})
    
API_URL = "https://api.open-meteo.com/v1/forecast"
data_folder_path = "weather_data_folder"
params = {
    # "end_date":"%7Bsearched_date%7D%60",
     # "start_date":"%7Bsearched_date%7D",
    "daily":"precipitation_sum",  
    "latitude":"51.50853",
    "longitude":"-0.12574",  
    "timezone":"Europe/London",
}
expected_date_format = "YYYY-MM-DD"
requested_date = input(f"Pass date you want to check in format ({expected_date_format}):")
file_path = os.path.join(data_folder_path, f"{requested_date}.pickle")

def create_forecast():
    if os.path.exists(file_path):
        print("Date present in history, getting from cache...")
    # open file, print the data
        with open(file_path, "rb") as f:
            data = pickle.load(f)
    else:
        print("Date not present in history, getting from API...")
    # get the data from API, save to file
        params["start_date"] = requested_date
        params["end_date"] = requested_date

    #Getting requst
    resp = requests.get(API_URL, params=params)

    if resp.ok:
        data = resp.json() 
        with open(file_path, "wb") as f:
            pickle.dump(data,f)
    else:
        data = {}
        print(f"Request was not successful: {resp.text}")

    precip = print(data.get("daily",{}).get("precipitation_sum",[-1])[0])

    if precip > 0:
        print("It will rain")
    elif precip == 0:
        print("It will not rain")
    else:
        print("I don't know")


    