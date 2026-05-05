# Project 4
# House Price Predictor

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


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


# Train/Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data:", len(X_train))
print("Testing Data:", len(X_test))


# Model

model = LinearRegression()
model.fit(X_train, y_train)


# Predictions

y_pred = model.predict(X_test)

print("\nTest Predictions:")
print(y_pred)


# Accuracy (R² Score)

accuracy = model.score(X_test, y_test)

print("\nModel Accuracy (R²):", round(accuracy, 2))


# Predict New House

new_prediction = model.predict([[2000, 3, 7]])

print("\nPredicted Price for Sample House:")
print(round(new_prediction[0], 2), "Lakhs")