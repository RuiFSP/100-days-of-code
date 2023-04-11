import json
import os
from time import sleep

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

load_dotenv()

# relevant links
url_form = os.getenv("URL_FORM")
url = os.getenv("URL_ZILLOW")

# scrapping current page:
headers = {
    "User-Agent": "en-US,en;q=0.5",
    "Accept-Language": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/110.0.0.0 Safari/537.36", }
params = {'searchQueryState': {"pagination": {"currentPage": 1}, "usersSearchTerm": "San Francisco, CA",
                               "mapBounds": {"west": -122.63417281103516, "east": -122.23248518896484,
                                             "south": 37.66503360680629, "north": 37.88538511109397}, "mapZoom": 12,
                               "regionSelection": [{"regionId": 20330, "regionType": 6}], "isMapVisible": 0,
                               "filterState": {"price": {"max": 872627}, "beds": {"min": 1}, "fore": {"value": 0},
                                               "mp": {"max": 3000}, "auc": {"value": 0}, "nc": {"value": 0},
                                               "fr": {"value": 1}, "fsbo": {"value": 0}, "cmsn": {"value": 0},
                                               "fsba": {"value": 1}}, "isListVisible": 1}}

response = requests.get(url=url, headers=headers, params=params)

properties_listing = response.content
soup = BeautifulSoup(properties_listing, 'html.parser')

data = json.loads(
    soup.select_one("script[data-zrr-shared-data-key]")
    .contents[0]
    .strip("!<>-")
)

all_data = data['cat1']['searchResults']['listResults']

list_address = []
list_of_prices = []
list_of_url = []

# scrap with Beautiful soup the price, address and url
for i in range(len(all_data)):
    # some items have the 'price' key nested inside units key, while others have simply inside data key
    try:
        price = all_data[i]['units'][0]['price']
    except KeyError:
        price = all_data[i]['price']
    address = all_data[i]['address']

    link = all_data[i]['detailUrl']
    # sometimes the link does not contain the starting website url, that's why we are inserting
    # "https://www.zillow.com{link}" at the starting of link
    if 'http' not in link:
        link_to_buy = f"https://www.zillow.com{link}"
    else:
        link_to_buy = link

    list_address.append(address)
    list_of_prices.append(price)
    list_of_url.append(link_to_buy)

driver_path = os.getenv("CHROME_DRIVER_PATH")
driver = webdriver.Chrome(service=Service(driver_path))

# fill google form with scrapped data
for n in range(len(list_address)):
    driver.get(os.getenv("URL_FORM"))

    sleep(2)
    address = driver.find_element(by=By.XPATH, value=os.getenv("ADDRESS_PATH"))
    price = driver.find_element(by=By.XPATH, value=os.getenv("PRICE_PATH"))
    link = driver.find_element(by=By.XPATH, value=os.getenv("LINK_PATH"))
    submit_button = driver.find_element(by=By.XPATH, value=os.getenv("SUBMIT_BUTTON_PATH"))

    address.send_keys(list_address[n])
    price.send_keys(list_of_prices[n])
    link.send_keys(list_of_url[n])
    submit_button.click()
