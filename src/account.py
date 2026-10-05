import math


BOLD = "\033[1m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


def styled(text: str, color: str, bold: bool = False) -> str:
    return f"{BOLD if bold else ''}{color}{text}{RESET}"


class Account:
    def __init__(self, account_number: int, name: str, pin: str):
        self.name: str = name
        self.pin: str = pin
        self.balance: float = 0.0
        self.transactions: list[str] = []
        self.account_number: int = account_number

    def deposit(self, amount: float):
        if math.isfinite(amount) and amount > 0:
            self.balance += amount
            self.transactions.append(f"Vklad: {amount} Kč")
            print(styled(f"Úspěšně vloženo: {amount} Kč", GREEN))
        else:
            print(styled("Neplatná částka pro vklad.", RED))

    def withdraw(self, amount: float):
        if not math.isfinite(amount) or amount <= 0:
            print(styled("Částka musí být větší než 0 Kč.", RED))
        elif amount > self.balance:
            print(styled("Nedostatek prostředků na účtu.", RED))
        else:
            self.balance -= amount
            self.transactions.append(f"Výběr: {amount} Kč")
            print(styled(f"Úspěšně vybráno: {amount} Kč", GREEN))
            print(styled(f"Zůstatek na účtu: {self.balance} Kč", GREEN, bold=True))