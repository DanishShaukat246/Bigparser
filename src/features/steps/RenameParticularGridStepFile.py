from behave import *

from src.features.pages.RenameParticularGripPageFile import Rename
import time

use_step_matcher("re")

class groupStep():

  @then("upload file and Verify its presence")
  def step_impl(context):
    bp = Rename(context)
    bp.loadBigparserSignIn()


@then("Click on more option button under that file")
def step_impl(context):
    bp = Rename(context)
    bp.ClickMoreOptions()


@then("click on Rename")
def step_impl(context):
    bp = Rename(context)
    bp.ClickRename()


@then("Clear rename text field and Enter new name")
def step_impl(context):
    bp = Rename(context)
    bp.RenameEdit()


@then("click on done button")
def step_impl(context):
    bp = Rename(context)
    bp.RenameDone()


@then("Verify that Rename Confirmation note appears after this")
def step_impl(context):
    bp = Rename(context)
    bp.RenameConfermation()


@then("Click on Cross button")
def step_impl(context):
    bp = Rename(context)
    bp.RenameClose()


@then("verify that Grid appears with edited name")
def step_impl(context):
    bp = Rename(context)
    bp.VerifyRenamed()


@then("Open that grid")
def step_impl(context):
    bp = Rename(context)
    bp.OpenGrid()


@then("Click on more options button")
def step_impl(context):
    bp = Rename(context)
    bp.MoreOptions()


@then("Click on Rename file")
def step_impl(context):
    bp = Rename(context)
    bp.RenameClickOpenedFile()


@then("Clear edit field and enter new name")
def step_impl(context):
    bp = Rename(context)
    bp.EditthatName()


@then("Click on Rename button")
def step_impl(context):
    bp = Rename(context)
    bp.ClickRenameButton()


@then("Verify that Rename confirmation note appears now")
def step_impl(context):
    bp = Rename(context)
    bp.ConfermafterOpen()


@then("click close it")
def step_impl(context):
    bp = Rename(context)
    bp.Cross()


@then("Verify that name has been edited")
def step_impl(context):
    bp = Rename(context)
    bp.Check()


@then("close that grid")
def step_impl(context):
    bp = Rename(context)
    bp.CloseGrid()


@then("Bypass demo widgets")
def step_impl(context):
    bp = Rename(context)
    bp.Bypass()