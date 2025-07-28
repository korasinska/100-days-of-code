from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

#clicking on a website
num_of_articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
#num_of_articles.click()
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
#all_portals.click()

#writing on a website with enter
search = driver.find_element(By.NAME, value="search")
#search.send_keys("Python")
search.send_keys("Python", Keys.ENTER)
