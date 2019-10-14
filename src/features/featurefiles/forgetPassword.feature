
Feature: Forget Password

  Scenario: Veridy that user receive email for forget password and can successfully sign in after resetting password
  Given user is at home page
    Then verify that all mendatory sign in fields are present
    Then click on forget password under sign in fields
    Then enter email and click send
    Then verify that email sent success confermation text apears after enterring
    Then open that given mail in new tab
    Then open gmail and enter email to login
    Then Enter password for that ID