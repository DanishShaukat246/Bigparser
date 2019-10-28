from behave import *

from src.features.pages.BigParserSignIn import benefitsPagesSignIn

from src.features.pages.signinpage import SignInPage
import time

use_step_matcher("re")

class groupStep():




    @given('user is at sign in home page "(?P<url>.+)"')
    def step_impl(context,url):
        bp = benefitsPagesSignIn(context)
        bp.loadBigparserSignIn(url)


    @then("verify that all mandatory sign in fields are present")
    def step_impl(context):
       bp=benefitsPagesSignIn(context)
       bp.verifyFieldPresence()





    @then("enter invalid email for sign in")
    def step_impl(context):
      bp = benefitsPagesSignIn(context)
      bp.enterEmail()


@then("enter invalid password")
def step_impl(context):

    bp=benefitsPagesSignIn(context)
    bp.invalidPassword()


@then("click on sign in button")
def step_impl(context):
    bp = benefitsPagesSignIn(context)
    bp.siginInButtonClick()


@then("verify that user see error note in case of invalid credentials")
def step_impl(context):
    bp = benefitsPagesSignIn(context)
    bp.invalidsignInNote()


@then("enter valid email")
def step_impl(context):
    bp=benefitsPagesSignIn(context)
    bp.validEmail()


@then("enter valid password")
def step_impl(context):
    bp=benefitsPagesSignIn(context)
    bp.validPassword()


@then("click on sign in button for valid credentials")
def step_impl(context):

    bp=benefitsPagesSignIn(context)
    bp.clickValid()


@then("verify that user is at home page")
def step_impl(context):

    bp=benefitsPagesSignIn(context)
    bp.verifyHomePage()


@then("click on continue and next button then ultimately finish demo screen")
def step_impl(context):
    bp=benefitsPagesSignIn(context)
    bp.continuePress()


@then("click on forget password under sign in fields")
def step_impl(context):
    bp = benefitsPagesSignIn(context)
    bp.forgetClick()


@then("enter email and click send")
def step_impl(context):
    bp = benefitsPagesSignIn(context)
    bp.forgotEmailEntery()


@then("verify that email sent success confermation text apears after enterring")
def step_impl(context):
    bp = benefitsPagesSignIn(context)
    bp.emilSentConfermationNote()


@then("open that given mail in new tab")
def step_impl(context):
    bp = benefitsPagesSignIn(context)
    bp.OpenGmailID()


@then("open gmail and enter email to login")
def step_impl(context):
    bp = benefitsPagesSignIn(context)
    bp.EnterGmailID()


@then("Enter password for that ID")
def step_impl(context):
    bp = benefitsPagesSignIn(context)
    bp.GmailPasswordEntry()


@then("Click create account without entering any thing in any required fiel")
def step_impl(context):
    bp = benefitsPagesSignIn(context)
    bp.ClickRegEmpty()


@then('Verify that Error message "Please Enter your name" appears')
def step_impl(context):
    bp = benefitsPagesSignIn(context)
    bp.ErrorName()

@then("Enter name")
def step_impl(context):
    bp = benefitsPagesSignIn(context)
    bp.EnterName()


@then("Click Create account and verify Error message of Empty email field appears")
def step_impl(context):
    bp = benefitsPagesSignIn(context)
    bp.ErrorEmail()


@then("Enter email")
def step_impl(context):
    bp = benefitsPagesSignIn(context)
    bp.EnterEmail()


@then("Click Create account and verify error message of empty password field appears")
def step_impl(context):
    bp = benefitsPagesSignIn(context)
    bp.ErrorPassword()


@then("Enter password")
def step_impl(context):
    bp = benefitsPagesSignIn(context)
    bp.EnterPassword()


@then("Enter invalid password and verify error message appears")
def step_impl(context):
    bp = benefitsPagesSignIn(context)
    bp.InvalidPassword()


@then("Enter email id and updated password in sign in section")
def step_impl(context):
    bp = benefitsPagesSignIn(context)
    bp.UpdatedCredentials()


@then("Verify that user is successfully logged in with updated credentials")
def step_impl(context):
    bp = benefitsPagesSignIn(context)
    bp.VerifyLoggedIn()


@then("log out")
def step_impl(context):
   bp = benefitsPagesSignIn(context)
   bp.logout()


@then("logout")
def step_impl(context):
    bp=benefitsPagesSignIn(context)
    bp.UpdatedCheckLogout()