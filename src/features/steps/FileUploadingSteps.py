from behave import *
from src.features.pages.BPFileUpload import fileUpload




from src.features.pages.signinpage import SignInPage
import time

use_step_matcher("re")


@then("enter valid email for sign in")
def step_impl(context):
    bp=fileUpload(context)
    bp.enterMail()


@then("enter valid admin password")
def step_impl(context):
    bp = fileUpload(context)
    bp.enterPWD()



@then("click on sign in button to go to home page")
def step_impl(context):
    bp = fileUpload(context)
    bp.ClickA()


@then("verify that uploading box is present")
def step_impl(context):
    bp = fileUpload(context)
    bp.UploadBoxP()


@then("upload file")
def step_impl(context):
    bp=fileUpload(context)
    bp.UploadFile()


@then("upload file but don't overright existig file")
def step_impl(context):
    bp=fileUpload(context)
    bp.dontOverwright()


@then("Try uploading a file and if its already uploaded cencel uploading")
def step_impl(context):
     bp=fileUpload(context)
     bp.cencelUpload()


@then("sign out")
def step_impl(context):

    bp=fileUpload(context)
    bp.signOut()


@then("clear credentials fields")
def step_impl(context):
    bp=fileUpload(context)
    bp.clearFields()


@given("user is at application page")
def step_impl(context):
    bp=fileUpload(context)
    bp.home()


@then("Try uploading a file by overwriting name and if its already uploaded cencel uploading")
def step_impl(context):
    bp = fileUpload(context)
    bp.overwite()


@then("Cut file and click done if its already uploaded")
def step_impl(context):
    bp = fileUpload(context)
    bp.doneClick()
