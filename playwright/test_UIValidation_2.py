import time

from playwright.sync_api import Page, expect


def testUICheck1(page:Page):
    #hide / display a placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #Alertboxes
    # before clicking the button we need to define the event handler for the alert box, because when we click
    # the button the alert box will appear and we need to handle it, if we don't handle it then our test case will fail
    page.on("dialog", lambda dialog:dialog.accept()) # to handle the alert box, we need to accept it, if we want to dismiss it then we can use dialog.dismiss())
    page.get_by_role("button", name="Confirm").click()
    time.sleep(5)
    print("confirm clicked")
    page.get_by_role("button", name="Alert").click()
    print("alert clicked")

    #Mouse hover
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()

    time.sleep(5)


    # frame handling
    pageFrame= page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link",name= "All Access Plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy")

    #Check the price of rice in dynamic webtable
    #identify the rice row
    #identify the price column
    #verify if price is 37

    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    riceRow= page.locator("tr").filter(has_text="Rice")

    #for index in range(page.locator("tr").count()):
    colCount = page.locator("th").count()
    for index in range(colCount):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            priceColIndex = index
            break
    print(priceColIndex)
    print(riceRow.locator("td").nth(priceColIndex).text_content())
    assert riceRow.locator("td").nth(priceColIndex).text_content() == "37","Price is not matching"







