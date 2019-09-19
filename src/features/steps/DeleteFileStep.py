from behave import *

from src.features.pages.DeleteGridPageFile import DeleteGrid

from src.features.pages.signinpage import SignInPage
import time

use_step_matcher("re")


@then("Delete that file")
def step_impl(context):
    delete =DeleteGrid(context)
    delete.DeleteGrid()