Feature: Bigparser general flow which a user follows in this web Application

  Scenario: Create an account and sig in in.Then upload a file , rename it , cover quick links and logout after deleting that file

    Given user is at home page

   #SignUp
    Then verify that all mandatory fields are present
    Then Click create account without entering any thing in any required fiel
    Then Verify that Error message "Please Enter your name" appears
    Then Enter name in full name field
    Then Click Create account and verify Error message of Empty email field appears
    Then Enter email in email field
    Then Click Create account and verify error message of empty password field appears
    Then Enter invalid password and verify error message appears
    Then Enter Password in password field
    Then Click on Sign Up button
    Then verify that user shows error massage of already existing email
    Then Enter new mail which is not already register
    Then click on sign up button again

    #Demo Screen
    Then verify that user is on get started page
    Then click on continue and next button then ultimately finish demo screen

     #Navbar Menu

    Then Click on Nav menu button
    Then Verify that My Data , Shared , Public and settings options are available
    Then Click on Shared and verify that user redirects to Shared Tab
    Then Go to nav menu and click Public
    Then Verify that user is in Public tab
    Then Click on Nav menu button
    Then Click on Basics
    Then Click on Products
    Then Go back to previous page
    Then Click on Nav menu button
    Then Click on Basics
    Then Click on Pricing
    Then Verify that user is at Pricing Page
    Then Click on Nav menu button
    Then Click on Get help
    Then Click on Support
    Then verify that user is redirected to Support page in new tab
    Then Close that tab and come back to home page
    Then Click on Help and Forums
    Then Verify that user is redirected to Help page in new tab
    Then Close that tab and come back to home page
    Then Click on FAQ page
    Then Verify that user is redirected to FAQ page in new tab
    Then Close that tab and come back to home page
    Then Click on Legal
    Then Click on Security
    Then Verify that user is at Security Page
    Then Click on BP Icon and go to main page
    Then Click on Nav menu button
    Then Click on Privacy and Terms
    Then Verify that user is at Privacy page
    Then Click on BP Icon again and go to main page
    Then Click on Nav menu button
    Then Click on Engage
    Then Click on Jobs
    Then Verify that user is at Jobs Page
    Then Click on BP Icon and go to main page from jobs page
    Then Click on Nav menu button
    Then Click on Blog
    Then Verify that user is at Blog Page
    Then Close that tab and come back to home page
    Then Click on Press and Media
    Then Verify that user is at Media Page
    Then Close that tab and come back to home page
    Then Click on Apps
    Then Click on more apps
    Then Verify that user is at App Store page
    Then Click on BP Icon and go to main page from app store page

    #Profile Settings

    Then Go to nav menu and click settings
    Then Verify that user is at Profile Settings page
    Then Verify that user name , emial fields and profile picture widget are present
    Then Uplaod new profile picture
    Then Edit name field and enter new user name you want to use
    Then Then Click on Change password
    Then Verify that Current Password , New Password and Confirm Password fields are present
    Then Enter your current password in its respective field
    Then Enter new password you want to change in its respective field
    Then Re-enter new password in Confirm password field
    Then Edit Add Mobile number field and input your mobile number
    Then Click on Update button
    Then Verify that "Profile Updated Successfuly" confirmation apears on top of page
    Then Hove over profile icon and verify that updated user name is apearing with profile picture
    Then log out

    #Sign In With Updated Password
    Then verify that all mandatory fields are present
    Then Enter email id and updated password in sign in section
    Then verify that user is at home page

     #Log out
    Then logout

    # Sign In with Admin Account
    Then verify that all mandatory sign in fields are present
    Then enter invalid email for sign in
    Then enter invalid password
    Then click on sign in button
    Then verify that user see error note in case of invalid credentials
    Then enter valid email
    Then enter valid password
    Then click on sign in button for valid credentials
    Then verify that user is at home page

    #App Store
    Then Click on App Store Button on Header
    Then Verify that user is on App Store page
    Then Verify that "All Bigparser Apps" filter is selected By Default
    Then Click on category filter and select "Pre-Installed Apps"
    Then Verify that "Share App" , "Grid App" and "Plug App" widgets appear
    Then Click on Category filter and select "Installed Apps"
    Then Verify that "Drop Box" , "One Drive" and "Google Drive" widgets appear
    Then Click on category filter and select "Uninstalled Apps"
    Then Verify that your uninstalled apps appear
    Then Click on category filter and Select "Pre-Order Apps"
    Then Verify that Pre-Order Apps like "Facebook" , "Skype" , "Gmail" , "LinkedIn" appear
    Then Go back to home page

    #File Uploading
    Then verify that uploading box is present
    Then upload file and Verify its presence

     #Global Search
    Then Enter uploaded file name in search field and verify if it is shown in grids section of My Data tab

    #Cross Sheet search
    Then Open that grid
    Then Enter any related key work in global search bar and press Enter

    #Cross Grid Search
    Then Select Search All Grids
    Then Click search button
    Then Verify that Grids Found text is displayed
    Then close grid

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
    Then Click on more options button
    Then Click on Rename file
    Then Clear edit field and enter new name
    Then Click on Rename button
    Then Verify that Rename confirmation note appears now
    Then click close it
    Then Verify that name has been edited
    Then close grid

    #Public Sharing
    Then Clear search field
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
    Then search name of file you shared
    Then verify that your shared file is present in shared tab
    Then Clear search field

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