import json
from pathlib import Path

from playwright.sync_api import Playwright

from config.config_reader import ConfigReader
config_reader = ConfigReader()
base_url = config_reader.getBaseUrl()
filepath = Path(__file__).parent

with open(f"{filepath}/orderPayload.json") as file:
    orders = json.load(file)
    print (orders)
    orderpayload = orders["orders"]




class apiUtil:

    def getToken(self, playwright,credential_list):
        api_request_context = playwright.request.new_context(base_url=base_url)
        response = api_request_context.post("/api/ecom/auth/login",
                                 data ={"userEmail": credential_list["useremail"],"userPassword": credential_list["userpassword"]})

        assert response.status == 200, f"Login failed with status code {response.status}"
        responsebody = response.json()
        return responsebody["token"]
       # token = response.json().get("token")
       # assert token is not None, "Token not found in the response"
       # print("Token retrieved successfully:", token)
       # return token

    def createOrder(self, playwright,credential_list):
        token= self.getToken(playwright,credential_list)
        api_request_context = playwright.request.new_context(base_url=base_url)
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data = orders,
                                 headers = {"Content-Type": "application/json", "Authorization": token},)
        print(response.json())
        responseBody = response.json()
        orderid =responseBody["orders"][0]
        return orderid