from lib2to3.fixes.fix_input import context
from selenium.webdriver.common.by import By
import json, os
from src.features.pages.header import Header

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from src.features.utilities import driver
import time
import datetime
from array import *
from src.features.pages.temporary import *
from random import *


class commonPage(Header):
    driver = None
    browser = None

    Locator_common_buttons = {
       "sign_out": (By.XPATH, '//*[@id="wrapper"]/navigation-header/div/div[2]/div[4]/div[2]/div/ul/li/ul/li/a')
    }

