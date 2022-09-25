# Created by sbt at 9/25/22
Feature: Testing Price Sliding Filter - No Match

  Scenario: "No products were found matching your selection." message shown on no match with selected filters
    Given Open Accessories Category Page
    When User sets the same price for maximum and minimum range and click filter button
    Then User get the message "No products were found matching your selection."
    Then User resets the filter to view all the products