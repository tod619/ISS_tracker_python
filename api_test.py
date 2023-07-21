# test api - testing getting data from an api using python
# 21/07/2023
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
