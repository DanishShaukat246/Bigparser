
Feature: Searching

  Scenario: Check Global , Cross Sheet and Cross Grid search
    Given user is at home page

   #SignUp and login
    Then verify that all mendatory sign in fields are present
    Then enter invalid email for sign in
    Then enter invalid password
    Then click on sign in button
    Then verify that user see error note in case of invalid credentials
    Then enter valid emial
    Then enter valid password
    Then click on sign in button for valid credentals
    Then verify that user is at home page

#    #Demo Screen
#    Then verify that user is on get started page
#    Then click on continue and next button then ultimately finish demo screen

    #File Uploading
    Then verify that uploading box is present
    Then upload file and Verify its presence

    #Global Search
    Then Enter uploaded file name in search field and verify if it is shown in grids section of My Data tab
    Then Clear search field

    #Cross Sheet search
    Then Open that grid
    Then Enter any related key work in global search bar and press Enter


    #Cross Grid Search
    Then Select Search All Grids
    Then Click search button
    Then Verify that Grids Found text is displayed
#    Then Click on selection type drop down icon
#    Then Uncheck any sheet
#    Then Click Search
#    Then Verify that count of showing Grids gets update