from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from time import time, sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

sleep(2)

try:
    # Select English language
    language_button = driver.find_element(by=By.ID, value="langSelect-EN")
    language_button.click()
    sleep(3) # more loading
except NoSuchElementException:
    print("Language selection not found")

sleep(1)

wait_time = 10
timeout = time() + wait_time

while True:
    cookie_button = driver.find_element(By.CSS_SELECTOR, value="#cookieAnchor button")
    cookie_button.click()
    if time() > timeout:
        cookies = driver.find_element(By.ID, value="cookies")
        cookie_text = cookies.text
        available_cookies = cookie_text.split(" ")[0]

        products = driver.find_elements(by=By.CSS_SELECTOR, value=".product.unlocked.enabled")

        max_price = 0
        best_item = None

        for product in products:
            product_price = float(product.text.split("\n")[1].replace(",", ""))
            print(product_price)
            if product_price > max_price:
                max_price = product_price
                best_item = product

        best_item.click()

        timeout = time() + wait_time







