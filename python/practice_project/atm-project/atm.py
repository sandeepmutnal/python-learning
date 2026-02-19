# ==========================================
# 💳 ATM Python Project - Advanced Version
# ==========================================

import sys

# ---------- GLOBAL VARIABLES ----------
correct_pin = "1234"
balance = 10000
attempts = 0
transaction_history = []

# ---------- FUNCTIONS ----------

def check_balance():
    print(f"\n💰 Your current balance is: ₹{balance}")


def deposit_money():
    global balance
    try:
        amount = int(input("Enter amount to deposit: ₹"))
        if amount > 0:
            balance += amount
            transaction_history.append(f"Deposited ₹{amount}")
            print("✅ Money deposited successfully")
            print(f"Updated balance: ₹{balance}")
        else:
            print("❌ Enter a valid amount")
    except ValueError:
        print("❌ Please enter numbers only")


def withdraw_money():
    global balance
    try:
        amount = int(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("❌ Invalid amount")
        elif amount > balance:
            print("❌ Insufficient balance")
        else:
            balance -= amount
            transaction_history.append(f"Withdrawn ₹{amount}")
            print("💵 Please collect your cash")
            print(f"Remaining balance: ₹{balance}")
    except ValueError:
        print("❌ Please enter numbers only")


def change_pin():
    global correct_pin
    old_pin = input("Enter old PIN: ")
    if old_pin == correct_pin:
        new_pin = input("Enter new PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            correct_pin = new_pin
            print("✅ PIN changed successfully")
        else:
            print("❌ PIN must be 4 digits")
    else:
        print("❌ Incorrect old PIN")


def show_history():
    print("\n📜 Transaction History:")
    if transaction_history:
        for t in transaction_history:
            print("➡", t)
    else:
        print("No transactions yet")


def save_history_to_file():
    with open("transactions.txt", "w") as f:
        for t in transaction_history:
            f.write(t + "\n")


# ---------- MAIN ATM SYSTEM ----------

def atm_system():
    global attempts

    # PIN Verification
    while attempts < 3:
        pin = input("Enter your PIN: ")

        if not pin.isdigit():
            print("❌ Please enter numbers only")
            continue

        if pin == correct_pin:
            print("✅ PIN verified successfully")
            break
        else:
            attempts += 1
            print(f"❌ Incorrect PIN ({attempts}/3)")

    if attempts == 3:
        print("🚫 Card blocked. Too many attempts.")
        sys.exit()

    # ATM MENU
    while True:
        print("\n======= 🏦 ATM MENU =======")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            withdraw_money()

        elif choice == "3":
            deposit_money()

        elif choice == "4":
            change_pin()

        elif choice == "5":
            show_history()

        elif choice == "6":
            save_history_to_file()
            print("🙏 Thank you for using ATM")
            break

        else:
            print("❌ Invalid option. Try again.")


# ---------- RUN PROGRAM ----------
if __name__ == "__main__":
    atm_system()
