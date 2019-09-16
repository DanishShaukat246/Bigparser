# Created by ZAWAR-PC at 9/2/2019
Feature: Deleting a Grid

  Scenario: Delete a specific grid without opening it
     Given user is at home page
     Then verify that all mendatory sign in fields are present
     Then clear credentials fields
     Then enter valid email for sign in
     Then enter valid admin password
     Then click on sign in button to go to home page
     Then Delete any file
     Then sign out