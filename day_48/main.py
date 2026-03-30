from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from time import time

driver = webdriver.Chrome()
driver.get("https://ozh.github.io/cookieclicker/")

sleep(3)

try:
    driver.find_element(by=By.ID, value="langSelect-EN").click()
    print("Language selected successfully.")
    sleep(3)
except NoSuchElementException:
    print("Failed to select language.")
    


try:
    cookie = driver.find_element(by=By.ID, value="bigCookie")
    print("cookie found successfully.")
except NoSuchElementException:
    print("Failed to find the big cookie.")
    quit()

tempo_confere_item = 5

while (True):
    cookie.click()
    
    if time() > tempo_confere_item:
        try:
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            cookie_text = cookies_element.text
            cookie_count = int(cookie_text.split()[0].replace(",", ""))
            print(f"Current cookies: {cookie_count}")
        except NoSuchElementException:
            print("Failed to retrieve cookie count.")
            continue

        products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")
        best_item = None
        for product in reversed(products):
            if "enabled" in product.get_attribute("class"):
                best_item = product
                break

        if best_item:
            try:
                best_item.click()
                print("Purchased an item.")
            except Exception as e:
                print(f"Failed to purchase item: {e}")
        
        tempo_confere_item = time() + 5  # Reset timer for next check    
    
