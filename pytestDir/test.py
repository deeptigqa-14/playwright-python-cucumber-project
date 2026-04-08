#!/bin/python3

import math
import os
import random
import re
import sys


class VendingMachine:
    # Implement the VendingMachine here
    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price

    def buy(self, req_items, money):
        totalamount = req_items * self.item_price
        if self.num_items >= req_items and money >= totalamount:
            self.num_items = self.num_items - req_items
        elif self.num_items < req_items:
            raise ValueError("Not enough items in the machine")
        elif money < totalamount:
            raise ValueError("Not enough coins")

        return money - totalamount

    pass


if __name__ == '__main__':
    fptr = open("../playwright/test.txt", 'w')

    print("Enter the number of items and the price of each item:")
    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    print("Enter how many times you want to run the test cases:")
    n = int(input())
    for _ in range(n):
        print(" req item and money")
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            print(str(change) + "\n")
        except ValueError as e:
            print(str(e) + "\n")

    fptr.close()
