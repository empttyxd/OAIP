from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, balance, owner, account_number):
        self.balance = balance
        self.owner = owner
        self.account_number = account_number

    @abstractmethod
    def calculate_interest(self):
        pass

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            return 'Insufficient funds'

    def __str__(self):
        return f'account {self.account_number} (Owner: {self.owner}) . Balance: {self.balance}. procents:'


class SavingsAccount(BankAccount):
    def __init__(self, balance, owner, account_number):
        super().__init__(balance, owner, account_number)

    def calculate_interest(self):
        return self.balance * 0.05

    def __str__(self):
        return f'{super().__str__()} {self.calculate_interest()}'


class CheckingAccount(BankAccount):
    def __init__(self, balance, owner, account_number):
        super().__init__(balance, owner, account_number)

    def calculate_interest(self):
        return 0

    def __str__(self):
        return f'{super().__str__()} {self.calculate_interest()}'
