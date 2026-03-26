from playwright.sync_api import Playwright

orderpayload = {"orders": [{"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}
loginpayload = {"userEmail":"deeptigqa@gmail.com","userPassword":"Pr@ctice2026"}

class apiUtil:

    def getToken(self, playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client/")
        response = api_request_context.post("/api/ecom/auth/login",
                                 data = loginpayload)

        assert response.status == 200, f"Login failed with status code {response.status}"
        responsebody = response.json()
        return responsebody["token"]
       # token = response.json().get("token")
       # assert token is not None, "Token not found in the response"
       # print("Token retrieved successfully:", token)
       # return token

    def createOrder(self, playwright:Playwright):
        token= self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client/")
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data = orderpayload,
                                 headers = {"Content-Type": "application/json", "Authorization": token},)
        print(response.json())
        responseBody = response.json()
        orderid =responseBody["orders"][0]
        return orderid