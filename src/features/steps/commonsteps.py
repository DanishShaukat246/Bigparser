from datetime import time

from behave import *

from src.features.pages.commonPage import commonPage
from src.features.pages.signinpage import SignInPage
from src.features.pages.basepage import basePage
import time

use_step_matcher("re")

class commonSteps():
    @given("user is at home page")
    def step_impl(context):
        signinPage = SignInPage(context)
        signinPage.assertUrl("https://qa.bigparser.com/")
