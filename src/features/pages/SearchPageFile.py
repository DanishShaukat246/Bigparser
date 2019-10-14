import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.features.pages.header import Header

sys.path.append("..")
import time


class Search(Header):
    browser = None
    header = None

    SearchFeatureXpaths = {
        "MainSearchBar": (By.XPATH, '//*[@id="mainheader"]/div[2]/div/div[6]/header/div[4]/div/input'),
        "LattestUploadedFile": (
            By.XPATH, '/html/body/div/ui-view/div[5]/div[3]/div/div[3]/ol/li[2]/div/div/div[1]/a/div/div/div[1]/h2'),
        "CrossButtonMainSearchBar": (By.XPATH, '//*[@id="mainheader"]/div[2]/div/div[6]/header/div[4]/div/button'),
        "CrossSheetSearchBar":(By.XPATH,'/html/body/div/ui-view/div/div/div[2]/div[1]/div/div/form/input'),
        "GridCell":(By.XPATH,'//*[@id="1570620613803-0-uiGrid-01GQ-cell"]/div/div'),
        "searchAllGrid":(By.XPATH,'/html/body/div/ui-view/div/div/div[1]/header/div[1]/div[2]/div[3]/div[1]/div/div/div/ul/li[2]/span'),
        "Search":(By.XPATH,"/html/body/div/ui-view/div/div/div[1]/header/div[1]/div[2]/div[3]/div[1]/button/span"),
        "searchResult":(By.XPATH,"//*[@id='divFoundSimilarGrid']/div[1]"),
        "downErrow":(By.XPATH,"//*[@id='divFoundSimilarGrid']/div[2]/a"),
        "SheetUncheck":(By.XPATH,"//*[@id='mCSB_29_container']/ul/li[1]/div/input"),
        "SearchButton":(By.XPATH,'//*[@id="divFoundSimilarGrid"]/div[2]/div/div[4]/div/input'),
        "GridsShowing":(By.XPATH,'//*[@id="divFoundSimilarGrid"]/div[1]/span[2]/span[1]'),
        "GridsFound":(By.XPATH,'//*[@id="divFoundSimilarGrid"]/div[1]/span[2]/span[2]')

    }

    def EnterText(self):
        self.browser.find_element(*self.SearchFeatureXpaths["MainSearchBar"]).send_keys("RenameTest")
        fileTitle = WebDriverWait(self.browser, 50).until(
            EC.presence_of_element_located(self.SearchFeatureXpaths["LattestUploadedFile"]))
        fileTitleText = fileTitle.text
        filePresence = False
        if fileTitleText == "RenameTest":
            filePresence = True
        else:
            assert (filePresence)
        assert (filePresence)
        time.sleep(5)
        print ("Global search throw main search bar of header successful ! \n")

    def ClearField(self):
        self.browser.find_element(*self.SearchFeatureXpaths['CrossButtonMainSearchBar']).click()
        time.sleep(10)


    def KeyEnter(self):
        searchBar = WebDriverWait(self.browser,10).until(
            EC.visibility_of_element_located(self.SearchFeatureXpaths["CrossSheetSearchBar"]))
        searchBar.click()
        searchBar.send_keys("call"+Keys.ENTER)


    def VerifyRelatedLoad(self):
       time.sleep(3)
       CellData = self.browser.find_element(*self.SearchFeatureXpaths["GridCell"]).text
       ResquiredText="Call"
       loadedText = CellData
       if ResquiredText in loadedText:
           assert (True)
       else:
           assert (False)

    def SearchAllOptionClick(self):
       searchAll = WebDriverWait(self.browser,20).until(
           EC.visibility_of_element_located(self.SearchFeatureXpaths["searchAllGrid"]))
       searchAll.click()

    def SearchClick(self):
        search = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.SearchFeatureXpaths["Search"]))
        search.click()

    def VerificationText(self):
        searchResult = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.SearchFeatureXpaths["searchResult"]))
        searchResult.click()

    def dropDownClick(self):
        errow = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.SearchFeatureXpaths["downErrow"]))
        errow.click()

    def Deselect(self):
        SheetNameRadioButton = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.SearchFeatureXpaths["SheetUncheck"]))
        SheetNameRadioButton.click()

    def ClickSearch(self):
        SearchButtonClick = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.SearchFeatureXpaths["SearchButton"]))
        SearchButtonClick.click()

    def VerifyCountUpdate(self):
       GridsFound = WebDriverWait(self.browser,5).until(EC.visibility_of_element_located(self.SearchFeatureXpaths["GridsFound"])).text
       GridsShowing =  WebDriverWait(self.browser,5).until(EC.visibility_of_element_located(self.SearchFeatureXpaths["GridsShowing"])).text
       RequiredNumber = int(GridsFound)-1
       if int(GridsShowing)==RequiredNumber:
           assert (True)
       else:
           assert (False)

    def searchInShared(self):
        self.browser.find_element(*self.SearchFeatureXpaths["MainSearchBar"]).send_keys("Second Edited Name")
        time.sleep(3)
