# ATM Python Project - Advanced Version

correct_pin = 1234
balance = 10000
attempts = 0
transaction_history = []

# Function to check balance
def check_balance():
    print("Your current balance is:", balance)

# Function to deposit money
def deposit_money():
    global balance
    amount = int(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        transaction_history.append(f"Deposited: {amount}")
        print("Money deposited successfully")
        print("Updated balance:", balance)
    else:
        print("Invalid amount")

# Function to withdraw money
def withdraw_money():
    global balance
    amount = int(input("Enter amount to withdraw: "))
    if amount <= balance and amount > 0:
        balance -= amount
        transaction_history.append(f"Withdrawn: {amount}")
        print("Please collect your cash")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance or invalid amount")

# Function to change PIN
def change_pin():
    global correct_pin
    old_pin = int(input("Enter old PIN: "))
    if old_pin == correct_pin:
        new_pin = int(input("Enter new PIN: "))
        correct_pin = new_pin
        print("PIN changed successfully")
    else:
        print("Incorrect old PIN")

# Function to show transaction history
def show_history():
    if transaction_history:
        print("\nTransaction History:")
        for t in transaction_history:
            print("-", t)
    else:
        print("No transactions yet")

# PIN Verification
while attempts < 3:
    try:
        pin = int(input("Enter your PIN: "))
    except ValueError:
        print("Please enter numbers only")
        continue

    if pin == correct_pin:
        print("PIN verified successfully")
        break
    else:
        attempts += 1
        print("Incorrect PIN")

if attempts == 3:
    print("Card blocked. Too many attempts.")
else:
    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        try:
            choice = int(input("Choose option: "))
        except ValueError:
            print("Invalid input")
            continue

        if choice == 1:
            check_balance()

        elif choice == 2:
            withdraw_money()

        elif choice == 3:
            deposit_money()

        elif choice == 4:
            change_pin()

        elif choice == 5:
            show_history()

        elif choice == 6:
            print("Thank you for using ATM")
            break

        else:
            print("Invalid option")
