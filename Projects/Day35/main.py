import requests
from datetime import datetime
from twilio.rest import Client
import os

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get("ACCOUNT_ID")  # TWILIO_ACCOUNT_SID
auth_token = os.environ.get("AUTH_TOKEN")  # TWILIO_ACCOUNT_TOKEN
account_id_num = os.environ.get("TWILIO_ACCOUNT_NUM")
MY_PHONE_NUMER = os.environ.get("MY_PHONE_NUMER")
API_KEY = os.environ.get("API_KEY")
MY_CITY = "lisbon"

# 1) Getting Latitude and Longitude from open weather and saving it

paras1 = {
    "q": MY_CITY,
    "appid": API_KEY,
}

# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
resp1 = requests.get(url="http://api.openweathermap.org/geo/1.0/direct", params=paras1)
resp1.raise_for_status()
data1 = resp1.json()

MY_LAT = data1[0]["lat"]
MY_LON = data1[0]["lon"]
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
UNITS = "metric"

# 2) Free tier has data blocks of 3 hours for next 5 days

# API - 5-day weather forecast
paras2 = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "metric": UNITS
}

# https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}&units={metric}

resp2 = requests.get(url=OWM_Endpoint, params=paras2)
resp2.raise_for_status()
data2 = resp2.json()

my_list_of_dicts = []

for forecast in data2["list"]:
    dt = forecast["dt"]
    # converting timestamp to hour/day
    convert_datetime_to_day = int(datetime.fromtimestamp(dt).day)
    convert_datetime_to_hour = int(datetime.fromtimestamp(dt).hour)
    weather_id = int(forecast["weather"][0]["id"])

    # only save for work hours
    if 8 <= convert_datetime_to_hour <= 18:
        my_list_of_dicts.append(
            {
                "day": convert_datetime_to_day,
                "hour": convert_datetime_to_hour,
                "id": weather_id
            })

# The normal forecast if for 5 days with a step of 3 hours - free tier
for block_3_hour in my_list_of_dicts[:4]:

    # id code < 700 might rain
    if block_3_hour["id"] < 700:
        day = block_3_hour["day"]
        hour = block_3_hour["hour"]

        # accessing twilio account
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"Bring an ☔ it might rain on day:{day} around {hour} hours",
            from_=account_id_num,
            to=MY_PHONE_NUMER
        )

        print(message.status)
        break  # first event
