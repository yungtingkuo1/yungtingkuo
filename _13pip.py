#API_URL= https://api.open-meteo.com/v1/forecast?daily=precipitation_sum&end_date=%7Bsearched_date%7D%60&latitude=%7Blatitude%7D&longitude=%7Blongitude%7D&start_date=%7Bsearched_date%7D&timezone=Europe%2FLondon

"""
- weather_data_folder
    \ 2023-08-26.pickle
"""

import requests
import datetime
import os
import pickle

# expected_date_format = "YYYY-MM-DD"

API_URL = "https://api.open-meteo.com/v1/forecast"
data_folder_path = "weather_data_folder"

# check if data folder exists, if not create it
if not os.path.exists(data_folder_path):
    os.makedirs(data_folder_path)

params = {
    # "end_date":"%7Bsearched_date%7D%60",
     # "start_date":"%7Bsearched_date%7D",
    "daily":"precipitation_sum",  
    "latitude":"51.50853",
    "longitude":"-0.12574",  
    "timezone":"Europe/London",
}

#Getting date from the user
expected_date_format = "YYYY-MM-DD"
requested_date = input(f"Pass date you want to check in format ({expected_date_format}):")

if not requested_date:
    print("using tomorrow as date...")
    requested_date = (datetime.datetime.today().date() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
else:
    print("using user provided date...")

# Validate date format
# 1. doas it have 2 hyphens
if not requested_date.count("-") == 2:
    print(f"Wrong date format:{requested_date}, expected:{expected_date_format}")
    quit()
if not len([ch for ch in requested_date if ch.isdigit()]) == 8:
    print(f"Wrong date format:{requested_date}, expected:{expected_date_format}")
    quit()   
year_part, month_part, day_part = requested_date.split('-')

print(f"Date passed correctly: {requested_date}. Getting the data...")

# check if the date was alreday downloaded if yes, return value from file
file_path = os.path.join(data_folder_path, f"{requested_date}.pickle")

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