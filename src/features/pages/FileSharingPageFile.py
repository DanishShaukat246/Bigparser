from telnetlib import EC
import time

from Tkinter import Tk
from behave.formatter import null
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from src.features.pages.temporary import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Share(Header):
    driver = None
    browser = None
    #
    Locator_login_buttons = {
        "EmailForSignIn": (By.XPATH, '//*[@id="loginEmailAddr"]'),
        "DeleteConfermationButton": (By.XPATH, '//*[@id="deleteModal0"]/div/div/footer/div/div/input'),
        "DeleteGridButton": (By.XPATH,
                             '/html/body/div/ui-view/div[5]/div[3]/div/div[3]/ol/li[2]/div/div/div[2]/div[1]/ul/li[3]/ul/div[3]/ul/li/span/a'),
        "moreOptions": (
        By.XPATH, '/html/body/div/ui-view/div[5]/div[3]/div/div[3]/ol/li[2]/div/div/div[2]/div[1]/ul/li[3]'),
        "CrossButton": (By.XPATH, '/html/body/div/ui-view/div[5]/div[6]/div/div[2]/ul/li[2]/span[2]'),
        "PasswordForSignIn": (
        By.XPATH, '//*[@id="mainheader"]/div[3]/div/header/div/div[2]/div[1]/form/div[1]/div[1]/div[2]/input'),
        "SignInButton": (By.XPATH, '//*[@id="mainheader"]/div[3]/div/header/div/div[2]/div[1]/form/input'),
        "continueButton": (By.XPATH, '/html/body/bp-global-overlays/div[3]/div[1]/div[3]/button'),
        "error note": (By.XPATH, '/html/body/div/ui-view/div/div/section/p'),
        "PublicTabFileShareButton": (
        By.XPATH, '/html/body/div[1]/ui-view/div[1]/div[4]/div/div/ol/li[1]/div/div[2]/ul/li[1]/span'),
        "ShareButton": (
        By.XPATH, '/html/body/div/ui-view/div[5]/div[3]/div/div[3]/ol/li[2]/div/div/div[2]/div[1]/ul/li[1]/span'),
        "eror page email field": (By.XPATH, '/html/body/div/ui-view/div/div/section/div/form/div[1]/input'),
        "error page password field": (By.XPATH, '/html/body/div/ui-view/div/div/section/div/form/div[2]/input'),
        "eror page sign in button": (By.XPATH, '/html/body/div/ui-view/div/div/section/div/form/div[3]/input'),
        "Big Parser iscon of Home Page": (By.XPATH, '//*[@id="mainheader"]/div[2]/div/div[6]/header/div[2]/a/img'),
        "uploadwidget": (By.XPATH, '(//SPAN[@class="upload-name"])[2]'),
        "upload": (By.XPATH, '/html/body/label[1]/input'),
        "DownloadButton": (
        By.XPATH, '/html/body/div/ui-view/div[5]/div[3]/div/div[3]/ol/li[2]/div/div/div[2]/div[1]/ul/li[2]/span'),
        "LattestUploadedFile": (
        By.XPATH, '/html/body/div/ui-view/div[5]/div[3]/div/div[3]/ol/li[2]/div/div/div[1]/a/div/div/div[1]/h2'),
        "logout": (By.XPATH,
                   '//*[@id="mainheader"]/div[2]/div/div[6]/header/div[6]/bp-user-avatar/span/div[1]/div/div[4]/div[4]/a'),
        "profileicon": (
        By.XPATH, '//*[@id="mainheader"]/div[2]/div/div[6]/header/div[6]/bp-user-avatar/span/div[1]/a/img[1]'),
        "DoneButtons": (By.XPATH, '/html/body/div/ui-view/div[5]/div[6]/div/footer/div/div/input'),
        "cencelButton": (By.XPATH, '/html/body/div[1]/ui-view/div[5]/div[6]/div/footer/div/div/a'),
        "PublicRadioButton": (By.XPATH, '//*[@id="file-xml"]'),
        "MyData": (By.XPATH, '/html/body/div[1]/ui-view/div[1]/div[1]/div/ul/li[1]/a'),
        "Public": (By.XPATH, '/html/body/div[1]/ui-view/div[5]/div[1]/div/ul/li[2]/a'),
        "Shared": (By.XPATH, '/html/body/div[1]/ui-view/div[1]/div[1]/div/ul/li[3]/a'),
        "PublicTabLink": (By.XPATH, '//*[@id="slSuccessMesg"]/ul/li[2]/a'),
        "ShareButtonModal": (By.XPATH, '//*[@id="shareModal"]/div/footer/div[1]/div/div/input'),
        "ShareSuccessMessage": (By.XPATH, '//*[@id="slSuccessMesg"]'),
        "LattestUploadPublicTab": (
        By.XPATH, '/html/body/div/ui-view/div[1]/div[4]/div/div/ol/li[1]/div/div[1]/div[1]/a/div[1]/h2'),
        "ShareCount": (
        By.XPATH, '/html/body/div[1]/ui-view/div[5]/div[3]/div/div[3]/ol/li[2]/div/div/div[2]/div[1]/ul/li[1]/span[2]'),
        "CloseShareModal": (By.XPATH, '/html/body/div[3]/div/div/div/div/div/div/header/span'),
        "Facebook": (By.XPATH, '/html/body/div[3]/div/div/div/div/div/div/form/div/div[3]/div[2]/a[1]'),
        "Twitter": (By.XPATH, '/html/body/div[3]/div/div/div/div/div/div/form/div/div[3]/div[2]/a[2]'),
        "Google": (By.XPATH, '/html/body/div[3]/div/div/div/div/div/div/form/div/div[3]/div[2]/a[3]'),
        "Linkdin": (By.XPATH, '/html/body/div[3]/div/div/div/div/div/div/form/div/div[3]/div[2]/a[4]'),
        "CrossButtonAfterError": (By.XPATH, '//*[@id="shareModal"]/div/header/div/span[1]'),
        "okeyButton": (By.XPATH, '//*[@id="confirmShareModal"]/div/div/footer/div/div/input'),
        "CrossMessage": (By.XPATH, '/html/body/div[3]/div/div/div/div/div/div/form/div/div[2]/div[2]/span'),
        "LinkCopyMessage": (By.XPATH, '/html/body/div[3]/div/div/div/div/div/div/form/div/div[2]/div[2]/p'),
        "CopyButton": (By.XPATH, '/html/body/div[3]/div/div/div/div/div/div/form/div/div[2]/div[1]/a'),
        "newRadioButton": (By.XPATH, '/html/body/div/ui-view/div[5]/div[6]/div/div[2]/ul/li[2]/div[2]/input'),
        "Existing email error pop up": (
        By.XPATH, '/html/body/div/ui-view/div[1]/div/div[1]/div/form/div[2]/div/div[3]'),
        "GetSharbleLik": (By.XPATH, '//*[@id="shareModal"]/div/div[2]/div[10]/div[1]/h2'),
        "Copy": (By.XPATH, '//*[@id="shareModal"]/div/div[2]/div[10]/div[2]/div[1]/a'),
        "CopyConfirm": (By.XPATH, '//*[@id="shareModal"]/div/div[2]/div[10]/div[2]/div[2]/p'),
        "linkField": (By.XPATH, '//INPUT[@id="share-email-copy"]'),
        "FileTitleIncognito": (By.XPATH, '/html/body/div/ui-view/div[1]/div/header/div/div[2]/div/h1'),
        "closeButton": (By.XPATH, '//*[@id="shareModal"]/div/header/div/span[1]'),
        "DataToShare":(By.XPATH,'/html/body/div/ui-view/div[5]/div[1]/div/ul/li[3]/a'),
        "ShareDopSelect":(By.XPATH,"//*[@id='shareModal']/div/div[2]/div[7]/div/div[1]/a"),
        "FileSelect":(By.XPATH,'//*[@id="shareModal"]/div/div[2]/div[7]/div/div[2]/div[1]/div[2]/div/input'),
        "done":(By.XPATH,'//*[@id="shareModal"]/div/div[2]/div[7]/div/div[2]/footer/button[1]')
    }

    def clickShare(self):
        time.sleep(3)
        self.browser.find_element(*self.Locator_login_buttons["ShareButton"]).click()
    def PublicRadio(self):
        time.sleep(3)
        self.browser.find_element(*self.Locator_login_buttons['PublicRadioButton']).click()

    def ClickShareButton(self):
        okey = self.browser.find_element(*self.Locator_login_buttons['okeyButton']).is_displayed()
        if (okey == True):
            self.browser.find_element(*self.Locator_login_buttons['okeyButton']).click()
            time.sleep(2)
            self.browser.find_element(*self.Locator_login_buttons['CrossButtonAfterError']).click()
        else:
            self.browser.find_element(*self.Locator_login_buttons['ShareButtonModal']).click()
        time.sleep(2)

    def VerifySuccess(self):
        dd = self.browser.find_element(*self.Locator_login_buttons['ShareSuccessMessage']).is_displayed()
        if (dd):
            assert (dd)
        else:
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(self.Locator_login_buttons['okeyButton'])).click()
            time.sleep(2)
            self.browser.find_element(*self.Locator_login_buttons['CrossButtonAfterError']).click()
            time.sleep(3)
            self.browser.find_element(*self.Locator_login_buttons['Public']).click()

    def GoPublic(self):
        try:
            qq = self.browser.find_element(*self.Locator_login_buttons['PublicTabLink']).is_displayed()
            if (qq):
                self.browser.find_element(*self.Locator_login_buttons['PublicTabLink']).click()
                time.sleep(3)
        except:
            assert (True)

    def VerifyPresence(self):
        loateFile = WebDriverWait(self.browser, 20).until(
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
        ff = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.Locator_login_buttons['LinkCopyMessage']))
        copiedLinkMessage = ff.is_displayed()
        assert (copiedLinkMessage)

    def CloseSuccessMsg(self):
        time.sleep(3)
        self.browser.find_element(*self.Locator_login_buttons['CrossMessage']).click()
        time.sleep(2)

    def VerifySocialShare(self):
        WebDriverWait(self.browser,10).until(EC.visibility_of_element_located(self.Locator_login_buttons["Facebook"]))
        facebook = self.browser.find_element(*self.Locator_login_buttons['Facebook']).is_displayed()
        assert (facebook)
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
        WebDriverWait(self.browser,10).until(EC.visibility_of_element_located(self.Locator_login_buttons["ShareCount"]))
        shareCount = self.browser.find_element(*self.Locator_login_buttons['ShareCount']).text
        count = str(shareCount)
        if (count >= 1):
            print("Share Count has been updated as "+count)
            assert (True)
        else:
            assert (False)

    def ClickLik(self):
        getSharableLink = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable(self.Locator_login_buttons["GetSharbleLik"]))
        getSharableLink.click()

    def Copy(self):
        time.sleep(10)
        copy = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.Locator_login_buttons["Copy"]))
        copy.click()

    def ShiftToIncognito(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome('C:\Users\ZAWAR-PC\Desktop\chromedriver.exe')
        ClipBoardText = Tk().clipboard_get()
        driver.get(ClipBoardText)
        time.sleep(10)
        driver.close()


    def ConfirmCopy(self):
        time.sleep(2)
        message = self.browser.find_element(*self.Locator_login_buttons['LinkCopyMessage']).is_displayed()
        assert (message)

    def VerifyFileLoad(self):
        driver = webdriver.Chrome('C:\Users\ZAWAR-PC\Desktop\chromedriver.exe')
        window_after = driver.window_handles[0]
        driver.switch_to.window(window_after)
        try:
            WebDriverWait(self.browser, 30).until(
                EC.visibility_of_element_located(self.Locator_login_buttons["FileTitleIncognito"]))
            FileName = self.browser.find_element(*self.Locator_login_buttons["FileTitleIncognito"]).text
            ExpectedName = "RenameTest.grid"
            if (FileName == ExpectedName):
                print ("Shared File opened in Incognito mood")
                assert (True)
        except:
            print("Shared File is not opened")
            assert (False)

    def closeShareModal(self):
        WebDriverWait(self.browser,10).until(EC.visibility_of_element_located(self.Locator_login_buttons["closeButton"])).click()

    def GoShare(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["DataToShare"])).click()

    def ShareDropSelect(self):
        WebDriverWait(self.browser,5).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["ShareDopSelect"])).click()



    def ConfirmCopy(self):
        copyMessage = WebDriverWait(self.browser, 10).until(
         EC.invisibility_of_element_located(self.Locator_login_buttons["CopyConfirm"]))
        copyMessage.click()

    def SelectFile(self):
        time.sleep(2)
        self.browser.find_element(*self.Locator_login_buttons["FileSelect"]).click()
    def Done(self):
        time.sleep(2)
        self.browser.find_element(*self.Locator_login_buttons["done"]).click()