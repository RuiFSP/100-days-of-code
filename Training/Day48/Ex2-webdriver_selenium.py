from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)
chrome_drive_path = Service("c:\seleniumDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_drive_path, options=op)
driver.maximize_window()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# grad some information
article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')

#click a link
forest_link = driver.find_element(By.LINK_TEXT, 'forest fires')
# forest_link.click()

# fill and search  something
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)


