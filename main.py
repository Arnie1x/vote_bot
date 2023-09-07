import random
import time

from selenium import webdriver
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


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


successfulVotes = 0
unsuccessfulVotes = 0

for i in range(0, 1000):
    try:
        # Get email first
        mailDriver = webdriver.Firefox()
        mailAction = ActionChains(mailDriver)
        mailDriver.get("https://www.minuteinbox.com/")
        voteDriver = webdriver.Firefox()
        voteAction = ActionChains(voteDriver)
        voteDriver.get("https://cup.craydel.com/submissions/1738850155")
        ActionBuilder(voteDriver).clear_actions()
        ActionBuilder(mailDriver).clear_actions()
        # mailDriver.set_window_size(1024, 768)
        # voteDriver.set_window_size(1024, 768)
        mailDriver.implicitly_wait(120)
        voteDriver.implicitly_wait(120)

        name = get_new_name()
        email = mailDriver.find_element(by=By.ID, value="email").text

        # Initiate Voting on Website
        # voteDriver.implicitly_wait(20)
        voteButton = voteDriver.find_element(By.XPATH,
                                             '//*[@id="app"]/div/main/div/div/section[1]/div/div[2]/div[2]/div[2]/a/span')
        voteAction.move_to_element(voteButton).pause(0.5).click().perform()

        # voteDriver.implicitly_wait(10)
        nameField = voteDriver.find_element(by=By.ID, value="vote_name")
        emailField = voteDriver.find_element(by=By.ID, value="vote_email")

        nameField.send_keys(name)
        emailField.send_keys(email)

        # voteDriver.implicitly_wait(3)
        voteNowButton = voteDriver.find_element(By.XPATH, "//div[@id='app']/div[3]/div/div/div/form/div[5]/button/span")
        voteAction.move_to_element(voteNowButton).pause(0.5).click().perform()

        # Now, get the OTP code from 10minutemail

        mailReceived = False
        while not mailReceived:
            time.sleep(30)
            # mailDriver.implicitly_wait(10)
            mailList = mailDriver.find_elements(by=By.TAG_NAME, value="td")
            for mail in mailList:
                if mail.text.__contains__('Craydel'):
                    mailReceived = True
                    mailAction.move_to_element(mail).pause(0.5).double_click().perform()
                    break
                else:
                    print('Waiting for Mail...')
                time.sleep(10)

        # mailDriver.implicitly_wait(20)
        time.sleep(2)
        mailDriver.switch_to.frame(mailDriver.find_element(By.ID, 'iframeMail'))
        mailText = mailDriver.find_elements(By.TAG_NAME, "p")
        # print(mailText.text)

        otpCode = ''
        for text in mailText:
            if text.text[0].startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
                otpCode = text.text

        # voteDriver.implicitly_wait(20)
        otpField = voteDriver.find_element(by=By.CLASS_NAME, value="otp-field-box--0")
        otpField1 = voteDriver.find_element(by=By.CLASS_NAME, value="otp-field-box--1")
        otpField2 = voteDriver.find_element(by=By.CLASS_NAME, value="otp-field-box--2")
        otpField3 = voteDriver.find_element(by=By.CLASS_NAME, value="otp-field-box--3")
        otpField4 = voteDriver.find_element(by=By.CLASS_NAME, value="otp-field-box--4")
        otpField5 = voteDriver.find_element(by=By.CLASS_NAME, value="otp-field-box--5")

        otpField.send_keys(otpCode[0])
        otpField1.send_keys(otpCode[1])
        otpField2.send_keys(otpCode[2])
        otpField3.send_keys(otpCode[3])
        otpField4.send_keys(otpCode[4])
        otpField5.send_keys(otpCode[5])

        # voteDriver.implicitly_wait(10)
        placeVoteNowButton = voteDriver.find_element(By.XPATH,
                                                     "//*[@id='app']/div[3]/div/div/div/form/div[3]/button[1]")
        voteAction.move_to_element(placeVoteNowButton).pause(0.5).click().perform()
        time.sleep(0.5)
        voteDriver.close()
        mailDriver.close()
        voteDriver.quit()
        mailDriver.quit()
        successfulVotes += 1
    except Exception as N:
        unsuccessfulVotes += 1
        print('An error occurred on run: ' + str(i + 1) + '. Restarting...')
        print(N)
        voteDriver.close()
        mailDriver.close()
        voteDriver.quit()
        mailDriver.quit()
    else:
        print('\nRun #' + str(i + 1))
        print('\tSuccessful Votes: ' + str(successfulVotes))
        print('\tUnsuccessful Votes: ' + str(unsuccessfulVotes))
