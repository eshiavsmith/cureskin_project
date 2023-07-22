Feature: Test shop for name, image, price

  Scenario: Search results page
      Given Open cureskin page
      Then Verify search results count is 19
      And Verify name
      And Verify image
      And Verify price

