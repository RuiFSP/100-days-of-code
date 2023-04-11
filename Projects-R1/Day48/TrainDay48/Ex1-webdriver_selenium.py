from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

load_dotenv()

op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)
chrome_drive_path = Service("c:\seleniumDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_drive_path, options=op)
driver.maximize_window()

driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, '.medium-widget.event-widget.last time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.medium-widget.event-widget.last li a')

events = {n: {"time": event_times[n].text, "names": event_names[n].text} for n in range(len(event_times))}

print(events)

driver.quit()
