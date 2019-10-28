from lib2to3.fixes.fix_input import context
import time
from random import randint

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.features.pages.temporary import *
from src.features.pages.signinpage import SignInPage
from Tkinter import Tk

class benefitsPagesSignIn(Header):
    driver = None
    browser = None
    #
    Locator_login_buttons = {
        "EmailForSignIn": (By.XPATH, '//*[@id="loginEmailAddr"]'),
        "EmailSentConfermationNote":(By.XPATH,'/html/body/div/ui-view/div/div/section/form/div/div[1]'),
        "sendAndResetPassword":(By.XPATH,'/html/body/div/ui-view/div/div/section/form/div/input[2]'),
        "emailFieldForForgotPassword":(By.XPATH,'/html/body/div/ui-view/div/div/section/form/div/input[1]'),
        "FogotYourPassword":(By.XPATH,'//*[@id="mainheader"]/div[3]/div/header/div/div[2]/div[1]/form/div[1]/div[2]/div/a'),
        "PasswordForSignIn": (By.XPATH, '//*[@id="mainheader"]/div[3]/div/header/div/div[2]/div[1]/form/div[1]/div[1]/div[2]/input'),
        "SignInButton": (By.XPATH, '//*[@id="mainheader"]/div[3]/div/header/div/div[2]/div[1]/form/input'),
        "continueButton": (By.XPATH, '/html/body/bp-global-overlays/div[3]/div[1]/div[3]/button'),
        "firstNextButton":(By.XPATH,'/html/body/bp-global-overlays/div[3]/div[2]/div[4]/button'),
        "secondNextButton":(By.XPATH,'/html/body/bp-global-overlays/div[3]/div[3]/div[4]/button'),
        "thirdNextButton":(By.XPATH,'/html/body/bp-global-overlays/div[3]/div[4]/div[4]/button'),
        "finishButton":(By.XPATH,'/html/body/bp-global-overlays/div[3]/div[5]/div[2]/button'),
        "error note":(By.XPATH,'/html/body/div/ui-view/div/div/section/p'),
        "gmailIDField":(By.XPATH,'//*[@id="identifierId"]'),
        "NextButtonPasswordPageGmail":(By.XPATH,'//*[@id="passwordNext"]/span/span'),
        "PasswordFieldGmail":(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input'),
        "NextButtonofGmailEmailIDPage":(By.XPATH,'//*[@id="identifierNext"]/span/span'),
        "forgotYourPasswordText":(By.XPATH,'/html/body/div/ui-view/div/div/section/h1'),
        "eror page email field":(By.XPATH,'/html/body/div/ui-view/div/div/section/div/form/div[1]/input'),
        "error page password field":(By.XPATH,'/html/body/div/ui-view/div/div/section/div/form/div[2]/input'),
        "eror page sign in button":(By.XPATH,'/html/body/div/ui-view/div/div/section/div/form/div[3]/input'),
        "Big Parser iscon of Home Page":(By.XPATH,'//*[@id="mainheader"]/div[2]/div/div[6]/header/div[2]/a/img'),
        "Existing email error pop up": (By.XPATH, '/html/body/div/ui-view/div[1]/div/div[1]/div/form/div[2]/div/div[3]'),
        "CreateAccount":(By.XPATH,'/html/body/div/ui-view/div[1]/div/div[1]/div/form/input'),
        "NameError":(By.XPATH,'/html/body/div/ui-view/div[1]/div/div[1]/div/form/div[1]/div/div'),
        "EmailError":(By.XPATH,'/html/body/div/ui-view/div[1]/div/div[1]/div/form/div[2]/div/div[1]'),
        "PasswordError":(By.XPATH,'/html/body/div/ui-view/div[1]/div/div[1]/div/form/div[3]/div[1]/div'),
        "NameField":(By.XPATH,'//*[@id="fullName"]'),
        "EmailField":(By.XPATH,'//*[@id="emailAddr"]'),
        "UpdatedProfileIcon":(By.XPATH,'//*[@id="mainheader"]/div[2]/div/div[6]/header/div[6]/bp-user-avatar/span/div[1]/a/img[2]'),
        "logout":(By.XPATH,'//*[@id="mainheader"]/div[2]/div/div[6]/header/div[6]/bp-user-avatar/span/div[1]/div/div[4]/div[4]/a'),
        "PasswordField":(By.XPATH,'/html/body/div/ui-view/div[1]/div/div[1]/div/form/div[3]/input'),
        "InvalidPasswordMessage":(By.XPATH,'/html/body/div/ui-view/div[1]/div/div[1]/div/form/div[3]/div[2]/div'),
        "ProfileIcon":(By.XPATH,'//*[@id="mainheader"]/div[2]/div/div[6]/header/div[6]/bp-user-avatar/span/div[1]/a/img[1]')
    }

    def loadBigparserSignIn(self, url):
        signinPage = SignInPage(context)
        signinPage.assertUrl(url)

    def verifyFieldPresence(self):

        a = self.browser.find_element(*self.Locator_login_buttons['EmailForSignIn']).is_displayed()
        b = self.browser.find_element(*self.Locator_login_buttons['PasswordForSignIn']).is_displayed()
        c = self.browser.find_element(*self.Locator_login_buttons['SignInButton']).is_displayed()
        assert (a)
        assert (b)
        assert (c)

    def enterEmail(self):
        self.browser.find_element(*self.Locator_login_buttons['EmailForSignIn']).clear()
        self.browser.find_element(*self.Locator_login_buttons['EmailForSignIn']).send_keys("danish@gmail.com")

    def invalidPassword(self):
        self.browser.find_element(*self.Locator_login_buttons['PasswordForSignIn']).send_keys("1234")

    def siginInButtonClick(self):
       self.browser.find_element(*self.Locator_login_buttons['SignInButton']).click()

    def invalidsignInNote(self):
        time.sleep(3)
        d = self.browser.find_element(*self.Locator_login_buttons['error note']).is_displayed()
        assert (d)

    def validEmail(self):
        self.browser.find_element(*self.Locator_login_buttons['eror page email field']).send_keys("danishshaukatmalik@gmail.com")

    def validPassword(self):
        self.browser.find_element(*self.Locator_login_buttons['error page password field']).send_keys("123456789")

    def clickValid(self):
        self.browser.find_element(*self.Locator_login_buttons['eror page sign in button']).click()

    def verifyHomePage(self):
        time.sleep(5)
        e = self.browser.find_element(*self.Locator_login_buttons['Big Parser iscon of Home Page']).is_displayed()
        assert (e)

    def continuePress(self):
        WebDriverWait(self.browser,5).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["continueButton"])).click()
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["firstNextButton"])).click()
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["secondNextButton"])).click()
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["thirdNextButton"])).click()
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["finishButton"])).click()

    def forgetClick(self):
        self.browser.find_element(*self.Locator_login_buttons['FogotYourPassword']).click()
        time.sleep(2)
        g=self.browser.find_element(*self.Locator_login_buttons['forgotYourPasswordText']).is_displayed()
        assert (g)

    def forgotEmailEntery(self):
        time.sleep(3)
        self.browser.find_element(*self.Locator_login_buttons['emailFieldForForgotPassword']).send_keys(
            'bigparserautomation@gmail.com')
        self.browser.find_element(*self.Locator_login_buttons['sendAndResetPassword']).click()

    def emilSentConfermationNote(self):
        time.sleep(5)
        g = self.browser.find_element(*self.Locator_login_buttons['EmailSentConfermationNote']).is_displayed()
        assert (g)

    def OpenGmailID(self):
        self.browser.implicitly_wait(3)
        self.browser.execute_script("window.open('https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin','new window')")
        time.sleep(5)

    def EnterGmailID(self):
        self.browser.find_element(*self.Locator_login_buttons['gmailIDField']).send_keys('bigparserautomation@gmail.com')
        self.browser.find_element(*self.Locator_login_buttons['NextButtonofGmailEmailIDPage']).click()

    def GmailPasswordEntry(self):
        self.browser.find_element(*self.Locator_login_buttons['PasswordFieldGmail']).send_keys('123456789')
        self.browser.find_element(*self.Locator_login_buttons['NextButtonPasswordPageGmail']).click()

    def ClickRegEmpty(self):
        WebDriverWait(self.browser,10).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["CreateAccount"])).click()


    def ErrorName(self):
        nameErrorMessage = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["NameError"])).is_displayed()
        assert (nameErrorMessage)

    def EnterName(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["NameField"])).send_keys("tes_12")

    def ErrorEmail(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["CreateAccount"])).click()
        nameEmailMessage = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["EmailError"])).is_displayed()
        assert (nameEmailMessage)

    def EnterEmail(self):
        nRand = randint(1, 9999)
        emailToBeCleared = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.Locator_login_buttons["EmailField"]))
        emailToBeCleared.send_keys("Tester_" + str(nRand) + "@gmail.com")

    def ErrorPassword(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["CreateAccount"])).click()
        namePasswordMessage = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["PasswordError"])).is_displayed()
        assert (namePasswordMessage)

    def EnterPassword(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["PasswordField"])).send_keys("123456789")

    def InvalidPassword(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["PasswordField"])).send_keys("123")
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["CreateAccount"])).click()
        InvalidPasswordMessage = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["InvalidPasswordMessage"])).is_displayed()
        assert (InvalidPasswordMessage)
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["PasswordField"])).clear()

    def UpdatedCredentials(self):
        # updatedEmial = Tk.clipboard_get()
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["EmailForSignIn"])).send_keys(Keys.CONTROL+"v")
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["PasswordForSignIn"])).send_keys("danish123456789")
        self.browser.find_element(*self.Locator_login_buttons['SignInButton']).click()
        time.sleep(5)
    def VerifyLoggedIn(self):
         profileIcon = WebDriverWait(self.browser,10).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["ProfileIcon"])).is_displayed()
         assert (profileIcon)

    def logout(self):
         WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["logout"])).click()
         time.sleep(5)

    def UpdatedCheckLogout(self):
        WebDriverWait(self.browser,10).until(EC.visibility_of_element_located(self.Locator_login_buttons["UpdatedProfileIcon"])).click()
        time.sleep(2)
        self.browser.find_element(*self.Locator_login_buttons["logout"]).click()
        time.sleep(5)













