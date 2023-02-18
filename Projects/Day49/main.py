import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from dotenv import load_dotenv

load_dotenv()

# Get the webdriver path
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)
ser = Service("../../chrome_driver/chromedriver.exe")
driver = webdriver.Chrome(service=ser)

# provide the homepage and pause
driver.get(url="https://www.linkedin.com/home")
driver.implicitly_wait(5)

# reject cookies
reject_cookie = driver.find_element(by=By.XPATH, value=os.getenv(key="COOKIE_PATH"))
reject_cookie.click()

# sign in
driver.find_element(by=By.ID, value='session_key').send_keys(os.getenv(key="EMAIL"))
driver.find_element(by=By.ID, value='session_password').send_keys(os.getenv(key="PASSWORD"))
driver.find_element(by=By.XPATH, value=os.getenv(key="LOGIN_BTN")).click()
driver.implicitly_wait(30)

time.sleep(30)

driver.quit()