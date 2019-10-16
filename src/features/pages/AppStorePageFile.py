
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.features.pages.header import Header
sys.path.append("..")
import time

class AppStore(Header):

    browser = None
    header = None

    AppStoreXpaths = {
        "AppStoreIcon":(By.XPATH,'//*[@id="mainheader"]/div[2]/div/div[6]/header/div[6]/a'),
        "AppStoreTitle":(By.XPATH,'/html/body/div/ui-view/div[8]/div/div[1]/div[2]/div[1]/div/h1/div'),
        "FilterButton":(By.XPATH,'//*[@id="single-button"]'),
        "PreInstalled":(By.XPATH,'/html/body/div/ui-view/div[8]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/ul/li[2]/a'),
        "GridApp":(By.XPATH,'/html/body/div/ui-view/div[8]/div/div[1]/div[2]/div[3]/ol/li[1]/div/h2'),
        "ShareApp":(By.XPATH,'/html/body/div/ui-view/div[8]/div/div[1]/div[2]/div[3]/ol/li[2]/div/h2'),
        "PlugApp":(By.XPATH,'/html/body/div/ui-view/div[8]/div/div[1]/div[2]/div[3]/ol/li[3]/div/h2'),
        "Installed":(By.XPATH,'/html/body/div/ui-view/div[8]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/ul/li[3]/a'),
        "GoogleDrive":(By.XPATH,'/html/body/div/ui-view/div[8]/div/div[1]/div[2]/div[3]/ol/li[1]/div/h2'),
        "DropBox":(By.XPATH,'/html/body/div/ui-view/div[8]/div/div[1]/div[2]/div[3]/ol/li[2]/div/h2'),
        "OneDrive":(By.XPATH,'/html/body/div/ui-view/div[8]/div/div[1]/div[2]/div[3]/ol/li[3]/div/h2'),
        "Uninstalled":(By.XPATH,'/html/body/div/ui-view/div[8]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/ul/li[4]/a'),
        "PreOrder":(By.XPATH,'/html/body/div/ui-view/div[8]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/ul/li[5]/a'),
        "Skype":(By.XPATH,'/html/body/div/ui-view/div[8]/div/div[1]/div[2]/div[3]/ol/li[3]/div/h2'),
        "BPIcon":(By.XPATH,'//*[@id="mainheader"]/div[2]/div/div[6]/header/div[2]/a/img')
    }

    def GoToAppStore(self):
      self.browser.find_element(*self.AppStoreXpaths["AppStoreIcon"]).click()


    def VerifyPageLoad(self):
        AppStore = WebDriverWait(self.browser,20).until(EC.visibility_of_element_located(self.AppStoreXpaths["AppStoreTitle"]))
        title = AppStore.is_displayed()
        assert (title)

    def VerifDefaultFilter(self):
        FiterButton = WebDriverWait(self.browser,5).until(EC.visibility_of_element_located(self.AppStoreXpaths["FilterButton"]))
        ButtonText = FiterButton.text
        ExpectedText =  "All BigParser Apps"
        if ButtonText == ExpectedText:
            assert (True)
        else:
            assert (False)

    def SelectPreInstalled(self):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["FilterButton"])).click()
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["PreInstalled"])).click()
        time.sleep(3)

    def VerifyPreInstalled(self):
       time.sleep(2)
       GridApp = self.browser.find_element(*self.AppStoreXpaths["GridApp"]).is_displayed()
       ShareApp = self.browser.find_element(*self.AppStoreXpaths["ShareApp"]).is_displayed()
       PlugApp = self.browser.find_element(*self.AppStoreXpaths["PlugApp"]).is_displayed()
       assert (GridApp)
       assert (ShareApp)
       assert (PlugApp)


    def SelectInstalledApps(self):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["FilterButton"])).click()
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["Installed"])).click()
        time.sleep(3)

    def VerifyInstalled(self):
        time.sleep(2)
        GoogleDrive = self.browser.find_element(*self.AppStoreXpaths["GoogleDrive"]).is_displayed()
        Dropbox = self.browser.find_element(*self.AppStoreXpaths["DropBox"]).is_displayed()
        OneDrive = self.browser.find_element(*self.AppStoreXpaths["OneDrive"]).is_displayed()
        assert (GoogleDrive)
        assert (Dropbox)
        assert (OneDrive)


    def SelectUninstalledApps(self):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["FilterButton"])).click()
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["Uninstalled"])).click()
        time.sleep(3)

    def VerifyUnInstalled(self):
        pass

    def SelectPreOrder(self):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["FilterButton"])).click()
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["PreOrder"])).click()
        time.sleep(3)

    def VerifyPreOrder(self):
        Skype = self.browser.find_element(*self.AppStoreXpaths["Skype"]).is_displayed()
        assert (Skype)

    def GoHome(self):
        self.browser.find_element(*self.AppStoreXpaths["BPIcon"]).click()