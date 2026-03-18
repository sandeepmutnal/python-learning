# Practice Day 04
# Topics: Strings, String Methods, Patterns, Logic

# 1️⃣ String Basics
text = "python programming"

print("Original:", text)
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())


# 2️⃣ String Indexing & Slicing
name = "Sandeep"

print("\nFirst letter:", name[0])
print("Last letter:", name[-1])
print("Slice (0-4):", name[0:4])


# 3️⃣ Reverse String
s = "hello"
rev = ""

for char in s:
    rev = char + rev

print("\nReversed string:", rev)


# 4️⃣ Count vowels
text = "education"
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Vowel count:", count)


# 5️⃣ Palindrome Check
word = input("\nEnter a word: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# 6️⃣ Pattern 1
print("\nPattern 1")
for i in range(1, 6):
    print("*" * i)


# 7️⃣ Pattern 2
print("\nPattern 2")
for i in range(5, 0, -1):
    print("*" * i)