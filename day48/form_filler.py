from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Karolina")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Kowalczuk")

email = driver.find_element(By.NAME, value="email")
email.send_keys("KKowalczuk@wp.pl")

sign_up_button = driver.find_element(By.CSS_SELECTOR, value="form button")
sign_up_button.click()