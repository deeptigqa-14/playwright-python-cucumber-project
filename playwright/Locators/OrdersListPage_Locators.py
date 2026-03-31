from playwright.sync_api import Page


class OrdersListPageLocators:
    orders_list_page_title = "h1:has-text('Your Orders')"
    no_Orders_message = ".mt-4"
    def orderPageDisplayed(self,page:Page):
        return page.locator(self.orders_list_page_title).is_visible()
    def clickViewButton_firstOrder(self,page:Page):
        page.get_by_role("button",name="View").first.click()
    def isNoOrdersMsgVisible(self,page:Page):
        return page.locator(self.no_Orders_message).is_visible()