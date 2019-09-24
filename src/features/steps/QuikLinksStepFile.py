from behave import *

from src.features.pages.QuickLinksPageFile import QuickLink

from src.features.pages.signinpage import SignInPage
import time

use_step_matcher("re")




@then("Howe over profile icon and select Quick links")
def step_impl(context):
    quick=QuickLink(context)
    quick.ClickQuickLinksButton()


@then("Click on Get Started")
def step_impl(context):
    quick=QuickLink(context)
    quick.GetStarted()


@then("Click on Watch a Video")
def step_impl(context):
    quick = QuickLink(context)
    quick.WatchVideo()


@then("Verify that video is loaded")
def step_impl(context):
    quick = QuickLink(context)
    quick.closeVideo()


@then("Close Video")
def step_impl(context):
    quick = QuickLink(context)
    quick.ClosePlayingVideo()


@then("Click on Chat with Us")
def step_impl(context):
    quick = QuickLink(context)
    quick.chat()


@then("Click on Show Hints")
def step_impl(context):
    quick = QuickLink(context)
    quick.hints()


@then("Verify that user is on Hints page")
def step_impl(context):
    quick = QuickLink(context)
    quick.HintsPageConferm()


@then("Close Hints Page")
def step_impl(context):
    quick = QuickLink(context)
    quick.CloseHints()


@then("Click on Apply for Jobs/Internships")
def step_impl(context):
    quick = QuickLink(context)
    quick.job()


@then("Verify that user is on Jobs / Internship Application form")
def step_impl(context):
    quick = QuickLink(context)
    quick.VerifyjobsPage()


@then("Close that page and go to main page")
def step_impl(context):
    quick = QuickLink(context)
    quick.closeForm()