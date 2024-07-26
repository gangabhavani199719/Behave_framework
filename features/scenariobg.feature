Feature: OrangeHRM Login

  Background: Common steps
    Given I launch browser
    When I open application
    And Enter valid username and password
    And click on Login

  @smoke
  Scenario: Login to OrangeHRM application
    Then User must login to the Dashboard page
  @smoke
  Scenario: Search User
    When navigate to search page
    Then Search page should display
  @sanity
  Scenario: Advance Search User
    When Navigate to advance search page
    Then advanced search page should display
