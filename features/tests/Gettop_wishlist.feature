# Created by sbt at 9/22/22
Feature:  Testing Wishlist Feature of Gettop website

  Scenario: User can add, share and open product page.
    Given Open Laptop Category Page
    When User adds the product to wishlist
    And User open the wishlist page
    Then Verify product in wishlist
    And User can see Social Logos to share
    And User can open product detail page


  Scenario: User can add and remove product from Wishlist
    Given Open Phones Category Page
    When User adds the product to wishlist
    And User open the wishlist page
    Then Verify product in wishlist
    And User can remove product from Wishlist
    And User Can See Confirmation Message

