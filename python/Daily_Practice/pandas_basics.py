# Practice Day 17
# Topic: Pandas Basics (Dataset Handling)

import pandas as pd


# 1️⃣ Create Series

numbers = pd.Series([10, 20, 30, 40])

print("Series:")
print(numbers)


# 2️⃣ Create DataFrame

data = {
    "Name": ["Rahul", "Priya", "Amit"],
    "Age": [21, 22, 23],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)


# 3️⃣ Select column

print("\nNames column:")
print(df["Name"])


# 4️⃣ Select row

print("\nFirst row:")
print(df.loc[0])


# 5️⃣ Dataset information

print("\nDataset Info:")
print(df.info())


# 6️⃣ Statistical summary

print("\nSummary:")
print(df.describe())


# 7️⃣ Add new column

df["Passed"] = ["Yes", "Yes", "Yes"]

print("\nUpdated DataFrame:")
print(df)


# 8️⃣ Save dataset to CSV file

df.to_csv("students.csv", index=False)

print("\nCSV file saved successfully!")