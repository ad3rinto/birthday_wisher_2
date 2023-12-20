##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details.

# HINT: Make sure one of the entries matches today's date for testing purposes. 
import datetime as dt
import smtplib
from key import PASSWORD

import pandas as pd
import random

my_email = "mojojo.aderinto@gmail.com"
my_password = PASSWORD

day_of_week = dt.datetime.now()
today = day_of_week.day
month = day_of_week.month
print(month, today)
# 2. Check if today matches a birthday in the birthdays.csv
df = pd.read_csv("birthdays.csv")
print(df)
birthday_dictionary = df.to_dict("records")
print(birthday_dictionary)

for i in birthday_dictionary:
    if i["day"] == today and i["month"] == month:
        selector = random.randint(1, 3)
        with open(f"letter_templates/letter_{selector}.txt", "r") as letter:
            content = letter.read()
            real_content = content.replace("[NAME]", i["name"])
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(my_email, my_password)
                connection.sendmail(from_addr=my_email, to_addrs="agbako@myyahoo.com",
                                    msg=f"subject:Happy Birthday\n\n{real_content}")

# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
