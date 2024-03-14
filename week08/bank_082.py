#!/usr/bin/env python3

class BankAccount(object):
        def __init__(self, balance = 0.00):
                self.balance = balance

        def deposit(self, amount):
                self.balance += amount

        def withdraw(self, amount):
                if amount <= self.balance:
                        self.balance -= amount

        def __str__(self):
                return "Your current balance is " + f"{self.balance:.2f}" + " euro"
