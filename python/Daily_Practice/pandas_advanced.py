# Practice Day 18
# Topic: Pandas Advanced Dataset Operations

import pandas as pd
import numpy as np


# 1️⃣ Create dataset with missing values

data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Age": [21, 22, np.nan, 24],
    "Marks": [85, 90, 88, np.nan]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


# 2️⃣ Filtering data

print("\nStudents with Marks > 85:")
print(df[df["Marks"] > 85])


# 3️⃣ Sorting dataset

print("\nSorted by Age:")
print(df.sort_values("Age"))


# 4️⃣ Fill missing values

df["Age"].fillna(df["Age"].mean(), inplace=True)

df["Marks"].fillna(0, inplace=True)

print("\nAfter Filling Missing Values:")
print(df)


# 5️⃣ Drop column example

df.drop("Marks", axis=1, inplace=True)

print("\nAfter Dropping Marks Column:")
print(df)


# 6️⃣ Add new column

df["Passed"] = ["Yes", "Yes", "Yes", "Yes"]

print("\nFinal Dataset:")
print(df)