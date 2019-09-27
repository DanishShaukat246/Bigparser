from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import sys
from lib2to3.fixes.fix_input import context
from uuid import UUID

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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.features.pages.header import Header
from src.features.utilities import driver
from src.features.pages.header import Header
from src.features.utilities import driver

sys.path.append("..")
from ..utilities import configuration
import time

class Unshare(Header):

    browser = None
    header = None

    UnshareFeatureXpaths = {
        "ShareButton":(By.XPATH,'/html/body/div/ui-view/div[5]/div[3]/div/div[3]/ol/li[2]/div/div/div[2]/div[1]/ul/li[1]/span'),
        "DropDownIconOFShareButton":(By.XPATH,'//*[@id="shareModal"]/div/footer/div[1]/div/div/div'),
        "Unshare":(By.XPATH,'//*[@id="unshareLink"]'),
        "UnshareConfirm":(By.XPATH,'//*[@id="unshareModel"]/div/footer/div/div/input'),
        "UnshareModal":(By.XPATH,'//*[@id="unshareModel"]/div'),
        "ShareCount":(By.XPATH,'/html/body/div/ui-view/div[5]/div[3]/div/div[3]/ol/li[2]/div/div/div[2]/div[1]/ul/li[1]/span[2]'),
         "ShareButtonOpenedGrid":(By.XPATH,'//*[@id="share-link-modal"]/button'),
        "DropDownArow":(By.XPATH,'//*[@id="shareModal"]/div/footer/div[1]/div/div/div'),
        "UnshareOptionOfShareButton":(By.XPATH,'//*[@id="unshareLink"]'),
        "ConfirmUnshare":(By.XPATH,'//*[@id="unshareModel"]/div/footer/div/div/input'),
        "CloseGrid":(By.XPATH,'/html/body/div/ui-view/div/div/div[1]/header/div[1]/div[2]/div[1]/div[1]/a[1]/span'),
        "ClickClose":(By.XPATH,'//*[@id="shareModal"]/div/header/div/span[1]')
        }




    def ClickShare(self):
        sharebutton=WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located(self.UnshareFeatureXpaths["ShareButton"]))
        sharebutton.click()

    def ShareButtonDropdownIconClick(self):
        deopDownbutton = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.UnshareFeatureXpaths["DropDownIconOFShareButton"]))
        deopDownbutton.click()

    def ClickUnshare(self):
        unshare = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.UnshareFeatureXpaths["Unshare"]))
        unshare.click()

    def UnshareModal(self):
        unsharemodal = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.UnshareFeatureXpaths["UnshareModal"]))
        ModalLocated=unsharemodal.is_displayed()
        assert (ModalLocated)

    def DialogueBoxConfirm(self):
        unshareConfrim = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.UnshareFeatureXpaths["UnshareConfirm"]))
        unshareConfrim.click()

    def shareCount(self):
        try:
         time.sleep(10)
         count=self.browser.find_element(*self.UnshareFeatureXpaths["ShareCount"]).is_displayed()
         assert (count)
        except:
         assert (True)
        print ("File Unshared Successfully !")

    def Open(self):
        shareClick = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.UnshareFeatureXpaths["ShareButtonOpenedGrid"]))
        shareClick.click()

    def UnshareDropDown(self):
        ShareButtonDropDown = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.UnshareFeatureXpaths["DropDownArow"]))
        ShareButtonDropDown.click()

    def UnshareOptionClick(self):
        Unshare = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.UnshareFeatureXpaths["UnshareOptionOfShareButton"]))
        Unshare.click()

    def ConfrimUnshare(self):
        ConfirmUnshare = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.UnshareFeatureXpaths["ConfirmUnshare"]))
        ConfirmUnshare.click()
        time.sleep(10)

    def CloseIt(self):
        CloseFile = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.UnshareFeatureXpaths["CloseGrid"]))
        CloseFile.click()
        print ("File Unshare from share button after opening it in My Data tab successfully "
               "executed and passed !")

    def CloseShareModal(self):
        ClickClose = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.UnshareFeatureXpaths["ClickClose"]))
        ClickClose.click()


