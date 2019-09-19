
Feature: Bigparser gereral flow which a user follows in this web Application

  Scenario: Create an account and sigin in.Then upload a file , rename it and logout after deleting that file
    Given user is at home page
    Then verify that all mendatory fields are present
    Then Enter name in full name field
    Then Enter Password in passsword field
    Then Enter email in emial field
    Then Click on Sign Up button
    Then verify that user shows eror massage of already existing email
    Then Enter new mail which is not already register
    Then click pn sign up button again
    Then verify that user is on get started page
    Then click on continue and next button then ultimately finish demo screen
    Then verify that uploading box is present
    Then upload file and Verify its presence
    Then click on download button and verify that file is downloaded
    Then Click on more option button under that file
    Then click on Rename
    Then Clear rename text field and Enter new name
    Then click on done button
    Then Verify that Rename Confermation note apears
    Then Click on Cross button
    Then verify that Grid apears with edited name
    Then Open that grid
    Then Bypass demo widgets
    Then Click on more options button
    Then Click on Rename file
    Then Clear editfield and enter new name
    Then Click on Rename button
    Then Verify that Rename confermation note apears now
    Then click close it
    Then Verify that name has been edited
    Then close that grid
    Then click on share button
    Then check public radio button
    Then Click on Share Button to share file
    Then verify share success message appears
    Then go to public tab
    Then verify that shared file is present in public tab
    Then click on share button under shred file in shared tab
    Then verify that social share options are present
    Then verify that sharable link and copy button are present
    Then click on copy button to copy sharable link
    Then verify that sharable link is copies successfully
    Then close success message
    Then close share modal
    Then go back to My Data tab
    Then verify that share count of that file has been updated
    Then Delete that file
    Then sign out