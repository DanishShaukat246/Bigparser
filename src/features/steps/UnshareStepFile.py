from behave import *
from src.features.pages.UnSharePageFile import Unshare


use_step_matcher("re")


@then("Click on Share Button bellow that grid")
def step_impl(context):
    unshare=Unshare(context)
    unshare.ClickShare()


@then("Click on Drop down icon on share button")
def step_impl(context):
    unshare=Unshare(context)
    unshare.ShareButtonDropdownIconClick()


@then("Click on Unshare")
def step_impl(context):
    unshare=Unshare(context)
    unshare.ClickUnshare()


@then("Verify that Confirmation pop up appears")
def step_impl(context):
    unshare=Unshare(context)
    unshare.UnshareModal()


@then("Click on Unshare on button of Confirmation dialogue box")
def step_impl(context):
    unshare = Unshare(context)
    unshare.DialogueBoxConfirm()


@then("Verify that share count updates after unsharing a grid")
def step_impl(context):
    unshare = Unshare(context)
    unshare.shareCount()

@then("Open that gird which you have just shared")
def step_impl(context):
    pass


@then("Click on Share button which appears top right side of grid after opening it")
def step_impl(context):
    unshare = Unshare(context)
    unshare.Open()


@then("Click on drop down icon of share button")
def step_impl(context):
    unshare = Unshare(context)
    unshare.UnshareDropDown()


@then("click on unshare option")
def step_impl(context):
    unshare = Unshare(context)
    unshare.UnshareOptionClick()


@then("click on ushare button of confirmation dialogue")
def step_impl(context):
    unshare = Unshare(context)
    unshare.ConfrimUnshare()


@then("close the grid")
def step_impl(context):
    unshare = Unshare(context)
    unshare.CloseIt()


@then("Click Cross button and Close Share modal")
def step_impl(context):
    unshare = Unshare(context)
    unshare.CloseShareModal()


@then("Click on Private radio button")
def step_impl(context):
    unshare = Unshare(context)
    unshare.PrivateRadioButtonClick()


@then("Click on email field and enter email you want to use")
def step_impl(context):
    unshare = Unshare(context)
    unshare.EnterEmail()


@then("Go to Shared Tab")
def step_impl(context):
    unshare = Unshare(context)
    unshare.GoToSharedTab()


@then("Verify that shared Confirmation pop up appears")
def step_impl(context):
    unshare = Unshare(context)
    unshare.Verify()


@then('click on share type drop down and select  "Shared by me"')
def step_impl(context):
    unshare = Unshare(context)
    unshare.SharedByMe()


@then('Check "Select All" and "Multi Select" radio buttons')
def step_impl(context):
    unshare = Unshare(context)
    unshare.SelectPermissions()


@then("Click on unshare button")
def step_impl(context):
    unshare = Unshare(context)
    unshare.UnshareButtonClick()


@then("verify that your shared file is present in shared tab")
def step_impl(context):
    unshare = Unshare(context)
    unshare.VerifyPresence()
