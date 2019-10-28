# Created by ZAWAR-PC at 8/23/2019
Feature:Big Parser Sign In

  Scenario:Verify all possitve and negative test cases
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

    #ProfileSettings

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