import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

ORANGEHRM_LOGIN_PAGE = 'https://opensource-demo.orangehrmlive.com/'

# Scenarios
scenarios('../features/VerifyData.feature')


# Fixtures
@pytest.fixture
def browser():
    b = webdriver.Chrome(ChromeDriverManager().install())
    b.implicitly_wait(10)
    yield b
    b.quit()


# Given Steps
@given('User is on OrangeHRM Login Page')
def orange_home(browser):
    browser.get(ORANGEHRM_LOGIN_PAGE)


# Then Steps
@then('Verify the Login Page displayed')
def verify_login_page(browser):
    login_title = browser.title
    assert login_title == "OrangeHRM"


# When Steps
@when('User login using username and password')
def user_logged_in(browser):
    browser.find_element_by_id('txtUsername').send_keys('Admin')
    browser.find_element_by_id('txtPassword').send_keys('admin123')
    browser.find_element_by_id('btnLogin').click()

# Then Steps
@then('User should be successfully navigated to dashboard page')
def user_dashboard_page(browser, phrase):
    links_div = browser.find_element_by_id('links')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    search_input = browser.find_element_by_id('search_form_input')
    assert search_input.get_attribute('value') == phrase


# When Steps
@when(parsers.parse('the user searches for "{phrase}"'))
def search_phrase(browser, phrase):
    search_input = browser.find_element_by_id('search_form_input_homepage')
    search_input.send_keys(phrase + Keys.RETURN)


# Then Steps
@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    links_div = browser.find_element_by_id('links')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    search_input = browser.find_element_by_id('search_form_input')
    assert search_input.get_attribute('value') == phrase


# Then Steps
@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    links_div = browser.find_element_by_id('links')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    search_input = browser.find_element_by_id('search_form_input')
    assert search_input.get_attribute('value') == phrase