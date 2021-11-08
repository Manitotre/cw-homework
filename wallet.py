# wallet.py

class InsufficientAmount(Exception):
    print('Insufficient Amount')
    pass


class Wallet(object):
    def __init__(self, initial_amount=0, balance=0):
        self.initial_amount=initial_amount
        self.balance=initial_amount
        #raise NotImplementedError

    def spend_cash(self, amount):
        if self.balance<amount: 
            raise(InsufficientAmount)
        else:
            self.balance -= amount
            return self.balance
       # raise NotImplementedError

    def add_cash(self, amount):
        self.balance += amount
        return self.balance
        #raise NotImplementedError