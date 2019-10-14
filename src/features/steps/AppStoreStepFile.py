from behave import *
from src.features.pages.AppStorePageFile import AppStore

use_step_matcher("re")


@then("Click on App Store Button on Header")
def step_impl(context):
   App=AppStore(context)
   App.GoToAppStore()

@then("Verify that user is on App Store page")
def step_impl(context):
    App = AppStore(context)
    App.VerifyPageLoad()


@then('Verify that "All Bigparser Apps" filter is selected By Default')
def step_impl(context):
    App = AppStore(context)
    App.VerifDefaultFilter()

@then('Click on category filter and select "Pre-Installed Apps"')
def step_impl(context):
    App = AppStore(context)
    App.SelectPreInstalled()

@then('Verify that "Share App" , "Grid App" and "Plug App" widgets appear')
def step_impl(context):
    App = AppStore(context)
    App.VerifyPreInstalled()
@then('Click on Category filter and select "Installed Apps"')
def step_impl(context):
    App = AppStore(context)
    App.SelectInstalledApps()

@then('Verify that "Drop Box" , "One Drive" and "Google Drive" widgets appear')
def step_impl(context):
        App = AppStore(context)
        App.VerifyInstalled()

@then('Click on category filter and select "Uninstalled Apps"')
def step_impl(context):
    App = AppStore(context)
    App.SelectUninstalledApps()


@then("Verify that your uninstalled apps appear")
def step_impl(context):
    App = AppStore(context)
    App.VerifyUnInstalled()


@then('Click on category filter and Select "Pre-Order Apps"')
def step_impl(context):
    App = AppStore(context)
    App.SelectPreOrder()


@then('Verify that Pre-Order Apps like "Facebook" , "Skype" , "Gmail" , "LinkedIn" appear')
def step_impl(context):
    App = AppStore(context)
    App.VerifyPreOrder()


@then("Go back to home page")
def step_impl(context):
    App = AppStore(context)
    App.GoHome()
