##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import smtplib
import datetime as dt
import random

# Import the data into a dictionary

birthday_df = pandas.read_csv("birthdays.csv")
birthday_dic = birthday_df.to_dict(orient= "records")

#Get today's date and month

now = dt.datetime.now()
current_month = now.month
current_day = now.day

# Iterate through the dictionary and if the current date matches a birthday, then proceed

for birthday in birthday_dic:
    if birthday["month"] == current_month and birthday["day"] == current_day:
        # Create a list of letters
        birthday_letters = []
        for i in range(1, 4):
            with open(f"letter_templates/letter_{i}.txt", 'r') as file:
                curr_letter = file.read()
                updated_letter = curr_letter.replace("[NAME]", birthday["name"])
                birthday_letters.append(updated_letter)
        # Choose a random letter
        letter_to_send = random.choice(birthday_letters)

        # Send them an email
        my_email = "senderemailhere@gmail.com"
        password = "app password here"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday["email"],
                                msg=f"Subject:Happy Birthday!\n\n{letter_to_send}")




