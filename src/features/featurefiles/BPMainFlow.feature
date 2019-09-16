# Created by ZAWAR-PC at 9/4/2019
Feature: Bigparser gereral flow which a user follows in this web Application

  Scenario: Create an account and sigin in.Then upload a file , rename it and logout after deleting that file
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
    Then Delete any file
    Then sign out