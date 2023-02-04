import requests

API_KEY = "your_key"
MY_CITY = "lisbon"

paras1 = {
    "q": MY_CITY,
    "appid": API_KEY,
}

# getting Latitude and Longitude

# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
# https://api.openweathermap.org/geo/1.0/direct?q=lisbon&appid=your_key
resp1 = requests.get(url="http://api.openweathermap.org/geo/1.0/direct", params=paras1)
resp1.raise_for_status()
data1 = resp1.json()

MY_LAT = data1[0]["lat"]
MY_LON = data1[0]["lon"]
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"

# API - 5 day weather forecast
paras2 = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
}

# https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
# https://api.openweathermap.org/data/2.5/forecast?lat=38.7077507&lon=-9.1365919&appid=your_key

resp2 = requests.get(url=OWM_Endpoint, params=paras2)
resp2.raise_for_status()
data2 = resp2.json()
print(data2)





