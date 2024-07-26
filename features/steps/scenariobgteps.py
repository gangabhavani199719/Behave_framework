from behave import *
@given('I launch browser')
def launchbrowser(context):
    assert True, "Test Passed"


@when('I open application')
def openApplication(context):
    assert True, "Test Passed"


@when('Enter valid username and password')
def passcredentials(context):
    assert True, "Test Passed"


@when('click on Login')
def loginbutton(context):
    assert True, "Test Passed"


@then('User must login to the Dashboard page')
def logindashboard(context):
    assert True, "Test Passed"


@when('navigate to search page')
def opensearchpage(context):
    assert True, "Test Passed"


@then('Search page should display')
def displaySearchpage(context):
    assert True, "Test Passed"


@when('Navigate to advance search page')
def opendvancesearchpage(context):
    assert True, "Test Passed"


@then('advanced search page should display')
def displayadvancesearchpage(context):
    assert True, "Test Passed"
