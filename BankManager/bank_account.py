import random

class BankAccount:
    def __init__(self, owner, initial_balance=0.0, interest_rate=0.02):
        self.owner = owner
        self.account_number = self._generate_account_number()
        self.balance = float(initial_balance)
        self.interest_rate = interest_rate
        self.transactions = []

    def _generate_account_number(self):
        return str(random.randint(100000, 999999))

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        self.transactions.append(f"Κατάθεση: +{amount:.2f}€")
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        self.transactions.append(f"Ανάληψη: -{amount:.2f}€")
        return True

    def calculate_simple_interest(self, years):
        return self.balance * self.interest_rate * years

    def calculate_compound_interest(self, years):
        return self.balance * (1 + self.interest_rate) ** years

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions