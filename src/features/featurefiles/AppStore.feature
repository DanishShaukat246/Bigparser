
Feature: App Store

  Scenario: Go to app store and verify that all of its filters work fine
    Given user is at home page
     #Sign In
    Then verify that all mandatory sign in fields are present
    Then enter invalid email for sign in
    Then enter invalid password
    Then click on sign in button
    Then verify that user see error note in case of invalid credentials
    Then enter valid email
    Then enter valid password
    Then click on sign in button for valid credentials
    Then verify that user is at home page

    #App Store
    Then Click on App Store Button on Header
    Then Verify that user is on App Store page
    Then Verify that "All Bigparser Apps" filter is selected By Default
    Then Click on category filter and select "Pre-Installed Apps"
    Then Verify that "Share App" , "Grid App" and "Plug App" widgets appear
    Then Click on Category filter and select "Installed Apps"
    Then Verify that "Drop Box" , "One Drive" and "Google Drive" widgets appear
    Then Click on category filter and select "Uninstalled Apps"
    Then Verify that your uninstalled apps appear 
    Then Click on category filter and Select "Pre-Order Apps"
    Then Verify that Pre-Order Apps like "Facebook" , "Skype" , "Gmail" , "LinkedIn" appear
    Then Go back to home page

