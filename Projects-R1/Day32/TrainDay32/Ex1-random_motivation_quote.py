import datetime as dt
from tkinter import messagebox
import random
import smtplib

# Use the datetime module to obtain the current dat of the week
# current date and time as a datetime object
now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)  # 2

if day_of_week == 2:

    # Open the quotes.txt file and obtain a list of quotes
    try:
        with open("quotes.txt") as quotes:
            list_of_quotes = [line for line in quotes.readlines()]
    except FileNotFoundError:
        messagebox.showinfo(title="File not found", message="No Data file Found")
    else:
        # Use the random module to pick a random quote from your list of quotes
        random_quote = random.choice(list_of_quotes)

    # Use the smtplib to send the email to yourself
    MY_EMAIL = "my_email@gmail.com"
    TO_EMAIL = "other_email@gmail.com"
    MY_PASSWORD = "my_password"
    email_text = """
    
    """

    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_EMAIL,
                msg=f"Subject: Wednesday Motivation\n\n{random_quote}"
            )
    except Exception as ex:
        print("Something went wrong..", ex)

