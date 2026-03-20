# Practice Day 06
# Topics: Lists Advanced + Logic Building

# 1️⃣ Reverse a list
nums = [1, 2, 3, 4, 5]

reversed_list = []
for i in range(len(nums)-1, -1, -1):
    reversed_list.append(nums[i])

print("Reversed list:", reversed_list)


# 2️⃣ Find largest and smallest
nums = [10, 5, 20, 8, 15]

largest = nums[0]
smallest = nums[0]

for n in nums:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print("Largest:", largest)
print("Smallest:", smallest)


# 3️⃣ Remove duplicates
nums = [1, 2, 2, 3, 4, 4, 5]

unique = []
for n in nums:
    if n not in unique:
        unique.append(n)

print("Without duplicates:", unique)


# 4️⃣ Find second largest
nums = [10, 20, 4, 45, 99]

largest = second = -9999

for n in nums:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print("Second largest:", second)


# 5️⃣ Count frequency
nums = [1,1,2,3,3,3,4]

freq = {}

for n in nums:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1

print("Frequency:", freq)


# 6️⃣ Merge two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged = list1 + list2
print("Merged list:", merged)