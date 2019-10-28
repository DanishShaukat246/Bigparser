from lib2to3.fixes.fix_input import context
from uuid import UUID
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json, os
from src.features.pages.header import Header
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from src.features.utilities import driver, configuration
import time
import random
import datetime
from array import *
from src.features.pages.temporary import *
from src.features.pages.signinpage import SignInPage
from random import *


class benefitsPages(Header):
    driver = None
    browser = None
    #
    Locator_login_buttons = {
        "NameForSignUp": (By.XPATH, "//*[@id='fullName']"),
        "EmailForSignUp": (By.XPATH, '//*[@id="emailAddr"]'),
        "PasswordForSignUp": (By.XPATH, '/html/body/div/ui-view/div[1]/div/div[1]/div/form/div[3]/input'),
        "SignUpButton": (By.XPATH, '/html/body/div/ui-view/div[1]/div/div[1]/div/form/input'),
        "continueButton": (By.XPATH, '/html/body/bp-global-overlays/div[3]/div[1]/div[3]/button'),
        "firstNextButton":(By.XPATH,'/html/body/bp-global-overlays/div[3]/div[2]/div[4]/button'),
        "secondNextButton":(By.XPATH,'/html/body/bp-global-overlays/div[3]/div[3]/div[4]/button'),
        "thirdNextButton":(By.XPATH,'/html/body/bp-global-overlays/div[3]/div[4]/div[4]/button'),
        "finishButton":(By.XPATH,'/html/body/bp-global-overlays/div[3]/div[5]/div[2]/button'),
        "Existing email error pop up": (By.XPATH, '/html/body/div/ui-view/div[1]/div/div[1]/div/form/div[2]/div/div[3]')
    }


    def  loadBigparser(self,url):
        signinPage = SignInPage(context)
        signinPage.assertUrl(url)

    def entername(self):
        self.browser.find_element(*self.Locator_login_buttons['NameForSignUp']).send_keys("Testing name 123")
        time.sleep(5)

    def enterPassword(self):
        self.browser.find_element(*self.Locator_login_buttons['PasswordForSignUp']).send_keys("123456789")

    def enterEmailForSignUp(self):
        self.browser.find_element(*self.Locator_login_buttons['EmailForSignUp']).send_keys("tester598@gmail.com")

    def clickSignUpButton(self):
        self.browser.find_element(*self.Locator_login_buttons['SignUpButton']).click()

    def ClickCreateAccuntButton(self):
        WebDriverWait(self.browser,50).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["continueButton"]))
        a = self.browser.find_element(*self.Locator_login_buttons['continueButton']).is_displayed()
        assert (a)
        print ("User Logged in successfully !  \n")
    def VerifyPresenceSignUp(self):
        time.sleep(2)
        b = self.browser.find_element(*self.Locator_login_buttons['NameForSignUp']).is_displayed()
        c = self.browser.find_element(*self.Locator_login_buttons['PasswordForSignUp']).is_displayed()
        d = self.browser.find_element(*self.Locator_login_buttons['EmailForSignUp']).is_displayed()
        e = self.browser.find_element(*self.Locator_login_buttons['SignUpButton']).is_displayed()
        assert (b)
        assert (c)
        assert (d)
        assert (e)

    def LocatePopUp(self):
        time.sleep(5)
        f = self.browser.find_element(*self.Locator_login_buttons['Existing email error pop up']).is_displayed()
        assert (f)

    def rendomizeEmail(self):
        nRand = randint(1, 9999)

        emailToBeCleared = WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located(self.Locator_login_buttons["EmailForSignUp"]))
        emailToBeCleared.clear()
        emailToBeCleared.send_keys("Tester_" + str(nRand) + "@gmail.com")
        emailToBeCleared.send_keys(Keys.CONTROL+'a')
        emailToBeCleared.send_keys(Keys.CONTROL+'c')

    def afterRandomizing(self):
        self.browser.find_element(*self.Locator_login_buttons['SignUpButton']).click()

    def incognito(self):
        time.sleep(10)
        b = self.browser.find_element(*self.Locator_login_buttons['NameForSignUp']).is_displayed()
        c = self.browser.find_element(*self.Locator_login_buttons['PasswordForSignUp']).is_displayed()
        d = self.browser.find_element(*self.Locator_login_buttons['EmailForSignUp']).is_displayed()
        e = self.browser.find_element(*self.Locator_login_buttons['SignUpButton']).is_displayed()
        assert (b)
        assert (c)
        assert (d)
        assert (e)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        window_2 = self.browser.window_handles[0]
        self.browser.switch_to_window(window_2)
        driver = webdriver.Chrome('C:\Users\ZAWAR-PC\Desktop\chromedriver.exe')
        driver.get("https://chrome.google.com/webstore/category/extensions?hl=en")
        time.sleep(10)
