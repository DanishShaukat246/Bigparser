from behave import *

from src.features.pages.BigParserFunctions import benefitsPages

from src.features.pages.signinpage import SignInPage
import time

use_step_matcher("re")

class groupSteps():




  @then("Enter name in full name field")
  def step_impl(context):
    bp=benefitsPages(context)
    bp.entername()


@then("Enter Password in passsword field")
def step_impl(context):
    bp=benefitsPages(context)
    bp.enterPassword()


@then("Enter email in email field")
def step_impl(context):
    bp=benefitsPages(context)
    bp.enterEmailForSignUp()


@then("Click on Sign Up button")
def step_impl(context):
    bp=benefitsPages(context)
    bp.clickSignUpButton()


@then("verify that user is on get started page")
def step_impl(context):
    bp=benefitsPages(context)
    bp.ClickCreateAccuntButton()


@then("verify that all mendatory fields are present")
def step_impl(context):
    bp=benefitsPages(context)
    bp.VerifyPresenceSignUp()


@then("verify that user shows eror massage of already existing email")
def step_impl(context):
    bp=benefitsPages(context)
    bp.LocatePopUp()


@then("Enter new mail which is not already register")
def step_impl(context):
    bp=benefitsPages(context)
    bp.rendomizeEmail()


@then("click pn sign up button again")
def step_impl(context):
    bp=benefitsPages(context)
    bp.afterRandomizing()