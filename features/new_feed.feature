Feature: Create a New Feed with no data

  Scenario: 
     Given I am on the service-periods page and logged in
      When I click on New Feed on the Service-Periods page
      And I click on Save on the New page
      Then the submission fails