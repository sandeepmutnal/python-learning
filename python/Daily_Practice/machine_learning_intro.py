# Practice Day 22
# Introduction to Machine Learning Dataset Preparation

import pandas as pd


# Example ML Dataset

data = {
    "Study_Hours": [2, 4, 6, 8, 10],
    "Marks": [40, 50, 65, 80, 95]
}

df = pd.DataFrame(data)

print("Dataset:\n")
print(df)


# Features and Labels

X = df[["Study_Hours"]]   # Feature (Input)
y = df["Marks"]          # Label (Output)


print("\nFeatures (Input):")
print(X)


print("\nLabels (Output):")
print(y)