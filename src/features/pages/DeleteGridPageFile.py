from lib2to3.fixes.fix_input import context
from telnetlib import EC
from uuid import UUID
from  selenium.webdriver.support import expected_conditions as wait
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import json, os
from src.features.pages.header import Header
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from src.features.utilities import driver, configuration
import time
# from selenium import iframe
from selenium import webdriver
import random
import datetime
from array import *
from src.features.pages.temporary import *
from src.features.pages.signinpage import SignInPage
from random import *



class DeleteGrid(Header):
    driver = None
    browser = None
    #
    Locator_login_buttons = {
        "EmailForSignIn": (By.XPATH, '//*[@id="loginEmailAddr"]'),
        "DeleteConfermationButton":(By.XPATH,'//*[@id="deleteModal0"]/div/div/footer/div/div/input'),
        "DeleteGridButton":(By.XPATH,'/html/body/div/ui-view/div[5]/div[3]/div/div[3]/ol/li[2]/div/div/div[2]/div[1]/ul/li[3]/ul/div[3]/ul/li/span/a'),
        "moreOptions":(By.XPATH,'/html/body/div/ui-view/div[5]/div[3]/div/div[3]/ol/li[2]/div/div/div[2]/div[1]/ul/li[3]'),
        "CrossButton":(By.XPATH,'/html/body/div/ui-view/div[5]/div[6]/div/div[2]/ul/li[2]/span[2]'),
        "PasswordForSignIn": (By.XPATH, '//*[@id="mainheader"]/div[3]/div/header/div/div[2]/div[1]/form/div[1]/div[1]/div[2]/input'),
        "SignInButton": (By.XPATH, '//*[@id="mainheader"]/div[3]/div/header/div/div[2]/div[1]/form/input'),
        "continueButton": (By.XPATH, '/html/body/bp-global-overlays/div[3]/div[1]/div[3]/button'),
        "error note":(By.XPATH,'/html/body/div/ui-view/div/div/section/p'),
        "eror page email field":(By.XPATH,'/html/body/div/ui-view/div/div/section/div/form/div[1]/input'),
        "error page password field":(By.XPATH,'/html/body/div/ui-view/div/div/section/div/form/div[2]/input'),
        "eror page sign in button":(By.XPATH,'/html/body/div/ui-view/div/div/section/div/form/div[3]/input'),
        "Big Parser iscon of Home Page":(By.XPATH,'//*[@id="mainheader"]/div[2]/div/div[6]/header/div[2]/a/img'),
        "uploadwidget":(By.XPATH,'(//SPAN[@class="upload-name"])[2]'),
        "upload":(By.XPATH,'/html/body/label[1]/input'),
        "LattestUploadedFile":(By.XPATH,'/html/body/div/ui-view/div[5]/div[3]/div/div[3]/ol/li[2]/div/div/div[1]/a/div/div/div[1]/h2'),
        "logout":(By.XPATH,'//*[@id="mainheader"]/div[2]/div/div[6]/header/div[6]/bp-user-avatar/span/div[1]/div/div[4]/div[4]/a'),
        "profileicon":(By.XPATH,'//*[@id="mainheader"]/div[2]/div/div[6]/header/div[6]/bp-user-avatar/span/div[1]/a/img[1]'),
        "DoneButtons": (By.XPATH, '/html/body/div/ui-view/div[5]/div[6]/div/footer/div/div/input'),
        "cencelButton":(By.XPATH,'/html/body/div[1]/ui-view/div[5]/div[6]/div/footer/div/div/a'),
        "newRadioButton":(By.XPATH,'/html/body/div/ui-view/div[5]/div[6]/div/div[2]/ul/li[2]/div[2]/input'),
        "Existing email error pop up": (By.XPATH, '/html/body/div/ui-view/div[1]/div/div[1]/div/form/div[2]/div/div[3]')
    }

    def DeleteGrid(self):
        try:
         time.sleep(3)
         self.browser.find_element(*self.Locator_login_buttons['moreOptions']).click()
         time.sleep(3)
         self.browser.find_element(*self.Locator_login_buttons['DeleteGridButton']).click()
         time.sleep(5)
         self.browser.find_element(*self.Locator_login_buttons['DeleteConfermationButton']).click()
         time.sleep(5)
         print ("File has been deleted !  \n")
        except:
            print ("Some Exception Raised During Execution ")