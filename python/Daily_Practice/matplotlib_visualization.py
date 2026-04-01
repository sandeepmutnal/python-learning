# Practice Day 19
# Topic: Data Visualization using Matplotlib

import matplotlib.pyplot as plt


# 1️⃣ Line Chart Example

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y)

plt.title("Line Chart Example")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()


# 2️⃣ Bar Chart Example

students = ["Rahul", "Priya", "Amit"]
marks = [85, 90, 88]

plt.bar(students, marks)

plt.title("Student Marks Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()


# 3️⃣ Scatter Plot Example

age = [21, 22, 23, 24]
salary = [20000, 25000, 30000, 35000]

plt.scatter(age, salary)

plt.title("Age vs Salary Scatter Plot")
plt.xlabel("Age")
plt.ylabel("Salary")

plt.show()


# 4️⃣ Save graph as image

plt.plot(x, y)
plt.title("Saved Graph Example")

plt.savefig("my_graph.png")

print("Graph saved successfully!")