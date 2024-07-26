from behave import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import time




@given('I launch Chrome browser')
def launchbrowser(context):
    context.driver = webdriver.Chrome(executable_path=r'E:\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    context.driver.maximize_window()


@when('I open orange HRM Homepage')
def openhomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(10)

@when('Enter username "{user}" and password "{pwd}"')
def enteruserpwd(context,user,pwd):
    context.driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys(user)
    context.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(pwd)


@when('click on login button')
def loginbutton(context):
    context.driver.find_element_by_xpath("//button[normalize-space()='Login']").click()
    time.sleep(7)


@then('user must successfully login into dashboard page')
def checkloginstatus_success(context):
    try:
        captured_text = context.driver.find_element_by_xpath("//div[@class='oxd-topbar-header-title']").text
        time.sleep(5)
        dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        if captured_text == "Dashboard":
            context.driver.save_screenshot(f"C:\\python-selenium\\pythonProject\\behaveproject\\features\\screenshots\\Success\\success_{dt}.png")
            context.driver.close()
            assert True, "Test Passed"
        else:
            context.driver.save_screenshot(f"C:\\python-selenium\\pythonProject\\behaveproject\\features\\screenshots\\Failures\\failure_{dt}.png")
            context.driver.close()
            assert False, "Test Failed"
    except NoSuchElementException:
        dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        context.driver.save_screenshot(f"C:\\python-selenium\\pythonProject\\behaveproject\\features\\screenshots\\Failures\\failure_{dt}.png")
        context.driver.close()
        assert False, "Test Failed"

@then('user shouldnot successfully login into dashboard page')
def checkloginstatus_failure(context):
    try:
        dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        captured_text = context.driver.find_element_by_xpath("//div[@class='oxd-topbar-header-title']").text
        time.sleep(5)
        if captured_text != "Dashboard":
            context.driver.save_screenshot(f"C:\\python-selenium\\pythonProject\\behaveproject\\features\\screenshots\\Success\\success_{dt}.png")
            context.driver.close()
            assert True, "Test Passed"
        else:
            context.driver.save_screenshot(f"C:\\python-selenium\\pythonProject\\behaveproject\\features\\screenshots\\Failures\\failure_{dt}.png")
            context.driver.close()
            assert False, "Test Failed"
    except NoSuchElementException:
        dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        context.driver.save_screenshot(f"C:\\python-selenium\\pythonProject\\behaveproject\\features\\screenshots\\Success\\success_{dt}.png")
        context.driver.close()
        assert True, "Test Passed"


