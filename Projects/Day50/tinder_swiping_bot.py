import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

# Get the webdriver path
ser = Service("../../chrome_driver/chromedriver.exe")
driver = webdriver.Chrome(service=ser)

# provide the homepage and pause
driver.get(url="https://tinder.com/")

# login tinder
time.sleep(3)
driver.find_element(by=By.XPATH, value=os.getenv('login_tinder_path')).click()

# login facebook
time.sleep(3)
driver.find_element(by=By.XPATH, value=os.getenv('login_fb_path')).click()

time.sleep(3)
print(f"tinder: {driver.title}")
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(f"facebook: {driver.title}")

# fill fb email/password
time.sleep(3)
driver.find_element(by=By.XPATH, value='//*[@id="email"]').send_keys(os.getenv("email"))
driver.find_element(by=By.XPATH, value='//*[@id="pass"]').send_keys(os.getenv('password') + Keys.ENTER)

time.sleep(5)
driver.switch_to.window(base_window)
print(f"window: {driver.title}")

time.sleep(10)
# accept_location
location_btn = driver.find_element(by=By.XPATH, value=os.getenv('tinder_location_path'))
location_btn.click()

# deactivate notifications
no_notifications_btn = driver.find_element(by=By.XPATH, value=os.getenv('tinder_no_notifications_path'))
no_notifications_btn.click()
time.sleep(5)

# reject cookies
no_cookies = driver.find_element(by=By.XPATH, value=os.getenv('tinder_no_cookies_path'))
no_cookies.click()
time.sleep(3)

# starting daily "like/swipe right" for 100 people 🤣
counter = 1
# Loop like until dail limit of 100
while counter < 101:
    print(f"counter number is: {counter}")
    time.sleep(5)
    try:
        # Check if it's first card or not
        if counter == 1:
            driver.find_element(by=By.XPATH, value=os.getenv('tinder_first_person_path')).click()
            print('Clicked the 1st like')

        elif counter > 1:
            driver.find_element(by=By.XPATH, value=os.getenv('tinder_next_person_path')).click()
            print(f'This is like number: {counter}')
        else:
            try:
                back_out = driver.find_element(by=By.XPATH, value=os.getenv('tinder_found_a_match_path'))
                back_out.click()
                print('You found a match, plan a date')
            except NoSuchElementException:
                print("No Match with Person")
                continue

            try:
                # Sometimes tinder asks to add desktop app so this says no
                no_add_app = driver.find_element(by=By.XPATH, value=os.getenv('tinder_no_desktop_app_path'))
                no_add_app.click()
                # print("No add app to desktop")
            except NoSuchElementException:
                print("Add App Pop Up doesn't exist")

            try:
                no_more_likes = driver.find_element(by=By.XPATH, value=os.getenv('tinder_out_of_likes_path'))
                no_more_likes.click()
                print(" -------------No more Likes--------------")
                break
            except NoSuchElementException:
                continue

    except NoSuchElementException:
        print('No Like Button?')

    counter += 1

print("we finished no errors last line")
driver.quit()
