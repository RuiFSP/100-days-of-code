import os
from datetime import datetime

import requests

# STEP1 - Setup API credentials and Google Spreadsheet
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
MY_GENDER = "male"
MY_WEIGHT = "your weight"
MY_HEIGHT = "your height"
MY_AGE = "your age"

nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# STEP2 - Get Exercise Stats using Natural Language
exercise_input = input("Tell which exercise you did today?: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}
nutritionix_params = {
    "query": exercise_input,
    "gender": MY_GENDER,
    "weight_kg": MY_WEIGHT,
    "height_cm": MY_HEIGHT,
    "age": MY_AGE,
}

response = requests.post(url=nutri_endpoint, json=nutritionix_params, headers=headers)
response.raise_for_status()
result = response.json()

today_date = datetime.today().strftime('%d/%m/%Y')
today_time = f"{datetime.today().hour}:{datetime.today().minute}:00"

# STEP3 - Saving data into google using Sheety
sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
    "Content-Type": "application/json",
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=sheety_headers)

    print(sheet_response.text)
