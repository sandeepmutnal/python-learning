import math
import random

# ---------- GLOBAL ----------
history = []
last_result = None
memory = None
last_operation = None

# ---------- BASIC OPERATIONS ----------
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b

def divide(a, b):
    return "❌ Cannot divide by zero" if b == 0 else a / b

def power(a, b): return a ** b

def square_root(a):
    return "❌ Negative number not allowed" if a < 0 else math.sqrt(a)

def percentage(a, b):
    return (a / 100) * b

def minimum(a, b): return min(a, b)
def maximum(a, b): return max(a, b)

# ---------- SCIENTIFIC ----------
def sin(x): return math.sin(math.radians(x))
def cos(x): return math.cos(math.radians(x))

def log(x):
    return "❌ Invalid input" if x <= 0 else math.log10(x)

def factorial(x):
    return "❌ Negative number not allowed" if x < 0 else math.factorial(int(x))

# ---------- EXTRA FEATURES ----------
def random_number(a, b):
    return random.randint(int(a), int(b))

def average(numbers):
    return sum(numbers) / len(numbers)

def even_odd(n):
    return "Even" if int(n) % 2 == 0 else "Odd"

# ---------- HISTORY ----------
def add_to_history(record):
    history.append(record)

def show_history():
    if not history:
        print("📭 No history")
    else:
        print("\n📜 HISTORY")
        print("-" * 30)
        for item in history:
            print(item)

def clear_history():
    history.clear()
    print("🧹 History cleared")

def undo_last():
    if history:
        removed = history.pop()
        print(f"↩️ Removed: {removed}")
    else:
        print("❌ Nothing to undo")

# ---------- FILE SAVE ----------
def save_history():
    with open("calculator_history.txt", "w") as f:
        for item in history:
            f.write(item + "\n")
    print("💾 History saved to file")

def load_history():
    try:
        with open("calculator_history.txt", "r") as f:
            for line in f:
                history.append(line.strip())
        print("📂 History loaded")
    except:
        print("❌ No saved history file")

# ---------- MENU ----------
def menu():
    print("\n" + "="*45)
    print("🧮 ADVANCED CALCULATOR v4")
    print("="*45)

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Percentage")
    print("8. sin(x)")
    print("9. cos(x)")
    print("10. log(x)")
    print("11. Min")
    print("12. Max")

    print("13. Show History")
    print("14. Clear History")
    print("15. Undo Last")

    print("16. Store in Memory")
    print("17. Recall Memory")

    print("18. Repeat Last Operation")

    print("19. Factorial")
    print("20. Random Number")
    print("21. Average")
    print("22. Even / Odd Check")

    print("23. Save History to File")
    print("24. Load History from File")

    print("25. Exit")

# ---------- INPUT ----------
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("❌ Invalid input")

# ---------- MAIN ----------
while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "25":
        print("👋 Goodbye!")
        break

    elif choice == "13":
        show_history()
        continue

    elif choice == "14":
        clear_history()
        continue

    elif choice == "15":
        undo_last()
        continue

    elif choice == "16":
        if last_result is not None:
            memory = last_result
            print(f"💾 Stored: {memory}")
        else:
            print("❌ No result to store")
        continue

    elif choice == "17":
        if memory is not None:
            print(f"📌 Memory: {memory}")
        else:
            print("❌ Memory empty")
        continue

    elif choice == "18":
        if last_operation:
            result = last_operation()
            print("🔁 Result:", result)
            add_to_history(f"Repeat = {result}")
        else:
            print("❌ No operation to repeat")
        continue

    elif choice == "23":
        save_history()
        continue

    elif choice == "24":
        load_history()
        continue

# ---------- SINGLE INPUT ----------
    elif choice in ["6","8","9","10","19","22"]:
        num = get_number("Enter number: ")

        if choice == "6":
            result = square_root(num)
            exp = f"√{num}"

        elif choice == "8":
            result = sin(num)
            exp = f"sin({num})"

        elif choice == "9":
            result = cos(num)
            exp = f"cos({num})"

        elif choice == "10":
            result = log(num)
            exp = f"log({num})"

        elif choice == "19":
            result = factorial(num)
            exp = f"{num}!"

        elif choice == "22":
            result = even_odd(num)
            exp = f"{num}"

        print("Result:", result)
        add_to_history(f"{exp} = {result}")
        last_result = result
        last_operation = lambda: result

# ---------- DOUBLE INPUT ----------
    elif choice in ["1","2","3","4","5","7","11","12","20"]:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            result = add(num1, num2)
            op = "+"

        elif choice == "2":
            result = subtract(num1, num2)
            op = "-"

        elif choice == "3":
            result = multiply(num1, num2)
            op = "*"

        elif choice == "4":
            result = divide(num1, num2)
            op = "/"

        elif choice == "5":
            result = power(num1, num2)
            op = "^"

        elif choice == "7":
            result = percentage(num1, num2)
            op = "% of"

        elif choice == "11":
            result = minimum(num1, num2)
            op = "min"

        elif choice == "12":
            result = maximum(num1, num2)
            op = "max"

        elif choice == "20":
            result = random_number(num1, num2)
            op = "random"

        print("Result:", result)
        add_to_history(f"{num1} {op} {num2} = {result}")
        last_result = result
        last_operation = lambda: result

# ---------- AVERAGE ----------
    elif choice == "21":
        count = int(get_number("How many numbers? "))
        numbers = []

        for i in range(count):
            numbers.append(get_number(f"Number {i+1}: "))

        result = average(numbers)
        print("Average:", result)

        add_to_history(f"Average {numbers} = {result}")
        last_result = result

    else:
        print("❌ Invalid choice")