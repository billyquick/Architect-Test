Feature: New Feed

    Scenario Outline: Components
        Given I load the website
        And I am logged in
        When I go to the "New Feed" page
        Then I see this component "<buttons>"
        Examples:
            | buttons           |
            | Cancel            |
            | Save              |

    Scenario: Cancel New Feed creation
        Given I load the website
        When I go to "New Feed" page
        Then Clicking on Cancel should prompt user

    Scenario Outline: Creating a New Feed
        Given I load the website
        When I go to "New Feed" page
        And I fill "<fields>" with valid "<data>"
        Examples:
            | fields          | data          |
            | Feed Name       | NewFeed       |
            | Publisher Name  | NewPublisher  |
            | URL             | New.URL       |
            | Language        | es            |
        Then I click Save