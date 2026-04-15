# Project 1
# Student Marks Predictor

import pandas as pd
import matplotlib.pyplot as plt


# 1️⃣ Dataset

data = {
    "Study_Hours": [2,4,6,8,10,3,5,7,9],
    "Sleep_Hours": [7,6,6,5,5,7,6,6,5],
    "Attendance": [60,70,80,90,95,65,75,85,92],
    "Marks": [40,50,65,80,95,45,60,75,88]
}

df = pd.DataFrame(data)

print(df)


# 2️⃣ Visualization 1: Study Hours vs Marks

plt.plot(df["Study_Hours"], df["Marks"], marker="o")

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

plt.grid(True)

plt.show()


# 3️⃣ Visualization 2: Attendance vs Marks

plt.plot(df["Attendance"], df["Marks"], marker="o")

plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.title("Attendance vs Marks")

plt.grid(True)

plt.show()