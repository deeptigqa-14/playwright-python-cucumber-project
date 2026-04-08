import pytest


@pytest.fixture(scope="session")
def usercredentials(request): #request access global variable and local variable
    return request.param

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Browser to run tests on")
    parser.addoption("--url_name", action="store", default="chrome", help="Browser to run tests on")

# pytest test_accessCredentialFromJson.py --browser_name edge
# pytest test_accessCredentialFromJson.py --browser_name edge --url_name https://rahulshettyacademy.com/client/
@pytest.fixture()
def browserInstance(playwright,request):
    browser_name = request.config.getoption("browser_name")
    url_name = request.config.getoption("url_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    elif browser_name == "edge":
        browser = playwright.chromium.launch(channel="msedge", headless=False)

    context = browser.new_context()
    page = context.new_page()
    #page.goto(url_name)
    yield page
    context.close()
    browser.close()
