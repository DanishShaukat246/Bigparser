from .browsers import Browsers 


from src.features.utilities import configuration
import os
from selenium import webdriver
# import requests

def get_chrome():
    chromedriver = configuration.read_chromedriver_location()
    chromeOptions = webdriver.ChromeOptions()
    cwd = os.getcwd()
    prefs = {"download.default_directory": cwd+"\\downloads", "download.prompt_for_download": False}
    chromeOptions.add_experimental_option("prefs", prefs)
    os.environ["webdriver.chrome.driver"] = chromedriver
    return webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
    
def get_ie():
    iedriver = configuration.read_internetexplorer_location()
    os.environ["webdriver.ie.driver"] = iedriver
    return webdriver.Ie(iedriver)

# def get_crossbrowser():
#     username = "danish@avanoo.com"
#     authkey = "u7dd25704496f22b"
#
#     api_session = requests.Session()
#     api_session.auth = (username, authkey)
#
#     test_result = None
#
#     caps = {}
#
#     caps['name'] = 'Emergency Push Test Cases'
#     caps['build'] = '1.0'
#     caps['browserName'] = 'Chrome'
#     caps['version'] = '71x64'
#     caps['platform'] = 'Windows 10'
#     caps['screenResolution'] = '1366x768'
#     caps['record_video'] = 'true'
#     caps['record_network'] = 'false'
#
#     # start the remote browser on our server
#     driver = webdriver.Remote(
#         desired_capabilities=caps,
#         command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub" % (username, authkey))
#     return driver

# command_executor="http://USERNAME:ACCESS_KEY@YOUR_SUBDOMAIN.gridlastic.com:80/wd/hub",
def get_gridLastic():
    driver = webdriver.Remote(
        command_executor="http://xk2B73XvqAfctuZ0uNUPCfyLlLrnT7oh:hgIfawArWGtg1j7lXR1pXq181imLgATo@8WFVRWEJ.gridlastic.com:80/wd/hub",
        desired_capabilities={
            "browserName": "chrome",
            "version": "latest",
            "video": "True",
            "platform": "VISTA",
            "platformName": "windows",
        })
    return driver
    
def switch_browser(browser):
    return {
        Browsers.chrome : get_chrome,
        Browsers.internetexplorer : get_ie
    }.get(browser, lambda: webdriver.Firefox())()