import time

from playwright.sync_api import Page


class OrdersListPageLocators:
    def __init__(self,page):
        self.page = page

    orders_list_page_title = "h1:has-text('Your Orders')"
    no_Orders_message = ".mt-4"

    def orderPageDisplayed(self) -> bool:
        locator = self.page.locator(self.orders_list_page_title)
        locator.wait_for(state="visible", timeout=10000)
        return locator.is_visible()
    def clickViewButton_firstOrder(self):
        self.page.get_by_role("button",name="View").first.click()
    def isNoOrdersMsgVisible(self):
        return self.page.locator(self.no_Orders_message).is_visible()