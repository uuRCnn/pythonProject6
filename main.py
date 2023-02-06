import requests


# response = requests.\
#     get(url="http://api.open-notify.org/iss-now.json")
# print(response)

# istanbulun konumu:
parameters = {
    "lat": 41.008240,
    "lng": 28.978359,
    "formatted": 0
}

response2 = requests.get(url="https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400",
                         params=parameters)
response2.raise_for_status()
data = response2.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

