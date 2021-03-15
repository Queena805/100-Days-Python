# import smtplib
#
#
# my_email = "jingnasong@yahoo.com"
# password = "fiiynyubcimcuqrd"
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="jingnasong805@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email")




# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
#
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995 , month= 11, day= 12, hour=4)
# print(date_of_birth)

import smtplib
import datetime as dt
import random


now = dt.datetime.now()
current_day_of_week = now.weekday()
print(current_day_of_week)
with open("quotes.txt", 'r') as data:
    lines = data.readlines()
    quote = random.choice(lines)

if current_day_of_week == 3:

    my_email = "jingnasong805@gmail.com"
    password = "Sjn18275771142"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="paulvulf@gmail.com",
                            msg=f"Monday Motivation:{quote}")