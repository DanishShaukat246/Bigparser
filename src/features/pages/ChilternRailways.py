from lib2to3.fixes.fix_input import context
from selenium.webdriver.common.by import By
import json, os
from src.features.pages.header import Header
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from src.features.utilities import driver, configuration
import time
import datetime
from array import *
from src.features.pages.temporary import *
from random import *

class benefitsPage(Header):
    driver = None
    browser = None

    Locator_login_buttons = {
        "sigmup": (By.XPATH, '/html/body/ace-root/div/ace-header/header/div/div/ul/li[3]'),
        "reg":(By.XPATH, '/html/body/ace-root/div/main/div/ace-account/div/div/div[1]/a[2]'),
    }








    def input_data(self,password, Confirm_password):
        emails = self.browser.find_element(*self.Locator_login_buttons['password'])
        self.sendKeys(emails,password)
        pwdField = self.browser.find_element(*self.Locator_login_buttons['Confirm_password'])
        self.sendKeys(pwdField,Confirm_password)


    def flname(self,fname, lname):
        Fname = self.browser.find_element(*self.Locator_login_buttons['Fname'])
        self.sendKeys(Fname,fname)
        Lname = self.browser.find_element(*self.Locator_login_buttons['Lname'])
        self.sendKeys(Lname,lname)




