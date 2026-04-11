from playwright.sync_api import Page


class LoginLocators:

    def __init__(self,page):
        self.page = page
    user_name = "#userEmail"
    password = "#userPassword"
    login_button = "#login"


    def navigate_to_login_page(self):
        self.page.goto("https://rahulshettyacademy.com/client/")

    def login(self,user_email,pwd):
        self.page.fill(self.user_name,user_email)
        self.page.fill(self.password,pwd)
        self.page.click(self.login_button)

