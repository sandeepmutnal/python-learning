# Project 2
# Salary Predictor AI Model (Interactive Version)

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# Dataset

data = {
    "Experience": [1,2,3,4,5,6,7,8,9,10],
    "Salary": [2,3,4,5,6.5,7.5,8.5,9.5,10.5,12]
}

df = pd.DataFrame(data)

print("Dataset Loaded Successfully ✅\n")
print(df)


# Features and Label

X = df[["Experience"]]
y = df["Salary"]


# Train/Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Train Model

model = LinearRegression()
model.fit(X_train, y_train)


# Accuracy Score

accuracy = model.score(X_test, y_test)
print("\nModel Accuracy:", round(accuracy * 100, 2), "%")


# User Input

print("\nEnter Candidate Details:")

experience = float(input("Enter Years of Experience: "))


# Prediction

prediction = model.predict([[experience]])

print("\n🎯 Predicted Salary:", round(prediction[0], 2), "LPA")