from behave import *

from src.features.pages.ChilternRailways import benefitsPage

from src.features.pages.signinpage import SignInPage
import time

use_step_matcher("re")

class groupSteps():


    @step('enter "(?P<password>.+)" in password field and Confirm_password "(?P<Confirm_password>.+)"')
    def step_impl(context, password, Confirm_password):
        datas = benefitsPage(context)
        datas.input_data(password, Confirm_password)

    @step('enter first name "(?P<fname>.+)" and last name "(?P<lname>.+)"')
    def step_impl(context, fname, lname):
        data = benefitsPage(context)
        data.flname(fname, lname)

    @then('enter new email"(?P<nemail>.+)" and new password"(?P<npass>.+)"')
    def step_impl(context, nemail, npass):
        data = benefitsPage(context)
        data.nemailpas(nemail, npass)

