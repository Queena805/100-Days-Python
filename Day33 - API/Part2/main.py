import requests
from datetime import datetime
import smtplib
import time
MY_LAT = float(40.7195411) # Your latitude
MY_LONG = float(-73.8573807) # Your longitude
MY_EMAIL = "jingnasong805@gmail.com"
PASSWORD = "Sjn18275771142"

def is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude, iss_longitude)
    if abs(MY_LAT - iss_latitude) < 1 and abs(MY_LONG - iss_longitude) < 1:
        return True
    else:
        return False

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def is_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hr = int(data["results"]["sunrise"].split("T")[1].split(":")[0])-4
    sunset_hr = int(data["results"]["sunset"].split("T")[1].split(":")[0])-4
    time_now = str(datetime.now())
    time_hr = int(time_now.split(" ")[1].split(":")[0])

    if time_hr > sunset_hr or time_hr < sunrise_hr:
        return True
    else:
        return False





while True:
    if is_dark() and is_close():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="paulvulf@gmail.com",
                                msg=f"Subject:LOOK UP!! \n\n The ISS is above you!")
        break

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



