# Created by sbt at 9/19/22
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can click through all Categories
    Given open Gettop main page
    When User select category and verify correct category displayed
    Then Verify showing all N results reflects correct count of items
    Then Verify all items have Category, Name and Price
#
  Scenario: User can Open, Close and Add Prod to Cart from Quick view
    Given Open Gettop main page
    When User select category and verify correct category displayed
    Then Verify user can open and Close the Quick View
    Then Verify user can add product to cart from Quick View