from behave import *
from src.features.pages.ProfileSettings import Profile
use_step_matcher("re")


@then("Click on Nav menu button")
def step_impl(context):
    nav=Profile(context)
    nav.ClickNavButton()


@then("Verify that My Data , Shared , Public and settings options are available")
def step_impl(context):
    nav=Profile(context)
    nav.NavOptios()


@then("Click on Shared and verify that user redirects to Shared Tab")
def step_impl(context):
    nav=Profile(context)
    nav.ClickShare()

@then("Go to nav menu and click Public")
def step_impl(context):
    nav=Profile(context)
    nav.ClickPublic()


@then("Verify that user is in Public tab")
def step_impl(context):
    nav = Profile(context)
    nav.VerifyPublicTab()


@then("Go to nav menu and click settings")
def step_impl(context):
    nav=Profile(context)
    nav.ClickSettings()

@then("Verify that user is at Profile Settings page")
def step_impl(context):
    nav=Profile(context)
    nav.VerifySettingsPage()

@then("Verify that user name , emial fields and profile picture widget are present")
def step_impl(context):
    nav = Profile(context)
    nav.SettingsPageWidgets()


@then("Edit name field and enter new user name you want to use")
def step_impl(context):
    nav=Profile(context)
    nav.EnterName()

@then("Uplaod new profile picture")
def step_impl(context):
    nav=Profile(context)
    nav.UploadPicture()

@then("Then Click on Change password")
def step_impl(context):
    nav=Profile(context)
    nav.ClickChangePassword()


@then("Verify that Current Password , New Password and Confirm Password fields are present")
def step_impl(context):
    nav = Profile(context)
    nav.PasswordFields()


@then("Enter your current password in its respective field")
def step_impl(context):
    nav=Profile(context)
    nav.CurrentPassword()


@then("Enter new password you want to change in its respective field")
def step_impl(context):
    nav=Profile(context)
    nav.NewPassword()


@then("Re-enter new password in Confirm password field")
def step_impl(context):
    nav=Profile(context)
    nav.ConfirmPassword()

@then("Edit Add Mobile number field and input your mobile number")
def step_impl(context):
    nav = Profile(context)
    nav.CellNumber()


@then("Click on Update button")
def step_impl(context):
    nav = Profile(context)
    nav.ClickUpdateButton()


@then('Verify that "Profile Updated Successfuly" confirmation apears on top of page')
def step_impl(context):
    nav=Profile(context)
    nav.ConfirmUpdate()


@then("Hove over profile icon and verify that updated user name is apearing with profile picture")
def step_impl(context):
    nav=Profile(context)
    nav.FromPrifileIconConfirm()


@then("Verify updated credentials credentials")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Verify updated credentials credentials')