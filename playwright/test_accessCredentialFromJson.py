import json
from pathlib import Path

import pytest
from playwright.sync_api import Playwright
from Locators.Login_locators import LoginLocators

filepath =  Path(__file__).parent

loginLocator = LoginLocators()

with open(f'{filepath}/Utils/credentials.json') as file:
    test_data = json.load(file)
    credential_list = test_data["usercredentials"]


@pytest.mark.parametrize("usercredentials", credential_list)
def test_getCredntialFromJson(playwright:Playwright, usercredentials):
   browser = playwright.chromium.launch(headless=False)
   context = browser.new_context()
   page= context.new_page()
   print(credential_list)
   page.goto("https://rahulshettyacademy.com/client/")
   loginLocator.login(page, usercredentials["useremail"], usercredentials["userpassword"])
   # page.fill(loginLocator.user_name , credential_list[0]["useremail"])
   # page.fill(loginLocator.password ,credential_list[0]["userpassword"])
   # page.click(loginLocator.login_button)

