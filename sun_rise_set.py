import requests

MY_LAT = 51.507351
MY_LNG = -0.127758

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise, sunset)
