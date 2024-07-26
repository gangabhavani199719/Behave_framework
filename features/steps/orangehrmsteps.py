from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

@given('launch chrome browser')
def launchbrowser(context):
    context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    context.driver.maximize_window()


@when('open orange hrm homepage')
def openhomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(5)


@then('verify that the logo present on page')
def verifylogo(context):
    status=context.driver.find_element_by_xpath("//img[@alt='company-branding']").is_displayed()
    assert status is True

@then('close browser')
def closebrowser(context):
    context.driver.close()
