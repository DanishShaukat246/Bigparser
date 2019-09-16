from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import sys
from src.features.pages.header import Header
from src.features.utilities import driver

sys.path.append("..")
from ..utilities import configuration
import time

class SignInPage(Header):

    browser = None
    header = None

    locator_dictionary = {
        "emailField": (By.XPATH, '//*[@id="user_email"]'),
        "password": (By.XPATH, '//*[@id="user_password"]'),
        "signInButton": (By.XPATH, '//*[@id="top-row"]/div[2]/a'),
        "signIn": (By.XPATH, "//button[text()= 'Login']"),
        "LogIn": (By.XPATH, '//*[@id="et-secondary-nav"]/li/a'),
        "journal": (By.XPATH, '//*[@id="wrapper"]/navigation-menu/div/div[1]/div[1]/ul/li[2]/a'),
        "dayOne": (By.XPATH, '//*[@id="wrapper"]/div[2]/div[2]/div/div[1]/div/div[1]/div[4]/div[1]/div[4]/div/div[1]/div[1]/div'),
        "commentField": (By.XPATH, '//*[@id="textCommentNew"]'),
        "postComment":(By.XPATH, '//*[@id="btnCommentPost"]'),
        "video": (By.XPATH, '//*[@id="wrapper"]/div[2]/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[1]'),
        "viewLesson": (By.XPATH, '//*[@id="wrapper"]/div[2]/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[1]/div[1]/div/div/a'),
        "writeAction": (By.XPATH, '//*[@id="discussion-comment-box"]/div[2]/div[1]/div[1]/div[1]/textarea'),
        "commentBox": (By.XPATH, '//*[@id="textCommentNew"]'),
        "postAction": (By.XPATH, '//*[@id="btnCommentPost"]'),
        "close": (By.XPATH, '//*[@id="discussion-comment-box"]/div[2]/div/div[1]/div[1]/a'),
        "commentDiv": (By.XPATH, '//*[@id="public-reflections"]/div[2]'),
        "edit": (By.XPATH, '//*[@id="public-reflections"]/div[2]/div[1]'),
        "activityFeed": (By.XPATH, '//*[@id="wrapper"]/navigation-menu/div/div[1]/div[1]/ul/li[1]'),
        "addBuddy": (By.XPATH, '//*[@id="wrapper"]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div'),
        "firstBuddy": (By.XPATH, '//*[@id="buddies-scrollable"]/div[1]/div[1]/div[1]/div[1]/div[3]'),
        "secondBuddy": (By.XPATH, '//*[@id="buddies-scrollable"]/div[1]/div[2]/div[1]/div[1]/div[3]'),
        "thirdBuddy": (By.XPATH, '//*[@id="buddies-scrollable"]/div[1]/div[3]/div[1]/div[1]/div[3]'),
        "done":(By.XPATH, '//*[@id="buddies-scrollable"]/div[1]/div/div[1]/div[2]')
    }

    def __init__(self, context):
        self.browser = context.browser
        self.header = Header(context)
    
    def get_page_Url(self):
        return str(self.browser.current_url)

    def assertUrl(self, url):
        assert url in self.get_page_Url()

    def selectSignIn(self):
        self.click(self.browser.find_element(*self.locator_dictionary['signIn']))
        time.sleep(3)

    def inputEmail(self, email):
        self.sendKeys(self.browser.find_element(*self.locator_dictionary['emailField']), configuration.get_email(email))

    def inputPassword(self, password):
        self.sendKeys(self.browser.find_element(*self.locator_dictionary['password']), configuration.get_password(password))

