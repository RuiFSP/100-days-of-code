import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

load_dotenv()

PROMISED_DOWN = 200
PROMISED_UP = 20
CHROME_DRIVER_PATH = "../../chrome_driver/chromedriver.exe"
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=Service(driver_path))
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        # accept cookies.
        time.sleep(3)
        accept_button = self.driver.find_element(by=By.ID, value="onetrust-accept-btn-handler")
        accept_button.click()

        # start the scan
        time.sleep(3)
        go_button = self.driver.find_element(by=By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        # grab download and upload speeds
        time.sleep(40)
        self.up = float(self.driver.find_element(by=By.XPATH, value=os.getenv("SPEEDTEST_UPLOAD_PATH")).text)
        self.down = float(self.driver.find_element(by=By.XPATH, value=os.getenv("SPEEDTEST_DOWNLOAD_PATH")).text)
        print(self.down, self.up)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")
        time.sleep(10)

        # input email
        email = self.driver.find_element(by=By.XPATH, value='TWITTER_EMAIL_PATH')
        email.send_keys(TWITTER_EMAIL+Keys.ENTER)
        time.sleep(2)

        # input password
        password = self.driver.find_element(by=By.XPATH, value='TWITTER_PASSWORD_PATH')
        password.send_keys(TWITTER_PASSWORD+Keys.ENTER)
        time.sleep(2)

        # compose message
        tweet_compose = self.driver.find_element(by=By.XPATH, value='TWITTER_COMPOSE_PATH')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        time.sleep(3)
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(by=By.XPATH, value='TWITTER_BUTTON_PATH')
        tweet_button.click()
        time.sleep(2)
        print("Tweet Done")

        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
