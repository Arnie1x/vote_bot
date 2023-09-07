import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# This method is used to generate a new name from a dataset
def get_new_name():
    fNamesText = open('assets/fnames.txt', 'r')
    lNamesText = open('assets/lnames.txt', 'r')
    fNames = fNamesText.readlines()
    lNames = lNamesText.readlines()
    newName = fNames[random.randint(0, len(fNames))] + ' ' + lNames[random.randint(0, len(lNames))]
    lNamesText.close()
    fNamesText.close()
    return newName


for i in range(0, 1000):
    try:
        # Get email first
        mailDriver = webdriver.Firefox()
        mailAction = ActionChains(mailDriver)
        mailDriver.get("https://www.minuteinbox.com/")
        voteDriver = webdriver.Firefox()
        voteAction = ActionChains(voteDriver)
        voteDriver.get("https://cup.craydel.com/submissions/1738850155")
        mailDriver.set_window_size(1024, 768)
        voteDriver.set_window_size(1024, 768)

        name = get_new_name()
        mailDriver.implicitly_wait(5)
        email = mailDriver.find_element(by=By.ID, value="email").text

        # Initiate Voting on Website
        voteDriver.implicitly_wait(13)
        elements = voteDriver.find_elements(By.CLASS_NAME, 'label-with-icon')
        voteButton = voteDriver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/section[1]/div/div[2]/div[2]/div[2]/a/span')
        voteAction.move_to_element(voteButton).click().perform()
        voteDriver.implicitly_wait(5)

        nameField = voteDriver.find_element(by=By.ID, value="vote_name")
        emailField = voteDriver.find_element(by=By.ID, value="vote_email")

        nameField.send_keys(name)
        emailField.send_keys(email)

        voteDriver.implicitly_wait(3)
        voteNowButton = voteDriver.find_element(By.XPATH, "//div[@id='app']/div[3]/div/div/div/form/div[5]/button/span")
        voteAction.move_to_element(voteNowButton).click().perform()
        voteDriver.implicitly_wait(2)

        otpField = voteDriver.find_element(by=By.CLASS_NAME, value="otp-field-box--0")
        otpField1 = voteDriver.find_element(by=By.CLASS_NAME, value="otp-field-box--1")
        otpField2 = voteDriver.find_element(by=By.CLASS_NAME, value="otp-field-box--2")
        otpField3 = voteDriver.find_element(by=By.CLASS_NAME, value="otp-field-box--3")
        otpField4 = voteDriver.find_element(by=By.CLASS_NAME, value="otp-field-box--4")
        otpField5 = voteDriver.find_element(by=By.CLASS_NAME, value="otp-field-box--5")

        # Now, get the OTP code from 10minutemail

        mailReceived = False
        while not mailReceived:
            time.sleep(60)
            mailList = mailDriver.find_elements(by=By.TAG_NAME, value="td")
            for mail in mailList:
                if mail.text.__contains__('Craydel'):
                    mailReceived = True
                    mailAction.move_to_element(mail).double_click().perform()
                    mailDriver.implicitly_wait(2)
                    break
                else:
                    print('Waiting for Mail...')
                time.sleep(10)

        mailDriver.implicitly_wait(3)
        mailDriver.switch_to.frame(mailDriver.find_element(By.ID, 'iframeMail'))
        mailText = mailDriver.find_elements(By.TAG_NAME, "p")
        # print(mailText.text)

        otpCode = ''
        for text in mailText:
            if text.text[0].startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
                otpCode = text.text

        otpField.send_keys(otpCode[0])
        otpField1.send_keys(otpCode[1])
        otpField2.send_keys(otpCode[2])
        otpField3.send_keys(otpCode[3])
        otpField4.send_keys(otpCode[4])
        otpField5.send_keys(otpCode[5])
        voteDriver.implicitly_wait(5)

        placeVoteNowButton = voteDriver.find_element(By.XPATH,
                                                     "//div[@id='app']/div[3]/div/div/div/form/div[3]/button/span")
        voteAction.move_to_element(placeVoteNowButton).click().perform()
        voteDriver.implicitly_wait(3)

        voteDriver.close()
        mailDriver.close()
    except Exception as N:
        print('An error occurred on run: ' + str(i + 1) + '. Restarting...')
        print(N)
        voteDriver.close()
        mailDriver.close()
    else:
        print('Vote #' + str(i + 1) + ' Submitted')
