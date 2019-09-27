
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

     #common steps of public sharing
#    Then check public radio button
#    Then Click on Share Button to share file
#    Then verify share success message appears
#    Then go to public tab
#    Then go back to My Data tab
#    Then verify that share count of that file has been updated

    #Unsharing a file a file in My data tab without opening it
#    Then Click on Share Button bellow that grid
#    Then Click on Drop down icon on share button
#    Then Click on Unshare
#    Then Verify that Confirmation pop up appears
#    Then Click on Unshare on button of Confirmation dialogue box

      #Unsharing a file from share button after opening it in My Data tab
#    Then Open that grid
#    Then Bypass demo widgets
#    Then Click on Share button which appears top right side of grid after opening it
#    Then Click on drop down icon of share button
#    Then click on unshare option
#    Then click on ushare button of confirmation dialogue
#    Then close the grid
#    Then Verify that share count updates after unsharing a grid