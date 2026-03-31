from playwright.sync_api import Page


class ShoppingPageLocators:

    orders_link = "text='  ORDERS'"
    def clickOrders(self,page:Page):
       # page.get_by_role("Button", self.orders_link).click()
        page.click(self.orders_link)