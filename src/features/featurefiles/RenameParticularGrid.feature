# Created by ZAWAR-PC at 8/29/2019
Feature: Rename Grid

  Scenario: Rename a Particular grid throw more options button
    Given user is at home page
    Then verify that all mendatory sign in fields are present
    Then enter valid email for sign in
    Then enter valid admin password
    Then click on sign in button to go to home page
    Then verify that uploading box is present
    Then upload file and Verify its presence
    Then Click on more option button under that file
    Then click on Rename
    Then Clear rename text field and Enter new name
    Then click on done button
    Then Verify that Rename Confermation note apears
    Then Click on Cross button
    Then verify that Grid apears with edited name
    Then sign out