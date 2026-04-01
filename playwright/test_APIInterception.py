import time

from playwright.sync_api import Playwright
from Locators.Login_locators import LoginLocators
from Locators.OrdersListPage_Locators import OrdersListPageLocators
from Locators.ShoppingPage_locators import ShoppingPageLocators
from config.config_reader import ConfigReader

config_reader = ConfigReader()
loginlocator = LoginLocators()
shoppingpagelocator = ShoppingPageLocators()
orderlistpagelocator = OrdersListPageLocators()

base_url = config_reader.getBaseUrl()
username= config_reader.getUserName()
password = config_reader.getPassword()


fakeresponse = {"data":[],"message":"No Orders"}
def response_interception(route):
    route.fulfill(json = fakeresponse)
    # for the fake request use route.continue() instead of route.fulfill()
    #route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/somewrongcustomerid")

def test_apiResponseIntercetion(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page= context.new_page()
    page.goto(base_url)
    loginlocator.login(page, username, password)
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",response_interception)
    shoppingpagelocator.clickOrders(page)
    time.sleep(5)
   # assert orderlistpagelocator.orderPageDisplayed(page), "Order page is not displayed"
    #orderlistpagelocator.clickViewButton_firstOrder(page)



