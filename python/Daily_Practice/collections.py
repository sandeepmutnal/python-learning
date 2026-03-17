# Practice Day 03
# Topics: Lists, Tuples, Sets, Dictionaries

# 1️⃣ LISTS
numbers = [10, 20, 30, 40, 50]

print("List:", numbers)
print("First element:", numbers[0])

numbers.append(60)
print("After adding:", numbers)

numbers.remove(20)
print("After removing:", numbers)


# 2️⃣ Loop through list
print("\nLooping list:")
for n in numbers:
    print(n)


# 3️⃣ Find sum of list
total = 0
for n in numbers:
    total += n

print("Sum of list:", total)


# 4️⃣ TUPLES (immutable)
my_tuple = (1, 2, 3, 4)

print("\nTuple:", my_tuple)
print("First element:", my_tuple[0])


# 5️⃣ SETS (unique values)
my_set = {1, 2, 3, 3, 4, 4}

print("\nSet (no duplicates):", my_set)

my_set.add(5)
print("After adding:", my_set)


# 6️⃣ DICTIONARY (key-value)
student = {
    "name": "Sandeep",
    "age": 22,
    "course": "Python"
}

print("\nDictionary:", student)
print("Name:", student["name"])

# Add new key
student["city"] = "Shimoga"
print("Updated dictionary:", student)


# 7️⃣ Loop dictionary
print("\nLoop dictionary:")
for key, value in student.items():
    print(key, ":", value)