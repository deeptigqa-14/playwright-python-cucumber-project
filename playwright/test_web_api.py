from playwright.sync_api import Playwright, expect

from Utils.apiBase import apiUtil


def test_apiValidation(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context= browser.new_context()
    page= context.new_page()

    #create order using API and get the token
    api_util = apiUtil()
    orderid = api_util.createOrder(playwright)

    page.goto("https://rahulshettyacademy.com/client/")
    page.locator("#userEmail").fill("deeptigqa@gmail.com")
    page.locator("#userPassword").fill("Pr@ctice2026")
    page.locator("#login").click()

    page.get_by_role("Button", name="  ORDERS").click()
    orderRow= page.locator("tr").filter(has_text=orderid)
    orderRow.get_by_role("button",name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    assert (page.locator(".-main").text_content()==orderid), f"Order id is not matching, expected {orderid} but got {page.locator('.-main').text_content()}"



