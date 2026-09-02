balance = 10000


def check_balance():
    print("Current balance: ₹", balance)


def deposit_money():
    global balance

    amount = float(input("Enter deposit amount: "))

    if amount > 0:
        balance = balance + amount
        print("Money deposited successfully.")
        print("New balance: ₹", balance)
    else:
        print("Invalid amount.")


def withdraw_money():
    global balance

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount.")

    elif amount > balance:
        print("Insufficient balance.")

    else:
        balance = balance - amount
        print("Please collect your cash.")
        print("Remaining balance: ₹", balance)


def display_menu():
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")


def atm():
    while True:

        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit_money()

        elif choice == "3":
            withdraw_money()

        elif choice == "4":
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice. Please try again.")


atm()