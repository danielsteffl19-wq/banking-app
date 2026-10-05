import math

from bank import Bank

BOLD = "\033[1m"
WHITE = "\033[97m"
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


def styled(text, color, bold=False):
    return f"{BOLD if bold else ''}{color}{text}{RESET}"


def account_menu(account, bank):
    while True:
        print(f"\n{styled('    ÚČETNÍ MENU', BLUE, bold=True)}")
        print(styled("--------------------", BLUE))
        print(styled("1. Zobrazit zůstatek", WHITE))
        print(styled("2. Vklad", WHITE))
        print(styled("3. Výběr", WHITE))
        print(styled("4. Historie transakcí", WHITE))
        print(styled("5. Odhlásit se", WHITE))
        print(styled("--------------------", BLUE))

        volba = input(styled("Vyber možnost: ", BLUE, bold=True))

        if volba == "1":
            print(f"\n{styled(f'Zůstatek: {account.balance} Kč', GREEN, bold=True)}")

        elif volba == "2":
            try:
                amount = float(input(styled("Zadej částku k vkladu: ", BLUE)))
            except ValueError:
                print(styled("Částka musí být číslo.", RED))
                continue

            if not math.isfinite(amount) or amount <= 0:
                print(styled("Částka musí být větší než 0 Kč.", RED))
                continue

            account.deposit(amount)
            bank.save_accounts()

        elif volba == "3":
            try:
                amount = float(input(styled("Zadej částku k výběru: ", BLUE)))
            except ValueError:
                print(styled("Částka musí být číslo.", RED))
                continue

            if not math.isfinite(amount) or amount <= 0:
                print(styled("Částka musí být větší než 0 Kč.", RED))
                continue

            account.withdraw(amount)
            bank.save_accounts()

        elif volba == "4":
            print(f"\n{styled('Historie transakcí', BLUE, bold=True)}")

            if not account.transactions:
                print(styled("Zatím žádné transakce.", WHITE))
            else:
                for transaction in account.transactions:
                    print(styled(transaction, WHITE))

        elif volba == "5":
            print(f"\n{styled('Odhlášení...', WHITE)}")
            break

        else:
            print(f"\n{styled('Neplatná volba!', RED)}")


def menu(bank: Bank):
    while True:
        print(f"\n{styled('     BANKING APP', BLUE, bold=True)}")
        print(styled("--------------------", BLUE))
        print(styled("1. Vytvořit účet", WHITE))
        print(styled("2. Přihlásit se", WHITE))
        print(styled("3. Konec", WHITE))
        print(styled("--------------------", BLUE))

        volba = input(styled("Vyber možnost: ", BLUE, bold=True))

        if volba == "1":
            print(f"\n{styled('Vytvoření účtu', BLUE, bold=True)}")

            name = input(styled("Zadej jméno: ", BLUE))
            if not name.strip():
                print(styled("Jméno nesmí být prázdné.", RED))
                continue

            pin = input(styled("Zadej PIN: ", BLUE))
            if not pin.isdigit() or len(pin) != 4:
                print(styled("PIN musí obsahovat přesně 4 číslice.", RED))
                continue

            account = bank.create_account(name, pin)
            print(styled(
                f"\nÚčet pro {name} byl vytvořen. \nČíslo účtu: {account.account_number}",
                GREEN,
            ))

        elif volba == "2":
            print(f"\n{styled('Přihlášení', BLUE, bold=True)}")

            try:
                account_number = int(input(styled("Zadej číslo účtu: ", BLUE)))
            except ValueError:
                print(styled("Číslo účtu musí být číslo.", RED))
                continue

            account = bank.find_account(account_number)

            if account is None:
                print(styled("Účet nebyl nalezen.", RED))
            else:
                pin = input(styled("Zadej PIN: ", BLUE))

                if pin == account.pin:
                    print(f"\n{styled(f'Vítej, {account.name}!', GREEN, bold=True)}")
                    account_menu(account, bank)
                else:
                    print(styled("Nesprávný PIN.", RED))

        elif volba == "3":
            print(f"\n{styled('Program ukončen.', WHITE)}")
            break
        else:
            print(f"\n{styled('Neplatná volba!', RED)}")


if __name__ == "__main__":
    bank = Bank()
    menu(bank)