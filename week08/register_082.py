#!/usr/bin/env python3

class CashRegister(object):

        def __init__(self, count = 0, total = 0.00):
                self.count = count
                self.total = total

        def add_item(self, price):
                self.count += 1
                self.total += price

        def clear(self):
                self.count = 0
                self.total = 0.00

        def __str__(self):
                return f"Items: {self.count}\nTotal: {self.total:.02f}"
