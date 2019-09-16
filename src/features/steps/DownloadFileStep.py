from behave import *
from src.features.pages.DownloadPageFile import Download
use_step_matcher("re")


@then("click on download button and verify that file is downloaded")
def step_impl(context):
    downloadFile=Download(context)
    downloadFile.download()