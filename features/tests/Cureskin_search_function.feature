# Created by sbt at 7/13/23
Feature: Testing the Search Functionality

  Scenario: User Search for product
    Given Open Cureskin shop Main page
    When User opens the search field
    And Insert cure in search field and click search
    Then User sees 19 products related to cure

  Scenario: User Search for product in Mobile version
    Given Open Cureskin shop Main page
    When User opens the search field in mobile version
    And Insert cure in search field and click search
    Then User sees 19 products related to cure


