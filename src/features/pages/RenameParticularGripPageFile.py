from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import sys
from src.features.pages.header import Header
from src.features.utilities import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.features.pages.header import Header
sys.path.append("..")
from ..utilities import configuration
import time

class Rename(Header):

    browser = None
    header = None

    Locator_login_buttons = {
        "CloseGrid":(By.XPATH,'/html/body/div/ui-view/div/div/div[1]/header/div[1]/div[2]/div[1]/div[1]/a[1]/span'),
        "EditedName":(By.XPATH,'/html/body/div/ui-view/div/div/div[1]/header/div[1]/div[2]/div[1]/div[2]/h1'),
        "MoreOptionsOpenedFile":(By.XPATH,'/html/body/div/ui-view/div/div/div[1]/header/div[1]/div[2]/div[1]/div[2]/span'),
        "EmailForSignIn": (By.XPATH, '//*[@id="loginEmailAddr"]'),
        "FirstNext":(By.XPATH,'/html/body/bp-global-overlays/div[5]/div[1]/div[4]/button'),
        "FitlersNext":(By.XPATH,'/html/body/bp-global-overlays/div[5]/div[2]/div[4]/button'),
        "DownloadNext": (By.XPATH, '/html/body/bp-global-overlays/div[5]/div[3]/div[4]/button'),
        "DemoFinish": (By.XPATH, '/html/body/bp-global-overlays/div[5]/div[4]/div[2]/button'),
        "Cross":(By.XPATH,'/html/body/div[3]/div/div/div/div/header/div/span'),
        "EditedConfermationafteropening":(By.XPATH,'/html/body/div[3]/div/div/div/div/div[1]/p/a'),
        "RenameAfterOpen":(By.XPATH,'/html/body/div/ui-view/div/div/div[1]/header/div[1]/div[2]/div[1]/div[2]/ul/ul/li[1]/span/a'),
        "CrossButton": (By.XPATH, '/html/body/div/ui-view/div[5]/div[6]/div/div[2]/ul/li[2]/span[2]'),
        "PasswordForSignIn": (By.XPATH, '//*[@id="mainheader"]/div[3]/div/header/div/div[2]/div[1]/form/div[1]/div[1]/div[2]/input'),
        "SignInButton": (By.XPATH, '//*[@id="mainheader"]/div[3]/div/header/div/div[2]/div[1]/form/input'),
        "continueButton": (By.XPATH, '/html/body/bp-global-overlays/div[3]/div[1]/div[3]/button'),
        "RenameTextField":(By.XPATH,'/html/body/div[3]/div/div/div/div/form/div/div/input'),
        "RenameAfterOpenEditField":(By.XPATH,'/html/body/div[3]/div/div/div/div/form/div/div/input'),
        "RenameButtonAfterOpening":(By.XPATH,'/html/body/div[3]/div/div/div/div/form/footer/div[1]/div/input'),
        "RenameConfermationNote":(By.XPATH,'/html/body/div[3]/div/div/div/div/div[1]/p/a'),
        "RenameCloseButton":(By.XPATH,'/html/body/div[3]/div/div/div/div/header/div/span'),
        "RenameButton":(By.XPATH,'/html/body/div[3]/div/div/div/div/form/footer/div[1]/div/input'),
        "error note": (By.XPATH, '/html/body/div/ui-view/div/div/section/p'),
        "GridToOpen":(By.XPATH,'/html/body/div/ui-view/div[5]/div[3]/div/div[3]/ol/li[2]/div/div/div[1]/a/div/div'),
        "eror page email field": (By.XPATH, '/html/body/div/ui-view/div/div/section/div/form/div[1]/input'),
        "error page password field": (By.XPATH, '/html/body/div/ui-view/div/div/section/div/form/div[2]/input'),
        "eror page sign in button": (By.XPATH, '/html/body/div/ui-view/div/div/section/div/form/div[3]/input'),
        "Big Parser iscon of Home Page": (By.XPATH, '//*[@id="mainheader"]/div[2]/div/div[6]/header/div[2]/a/img'),
        "uploadwidget": (By.XPATH, '(//SPAN[@class="upload-name"])[2]'),
        "Rename":(By.XPATH,'/html/body/div/ui-view/div[5]/div[3]/div/div[3]/ol/li[2]/div/div/div[2]/div[1]/ul/li[3]/ul/ul/li[1]/span/a'),
        "ConfermationBox":(By.XPATH,'/html/body/div/ui-view/div[5]/div[6]/div'),
        "MoreOptions":(By.XPATH,'/html/body/div/ui-view/div[5]/div[3]/div/div[3]/ol/li[2]/div/div/div[2]/div[1]/ul/li[3]'),
        "upload": (By.XPATH, '/html/body/label[1]/input'),
        "LattestUploadedFile": (By.XPATH, '/html/body/div/ui-view/div[5]/div[3]/div/div[3]/ol/li[2]/div/div/div[1]/a/div/div/div[1]/h2'),
        "logout": (By.XPATH,'//*[@id="mainheader"]/div[2]/div/div[6]/header/div[6]/bp-user-avatar/span/div[1]/div/div[4]/div[4]/a'),
        "profileicon": (By.XPATH, '//*[@id="mainheader"]/div[2]/div/div[6]/header/div[6]/bp-user-avatar/span/div[1]/a/img[1]'),
        "DoneButtons": (By.XPATH, '/html/body/div/ui-view/div[5]/div[6]/div/footer/div/div/input'),
        "cencelButton": (By.XPATH, '/html/body/div[1]/ui-view/div[5]/div[6]/div/footer/div/div/a'),
        "newRadioButton": (By.XPATH, '/html/body/div/ui-view/div[5]/div[6]/div/div[2]/ul/li[2]/div[2]/input'),
        "Existing email error pop up": (By.XPATH, '/html/body/div/ui-view/div[1]/div/div[1]/div/form/div[2]/div/div[3]')
    }

    def loadBigparserSignIn(self):
        time.sleep(3)
        self.browser.find_element(*self.Locator_login_buttons["upload"]).send_keys("E:\\Bigparser\\RenameTest.xlsx")
        time.sleep(10)
        c=self.browser.find_element(*self.Locator_login_buttons["ConfermationBox"]).is_displayed()
        if c==True:
         time.sleep(3)
         self.browser.find_element(*self.Locator_login_buttons["DoneButtons"]).click()
         time.sleep(20)
        else:
         c==False
         time.sleep(10)
        d=WebDriverWait(self.browser,50).until(
             EC.presence_of_element_located(self.Locator_login_buttons["LattestUploadedFile"]))
        e=d.text
        f=False
        if e=="RenameTest":
            f=True
        else:
         assert (f)
        assert (f)
        print ("File Uploaded successfully \n")
    def ClickMoreOptions(self):
        time.sleep(5)
        self.browser.find_element(*self.Locator_login_buttons["MoreOptions"]).click()
        time.sleep(2)

    def ClickRename(self):
        WebDriverWait(self.browser,10).until(EC.visibility_of_element_located(self.Locator_login_buttons["Rename"])).click()

    def RenameEdit(self):
        WebDriverWait(self.browser,10).until(EC.visibility_of_element_located(self.Locator_login_buttons["RenameTextField"])).clear()
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["RenameTextField"])).send_keys("Edited Name")
    def RenameDone(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["RenameButton"])).click()

    def RenameConfermation(self):
        WebDriverWait(self.browser,20).until(EC.visibility_of_element_located(self.Locator_login_buttons["RenameConfermationNote"]))
        r = self.browser.find_element(*self.Locator_login_buttons["RenameConfermationNote"]).is_displayed()
        assert (r)
        time.sleep(2)

    def RenameClose(self):
        self.browser.find_element(*self.Locator_login_buttons["RenameCloseButton"]).click()


    def VerifyRenamed(self):
        q = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["LattestUploadedFile"])).is_displayed()
        assert (q)
        s = self.browser.find_element(*self.Locator_login_buttons["LattestUploadedFile"])
        time.sleep(5)
        t = s.text
        u = False
        if t == "Edited Name":
         u = True
        else:
         assert (u)
        assert (u)
        print ("File has been renamed without opening using more options button under grid ! \n")
    def OpenGrid(self):
        updatedGrid = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.Locator_login_buttons["GridToOpen"]))
        updatedGrid.click()

    def MoreOptions(self):
        updatedGrid = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable(self.Locator_login_buttons["MoreOptionsOpenedFile"])).click()

    def RenameClickOpenedFile(self):
        renameOption=WebDriverWait(self.browser,20).until(
            EC.presence_of_element_located(self.Locator_login_buttons["RenameAfterOpen"]))
        renameOption.click()
        time.sleep(3)

    def EditthatName(self):
        WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(self.Locator_login_buttons["RenameAfterOpenEditField"])).clear()
        WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(self.Locator_login_buttons["RenameAfterOpenEditField"])).send_keys("Second Edited Name")

    def ClickRenameButton(self):
        WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(self.Locator_login_buttons["RenameButtonAfterOpening"])).click()

    def ConfermafterOpen(self):
        m =  WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["RenameConfermationNote"])).is_displayed()
        assert (m)

    def Cross(self):
        self.browser.find_element(*self.Locator_login_buttons["Cross"]).click()
        time.sleep(3)

    def Check(self):
        l = self.browser.find_element(*self.Locator_login_buttons["EditedName"]).is_displayed()
        assert (l)
        time.sleep(5)
        x=self.browser.find_element(*self.Locator_login_buttons["EditedName"])
        y = x.text
        n = False
        if y == "Second Edited Name":
            n = True
        else:
            assert (n)
        assert (n)
        print ("File has been renamed after opening it and we have verified that title is renamed successfully !  \n")
    def CloseGrid(self):

        WebDriverWait(self.browser,20).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["CloseGrid"])).click()

    def Bypass(self):

        WebDriverWait(self.browser,20).until(EC.visibility_of_element_located(self.Locator_login_buttons["FirstNext"])).click()
        time.sleep(2)
        WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["FitlersNext"])).click()
        time.sleep(2)
        WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["DownloadNext"])).click()
        time.sleep(2)
        WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located(self.Locator_login_buttons["DemoFinish"])).click()

        time.sleep(5)








