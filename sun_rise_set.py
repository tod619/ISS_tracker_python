import requests

response = requests.get("https://api.sunrise-sunset.org/json")
response.raise_for_status()
data = response.json()
print(data)
