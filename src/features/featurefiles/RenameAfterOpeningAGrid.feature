# Created by ZAWAR-PC at 8/29/2019
Feature: Rename File

  Scenario: Rename a grid after opening it
    Given user is at home page
    Then verify that all mendatory sign in fields are present
    Then enter valid email for sign in
    Then enter valid admin password
    Then click on sign in button to go to home page
    Then verify that uploading box is present
    Then upload file and Verify its presence
    Then Open that grid
    Then Click on more options button
    Then Click on Rename file
    Then Clear editfield and enter new name
    Then Click on Rename button
    Then Verify that Rename confermation note apears now
    Then click close it
    Then Verify that name has been edited
    Then close that grid
    Then sign out