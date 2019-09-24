
Feature: Quick Links

  Scenario: Open Quick links and verify that they are loading and working fine
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
    Then Howe over profile icon and select Quick links
    Then Click on Get Started
    Then click on continue and next button then ultimately finish demo screen
    Then Howe over profile icon and select Quick links
    Then Click on Watch a Video
    Then Verify that video is loaded
    Then Close Video
    Then Howe over profile icon and select Quick links
    Then Click on Chat with Us
    Then Howe over profile icon and select Quick links
    Then Click on Show Hints
    Then Verify that user is on Hints page
    Then Close Hints Page
    Then Howe over profile icon and select Quick links
    Then Click on Apply for Jobs/Internships
    Then Verify that user is on Jobs / Internship Application form
    Then Close that page and go to main page


