import requests
from datetime import datetime
import os
import smtplib

end_point = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "cd01f1cd69631bdb8d2f040577e01260"
my_email = "jingnasong805@gmail.com"
password = "Sjn18275771142"

parameters ={
    "lat": 40.759780,
    "lon": -73.817300,
    "exclude":"current,minutely,daily",
    "appid": api_key,
}



response = requests.get(end_point, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_hourly = weather_data["hourly"]
will_rain = False
# weather_list = []

for hour_data in weather_hourly[:12]:
    print("Time:",datetime.utcfromtimestamp(hour_data['dt']),"Weather ID:",hour_data['weather'][0]['id'])
    if hour_data['weather'][0]['id'] < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="queenasong805@gmail.com",
                            msg="Subject:Rain Alert\nIt's going to rain today. Remember to bring an unbrella. ")
else:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="queenasong805@gmail.com",
                            msg="Subject: Rain Alert\nIt's not going to rain today. Have a great day! ")







