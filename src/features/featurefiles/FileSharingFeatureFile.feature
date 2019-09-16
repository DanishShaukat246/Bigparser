# Created by ZAWAR-PC at 9/16/2019
Feature:File Sharing

  Scenario: Share a file publically,unlistedly,privatly and verify it has been shared
    Given user is at home page
    Then verify that all mendatory sign in fields are present
    Then enter valid email for sign in
    Then enter valid admin password
    Then click on sign in button to go to home page
    Then verify that uploading box is present
    Then upload file and Verify its presence
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