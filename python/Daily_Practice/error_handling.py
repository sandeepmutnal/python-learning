# Practice Day 11
# Topics: Error Handling in Python


# 1️⃣ Basic try-except example

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Invalid input! Please enter a number.")


# 2️⃣ Handling ZeroDivisionError

try:
    a = 10
    b = int(input("Enter divisor: "))
    print("Result:", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero!")


# 3️⃣ Multiple exceptions handling

try:
    num = int(input("Enter number: "))
    result = 10 / num
    print(result)

except ValueError:
    print("Invalid number entered")

except ZeroDivisionError:
    print("Division by zero is not allowed")


# 4️⃣ Using finally block

try:
    print("Opening file...")

    x = 5 / 1

except:
    print("Error occurred")

finally:
    print("Closing program safely")


# 5️⃣ Safe list access example

numbers = [10, 20, 30]

try:
    print(numbers[5])

except IndexError:
    print("Index out of range")