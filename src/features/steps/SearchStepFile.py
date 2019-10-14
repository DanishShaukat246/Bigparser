from behave import *
from src.features.pages.SearchPageFile import Search
use_step_matcher("re")


@then("Enter uploaded file name in search field and verify if it is shown in grids section of My Data tab")
def step_impl(context):
    search=Search(context)
    search.EnterText()

@then("Clear search field")
def step_impl(context):
    search=Search(context)
    search.ClearField()


@then("Enter any related key work in global search bar and press Enter")
def step_impl(context):
    search = Search(context)
    search.KeyEnter()


@then("Verify that data related to that key word loads in grid")
def step_impl(context):
    search = Search(context)
    search.VerifyRelatedLoad()


@then("Select Search All Grids")
def step_impl(context):
    search = Search(context)
    search.SearchAllOptionClick()


@then("Click search button")
def step_impl(context):
    search = Search(context)
    search.SearchClick()


@then("Verify that Grids Found text is displayed")
def step_impl(context):
    search = Search(context)
    search.VerificationText()


@then("Click on selection type drop down icon")
def step_impl(context):
    search = Search(context)
    search.dropDownClick()


@then("Uncheck any sheet")
def step_impl(context):
    search = Search(context)
    search.Deselect()


@then("Click Search")
def step_impl(context):
    search = Search(context)
    search.ClickSearch()


@then("Verify that count of showing Grids gets update")
def step_impl(context):
    search = Search(context)
    search.VerifyCountUpdate()


@then("search name of file you shared")
def step_impl(context):
    search = Search(context)
    search.searchInShared()