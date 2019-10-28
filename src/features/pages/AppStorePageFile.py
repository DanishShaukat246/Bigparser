
import sys

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        "BPIcon":(By.XPATH,'/html/body/div/ui-view/div[1]/div/div[1]/a/img'),
        "Basics":(By.XPATH,'//*[@id="leftSideNav"]/div/div[2]/div[2]/uib-accordion/div/div[1]/div[1]/h4/a/span/span[1]'),
        "Products":(By.XPATH,'//*[@id="leftSideNav"]/div/div[2]/div[2]/uib-accordion/div/div[1]/div[2]/div/ul[1]/li/a/span'),
        "ChatbotIcon":(By.XPATH,'/html/body/bp-chatbot-launcher/div/div'),
        "Pricing":(By.XPATH,'//*[@id="leftSideNav"]/div/div[2]/div[2]/uib-accordion/div/div[1]/div[2]/div/ul[2]/li/a'),
        "PricingPageTitle":(By.XPATH,'/html/body/div/ui-view/div[2]/div/div[2]/div/h1/div'),
        "Support":(By.XPATH,'//*[@id="leftSideNav"]/div/div[2]/div[2]/uib-accordion/div/div[2]/div[2]/div/ul[2]/li/a/span'),
        "Help":(By.XPATH,'//*[@id="leftSideNav"]/div/div[2]/div[2]/uib-accordion/div/div[2]/div[1]/h4/a'),
        "FAQ":(By.XPATH,'//*[@id="leftSideNav"]/div/div[2]/div[2]/uib-accordion/div/div[2]/div[2]/div/ul[4]/li/a/span'),
        "SupportPageTitle":(By.XPATH,'//*[@id="wrapper"]/div[3]/div/div/div/h1'),
        "HelpPageTitle":(By.XPATH,'//*[@id="wrapper"]/div[3]/div/div/div/h1'),
        "HelpandForum":(By.XPATH,'//*[@id="leftSideNav"]/div/div[2]/div[2]/uib-accordion/div/div[2]/div[2]/div/ul[3]/li/a/span'),
        "FAQPageTitle":(By.XPATH,'//*[@id="wrapper"]/div[3]/div/div/div/h1'),
        "Apps":(By.XPATH,'//*[@id="leftSideNav"]/div/div[2]/div[2]/uib-accordion/div/div[3]/div[1]/h4/a/span/span[1]'),
        "MoreApps":(By.XPATH,'//*[@id="leftSideNav"]/div/div[2]/div[2]/uib-accordion/div/div[3]/div[2]/div/ul/li/a/span'),
        "Legal":(By.XPATH,'//*[@id="leftSideNav"]/div/div[2]/div[2]/uib-accordion/div/div[4]/div[1]/h4/a'),
        "Security":(By.XPATH,'//*[@id="leftSideNav"]/div/div[2]/div[2]/uib-accordion/div/div[4]/div[2]/div/ul[1]/li/a/span'),
        "SecurityPageTitle":(By.XPATH,'/html/body/div/ui-view/div[2]/div[1]/div/ul/li/a'),
        "Privacy":(By.XPATH,'//*[@id="leftSideNav"]/div/div[2]/div[2]/uib-accordion/div/div[4]/div[2]/div/ul[2]/li/a/span'),
        "PrivacyPageTermsLinks":(By.XPATH,'/html/body/div/ui-view/div/div[1]/div/ul/li[2]/a'),
        "Engage":(By.XPATH,'//*[@id="leftSideNav"]/div/div[2]/div[2]/uib-accordion/div/div[5]/div[1]/h4/a/span/span[1]'),
        "Jobs":(By.XPATH,'//*[@id="leftSideNav"]/div/div[2]/div[2]/uib-accordion/div/div[5]/div[2]/div/ul[1]/li/a/span'),
        "JobsPageTitle":(By.XPATH,'/html/body/div/ui-view/div/section[2]/div/h2'),
        "Blog":(By.XPATH,'//*[@id="leftSideNav"]/div/div[2]/div[2]/uib-accordion/div/div[5]/div[2]/div/ul[2]/li/a/span'),
        "BlogPage":(By.XPATH,'//*[@id="main"]/div/div[1]/h1'),
        "Media":(By.XPATH,'//*[@id="leftSideNav"]/div/div[2]/div[2]/uib-accordion/div/div[5]/div[2]/div/ul[3]/li/a/span'),
        "MediaPage":(By.XPATH,'//*[@id="wrapper"]/div[3]/div/div/div/h1'),
        "BPIconSecurityPage":(By.XPATH,'//*[@id="mainheader"]/div[2]/div/div[6]/header/div[2]/a/img'),
        "BPIconJobsPage":(By.XPATH,'/html/body/div/ui-view/div/header/div[1]/div[1]/a/img'),
        "BPIconAppStorePage":(By.XPATH,'//*[@id="mainheader"]/div[2]/div/div[6]/header/div[2]/a/img')


    }

    def GoToAppStore(self):
      self.browser.find_element(*self.AppStoreXpaths["AppStoreIcon"]).click()
      time.sleep(3)


    def VerifyPageLoad(self):
        time.sleep(2)
        AppStore = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located(self.AppStoreXpaths["AppStoreTitle"]))
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
        self.browser.find_element(*self.AppStoreXpaths["BPIconAppStorePage"]).click()

    def ClickBasics(self):

        WebDriverWait(self.browser,10).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["Basics"])).click()

    def ClickProducts(self):
        time.sleep(2)
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["Products"])).click()

    def GoToPreviousPage(self):
        self.browser.execute_script("window.history.go(-1)")

    def VerifyHome(self):
        bp = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["BPIcon"])).is_displayed()
        assert (bp)

    def ClickPricing(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["Pricing"])).click()

    def VerifyPricingPage(self):
        time.sleep(2)
        PricingPageTitle = self.browser.find_element(*self.AppStoreXpaths["PricingPageTitle"]).is_displayed()
        assert (PricingPageTitle)
        self.browser.execute_script("window.history.go(-1)")

    def ClickGetHelp(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["Help"])).click()

    def ClickSuport(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["Support"])).click()

    def VerifySupportPage(self):
        time.sleep(2)
        allTabs = self.browser.window_handles
        self.browser.switch_to_window(allTabs[1])
        SupportPageTitle = self.browser.find_element(*self.AppStoreXpaths["SupportPageTitle"])
        title = SupportPageTitle.is_displayed()
        assert (title)

    def CloseTab(self):
        allTabs = self.browser.window_handles
        self.browser.close()
        self.browser.switch_to_window(allTabs[0])

    def ClickHelpandForum(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["HelpandForum"])).click()

    def VerifyHelpPage(self):
        allTabs = self.browser.window_handles
        self.browser.switch_to_window(allTabs[1])
        time.sleep(3)
        HelpPageTitle = self.browser.find_element(*self.AppStoreXpaths["HelpPageTitle"]).is_displayed()
        assert (HelpPageTitle)

    def ClickFAQ(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["FAQ"])).click()

    def VerifyFAQPage(self):
        allTabs = self.browser.window_handles
        self.browser.switch_to_window(allTabs[1])
        time.sleep(2)
        FAQPageTitle = self.browser.find_element(*self.AppStoreXpaths["FAQPageTitle"]).is_displayed()
        assert (FAQPageTitle)

    def ClickApps(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["Apps"])).click()

    def VerifyAppStorePage(self):
        time.sleep(5)
        AppStore = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["AppStoreTitle"]))
        title = AppStore.is_displayed()
        assert (title)

    def ClickLegal(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["Legal"])).click()

    def ClickSecurity(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["Security"])).click()

    def VerifySecurityPage(self):
        time.sleep(2)
        SecurityPageTitle = self.browser.find_element(*self.AppStoreXpaths["SecurityPageTitle"]).is_displayed()
        assert (SecurityPageTitle)

    def ClickBPIcon(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["BPIcon"])).click()

    def ClickPrivacyandTerms(self):
        time.sleep(2)
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["Privacy"])).click()

    def VerifyPrivacyPage(self):
        time.sleep(2)
        PrivacyPageTitle = self.browser.find_element(*self.AppStoreXpaths["PrivacyPageTermsLinks"]).is_displayed()
        assert (PrivacyPageTitle)
    def ClickEngage(self):
        time.sleep(2)
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["Engage"])).click()

    def ClickJobs(self):
        time.sleep(2)
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["Jobs"])).click()

    def VerifyJobsPage(self):
        time.sleep(2)
        JobsPageTitle = self.browser.find_element(*self.AppStoreXpaths["JobsPageTitle"]).is_displayed()
        assert (JobsPageTitle)

    def ClickBlog(self):
        time.sleep(2)
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["Blog"])).click()

    def VerifyBlogPage(self):
        allTabs = self.browser.window_handles
        self.browser.switch_to_window(allTabs[1])
        BlogPageTitle = self.browser.find_element(*self.AppStoreXpaths["BlogPage"]).is_displayed()
        assert (BlogPageTitle)

    def ClickPressandMedia(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["Media"])).click()

    def VerifyMediaPage(self):
        allTabs = self.browser.window_handles
        self.browser.switch_to_window(allTabs[1])
        time.sleep(3)
        MediaPageTitle = self.browser.find_element(*self.AppStoreXpaths["MediaPage"]).is_displayed()
        assert (MediaPageTitle)

    def ClickMoreApps(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["MoreApps"])).click()

    def ClickBigparserIcon(self):
        WebDriverWait(self.browser,10).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["BPIconSecurityPage"])).click()

    def ClickBigparserIconJob(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["BPIconJobsPage"])).click()

    def ClickBigparserIconAppStore(self):
        WebDriverWait(self.browser,10).until(
            EC.visibility_of_element_located(self.AppStoreXpaths["BPIconAppStorePage"])).click()




