from bank import Bank

def account_menu(account, bank):
    while True:
        print("\n====================")
        print("    ÚČETNÍ MENU")
        print("====================")
        print("1. Zobrazit zůstatek")
        print("2. Vklad")
        print("3. Výběr")
        print("4. Historie transakcí")
        print("5. Odhlásit se")
        print("====================")

        volba = input("Vyber možnost: ")

        if volba == "1":
            print(f"\nZůstatek: {account.balance} Kč")

        elif volba == "2":
            try:
                amount = float(input("Zadej částku k vkladu: "))
            except ValueError:
                print("Částka musí být číslo.")
                continue

            if amount <= 0:
                print("Částka musí být větší než 0 Kč.")
                continue

            account.deposit(amount)
            bank.save_accounts()

        elif volba == "3":
            try:
                amount = float(input("Zadej částku k výběru: "))
            except ValueError:
                print("Částka musí být číslo.")
                continue

            if amount <= 0:
                print("Částka musí být větší než 0 Kč.")
                continue

            account.withdraw(amount)
            bank.save_accounts()

        elif volba == "4":
            print("\n--- Historie transakcí ---")

            if not account.transactions:
                print("Zatím žádné transakce.")
            else:
                for transaction in account.transactions:
                    print(transaction)

        elif volba == "5":
            print("\nOdhlášení...")
            break

        else:
            print("\nNeplatná volba!")

def menu(bank: Bank):
    while True:
        print("\n====================")
        print("     BANKING APP")
        print("====================")
        print("1. Vytvořit účet")
        print("2. Přihlásit se")
        print("3. Konec")
        print("====================")

        volba = input("Vyber možnost: ")

        if volba == "1":
            print("\n--- Vytvoření účtu ---")

            name = input("Zadej jméno: ")
            if not name.strip():
                print("Jméno nesmí být prázdné.")
                continue

            pin = input("Zadej PIN: ")
            if not pin.isdigit() or len(pin) != 4:
                print("PIN musí obsahovat přesně 4 číslice.")
                continue

            bank.create_account(name, pin)

        elif volba == "2":
            print("\n--- Přihlášení ---")

            try:
                account_number = int(input("Zadej číslo účtu: "))
            except ValueError:
                print("Číslo účtu musí být číslo.")
                continue

            account = bank.find_account(account_number)

            if account is None:
                print("Účet nebyl nalezen.")
            else:
                pin = input("Zadej PIN: ")

                if pin == account.pin:
                    print(f"\nVítej, {account.name}!")
                    account_menu(account, bank)
                else:
                    print("Nesprávný PIN.")

        elif volba == "3":
            print("\nProgram ukončen.")
            break
        else:
            print("\nNeplatná volba!")

if __name__ == "__main__":
    bank = Bank()
    menu(bank)