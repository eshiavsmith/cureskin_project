Feature: Test shop for name, image, price

  Scenario: Search results page
      Given Open cureskin page
      #Then Verify search results count is 19
      Then Verify name
      Then Verify image
      And Verify price

