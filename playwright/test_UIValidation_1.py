import time

from playwright.sync_api import Page, expect


def test_UIValidationDynamiccript(page:Page):
    # iphone X, Nokia Edge--> Verify 2 items as showing in cart
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("UserName").fill("rahulshettyacademy")  # should have a label tag. input tag should be wrapped between the label tag
    page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="Terms and Conditions").click()
    page.get_by_role("button", name="Sign in").click()
    time.sleep(5)
    iphoneproduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneproduct.get_by_role("button").click()
    nokiaproduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaproduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body"),"Count is not matching.").to_have_count(3)  # to verify the number of items in the cart, it should be 2 because we added 2 items in the cart
    time.sleep(5)

def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newpage:
        page.locator(".blinkingText").filter(has_text="Free Access to InterviewQues").click()
        childpage = newpage.value
        childpage.wait_for_load_state()
        text=childpage.locator(".red").text_content()
        print(childpage.title() + "----" + text)
        words = text.split(" ")
        assert "mentor@rahulshettyacademy.com" in words
        for word in words:
            if "@" in word:
                email= word
                print(email)
        assert email == "mentor@rahulshettyacademy.com" ,"Email is not matching"
