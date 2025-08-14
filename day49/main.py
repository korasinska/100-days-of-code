from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

webdriver = webdriver.Chrome(options=chrome_options)
webdriver.get("link")
sing_in_button = webdriver.find_element(By.CSS_SELECTOR, value="div .sign-in-modal button")
sing_in_button.click()

time.sleep(1)

email = webdriver.find_element(By.ID, value="base-sign-in-modal_session_key")
email.send_keys("email")
password = webdriver.find_element(By.ID, value="base-sign-in-modal_session_password")
password.send_keys("pass", Keys.ENTER)

time.sleep(2)

#################send application############################
# easy_apply_button = webdriver.find_element(By.CLASS_NAME, value="jobs-apply-button")
# easy_apply_button.click()
# time.sleep(1)
# phone_number = webdriver.find_element(By.ID, value="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4279883140-9-phoneNumber-nationalNumber")
# phone_number.send_keys("666777888")

################save job posting####################

# save_button = webdriver.find_element(By.CLASS_NAME, value="jobs-save-button__text")
# save_button.click()

################save all the postings###################

jobs_list = webdriver.find_elements(By.CLASS_NAME, value="job-card-container--clickable")

for job in jobs_list:
    job.click()
    time.sleep(2)
    save_button = webdriver.find_element(By.CLASS_NAME, value="jobs-save-button__text")
    save_button.click()