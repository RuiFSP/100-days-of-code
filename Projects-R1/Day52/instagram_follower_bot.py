import os
from random import choice
from time import sleep


from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()


def wait():
    """generates a random wait time"""
    random_time = [5, 8, 13]
    sleep(choice(random_time))


# Careful with bots in social networks you might get banned/restricted 😃🤣
class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=Service(driver_path),
                                       options=webdriver.ChromeOptions().add_experimental_option("detach", "True"))

    def login(self):
        """login to instagram account and accepts essential cookies"""
        self.driver.get("https://www.instagram.com/accounts/login/")
        wait()
        # accept essential cookies
        self.driver.find_element(by=By.CSS_SELECTOR, value='button._a9--._a9_1').click()
        wait()

        # input username
        user = self.driver.find_element(by=By.XPATH, value='USER_PATH')
        user.send_keys(os.getenv('USER'))

        # input password
        password = self.driver.find_element(by=By.XPATH, value='PASSWORD_PATH')
        password.send_keys(os.getenv('PASSWORD') + Keys.ENTER)
        wait()

    def find_followers(self):
        """clicks on the followers of target account"""
        self.driver.get(f"https://www.instagram.com/{os.getenv('SIMILAR_ACCOUNT')}")
        wait()

        followers = self.driver.find_element(by=By.XPATH, value='FOLLOWERS_PATH')
        followers.click()

        wait()

        # scrolling down
        modal = self.driver.find_element(by=By.XPATH, value='FOLLOWERS_BUTTONS_PATH')
        for _ in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            wait()

    def follow(self):
        """method find all the follow buttons in the modal (popup) and click on each of them in turn """
        all_buttons = self.driver.find_elements(by=By.CSS_SELECTOR, value="li button")
        for button in all_buttons:
            try:
                button.click()
                wait()
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value='CANCEL_BUTTON_PATH')
                cancel_button.click()


bot_instagram = InstaFollower(os.getenv("CHROME_DRIVER_PATH"))
bot_instagram.login()
bot_instagram.find_followers()
bot_instagram.follow()
