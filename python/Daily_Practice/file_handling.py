# Practice Day 12
# Topics: File Handling in Python


# 1️⃣ Write file (creates file if not exists)

file = open("sample.txt", "w")

file.write("Hello Python\n")
file.write("Learning file handling")

file.close()

print("File written successfully")


# 2️⃣ Read file

file = open("sample.txt", "r")

content = file.read()

print("\nFile content:")
print(content)

file.close()


# 3️⃣ Append file (adds new content)

file = open("sample.txt", "a")

file.write("\nAppending new line")

file.close()

print("\nContent appended successfully")


# 4️⃣ Read file line by line

file = open("sample.txt", "r")

for line in file:
    print(line.strip())

file.close()


# 5️⃣ Safe file handling using with statement

with open("sample.txt", "r") as file:
    content = file.read()
    print("\nReading using with statement:")
    print(content)