import pytest
from pytest_bdd import given, when, then, parsers, scenarios

from Locators.Login_locators import LoginLocators
from Locators.ShoppingPage_locators import ShoppingPageLocators
from Utils.apiBaseFramework import apiUtil
from conftest import browserInstance

scenarios('test_pytest-bdd.feature')

@pytest.fixture
def shared_data():
    return {}


@given(parsers.parse('Place the item order with {username} and {password}'))
def place_order(playwright,username, password,shared_data):
    user_credential_list = {"useremail": username, "userpassword": password}
    api_Util = apiUtil()
    orderID = api_Util.createOrder(playwright,browserInstance, user_credential_list)
    shared_data["orderID"] = orderID

@given('user is on login page')
def user_on_loginpage(browserInstance, shared_data):
    page = browserInstance
    loginLocatorpage = LoginLocators(page)
    loginLocatorpage.navigate_to_login_page()
    #loginLocatorpage.login()
    shared_data['login_page'] = loginLocatorpage

@when(parsers.parse('I login to portal with {Username} and {password}'))
def user_login(browserInstance, username, password,shared_data):
    loginpage = shared_data['login_page']
    dashboard= loginpage.login(username, password)
    shared_data["dashboard"] = dashboard

@when('Navigated to order page')
def navigate_to_order_page(browserInstance, shared_data):
    shoppingPage = shared_data["dashboard"]
    order_page=shoppingPage.clickOrders()
    shared_data["orderPage"] = order_page


@when('select orderId')
def select_orderid(browserInstance, shared_data):
    order_id = shared_data["orderID"]
    page = shared_data["orderPage"]
    orderRow = page.locator("tr").filter(has_text=order_id)
    orderRow.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")

@then('validate orderId')
def validate_orderid(browserInstance, shared_data):
   print(shared_data["orderID"])
   # expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")




