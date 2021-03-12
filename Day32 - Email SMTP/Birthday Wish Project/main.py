##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib

S_EMAIL = "jingnasong805@gmail.com"
S_PASS = "Sjn18275771142"

now = dt.datetime.now()
today = (now.month, now.day)

birthday_info = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthday_info.iterrows()}

if today in birthday_dict:
    letter_num = random.choice([1,2,3])
    person = birthday_dict[today]
    name, email = person["name"], person["email"]

    with open("letter_templates/letter_"+str(letter_num)+".txt", "r") as letter:
        content = letter.read()
        content = content.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(S_EMAIL, S_PASS)
        connection.sendmail(from_addr=S_EMAIL,
                            to_addrs=email, 
                            msg=f"Subject:Happy Birthday!! \n\n{content}")







# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




