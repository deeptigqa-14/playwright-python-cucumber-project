import time
from playwright.sync_api import Page, expect, Playwright  #

def test_playwrightBasics(playwright): # globally available feature which we can use in our test cases need to pass a argument to use it
    # create a browser instance
    browser = playwright.chromium.launch(headless=False) #default is headless mode, to see the browser we need to set headless to false
    context = browser.new_context() # create a new browser context, it is like a new incognito window
    page = context.new_page()   # create a new page in the browser context
    page.goto("https://rahulshettyacademy.com/")

#page fixture is only used for chromium(chrome or edge) browser and in headless mode
#page fixture coming from Page class , if you want to all the methods of Page class you need to import it and use it as a argument in the test case, it will automatically create a page instance for you and you can use it in your test case
def test_playwrightShortcut(page:Page):
    page.goto("https://rahulshettyacademy.com/")


# css locator present with "#id" or ".class" or "tagname[attribute='value']"
def test_corelocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    #page.get_by_role("button", name="Sign in").click()
    expect(page.get_by_text("Empty username/password.")).to_be_visible()

    page.get_by_label("UserName").fill("rahulshettyacademy") # should have a label tag. input tag should be wrapped between the label tag
    page.get_by_label("Password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="Terms and Conditions").click()
    time.sleep(5)
    page.get_by_role("button", name="Sign in").click()

def test_firefoxBrowser(playwright:Playwright):
    firfoxbrowser = playwright.firefox.launch(headless=False)
    context = firfoxbrowser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_role("button", name="Sign in").click()
    expect(page.get_by_text("Empty username/password.")).to_be_visible()

    page.get_by_label("UserName").fill(
        "rahulshettyacademy")  # should have a label tag. input tag should be wrapped between the label tag
    page.get_by_label("Password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="Terms and Conditions").click()
    time.sleep(5)
    page.get_by_role("button", name="Sign in").click()
