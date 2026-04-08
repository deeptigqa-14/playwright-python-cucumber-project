import json
import time
from pathlib import Path
# > pytest --browser_name chrome  -n 3 --tracing on --html=report.html
# trace.playwright.dev location to see the traced zip file, you can open the zip file in the trace viewer and
import pytest
from playwright.sync_api import Playwright, expect
from Locators.Login_locators import LoginLocators
from Locators.OrdersListPage_Locators import OrdersListPageLocators
from Locators.ShoppingPage_locators import ShoppingPageLocators

filepath =  Path(__file__).parent



with open(f'{filepath}/Utils/credentials.json') as file:
    test_data = json.load(file)
    credential_list = test_data["usercredentials"]


@pytest.mark.parametrize("usercredentials", credential_list)
def test_getCredntialFromJson(playwright:Playwright,browserInstance, usercredentials):
    page = browserInstance
    loginLocator = LoginLocators(page)
    shoppingPage = ShoppingPageLocators(page)
    orderListPage = OrdersListPageLocators(page)

    loginLocator.navigate_to_login_page()
    #page.goto("https://rahulshettyacademy.com/client/")
    loginLocator.login(usercredentials["useremail"], usercredentials["userpassword"])
    shoppingPage.clickOrders()
   #time.sleep(5)
    print(orderListPage.orderPageDisplayed())
    assert(orderListPage.orderPageDisplayed()), "Orders page is not displayed"


