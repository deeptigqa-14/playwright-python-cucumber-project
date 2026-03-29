from playwright.sync_api import Page


class LoginLocators:
    user_name = "#userEmail"
    password = "#userPassword"
    login_button = "#login"

    def login(self,page:Page,user_email,pwd):
        page.fill(self.user_name,user_email)
        page.fill(self.password,pwd)
        page.click(self.login_button)

