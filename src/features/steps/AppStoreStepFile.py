from behave import *
from src.features.pages.AppStorePageFile import AppStore

use_step_matcher("re")


@then("Click on App Store Button on Header")
def step_impl(context):
    App = AppStore(context)
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


@then("Click on Basics")
def step_impl(context):
    App = AppStore(context)
    App.ClickBasics()


@then("Click on Products")
def step_impl(context):
    App = AppStore(context)
    App.ClickProducts()


@then("Go back to previous page")
def step_impl(context):
    App = AppStore(context)
    App.GoToPreviousPage()


@then("verify that user is again at home page")
def step_impl(context):
    App = AppStore(context)
    App.VerifyHome()


@then("Click on Pricing")
def step_impl(context):
    App = AppStore(context)
    App.ClickPricing()


@then("Verify that user is at Pricing Page")
def step_impl(context):
    App = AppStore(context)
    App.VerifyPricingPage()


@then("Click on Get help")
def step_impl(context):
    App = AppStore(context)
    App.ClickGetHelp()

@then("Click on Support")
def step_impl(context):
    App = AppStore(context)
    App.ClickSuport()


@then("verify that user is redirected to Support page in new tab")
def step_impl(context):
    App = AppStore(context)
    App.VerifySupportPage()


@then("Close that tab and come back to home page")
def step_impl(context):
    App = AppStore(context)
    App.CloseTab()

@then("Click on Help and Forums")
def step_impl(context):
    App = AppStore(context)
    App.ClickHelpandForum()


@then("Verify that user is redirected to Help page in new tab")
def step_impl(context):
    App = AppStore(context)
    App.VerifyHelpPage()


@then("Click on FAQ page")
def step_impl(context):
    App = AppStore(context)
    App.ClickFAQ()

@then("Verify that user is redirected to FAQ page in new tab")
def step_impl(context):
    App = AppStore(context)
    App.VerifyFAQPage()


@then("Click on Apps")
def step_impl(context):
    App = AppStore(context)
    App.ClickApps()


@then("Verify that user is at App Store page")
def step_impl(context):
    App = AppStore(context)
    App.VerifyAppStorePage()

@then("Click on Legal")
def step_impl(context):
    App = AppStore(context)
    App.ClickLegal()


@then("Click on Security")
def step_impl(context):
    App = AppStore(context)
    App.ClickSecurity()


@then("Verify that user is at Security Page")
def step_impl(context):
    App = AppStore(context)
    App.VerifySecurityPage()


@then("Click on BP Icon and go to main page")
def step_impl(context):
    App = AppStore(context)
    App.ClickBPIcon()


@then("Click on Privacy and Terms")
def step_impl(context):
    App = AppStore(context)
    App.ClickPrivacyandTerms()


@then("Verify that user is at Privacy page")
def step_impl(context):
    App = AppStore(context)
    App.VerifyPrivacyPage()


@then("Click on Engage")
def step_impl(context):
    App = AppStore(context)
    App.ClickEngage()


@then("Click on Jobs")
def step_impl(context):
    App = AppStore(context)
    App.ClickJobs()


@then("Verify that user is at Jobs Page")
def step_impl(context):
    App = AppStore(context)
    App.VerifyJobsPage()


@then("Click on Blog")
def step_impl(context):
    App = AppStore(context)
    App.ClickBlog()

@then("Verify that user is at Blog Page")
def step_impl(context):
    App = AppStore(context)
    App.VerifyBlogPage()

@then("Click on Press and Media")
def step_impl(context):
    App = AppStore(context)
    App.ClickPressandMedia()


@then("Verify that user is at Media Page")
def step_impl(context):
    App = AppStore(context)
    App.VerifyMediaPage()


@then("Click on more apps")
def step_impl(context):
    App = AppStore(context)
    App.ClickMoreApps()


@then("Click on BP Icon again and go to main page")
def step_impl(context):
    App = AppStore(context)
    App.ClickBigparserIcon()


@then("Click on BP Icon and go to main page from jobs page")
def step_impl(context):
    App = AppStore(context)
    App.ClickBigparserIconJob()


@then("Click on BP Icon and go to main page from app store page")
def step_impl(context):
    App = AppStore(context)
    App.ClickBigparserIconAppStore()