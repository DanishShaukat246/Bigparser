from behave import *
from src.features.pages.FileSharingPageFile import Share
use_step_matcher("re")


@then("click on share button")
def step_impl(context):
    a=Share(context)
    a.clickShare()


@then("check public radio button")
def step_impl(context):
    b=Share(context)
    b.PublicRadio()


@then("Click on Share Button to share file")
def step_impl(context):
    c=Share(context)
    c.ClickShareButton()

@then("verify share success message appears")
def step_impl(context):
    d=Share(context)
    d.VerifySuccess()


@then("go to public tab")
def step_impl(context):
   e=Share(context)
   e.GoPublic()


@then("verify that shared file is present in public tab")
def step_impl(context):
    f=Share(context)
    f.VerifyPresence()


@then("click on share button under shred file in shared tab")
def step_impl(context):
    g=Share(context)
    g.InTabShareButtonPress()


@then("click on copy button to copy sharable link")
def step_impl(context):
   h=Share(context)
   h.clickCopy()

@then("verify that sharable link is copies successfully")
def step_impl(context):
    i=Share(context)
    i.VerifyCopy()


@then("close success message")
def step_impl(context):
    j=Share(context)
    j.CloseSuccessMsg()


@then("verify that social share options are present")
def step_impl(context):
    k=Share(context)
    k.VerifySocialShare()

@then("verify that sharable link and copy button are present")
def step_impl(context):
    l=Share(context)
    l.verifyCopy()


@then("close share modal")
def step_impl(context):
    m=Share(context)
    m.CloseModal()


@then("go back to My Data tab")
def step_impl(context):
    n=Share(context)
    n.GoToMyData()


@then("verify that share count of that file has been updated")
def step_impl(context):
    o=Share(context)
    o.VerifyShareCount()