import json
from pathlib import Path

import pytest
from playwright.sync_api import Playwright, expect

from Locators.Login_locators import LoginLocators
from Utils.apiBaseFramework import apiUtil
from config.config_reader import ConfigReader
from test_accessCredentialFromJson import credential_list

# config_reader = ConfigReader()
# loginlocator = LoginLocators()
# username= config_reader.getUserName()
# password = config_reader.getPassword()
# base_url = config_reader.getBaseUrl()

filepath = Path(__file__).parent

with open(f"{filepath}/Utils/credentials.json") as file:
    test_data =json.load(file)
    credential_list= test_data["usercredentials"]

@pytest.mark.parametrize("credential", credential_list)
def test_apiValidationFromJson(playwright:Playwright, credential):

    #create order using API and get the token
    api_util = apiUtil()
    orderid = api_util.createOrder(playwright,credential)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/")
    loginLocator = LoginLocators(page)
    loginLocator.login(credential["useremail"], credential["userpassword"])

    page.get_by_role("button", name="  ORDERS").click()
    orderRow= page.locator("tr").filter(has_text=orderid)
    orderRow.get_by_role("button",name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    assert (page.locator(".-main").text_content()==orderid), f"Order id is not matching, expected {orderid} but got {page.locator('.-main').text_content()}"



