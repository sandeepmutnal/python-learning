import os
import json
import sys

# ✅ FIXED PATH (always inside atm-project)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_FILE = os.path.join(DATA_DIR, "account_data.json")

# ✅ Ensure folder exists
os.makedirs(DATA_DIR, exist_ok=True)

# ---------- SAVE ----------
def save_data(data):
    os.makedirs(DATA_DIR, exist_ok=True)  # double safety
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---------- LOAD ----------
def load_data():
    if not os.path.exists(DATA_FILE):
        default_data = {
            "pin": "1234",
            "balance": 10000,
            "history": []
        }
        save_data(default_data)
        return default_data

    with open(DATA_FILE, "r") as f:
        return json.load(f)

data = load_data()

# ---------- FUNCTIONS ----------

def check_balance():
    print(f"\n💰 Balance: ₹{data['balance']}")

def deposit_money():
    try:
        amount = int(input("Enter amount to deposit: ₹"))
        if amount > 0:
            data["balance"] += amount
            data["history"].append(f"Deposited ₹{amount}")
            save_data(data)
            print("✅ Deposited successfully")
        else:
            print("❌ Invalid amount")
    except ValueError:
        print("❌ Numbers only")

def withdraw_money():
    try:
        amount = int(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("❌ Invalid amount")
        elif amount > data["balance"]:
            print("❌ Insufficient balance")
        else:
            data["balance"] -= amount
            data["history"].append(f"Withdrawn ₹{amount}")
            save_data(data)
            print("💵 Collect your cash")
    except ValueError:
        print("❌ Numbers only")

def change_pin():
    old_pin = input("Enter old PIN: ")
    if old_pin == data["pin"]:
        new_pin = input("Enter new PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            data["pin"] = new_pin
            save_data(data)
            print("✅ PIN changed")
        else:
            print("❌ PIN must be 4 digits")
    else:
        print("❌ Wrong PIN")

def show_history():
    print("\n📜 Transaction History:")
    if data["history"]:
        for t in data["history"]:
            print("➡", t)
    else:
        print("No transactions")

# ---------- MAIN ----------

def atm_system():
    attempts = 0

    while attempts < 3:
        pin = input("Enter PIN: ")
        if pin == data["pin"]:
            print("✅ Login successful")
            break
        else:
            attempts += 1
            print(f"❌ Wrong PIN ({attempts}/3)")

    if attempts == 3:
        print("🚫 Card blocked")
        sys.exit()

    while True:
        print("\n====== 🏦 ATM ======")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Change PIN")
        print("5. History")
        print("6. Exit")

        choice = input("Choose: ")

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
            print("🙏 Thank you")
            break
        else:
            print("❌ Invalid option")

# ---------- RUN ----------
if __name__ == "__main__":
    print("📁 Saving to:", DATA_FILE)  # DEBUG
    atm_system()