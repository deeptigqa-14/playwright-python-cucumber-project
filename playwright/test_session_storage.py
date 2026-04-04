from playwright.sync_api import Playwright, expect

from Utils.apiBase import apiUtil
from config.config_reader import ConfigReader

config_reader= ConfigReader()
base_url = config_reader.getBaseUrl()
api_util= apiUtil()

def test_intersection_sessionStorage(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context= browser.new_context()
    page = context.new_page()
    sessionToken=api_util.getToken(playwright)

    #Intercepting the session storage and adding token to it(which is generated during login) and then validating the token in the session storage
    #provide javascript code to add token to session storage
    page.add_init_script(f"""localStorage.setItem('token', '{sessionToken}');""")
    page.goto(base_url)
    tokenvalue = page.evaluate("""localStorage.getItem('token')""")
    print(tokenvalue)

    page.get_by_role("button", name="  ORDERS").click()
    assert (page.get_by_text("Your Orders")), "page is not navigated to orders page"