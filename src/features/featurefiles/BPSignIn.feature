# Created by ZAWAR-PC at 8/23/2019
Feature:Big Parser Sign In

  Scenario:Verify all possitve and negative test cases
    Given user is at home page
    Then Click create account without entering any thing in any required fiel
    Then Verify that Error message "Please Enter your name" appears
    Then Enter name
    Then Click Create account and verify Error message of Empty email field appears
    Then Enter email
    Then Click Create account and verify error message of empty password field appears
    Then Enter password