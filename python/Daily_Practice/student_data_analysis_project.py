# Practice Day 20
# Mini Project: Student Data Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1️⃣ Create Dataset

data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Kiran"],
    "Math": [85, 90, 78, np.nan, 88],
    "Science": [92, 88, 80, 79, np.nan],
    "English": [75, 85, 82, 88, 90]
}

df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)


# 2️⃣ Handle Missing Values

df["Math"].fillna(df["Math"].mean(), inplace=True)
df["Science"].fillna(df["Science"].mean(), inplace=True)

print("\nAfter Handling Missing Values:\n")
print(df)


# 3️⃣ Add Total Marks Column

df["Total"] = df["Math"] + df["Science"] + df["English"]

print("\nDataset with Total Marks:\n")
print(df)


# 4️⃣ Add Average Marks Column

df["Average"] = df["Total"] / 3

print("\nDataset with Average Marks:\n")
print(df)


# 5️⃣ Find Top Scorer

top_student = df[df["Total"] == df["Total"].max()]

print("\nTop Scorer:\n")
print(top_student)


# 6️⃣ Statistical Summary

print("\nDataset Summary:\n")
print(df.describe())


# 7️⃣ Visualization (Bar Chart)

plt.bar(df["Name"], df["Total"])

plt.title("Student Total Marks")
plt.xlabel("Students")
plt.ylabel("Total Marks")

plt.show()


# 8️⃣ Save Dataset

df.to_csv("student_analysis_output.csv", index=False)

print("\nDataset saved successfully!")