from behave import *
from src.features.pages.FileSharingPageFile import Share

use_step_matcher("re")


@then("click on share button")
def step_impl(context):
    a = Share(context)
    a.clickShare()


@then("check public radio button")
def step_impl(context):
    b = Share(context)
    b.PublicRadio()


@then("Click on Share Button to share file")
def step_impl(context):
    c = Share(context)
    c.ClickShareButton()


@then("verify share success message appears")
def step_impl(context):
    d = Share(context)
    d.VerifySuccess()


@then("go to public tab")
def step_impl(context):
    e = Share(context)
    e.GoPublic()


@then("verify that shared file is present in public tab")
def step_impl(context):
    f = Share(context)
    f.VerifyPresence()


@then("click on share button under shred file in shared tab")
def step_impl(context):
    g = Share(context)
    g.InTabShareButtonPress()


@then("click on copy button to copy sharable link")
def step_impl(context):
    h = Share(context)
    h.clickCopy()


@then("verify that sharable link is copies successfully")
def step_impl(context):
    i = Share(context)
    i.VerifyCopy()


@then("close success message")
def step_impl(context):
    j = Share(context)
    j.CloseSuccessMsg()


@then("verify that social share options are present")
def step_impl(context):
    k = Share(context)
    k.VerifySocialShare()


@then("verify that sharable link and copy button are present")
def step_impl(context):
    l = Share(context)
    l.verifyCopy()


@then("close share modal")
def step_impl(context):
    m = Share(context)
    m.CloseModal()


@then("go back to My Data tab")
def step_impl(context):
    n = Share(context)
    n.GoToMyData()


@then("verify that share count of that file has been updated")
def step_impl(context):
    o = Share(context)
    o.VerifyShareCount()


@then("Click on Get Sharable link")
def step_impl(context):
    p = Share(context)
    p.ClickLik()


@then("Click on copy button")
def step_impl(context):
    q = Share(context)
    q.Copy()


@then("Verify that link copy success message appears")
def step_impl(context):
    r=Share(context)
    r.ConfirmCopy()


@then("Switch to Incognito and open copied link and verify that file is loaded")
def step_impl(context):
   s=Share(context)
   s.ShiftToIncognito()


@then("Verify that shared file is loaded")
def step_impl(context):
    t = Share(context)
    t.VerifyFileLoad()


@then("Go back to normal window and close share modal")
def step_impl(context):
    u = Share(context)
    u.closeShareModal()


@then("Go to Shared tab from my data Tab")
def step_impl(context):
     v = Share(context)
     v.GoShare()


@then("Click on open sheet drop down")
def step_impl(context):
    w = Share(context)
    w.ShareDropSelect()


@then("Select File name")
def step_impl(context):
    y = Share(context)
    y.SelectFile()


@then("Click on Done")
def step_impl(context):
     z = Share(context)
     z.Done()
