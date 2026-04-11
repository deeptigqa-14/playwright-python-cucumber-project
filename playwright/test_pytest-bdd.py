import pytest
from playwright.sync_api import expect
from pytest_bdd import given, when, then, parsers, scenarios

from Locators.Login_locators import LoginLocators
from Locators.OrdersListPage_Locators import OrdersListPageLocators
from Locators.ShoppingPage_locators import ShoppingPageLocators
from Utils.apiBaseFramework import apiUtil
from conftest import browserInstance

scenarios('features/orderTraction.feature')

@pytest.fixture
def shared_data():
    return {}


@given(parsers.parse('Place the item order with {username} and {password}'))
def place_order(playwright,username, password,shared_data):
    user_credential_list = {"useremail": username, "userpassword": password}
    api_Util = apiUtil()
    orderID = api_Util.createOrder(playwright, user_credential_list)
    shared_data["orderID"] = orderID

@given('user is on login page')
def user_on_loginpage(browserInstance, shared_data):
    page = browserInstance
    loginLocatorpage = LoginLocators(page)
    loginLocatorpage.navigate_to_login_page()
    shared_data['login_page'] = loginLocatorpage

@when(parsers.parse('I login to portal with {username} and {password}'))
def user_login(browserInstance,username, password,shared_data):
    loginpage = shared_data['login_page']
    loginpage.login(username, password)
    shopping_page = ShoppingPageLocators(browserInstance)
    shared_data['shopping_page'] = shopping_page



@when('Navigated to order page')
def navigate_to_order_page(browserInstance,shared_data):
    shoppingPage = shared_data["shopping_page"]
    shoppingPage.clickOrders()
    # orderlistPage = OrdersListPageLocators(browserInstance)
    # shared_data["orderPage"] = orderlistPage


@when('select orderId')
def select_orderid(browserInstance,shared_data):
    order_id = shared_data["orderID"]
    orderpage = browserInstance
    orderRow = orderpage.locator("tr").filter(has_text=order_id)
    orderRow.get_by_role("button", name="View").click()
    expect(orderpage.locator(".tagline")).to_have_text("Thank you for Shopping With Us")

@then('Verify order success message shown in detail page')
def validate_orderid(browserInstance, shared_data):
   print(shared_data["orderID"])
   # expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")




