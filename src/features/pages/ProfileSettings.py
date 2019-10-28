import sys

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.features.pages.header import Header

sys.path.append("..")
import time


class Profile(Header):
    browser = None
    header = None

    profileSettingsXpaths = {
       "NavMenuIcon":(By.XPATH,'//*[@id="mainheader"]/div[2]/div/div[6]/header/div[1]/span'),
        "PublicNaveMenu":(By.XPATH,'//*[@id="leftSideNav"]/div/div[1]/div[4]/ul/li[3]/div'),
        "SharedNavMenu":(By.XPATH,'//*[@id="leftSideNav"]/div/div[1]/div[4]/ul/li[2]/div'),
        "SettingsNavMenu":(By.XPATH,'//*[@id="leftSideNav"]/div/div[1]/div[4]/ul/li[7]/div'),
        "sharedTypeDropDown":(By.XPATH,'//*[@id="single-button"]'),
        "publicTab":(By.XPATH,'/html/body/div/ui-view/div[1]/div[1]/div/ul/li[2]/a'),
        "ProfileDetails":(By.XPATH,'/html/body/div/ui-view/div[2]/div[1]/div/h1/div[1]'),
        "UserNameInput":(By.XPATH,'//*[@id="name"]'),
        "EmailInput":(By.XPATH,'//*[@id="Email"]'),
        "profile":(By.XPATH,'/html/body/div/ui-view/div[2]/div[2]/div/section[1]/div[1]/div/div/div/a'),
        "PictureUploadWidget":(By.XPATH,'/html/body/label[2]/input'),
        "SetPasswordButton":(By.XPATH,'/html/body/div/ui-view/div[2]/div[2]/div/section[2]/form/h2'),
        "CurrentPasswordInput":(By.XPATH,'//*[@id="curr_pass"]'),
        "NewPasswordInput":(By.XPATH,'//*[@id="new_pass"]'),
        "ConfirmPasswordInput":(By.XPATH,'//*[@id="conf_pass"]'),
        "UpdateButton":(By.XPATH,'/html/body/div/ui-view/div[2]/div[2]/div/section[5]/div/div[2]/span'),
        "CellNumberInput":(By.XPATH,'//*[@id="mobile-number"]'),
        "ConfirmationNote":(By.XPATH,'/html/body/div/ui-view/div[2]/div[2]/div/div[1]/p'),
        "NameProfile":(By.XPATH,'//*[@id="mainheader"]/div[2]/div/div[6]/header/div[6]/bp-user-avatar/span/div[1]/div/div[3]/h2'),
        "profileIcon":(By.XPATH,'//*[@id="mainheader"]/div[2]/div/div[6]/header/div[6]/bp-user-avatar/span/div[1]/a/img[2]')
    }

    def ClickNavButton(self):
        time.sleep(3)
        WebDriverWait(self.browser,10).until(
            EC.visibility_of_element_located(self.profileSettingsXpaths["NavMenuIcon"])).click()

    def NavOptios(self):
        time.sleep(3)
        public = WebDriverWait(self.browser,20).until(
            EC.visibility_of_element_located(self.profileSettingsXpaths["PublicNaveMenu"])).is_displayed()
        shared = self.browser.find_element(*self.profileSettingsXpaths["SharedNavMenu"]).is_displayed()
        settings = self.browser.find_element(*self.profileSettingsXpaths["SettingsNavMenu"]).is_displayed()
        assert (public)
        assert (shared)
        assert (settings)

    def ClickShare(self):
        self.browser.find_element(*self.profileSettingsXpaths["SharedNavMenu"]).click()
        shareDropDown = WebDriverWait(self.browser,20).until(
            EC.visibility_of_element_located(self.profileSettingsXpaths["sharedTypeDropDown"])).is_displayed()
        assert (shareDropDown)


    def ClickPublic(self):
        time.sleep(2)
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.profileSettingsXpaths["NavMenuIcon"])).click()
        time.sleep(2)
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.profileSettingsXpaths["PublicNaveMenu"])).click()

    def VerifyPublicTab(self):
        public = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.profileSettingsXpaths["publicTab"])).is_displayed()
        assert (public)

    def ClickSettings(self):
        time.sleep(3)
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.profileSettingsXpaths["NavMenuIcon"])).click()
        time.sleep(3)
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.profileSettingsXpaths["SettingsNavMenu"])).click()

    def VerifySettingsPage(self):
        time.sleep(2)
        profile = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.profileSettingsXpaths["ProfileDetails"])).is_displayed()
        assert (profile)

    def SettingsPageWidgets(self):
        time.sleep(2)
        userName = WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located(self.profileSettingsXpaths["UserNameInput"])).is_displayed()
        Email = WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located(self.profileSettingsXpaths["EmailInput"])).is_displayed()
        ProfilePic = WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located(self.profileSettingsXpaths["profile"])).is_displayed()
        assert (userName)
        assert (Email)
        assert (ProfilePic)

    def EnterName(self):
        time.sleep(3)
        WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located(self.profileSettingsXpaths["UserNameInput"])).clear()
        time.sleep(3)
        WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located(self.profileSettingsXpaths["UserNameInput"])).send_keys("Edited User Name")

    def UploadPicture(self):
        time.sleep(2)
        self.browser.find_element(*self.profileSettingsXpaths["PictureUploadWidget"]).send_keys("C:\\Users\\ZAWAR-PC\\Desktop\\bp.png")

    def ClickChangePassword(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.profileSettingsXpaths["SetPasswordButton"])).click()

    def PasswordFields(self):
        time.sleep(2)
        currentPassword = self.browser.find_element(*self.profileSettingsXpaths["CurrentPasswordInput"]).is_displayed()
        NewPassword = self.browser.find_element(*self.profileSettingsXpaths["NewPasswordInput"]).is_displayed()
        ConfirmPassword = self.browser.find_element(*self.profileSettingsXpaths["ConfirmPasswordInput"]).is_displayed()
        assert (currentPassword)
        assert (NewPassword)
        assert (ConfirmPassword)

    def CurrentPassword(self):
        self.browser.find_element(*self.profileSettingsXpaths["CurrentPasswordInput"]).send_keys("123456789")

    def NewPassword(self):
        self.browser.find_element(*self.profileSettingsXpaths["NewPasswordInput"]).send_keys("danish123456789")

    def ConfirmPassword(self):
        self.browser.find_element(*self.profileSettingsXpaths["ConfirmPasswordInput"]).send_keys("danish123456789")

    def CellNumber(self):
        self.browser.find_element(*self.profileSettingsXpaths["CellNumberInput"]).send_keys("+926785439896")

    def ClickUpdateButton(self):
        self.browser.find_element(*self.profileSettingsXpaths["UpdateButton"]).click()

    def ConfirmUpdate(self):
        time.sleep(2)
        confirmation =  WebDriverWait(self.browser,50).until(
            EC.visibility_of_element_located(self.profileSettingsXpaths["ConfirmationNote"])).is_displayed()
        assert (confirmation)

    def FromPrifileIconConfirm(self):
        time.sleep(3)
        self.browser.find_element(*self.profileSettingsXpaths["profileIcon"]).click()
        time.sleep(2)
        UserName = WebDriverWait(self.browser,30).until(
            EC.visibility_of_element_located(self.profileSettingsXpaths["NameProfile"]))
        NameText = UserName.text
        if NameText == "Edited User Name":
            assert (True)
        else:
            assert (False)
