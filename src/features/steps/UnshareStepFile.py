from behave import *
from src.features.pages.commonPage import commonPage
from src.features.pages.UnSharePageFile import Unshare
from src.features.pages.basepage import basePage
import time
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