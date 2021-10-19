Feature: login


  Scenario: Correct login
  Given I want to login in "https://www.saucedemo.com/"
  When Enter the credentials
  |user_name    |password    |
  |standard_user|secret_sauce|
  Then I enter in products section



  Scenario: login without user name
    Given I want to login in "https://www.saucedemo.com/"
  When Enter the credentials
  |user_name    |password    |
  |             |secret_sauce|
  Then Error message must be appear
  |error_message|
  |Epic sadface: Username is required|


  Scenario: login without password
    Given I want to login in "https://www.saucedemo.com/"
  When Enter the credentials
  |user_name    |password    |
  |standard_user|            |
  Then Error message must be appear
  |error_message|
  |Epic sadface: Password is required|

  Scenario: login with wrong password
    Given I want to login in "https://www.saucedemo.com/"
  When Enter the credentials
  |user_name    |password    |
  |standard_user|secret_sau  |
  Then Error message must be appear
  |error_message|
  |Epic sadface: Username and password do not match any user in this service|

  Scenario: login with wrong user
    Given I want to login in "https://www.saucedemo.com/"
  When Enter the credentials
  |user_name    |password    |
  |standard     |secret_sauce|
  Then Error message must be appear
  |error_message|
  |Epic sadface: Username and password do not match any user in this service|

  Scenario: login with wrong user and password
    Given I want to login in "https://www.saucedemo.com/"
  When Enter the credentials
  |user_name    |password    |
  |standard     |secret_sau  |
  Then Error message must be appear
  |error_message|
  |Epic sadface: Username and password do not match any user in this service|


