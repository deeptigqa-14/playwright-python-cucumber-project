import configparser
import json
from pathlib import Path

from playwright.sync_api import Playwright

from config.config_reader import ConfigReader
config_reader = ConfigReader()
base_url = config_reader.getBaseUrl()

def getLoginPayload(filename: str ) -> dict:
    #print("SWD:",os.getcwd())
    filepath = Path(__file__).parent / filename
    file= filepath.open("r", encoding="utf-8")
    #with filepath.open("r", encoding="utf-8") as file:
    return json.load(file)

orderpayload = {"orders": [{"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}
loginpayload = getLoginPayload("loginpayload.json")
    #{"userEmail":"deeptigqa@gmail.com","userPassword":"Pr@ctice2026"}





class apiUtil:

    def getToken(self, playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url=base_url)
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
        api_request_context = playwright.request.new_context(base_url=base_url)
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data = orderpayload,
                                 headers = {"Content-Type": "application/json", "Authorization": token},)
        print(response.json())
        responseBody = response.json()
        orderid =responseBody["orders"][0]
        return orderid