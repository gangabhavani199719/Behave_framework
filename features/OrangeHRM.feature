Feature:OrangeHRM Logo
  Scenario: Logo presence on OrangeHRM home page
    Given launch chrome browser
    When open orange hrm homepage
    Then verify that the logo present on page
    And  close browser

#to install allure
#Open PowerShell Without Administrator Privileges
  #Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
#iwr -useb get.scoop.sh | iex
#scoop install allure
#allure --version



#NOTE : TO generate reports for particular feature which will give in json format
# behave -f allure_behave.formatter:AllureFormatter -o reports/ features/OrangeHRM.feature
  # to generate in html format
  # allure serve reports/

  #NOTE: to run only particular scenario in the feature
  #behave --tags=@smoke
