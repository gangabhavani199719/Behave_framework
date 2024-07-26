Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with valid parameters
    Given I launch Chrome browser
    When I open orange HRM Homepage
    And Enter username "admin" and password "admin123"
    And click on login button
    Then  user must successfully login into dashboard page


  Scenario Outline: Login to OrangeHRM with multiple parameters
    Given I launch Chrome browser
    When I open orange HRM Homepage
    And Enter username "<username>" and password "<password>"
    And click on login button
    Then  user shouldnot successfully login into dashboard page

    Examples:
      | username | password |
      | admin123 | admin    |
      | adminxyz | admin123 |
      | admin    | adminxyz |
      | Admin    | admin123 |