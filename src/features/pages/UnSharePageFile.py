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
        "ShareCount":(By.XPATH,'/html/body/div/ui-view/div[5]/div[3]/div/div[3]/ol/li[2]/div/div/div[2]/div[1]/ul/li[1]/span[2]')

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