Feature: New Feed

  Scenario: Creating a New Feed with no data
     Given I am on the service-periods page and logged in
      When I click on New Feed on the Service-Periods page
      And I click on Save on the New page
      Then the submission fails

  Scenario Outline: Creating a New Feed
  	 Given I am on the service-periods page and logged in
  	  When I click on New Feed on the Service-Periods page
  	  And I fill in "<fields>" with new "<data>"
  	  Examples:
  	      | fields        | data           |
  	      | Feed Name     | SomeNewFeed    |
  	      | Publisher     | NewPublisher   |
  	  And I click Save on the New Page
  	  Then the submission succeeds

  Scenario: Exiting the New Feed form
  	Given I am on the New Feed page
  	 When I click on Cancel
  	 Then I am prompted that I will lose progress on my form