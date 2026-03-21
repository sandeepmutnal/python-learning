# Practice Day 07
# Topics: Advanced String Problems

# 1️⃣ Reverse a string (without slicing)
text = "python"

reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print("Reversed:", reversed_text)


# 2️⃣ Count characters frequency
text = "banana"

freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Character frequency:", freq)


# 3️⃣ Remove spaces from string
text = "hello world python"

result = ""

for char in text:
    if char != " ":
        result += char

print("Without spaces:", result)


# 4️⃣ Check palindrome
word = "madam"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")


# 5️⃣ Count vowels and consonants
text = "education"

vowels = "aeiou"
v_count = 0
c_count = 0

for char in text:
    if char in vowels:
        v_count += 1
    else:
        c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)