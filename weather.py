from urllib import request, response
import requests
API_KEY = "9e657037f0d91ba69304b8d655b4c4b1"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    #print(data)
    weather = data['weather'][0]['description']
    print("Weather:", weather)
    temperature = round(data["main"]["temp"] -273.15,2)
    print("Temperature:", temperature, "celsius")

else:
    print("Error receiving data")     