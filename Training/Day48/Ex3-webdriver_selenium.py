from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)
chrome_drive_path = Service("c:\seleniumDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_drive_path, options=op)
driver.maximize_window()

driver.get("https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")

# fill first name
first_name = driver.find_element(By.NAME, 'fName')
first_name.send_keys("Pikatchu")

# fill last name
last_name = driver.find_element(By.NAME, 'lName')
last_name.send_keys("Zzzzzzz")

# fill email
email = driver.find_element(By.NAME, 'email')
email.send_keys("pikatchuzzzz@gmail.com")

#click sigup
sign_up = driver.find_element(By.CLASS_NAME, 'btn')
sign_up.click()