import json
from account import Account

class Bank:
    def __init__(self):
        self.accounts = []
        self.next_account_number = 100001
        self.load_accounts()

    def create_account(self, name: str, pin: str):
        account_number = self.next_account_number
        new_account = Account(account_number, name, pin)
        self.accounts.append(new_account)
        self.next_account_number += 1
        self.save_accounts()

        return new_account

    def find_account(self, account_number: int):
        for account in self.accounts:
            if account.account_number == account_number:
                return account

        return None

    def save_accounts(self):
        data = []

        for account in self.accounts:
            data.append({
                "account_number": account.account_number,
                "name": account.name,
                "pin": account.pin,
                "balance": account.balance,
                "transactions": account.transactions
            })

        with open("accounts.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_accounts(self):
        try:
            with open("accounts.json", "r", encoding="utf-8") as file:
                contents = file.read()
        except FileNotFoundError:
            return

        if not contents.strip():
            return

        data = json.loads(contents)

        for item in data:
            account = Account(
                item["account_number"],
                item["name"],
                item["pin"]
            )

            account.balance = item["balance"]
            account.transactions = item["transactions"]

            self.accounts.append(account)

        if self.accounts:
            self.next_account_number = max(
                account.account_number
                for account in self.accounts
            ) + 1