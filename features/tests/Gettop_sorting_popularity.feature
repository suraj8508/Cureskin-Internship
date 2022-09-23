# Created by sbt at 9/23/22
Feature: Testing the feature of Sorting by Popularity

  Scenario: User can Sort Product by Popularity
    Given Open the whole product page
    When User selects the sort by popularity
    Then User can click through sorted pages
    And User can reset to default sorting

  Scenario: User opens a web page with products sorted by popularity
    Given Open the products page sorted by popularity
    Then User verifies the correct page opened
