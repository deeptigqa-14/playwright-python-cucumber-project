from playwright.sync_api import Page


class ShoppingPageLocators:
    def __init__(self, page):
        self.page = page

    orders_link = "text='  ORDERS'"

    def clickOrders(self):
       # page.get_by_role("Button", self.orders_link).click()
        self.page.click(self.orders_link)