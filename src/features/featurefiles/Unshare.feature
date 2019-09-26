
Feature: Unshare

  Scenario: Unsharing a file in all possible scenarios
    Given user is at home page
    Then verify that all mandatory fields are present
    Then Enter name in full name field
    Then Enter Password in password field
    Then Enter email in email field
    Then Click on Sign Up button
    Then verify that user shows error massage of already existing email
    Then Enter new mail which is not already register
    Then click on sign up button again
    Then verify that user is on get started page
    Then click on continue and next button then ultimately finish demo screen
    Then verify that uploading box is present
    Then upload file and Verify its presence
    Then click on share button
    Then check public radio button
    Then Click on Share Button to share file
    Then verify share success message appears
    Then go to public tab
    Then go back to My Data tab
    Then verify that share count of that file has been updated
    Then Click on Share Button bellow that grid
    Then Click on Drop down icon on share button
    Then Click on Unshare
    Then Verify that Confirmation pop up appears
    Then Click on Unshare on button of Confirmation dialogue box
    Then Verify that share count updates after unsharing a grid