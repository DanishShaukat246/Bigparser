Feature:check benefits

  Scenario: Book the ticket and verify the booking reference number
    Given user is at home page
    Then verify that all mendatory fields are present
    Then Enter name in ful name field
    Then Enter Password in passsword field
    Then Enter email in emial field
    Then Click on Sign Up button
    Then verify that user shows eror massage of already existing email
    Then Enter new mail which is not already register
    Then click pn sign up button again
    Then verify that user is on get started page
    Then click on continue and next button then ultimately finish demo screen
    Then sign out