import requests
import smtplib
import os

LAT = 38.907192  #Your Latitude
LONG = -77.036873 # Your Longitude
api_key = os.getenv("OMW_API_Key", "Your API KEY Here") #Your API Key - https://openweathermap.org/price

weather_params = {
    "lat": LAT,
    "lon": LONG,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url = "https://api.openweathermap.org/data/2.5/forecast", params = weather_params)
response.raise_for_status()
weather_data = response.json()["list"]

counter = False

for i in range(0, 4):
    weather_id = weather_data[i]["weather"][0]["id"]
    if weather_id < 700:
        counter = True

if counter:
    my_email = os.getenv("my_email", "senderemail@gmail.com")
    password = os.getenv("password", "password here")
    receiver = os.getenv("receiver", "receiveremail@gmail.com")


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=receiver,
                            msg="Subject:Rain Today\n\nDon't forget to take an umbrella!")

