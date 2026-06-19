from bank_account import BankAccount

class BankSystem:
    def __init__(self):
        self.accounts = []

    def create_account(self, owner, initial_balance=0.0):
        account = BankAccount(owner, initial_balance)
        self.accounts.append(account)
        return account

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            return account.deposit(amount)
        return False

    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            return account.withdraw(amount)
        return False

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)
        if not from_account or not to_account:
            return False
        if from_account.withdraw(amount):
            to_account.deposit(amount)
            return True
        return False

    def list_accounts(self):
        return self.accounts