# Created by ZAWAR-PC at 8/28/2019
Feature:File Upload

  Scenario: Cencel uploading a file if it already exist
    Given user is at home page
#   Given user is at application page
    Then verify that all mendatory sign in fields are present
    Then clear credentials fields
    Then enter valid email for sign in
    Then enter valid admin password
    Then click on sign in button to go to home page
    Then verify that uploading box is present
    Then Try uploading a file and if its already uploaded cencel uploading
    Then sign out
