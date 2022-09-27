# Created by sbt at 9/26/22
Feature: Testing the Gettop Footer Content and Links

  Scenario: User can View the Footer content and links
    Given open Gettop main page
    Then User can view Best Selling, Latest, Top Rated categories
    Then User can view all products in the footer have price, name, star-rating
    And User can view "Copyright 2021" in footer
    And User can view Footer has button to go back to top
    And User can verify Footer has working links to all product categories
