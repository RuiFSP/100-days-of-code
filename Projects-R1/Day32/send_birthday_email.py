import datetime as dt
import pandas as pd
import random
import smtplib
import os

MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]
date_now = dt.datetime.now()
month_of_birthday = date_now.month
day_of_birthday = date_now.day


def send_happy_birthday_email(letter, email):
    # Use the smtplib to send the email to yourself
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject: Happy Birthday\n\n{letter}"
            )
    except Exception as ex:
        print("Something went wrong..", ex)


try:
    # 1. Update the birthdays.csv or generate data
    data_of_birthdays = pd.read_csv("birthdays.csv")
except FileNotFoundError:
    print("Something is wrong, file doe snot exist")
else:
    for _, row in data_of_birthdays.iterrows():
        # 2. Check if today matches a birthday in the birthdays.csv
        if int(row.get("month")) == month_of_birthday and int(row.get("day")) == day_of_birthday:
            person_name = row.get("name")
            person_to_send_email = row.get("email")

            # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
            # with the person's actual name from birthdays.csv
            try:
                with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt", mode='r') as letter_file:
                    letter_pick = letter_file.read()
            except FileNotFoundError:
                print("That file does not exist")
            else:
                personalized_letter = letter_pick.replace("[NAME]", person_name)

                # 4. Send the letter generated in step 3 to that person's email address.
                send_happy_birthday_email(letter=personalized_letter, email=person_to_send_email)
