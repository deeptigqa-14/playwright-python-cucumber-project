from playwright.sync_api import Page #

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