Feature: Test shop for name, image, price

  Scenario: Search results page
      Given Open cureskin page
      Then Verify search results count is 19 results found for “cure”
      Then Verify first results have name
      And Verify first results have image
      And Verify first results have price