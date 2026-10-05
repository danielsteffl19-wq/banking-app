class Account:
    def __init__(self, name: str, pin: str):
        self.name: str = name
        self.pin: str = pin
        self.balance: float = 0.0
        self.transactions: list[str] = []

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Vklad: {amount} Kč")
            print(f"Úspěšně vloženo: {amount} Kč")
        else:
            print("Neplatná částka pro vklad.")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Částka musí být větší než 0 Kč.")
        elif amount > self.balance:
            print("Nedostatek prostředků na účtu.")
        else:
            self.balance -= amount
            self.transactions.append(f"Výběr: {amount} Kč")
            print(f"Úspěšně vybráno: {amount} Kč")
            print(f"Zůstatek na účtu: {self.balance} Kč")