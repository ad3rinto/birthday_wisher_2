import requests

params = {
    "lat": 51.507351,
    "lng": -0.127758
}

response = requests.get("https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()
data = response.json()
print(data)
