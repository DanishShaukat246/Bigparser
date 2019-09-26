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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.features.pages.signinpage import SignInPage
from random import *



class Share(Header):
    driver = None
    browser = None
    #
    Locator_login_buttons = {
        "EmailForSignIn": (By.XPATH, '//*[@id="loginEmailAddr"]'),
        "DeleteConfermationButton": (By.XPATH, '//*[@id="deleteModal0"]/div/div/footer/div/div/input'),
        "DeleteGridButton": (By.XPATH,'/html/body/div/ui-view/div[5]/div[3]/div/div[3]/ol/li[2]/div/div/div[2]/div[1]/ul/li[3]/ul/div[3]/ul/li/span/a'),
        "moreOptions": ( By.XPATH, '/html/body/div/ui-view/div[5]/div[3]/div/div[3]/ol/li[2]/div/div/div[2]/div[1]/ul/li[3]'),
        "CrossButton": (By.XPATH, '/html/body/div/ui-view/div[5]/div[6]/div/div[2]/ul/li[2]/span[2]'),
        "PasswordForSignIn": (By.XPATH, '//*[@id="mainheader"]/div[3]/div/header/div/div[2]/div[1]/form/div[1]/div[1]/div[2]/input'),
        "SignInButton": (By.XPATH, '//*[@id="mainheader"]/div[3]/div/header/div/div[2]/div[1]/form/input'),
        "continueButton": (By.XPATH, '/html/body/bp-global-overlays/div[3]/div[1]/div[3]/button'),
        "error note": (By.XPATH, '/html/body/div/ui-view/div/div/section/p'),
        "PublicTabFileShareButton":(By.XPATH,'/html/body/div[1]/ui-view/div[1]/div[4]/div/div/ol/li[1]/div/div[2]/ul/li[1]/span'),
        "ShareButton":(By.XPATH,'/html/body/div/ui-view/div[5]/div[3]/div/div[3]/ol/li[2]/div/div/div[2]/div[1]/ul/li[1]/span'),
        "eror page email field": (By.XPATH, '/html/body/div/ui-view/div/div/section/div/form/div[1]/input'),
        "error page password field": (By.XPATH, '/html/body/div/ui-view/div/div/section/div/form/div[2]/input'),
        "eror page sign in button": (By.XPATH, '/html/body/div/ui-view/div/div/section/div/form/div[3]/input'),
        "Big Parser iscon of Home Page": (By.XPATH, '//*[@id="mainheader"]/div[2]/div/div[6]/header/div[2]/a/img'),
        "uploadwidget": (By.XPATH, '(//SPAN[@class="upload-name"])[2]'),
        "upload": (By.XPATH, '/html/body/label[1]/input'),
        "DownloadButton": (By.XPATH, '/html/body/div/ui-view/div[5]/div[3]/div/div[3]/ol/li[2]/div/div/div[2]/div[1]/ul/li[2]/span'),
        "LattestUploadedFile": (By.XPATH, '/html/body/div/ui-view/div[5]/div[3]/div/div[3]/ol/li[2]/div/div/div[1]/a/div/div/div[1]/h2'),
        "logout": (By.XPATH,'//*[@id="mainheader"]/div[2]/div/div[6]/header/div[6]/bp-user-avatar/span/div[1]/div/div[4]/div[4]/a'),
        "profileicon": (By.XPATH, '//*[@id="mainheader"]/div[2]/div/div[6]/header/div[6]/bp-user-avatar/span/div[1]/a/img[1]'),
        "DoneButtons": (By.XPATH, '/html/body/div/ui-view/div[5]/div[6]/div/footer/div/div/input'),
        "cencelButton": (By.XPATH, '/html/body/div[1]/ui-view/div[5]/div[6]/div/footer/div/div/a'),
        "PublicRadioButton":(By.XPATH,'//*[@id="file-xml"]'),
        "MyData":(By.XPATH,'/html/body/div[1]/ui-view/div[1]/div[1]/div/ul/li[1]/a'),
        "Public":(By.XPATH,'/html/body/div[1]/ui-view/div[5]/div[1]/div/ul/li[2]/a'),
        "Shared":(By.XPATH,'/html/body/div[1]/ui-view/div[1]/div[1]/div/ul/li[3]/a'),
        "PublicTabLink":(By.XPATH,'//*[@id="slSuccessMesg"]/ul/li[2]/a'),
        "ShareButtonModal":(By.XPATH,'//*[@id="shareModal"]/div/footer/div[1]/div/div/input'),
        "ShareSuccessMessage":(By.XPATH,'//*[@id="slSuccessMesg"]'),
        "LattestUploadPublicTab":(By.XPATH,'/html/body/div/ui-view/div[1]/div[4]/div/div/ol/li[1]/div/div[1]/div[1]/a/div[1]/h2'),
        "ShareCount":(By.XPATH,'/html/body/div[1]/ui-view/div[5]/div[3]/div/div[3]/ol/li[2]/div/div/div[2]/div[1]/ul/li[1]/span[2]'),
        "CloseShareModal":(By.XPATH,'/html/body/div[3]/div/div/div/div/div/div/header/span'),
        "Facebook":(By.XPATH,'/html/body/div[3]/div/div/div/div/div/div/form/div/div[3]/div[2]/a[1]'),
        "Twitter":(By.XPATH,'/html/body/div[3]/div/div/div/div/div/div/form/div/div[3]/div[2]/a[2]'),
        "Google":(By.XPATH,'/html/body/div[3]/div/div/div/div/div/div/form/div/div[3]/div[2]/a[3]'),
        "Linkdin":(By.XPATH,'/html/body/div[3]/div/div/div/div/div/div/form/div/div[3]/div[2]/a[4]'),
        "CrossButtonAfterError":(By.XPATH,'//*[@id="shareModal"]/div/header/div/span[1]'),
        "okeyButton":(By.XPATH,'//*[@id="confirmShareModal"]/div/div/footer/div/div/input'),
        "CrossMessage":(By.XPATH,'/html/body/div[3]/div/div/div/div/div/div/form/div/div[2]/div[2]/span'),
        "LinkCopyMessage":(By.XPATH,'/html/body/div[3]/div/div/div/div/div/div/form/div/div[2]/div[2]/p'),
        "CopyButton":(By.XPATH,'/html/body/div[3]/div/div/div/div/div/div/form/div/div[2]/div[1]/a'),
        "newRadioButton": (By.XPATH, '/html/body/div/ui-view/div[5]/div[6]/div/div[2]/ul/li[2]/div[2]/input'),
        "Existing email error pop up": (By.XPATH, '/html/body/div/ui-view/div[1]/div/div[1]/div/form/div[2]/div/div[3]')
    }
    def clickShare(self):
        self.browser.find_element(*self.Locator_login_buttons['ShareButton']).click()
        time.sleep(2)

    def PublicRadio(self):
        rr = self.browser.find_element(*self.Locator_login_buttons['PublicRadioButton']).is_selected()
        pp = False
        if (rr == True):
            pp = True
            assert (pp)
        else:
            self.browser.find_element(*self.Locator_login_buttons['PublicRadioButton']).click()

    def ClickShareButton(self):
        okey=self.browser.find_element(*self.Locator_login_buttons['okeyButton']).is_displayed()
        if(okey==True):
            self.browser.find_element(*self.Locator_login_buttons['okeyButton']).click()
            time.sleep(2)
            self.browser.find_element(*self.Locator_login_buttons['CrossButtonAfterError']).click()
        else:
            self.browser.find_element(*self.Locator_login_buttons['ShareButtonModal']).click()
        time.sleep(2)

    def VerifySuccess(self):
        dd=self.browser.find_element(*self.Locator_login_buttons['ShareSuccessMessage']).is_displayed()
        if(dd):
          assert (dd)
        else:
            time.sleep(5)
            self.browser.find_element(*self.Locator_login_buttons['okeyButton']).click()
            time.sleep(2)
            self.browser.find_element(*self.Locator_login_buttons['CrossButtonAfterError']).click()
            time.sleep(3)
            self.browser.find_element(*self.Locator_login_buttons['Public']).click()
        time.sleep(2)

    def GoPublic(self):
        try:
           qq=self.browser.find_element(*self.Locator_login_buttons['PublicTabLink']).is_displayed()
           if(qq):
              self.browser.find_element(*self.Locator_login_buttons['PublicTabLink']).click()
              time.sleep(3)
        except:
            assert (True)

    def VerifyPresence(self):
        loateFile=WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located(self.Locator_login_buttons["LattestUploadPublicTab"]))
        fileTitle = loateFile.text
        if fileTitle == 'Second Edited Name':
            a = True
        else:
            a = False
        assert (a)
        print ("Public File Sharing successful ! \n")

    def InTabShareButtonPress(self):
        self.browser.find_element(*self.Locator_login_buttons['PublicTabFileShareButton']).click()
        time.sleep(2)

    def clickCopy(self):
        self.browser.find_element(*self.Locator_login_buttons['CopyButton']).click()
        time.sleep(2)

    def VerifyCopy(self):
        ff=self.browser.find_element(*self.Locator_login_buttons['LinkCopyMessage']).is_displayed()
        assert (ff)

    def CloseSuccessMsg(self):
        time.sleep(3)
        self.browser.find_element(*self.Locator_login_buttons['CrossMessage']).click()
        time.sleep(2)

    def VerifySocialShare(self):
        gg = self.browser.find_element(*self.Locator_login_buttons['Facebook']).is_displayed()
        assert (gg)
        ii = self.browser.find_element(*self.Locator_login_buttons['Twitter']).is_displayed()
        assert (ii)
        jj = self.browser.find_element(*self.Locator_login_buttons['Google']).is_displayed()
        assert (jj)
        kk = self.browser.find_element(*self.Locator_login_buttons['Linkdin']).is_displayed()
        assert (kk)
    def verifyCopy(self):
        hh = self.browser.find_element(*self.Locator_login_buttons['CopyButton']).is_displayed()
        assert (hh)

    def CloseModal(self):
        time.sleep(3)
        self.browser.find_element(*self.Locator_login_buttons['CloseShareModal']).click()

    def GoToMyData(self):
        myData = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.Locator_login_buttons["MyData"]))
        myData.click()

    def VerifyShareCount(self):
        time.sleep(5)
        hh = self.browser.find_element(*self.Locator_login_buttons['ShareCount']).text
        kk=str(hh)
        m=False
        if(kk>=1):
            m=True
            assert (m)
        else:
            assert(m)


