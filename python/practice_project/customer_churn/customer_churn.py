# Project 5
# Customer Churn Prediction

import pandas as pd


# Dataset

data = {
    "Monthly_Bill": [500, 700, 300, 1000, 1200, 400, 900, 1500],
    "Tenure": [2, 5, 1, 10, 12, 3, 8, 15],
    "Support_Calls": [5, 2, 6, 1, 0, 4, 2, 1],
    "Churn": [1, 0, 1, 0, 0, 1, 0, 0]
}


df = pd.DataFrame(data)

print("Customer Churn Dataset Loaded Successfully ✅\n")
print(df)