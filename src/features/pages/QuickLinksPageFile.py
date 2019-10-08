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

sys.path.append("..")
from ..utilities import configuration
import time

class QuickLink(Header):

    browser = None
    header = None

    locator_dictionary = {
        "emailField": (By.XPATH, '//*[@id="user_email"]'),
        "password": (By.XPATH, '//*[@id="user_password"]'),
        "signInButton": (By.XPATH, '//*[@id="top-row"]/div[2]/a'),
        "signIn": (By.XPATH, "//button[text()= 'Login']"),
        "getStarted":(By.XPATH,'//*[@id="quickLinksOverlay"]/div[2]/ul/li[1]/a'),
        "LogIn": (By.XPATH, '//*[@id="et-secondary-nav"]/li/a'),
        "journal": (By.XPATH, '//*[@id="wrapper"]/navigation-menu/div/div[1]/div[1]/ul/li[2]/a'),
        "dayOne": (By.XPATH, '//*[@id="wrapper"]/div[2]/div[2]/div/div[1]/div/div[1]/div[4]/div[1]/div[4]/div/div[1]/div[1]/div'),
        "commentField": (By.XPATH, '//*[@id="textCommentNew"]'),
        "postComment":(By.XPATH, '//*[@id="btnCommentPost"]'),
        "profileicon": (By.XPATH, '//*[@id="mainheader"]/div[2]/div/div[6]/header/div[6]/bp-user-avatar/span/div[1]/a/img[1]'),
        "video": (By.XPATH, '//*[@id="wrapper"]/div[2]/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[1]'),
        "viewLesson": (By.XPATH, '//*[@id="wrapper"]/div[2]/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[1]/div[1]/div/div/a'),
        "writeAction": (By.XPATH, '//*[@id="discussion-comment-box"]/div[2]/div[1]/div[1]/div[1]/textarea'),
        "commentBox": (By.XPATH, '//*[@id="textCommentNew"]'),
        "WatchAVideo":(By.XPATH,'//*[@id="quickLinksOverlay"]/div[2]/ul/li[2]/a'),
        "postAction": (By.XPATH, '//*[@id="btnCommentPost"]'),
        "closeVideo":(By.XPATH,'/html/body/div[2]/div/div[1]/div/button'),
        "QuickLinks":(By.XPATH,'//*[@id="mainheader"]/div[2]/div/div[6]/header/div[6]/bp-user-avatar/span/div[1]/div/div[4]/div[3]/a'),
        "close": (By.XPATH, '//*[@id="discussion-comment-box"]/div[2]/div/div[1]/div[1]/a'),
        "commentDiv": (By.XPATH, '//*[@id="public-reflections"]/div[2]'),
        "edit": (By.XPATH, '//*[@id="public-reflections"]/div[2]/div[1]'),
        "continueButton": (By.XPATH, '/html/body/bp-global-overlays/div[3]/div[1]/div[3]/button'),
        "firstNextButton": (By.XPATH, '/html/body/bp-global-overlays/div[3]/div[2]/div[4]/button'),
        "secondNextButton": (By.XPATH, '/html/body/bp-global-overlays/div[3]/div[3]/div[4]/button'),
        "thirdNextButton": (By.XPATH, '/html/body/bp-global-overlays/div[3]/div[4]/div[4]/button'),
        "finishButton": (By.XPATH, '/html/body/bp-global-overlays/div[3]/div[5]/div[2]/button'),
        "activityFeed": (By.XPATH, '//*[@id="wrapper"]/navigation-menu/div/div[1]/div[1]/ul/li[1]'),
        "addBuddy": (By.XPATH, '//*[@id="wrapper"]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div'),
        "firstBuddy": (By.XPATH, '//*[@id="buddies-scrollable"]/div[1]/div[1]/div[1]/div[1]/div[3]'),
        "secondBuddy": (By.XPATH, '//*[@id="buddies-scrollable"]/div[1]/div[2]/div[1]/div[1]/div[3]'),
        "thirdBuddy": (By.XPATH, '//*[@id="buddies-scrollable"]/div[1]/div[3]/div[1]/div[1]/div[3]'),
        "done":(By.XPATH, '//*[@id="buddies-scrollable"]/div[1]/div/div[1]/div[2]'),
        "ChatWithUs":(By.XPATH,'//*[@id="quickLinksOverlay"]/div[2]/ul/li[3]/a'),
        "ShowHints":(By.XPATH,'//*[@id="quickLinksOverlay"]/div[2]/ul/li[4]/a'),
        "HintsPage":(By.XPATH,'/html/body/bp-global-overlays/div[2]/div[4]/div[1]/h1'),
        "CloseHints":(By.XPATH,'/html/body/bp-global-overlays/div[2]/div[5]/a/span'),
        "ApplyForJob":(By.XPATH,'//*[@id="quickLinksOverlay"]/div[2]/ul/li[5]/a'),
        "form":(By.XPATH,'/html/body/div[1]/ui-view/div[2]/div/div[1]/h1'),
        "BPIcon":(By.XPATH,'/html/body/div[1]/ui-view/div[1]/div/div/div[1]/a/img')
    }



    def ClickQuickLinksButton(self):
        elem = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((self.locator_dictionary["profileicon"])))
        ActionChains(self.browser).move_to_element(elem).perform()
        quick = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((self.locator_dictionary["QuickLinks"])))
        quick.click()

    def GetStarted(self):
        time.sleep(3)
        getStarted = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((self.locator_dictionary["getStarted"])))
        getStarted.click()

    def WatchVideo(self):
        time.sleep(3)
        watchVideo = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((self.locator_dictionary["WatchAVideo"])))
        watchVideo.click()

    def closeVideo(self):
        time.sleep(3)
        locateCrossButton=self.browser.find_element(*self.locator_dictionary['closeVideo']).is_displayed()
        assert (locateCrossButton)

    def ClosePlayingVideo(self):
        time.sleep(3)
        CloseVideo = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((self.locator_dictionary["closeVideo"])))
        CloseVideo.click()

    def chat(self):
        time.sleep(3)
        CloseVideo = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((self.locator_dictionary["ChatWithUs"])))
        CloseVideo.click()

    def hints(self):
        time.sleep(3)
        CloseVideo = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((self.locator_dictionary["ShowHints"])))
        CloseVideo.click()

    def HintsPageConferm(self):
        time.sleep(3)
        CloseVideo = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((self.locator_dictionary["HintsPage"])))
        CloseVideo.click()

    def CloseHints(self):
        time.sleep(3)
        CloseVideo = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((self.locator_dictionary["CloseHints"])))
        CloseVideo.click()

    def job(self):
        time.sleep(3)
        CloseVideo = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((self.locator_dictionary["ApplyForJob"])))
        CloseVideo.click()

    def VerifyjobsPage(self):
        time.sleep(3)
        CloseVideo = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((self.locator_dictionary["form"])))
        CloseVideo.click()

    def closeForm(self):
        goToHomePage = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((self.locator_dictionary["BPIcon"])))
        goToHomePage.click()