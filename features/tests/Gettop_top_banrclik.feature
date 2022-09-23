# Created by sbt at 9/23/22
Feature: Testing the Right and Left arrows on the Top Banner in main page

  Scenario: User can click right and left arrows to see top banners
    Given open Gettop main page
    Then User click top banner right arrow
    And User click top banner left arrow

