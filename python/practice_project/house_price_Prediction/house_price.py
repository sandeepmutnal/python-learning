# Project 4
# House Price Predictor

import pandas as pd
from sklearn.linear_model import LinearRegression


# Dataset

data = {
    "Area": [1000, 1500, 2000, 2500, 3000, 1200, 1800, 2200],
    "Bedrooms": [2, 3, 3, 4, 4, 2, 3, 4],
    "Location_Score": [5, 6, 7, 8, 9, 5, 7, 8],
    "Price": [30, 45, 60, 75, 90, 35, 55, 70]
}

df = pd.DataFrame(data)

print("Dataset Loaded Successfully ✅\n")
print(df)


# Features and Label

X = df[["Area", "Bedrooms", "Location_Score"]]
y = df["Price"]


# Create Model

model = LinearRegression()


# Train Model

model.fit(X, y)


# Predict Price

prediction = model.predict([[2000, 3, 7]])

print("\nPredicted House Price:")
print(round(prediction[0], 2), "Lakhs")