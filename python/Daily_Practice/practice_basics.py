# Practice Day 01
# Topics: Variables, Data Types, Input, Operators, Logic Building

# 1. Variables and Data Types
name = "Sandeep"
age = 22
height = 5.8
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)


# 2. Input / Output
user_name = input("Enter your name: ")
print("Welcome", user_name)


# 3. Operators
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


# 4. Logic Building Question 1
# Check if number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 5. Logic Building Question 2
# Find the largest of two numbers

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x > y:
    print("Largest number:", x)
else:
    print("Largest number:", y)


# 6. Loop Practice
print("Numbers from 1 to 5")

for i in range(1, 6):
    print(i)


# 7. List Practice
numbers = [10, 20, 30, 40]

total = 0
for n in numbers:
    total += n

print("Sum of list:", total)