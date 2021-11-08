# wallet.py

class InsufficientAmount(Exception):
    pass


class Wallet(object):
    def __init__(self, initial_amount=0, balance=0):
        self.initial_amount=initial_amount
        self.balance=initial_amount

    def spend_cash(self, amount):
        if self.balance<amount: 
            raise(InsufficientAmount)
        else:
            self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount
