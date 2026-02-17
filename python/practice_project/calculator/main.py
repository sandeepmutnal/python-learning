# Advanced Python CLI Calculator

import math
from datetime import datetime

# ---------- GLOBAL HISTORY ----------
history = []

# ---------- FUNCTIONS ----------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a % b

def power(a, b):
    return a ** b

def floor_division(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a // b

def square_root(a):
    if a < 0:
        return "Error: Cannot take square root of negative number"
    return math.sqrt(a)

# ---------- HISTORY FUNCTIONS ----------

def add_to_history(record):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append(f"[{timestamp}] {record}")

def show_history():
    if not history:
        print("📭 No calculations yet.")
    else:
        print("\n📜 --- Calculation History ---")
        for item in history:
            print(item)

def clear_history():
    history.clear()
    print("🗑️ History cleared successfully!")

def save_history_to_file():
    with open("history.txt", "w") as file:
        for item in history:
            file.write(item + "\n")
    print("💾 History saved to history.txt")

# ---------- MENU FUNCTION ----------

def show_menu():
    print("\n--- CALCULATOR MENU ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Power")
    print("7. Floor Division")
    print("8. Square Root")
    print("9. View History")
    print("10. Clear History")
    print("11. Save History to File")
    print("12. Exit")

# ---------- MAIN PROGRAM ----------

print("=================================")
print("🧮 Welcome to Advanced CLI Calculator 🧮")
print("=================================")

while True:
    show_menu()

    try:
        choice = int(input("Enter your choice (1-12): "))

        if choice == 12:
            print("👋 Goodbye!")
            break

        if choice not in range(1, 13):
            print("❌ Invalid choice. Try again.")
            continue

        if choice == 9:
            show_history()
            continue

        if choice == 10:
            clear_history()
            continue

        if choice == 11:
            save_history_to_file()
            continue

        if choice == 8:
            num = float(input("Enter number: "))
            result = square_root(num)
            print("Result:", result)
            add_to_history(f"√{num} = {result}")

        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                result = add(num1, num2)
                operation = f"{num1} + {num2}"
            elif choice == 2:
                result = subtract(num1, num2)
                operation = f"{num1} - {num2}"
            elif choice == 3:
                result = multiply(num1, num2)
                operation = f"{num1} * {num2}"
            elif choice == 4:
                result = divide(num1, num2)
                operation = f"{num1} / {num2}"
            elif choice == 5:
                result = modulus(num1, num2)
                operation = f"{num1} % {num2}"
            elif choice == 6:
                result = power(num1, num2)
                operation = f"{num1} ^ {num2}"
            elif choice == 7:
                result = floor_division(num1, num2)
                operation = f"{num1} // {num2}"

            print("Result:", result)
            add_to_history(f"{operation} = {result}")

    except ValueError:
        print("❌ Please enter valid numbers.")
