# Project 5
# Customer Churn Prediction

import pandas as pd
from sklearn.linear_model import LogisticRegression


# Dataset

data = {
    "Monthly_Bill": [500, 700, 300, 1000, 1200, 400, 900, 1500],
    "Tenure": [2, 5, 1, 10, 12, 3, 8, 15],
    "Support_Calls": [5, 2, 6, 1, 0, 4, 2, 1],
    "Churn": [1, 0, 1, 0, 0, 1, 0, 0]
}

df = pd.DataFrame(data)

print("Dataset Loaded Successfully ✅\n")
print(df)


# Features and Label

X = df[["Monthly_Bill", "Tenure", "Support_Calls"]]
y = df["Churn"]


# Create Model

model = LogisticRegression()


# Train Model

model.fit(X, y)


# Predict Customer Churn

prediction = model.predict([[800, 3, 5]])

print("\nPrediction Result:")
print(prediction)


# Final Output

if prediction[0] == 1:
    print("⚠️ Customer May Leave")
else:
    print("✅ Customer Will Stay")