Feature: Products




Scenario: Add product to cart list
  Given I want to login in "https://www.saucedemo.com/"
  When Enter the credentials
  |user_name    |password    |
  |standard_user|secret_sauce|
  Then I enter in products section
  When I want to remove products to the cart list
  |products|
  |Sauce Labs Backpack|