from account import Account

class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, name: str, pin: str) -> Account:
        new_account = Account(name, pin)
        self.accounts.append(new_account)

        print(f"Účet pro {name} byl úspěšně vytvořen.")

        return new_account