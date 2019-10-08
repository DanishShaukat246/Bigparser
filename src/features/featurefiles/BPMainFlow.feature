
Feature: Bigparser general flow which a user follows in this web Application

  Scenario: Create an account and sig in in.Then upload a file , rename it and logout after deleting that file

    Given user is at home page

   #SignUp and login
    Then verify that all mandatory fields are present
    Then Enter name in full name field
    Then Enter Password in password field
    Then Enter email in email field
    Then Click on Sign Up button
    Then verify that user shows error massage of already existing email
    Then Enter new mail which is not already register
    Then click on sign up button again

    #Demo Screen
    Then verify that user is on get started page
    Then click on continue and next button then ultimately finish demo screen

    #File Uploading
    Then verify that uploading box is present
    Then upload file and Verify its presence

    #File Download
    Then click on download button and verify that file is downloaded

    #Rename File Without opening it
    Then Click on more option button under that file
    Then click on Rename
    Then Clear rename text field and Enter new name
    Then click on done button
    Then Verify that Rename Confirmation note appears after this
    Then Click on Cross button
    Then verify that Grid appears with edited name

    #Rename Fle after opening it
    Then Open that grid
    Then Bypass demo widgets
    Then Click on more options button
    Then Click on Rename file
    Then Clear edit field and enter new name
    Then Click on Rename button
    Then Verify that Rename confirmation note appears now
    Then click close it
    Then Verify that name has been edited
    Then close grid

    #Public Sharing
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

    #Unshare a publicly shared file from My Data tab without opening it
    Then Click on Share Button bellow that grid
    Then Click on Drop down icon on share button
    Then Click on Unshare
    Then Verify that Confirmation pop up appears
    Then Click on Unshare on button of Confirmation dialogue box
    Then Verify that share count updates after unsharing a grid

    #Again sharing file to check second scenario of public sharing
    Then click on share button
    Then check public radio button
    Then Click on Share Button to share file
    Then verify share success message appears
    Then Click Cross button and Close Share modal

    #unsharing a publicly shared grid from My Data tab after opening it
    Then Open that grid
    Then Click on Share button which appears top right side of grid after opening it
    Then Click on drop down icon of share button
    Then click on unshare option
    Then click on ushare button of confirmation dialogue
    Then close the grid
    Then Verify that share count updates after unsharing a grid

    #Private Sharing of file
    Then click on share button
    Then Click on Private radio button
    Then Click on email field and enter email you want to use
    Then Click on Share Button to share file
    Then Verify that shared Confirmation pop up appears
    Then Go to Shared Tab
    Then click on share type drop down and select  "Shared by me"
    Then verify that your shared file is present in shared tab

    #Unsharing a privately shared file from My Data tab without opening it
    Then go back to My Data tab
    Then Click on Share Button bellow that grid
    Then Click on Drop down icon on share button
    Then Click on Unshare
    Then Check "Select All" and "Multi Select" radio buttons
    Then Click on unshare button

    #Unlisted Sharing
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

    #Unsharing an Unlisted Shared  File From My Data Tab without opening it
    Then Click on Share Button bellow that grid
    Then Click on Drop down icon on share button
    Then Click on Unshare
    Then Verify that Confirmation pop up appears
    Then Click on Unshare on button of Confirmation dialogue box

    #Again Sharing file for second scenario of unsharing
    Then click on share button
    Then Click on open sheet drop down
    Then Select File name
    Then Click on Done
    Then Click on Share Button to share file
    Then Click on Get Sharable link
    Then Click on copy button
    Then Switch to Incognito and open copied link and verify that file is loaded
    Then Go back to normal window and close share modal

    #Unsharing Unlisted shared file after opening it in My Data Tab
    Then Open that grid
    Then Click on Share button which appears top right side of grid after opening it
    Then Click on drop down icon of share button
    Then click on unshare option
    Then click on ushare button of confirmation dialogue
    Then close the grid
    Then Verify that share count updates after unsharing a grid

    #Delete File
    Then Delete the file

    #Quick Links
    Then Howe over profile icon and select Quick links
    Then Click on Get Started
    Then click on continue and next button then ultimately finish demo screen
    Then Howe over profile icon and select Quick links
    Then Click on Watch a Video
    Then Verify that video is loaded
    Then Close Video
    Then Howe over profile icon and select Quick links
    Then Click on Chat with Us
    Then Howe over profile icon and select Quick links
    Then Click on Show Hints
    Then Verify that user is on Hints page
    Then Close Hints Page
    Then Howe over profile icon and select Quick links
    Then Click on Apply for Jobs/Internships
    Then Verify that user is on Jobs / Internship Application form
    Then Close that page and go to main page

    #Log out
    Then sign out