# Created by ZAWAR-PC at 9/16/2019
Feature:File Sharing

  Scenario: Share a file publically,unlistedly,privatly and verify it has been shared
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
    Then Click on open sheet drop down
    Then Select File name
    Then Click on Done
    Then Click on Share Button to share file
    Then Click on Get Sharable link
    Then Click on copy button
    Then Switch to Incognito and open copied link and verify that file is loaded
    Then Go back to normal window and close share modal
    Then verify that share count of that file has been updated
    Then Go to Shared tab from my data Tab
    Then click on share type drop down and select  "Shared by me"
#    Then Verify that shared file is loaded
#    Then Exit incognito window and permform next steps
#    Then Verify that shared file opens
#    Then Switch back
#    Then click on share button
#    Then Click on drop down icon of share button
#    Then Click on Unshare
#    Then Click on Unshare on button of Confirmation dialogue box
#    Then Verify that share count updates after unsharing a grid
#    Then check public radio button
#    Then Click on Share Button to share file
#    Then verify share success message appears
#    Then go to public tab
#    Then verify that shared file is present in public tab
#    Then click on share button under shred file in shared tab
#    Then verify that social share options are present
#    Then verify that sharable link and copy button are present
#    Then click on copy button to copy sharable link
#    Then verify that sharable link is copies successfully
#    Then close success message
#    Then close share modal
#    Then go back to My Data tab
#    Then verify that share count of that file has been updated