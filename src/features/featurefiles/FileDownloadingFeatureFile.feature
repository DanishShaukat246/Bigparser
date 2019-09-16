# Created by ZAWAR-PC at 9/16/2019
Feature: File Download

  Scenario: Downloading a file and verifying that it exists in download directory
    Given user is at home page
    Then verify that all mendatory sign in fields are present
    Then enter valid email for sign in
    Then enter valid admin password
    Then click on sign in button to go to home page
    Then verify that uploading box is present
    Then upload file and Verify its presence
    Then click on download button and verify that file is downloaded