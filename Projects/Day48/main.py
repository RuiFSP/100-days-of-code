import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service("../../chrome_driver/chromedriver.exe")
driver = webdriver.Chrome(service=ser)

driver.get("https://orteil.dashnet.org/cookieclicker/")

# consent
driver.find_element(By.CLASS_NAME, 'fc-button-label').click()
driver.implicitly_wait(10)
# choose language
driver.find_element(By.CSS_SELECTOR, '#langSelect-EN').click()
driver.implicitly_wait(10)

time.sleep(5)
time_out = time.time() + 60 * 20
buy_time = time.time() + 30

cookie = driver.find_element(By.CSS_SELECTOR, '#bigCookie')

while time.time() < time_out:
    cookie.click()

    if time.time() > buy_time:
        unlocked_upgrades = driver.find_elements(By.CSS_SELECTOR, '.crate.upgrade.enabled')

        if len(unlocked_upgrades) > 0:
            id_index = (len(unlocked_upgrades) - 1)

            buy_upgrade = driver.find_element(
                By.CSS_SELECTOR, f'#upgrade{id_index}.crate.upgrade.enabled')

            buy_upgrade.click()

        unlock_items_prices = driver.find_elements(By.CSS_SELECTOR, '.product.unlocked.enabled span.price')
        unlock_items_prices = [int(price.text.replace(",", "")) for price in unlock_items_prices]

        id_index = unlock_items_prices.index(max(unlock_items_prices))

        buy_item = driver.find_element(By.CSS_SELECTOR, f'#product{id_index}.product.unlocked.enabled')

        buy_item.click()

        buy_time = time.time() + 30

cookie_per_sec = driver.find_element(By.CSS_SELECTOR, '#cookies div')
per_sec = cookie_per_sec.text.replace("per second : ", "")
print(f"cookies/second: {per_sec}")
driver.save_screenshot("result.png")
time.sleep(5)
driver.quit()
