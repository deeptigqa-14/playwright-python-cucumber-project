from playwright.sync_api import Playwright

from config.config_reader import ConfigReader

config_reader = ConfigReader()

base_url = config_reader.getBaseUrl()

def test_apiIntercetion(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page= context.new_page()
    page.goto(base_url)

