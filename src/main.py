def menu():
    while True:
        print("\n====================")
        print("     BANKING APP     ")
        print("====================")
        print("1. Vytvořit účet")
        print("2. Přihlásit se")
        print("3. Konec")
        print("====================")

        volba = input("Vyber možnost: ")

        if volba == "1":
            print("\nVytváření účtu...")
        elif volba == "2":
            print("\nPřihlašování...")
        elif volba == "3":
            print("\nProgram ukončen.")
            break
        else:
            print("\nNeplatná volba!")


if __name__ == "__main__":
    menu()
