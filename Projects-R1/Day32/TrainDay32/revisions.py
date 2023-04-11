# import -> smtplib
#
# from_email = "your_email@gmail.com"
# to_email = "another_email@gmail.com"
# password = "your_password"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=from_email, password=password)
#     connection.sendmail(
#         from_addr=from_email,
#         to_addrs=to_email,
#         msg="Subject:Hello\n\nThis is the body of my email"
#     )

import datetime as dt

# current date and time as a datetime object
now = dt.datetime.now()
print(now)  # not useful -> 2023-02-01 10:04:35.478033

year = now.year
print(year)
print(type(year))  # this is an int

month = now.month
print(month)
print(type(month))  # this is an int


# create a datetime object

date_of_birth = dt.datetime(year=1980, month=3, day=23)
print(date_of_birth)
