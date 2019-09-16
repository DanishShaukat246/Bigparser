# Created by ZAWAR-PC at 8/23/2019
Feature:Big Parser Sign In

  Scenario:Verify all possitve and negative test cases
    Given user is at home page
    Then verify that all mendatory sign in fields are present



    Then enter invalid email for sign in
    Then enter invalid password
    Then click on sign in button
    Then verify that user see error note in case of invalid credentials
    Then enter valid emial
    Then enter valid password
    Then click on sign in button for valid credentals
    Then verify that user is at home page
