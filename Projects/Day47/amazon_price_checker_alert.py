import os
import smtplib

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()


# Use BeautifulSoup to Scrape the Product Price
URL = os.getenv("URL")

headers = {
    "User-Agent": "en-US,en;q=0.5",
    "Accept-Language": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/110.0.0.0 Safari/537.36",
}

response = requests.get(URL, headers=headers)
amazon_page = response.text
soup = BeautifulSoup(amazon_page, "lxml")
price = soup.select_one("span.a-offscreen").getText().split("$")[1].split(".")[0].replace(",", ".")
price_as_float = float(price)

# Email Alert When Price Below Preset Value
BUY_PRICE = 2500

from_email = os.getenv("from_email")
to_email = os.getenv("to_email")
password = os.getenv("password")

title = soup.find(id="productTitle").getText().split(":")[0]

if price_as_float < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(
            from_addr=from_email,
            to_addrs=to_email,
            msg=f"Subject:Amazon Price Alert\n\n"
                f"{title} is now {price_as_float}\n "
                f"{URL}".encode("ascii", errors="ignore")
        )
