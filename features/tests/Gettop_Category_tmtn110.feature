# Created by sbt at 9/19/22
Feature: Testing the Gettop Category products name and price visible , adding to cart from quick view

  Scenario: User can click through all Categories
    Given open Gettop main page
    When User select category and verify correct category displayed
    Then Verify showing all N results reflects correct count of items
    Then Verify all items have Category, Name and Price
#
  Scenario: User can Open and  Close Quick view of Products
    Given Open Gettop main page
    When User select category and verify correct category displayed
    Then Verify user can open and Close the Quick View

  Scenario: User can Open and Add Prod to Cart from Quick view
    Given Open Phone Category Page
    Then Verify user can add product to cart from Quick View