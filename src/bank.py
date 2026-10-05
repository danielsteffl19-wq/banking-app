from account import Account

class Bank:
    def __init__(self):
        self.accounts = []
        self.next_account_number = 100001

    def create_account(self, name: str, pin: str):
        account_number = self.next_account_number
        new_account = Account(account_number, name, pin)
        self.accounts.append(new_account)
        self.next_account_number += 1

        print(f"Účet pro {name} byl úspěšně vytvořen.")
        print(f"Číslo účtu: {account_number}")

        return new_account