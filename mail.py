from selenium import webdriver
from selenium.webdriver.common.by import By

def getMail():
    driver = webdriver.Chrome()
    driver.get("https://10minutemail.net/")
    driver.implicitly_wait(5)

    email = driver.find_element(by=By.CLASS_NAME, value="mailtext").get_attribute('value')
    # submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    # text_box.send_keys("Selenium")
    # submit_button.click()
    return email