# Created by ZAWAR-PC at 8/29/2019
Feature: File Upload

  Scenario:If file is already existing cencel by clicking cross buttona and then click done button and verify that no file gets uploaded
  Given user is at home page
#   Given user is at application page
    Then verify that all mendatory sign in fields are present
    Then clear credentials fields
    Then enter valid email for sign in
    Then enter valid admin password
    Then click on sign in button to go to home page
    Then verify that uploading box is present
    Then Cut file and click done if its already uploaded
    Then sign out