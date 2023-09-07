from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


name = 'Lucas Kibet'

mailDriver = webdriver.Chrome()
mailDriver.get("https://10minutemail.net/")
mailDriver.implicitly_wait(5)

email = mailDriver.find_element(by=By.CLASS_NAME, value="mailtext").get_attribute('value')
# text_box.send_keys("Selenium")
# submit_button.click()
print(email)

voteDriver = webdriver.Chrome()
action = ActionChains(voteDriver)
voteDriver.get("https://cup.craydel.com/submissions/1738850155")
voteDriver.implicitly_wait(10)
elements = voteDriver.find_elements(By.CLASS_NAME, 'label-with-icon')
voteButton = voteDriver.find_element(By.XPATH,'//div[@id=\'app\']/div/main/div/div/section/div/div[2]/div[2]/div[2]/a/span')
action.move_to_element(voteButton).click().perform()
voteDriver.implicitly_wait(2)
#
# nameField = voteDriver.find_element(by=By.ID, value="vote_name")
# emailField = voteDriver.find_element(by=By.ID, value="vote_email")
#
# nameField.send_keys(name)
# emailField.send_keys(email)
#
# voteNowButton = voteDriver.find_element(By.CSS_SELECTOR, ".btn .btn-primary .v-btn .v-btn--is-elevated .v-btn--has-bg .theme--light .v-size--default")
# voteNowButton.click()
# voteDriver.implicitly_wait(2)
#
# otpField = voteDriver.find_element(by=By.CLASS_NAME, value="otp-field-box--0")
# otpField1 = voteDriver.find_element(by=By.CLASS_NAME, value="otp-field-box--1")
# otpField2 = voteDriver.find_element(by=By.CLASS_NAME, value="otp-field-box--2")
# otpField3 = voteDriver.find_element(by=By.CLASS_NAME, value="otp-field-box--3")
# otpField4 = voteDriver.find_element(by=By.CLASS_NAME, value="otp-field-box--4")
# otpField5 = voteDriver.find_element(by=By.CLASS_NAME, value="otp-field-box--5")
#
# otpField.send_keys('1')
# otpField1.send_keys('2')
# otpField2.send_keys('3')
# otpField3.send_keys('4')
# otpField4.send_keys('5')
# otpField5.send_keys('6')
# voteDriver.implicitly_wait(5)
