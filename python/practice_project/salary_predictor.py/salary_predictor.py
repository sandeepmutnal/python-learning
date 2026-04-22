# Project 2
# Salary Predictor AI Model

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


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


# Create Model

model = LinearRegression()


# Train Model

model.fit(X, y)


# Predict Salary

prediction = model.predict([[5]])

print("\nPredicted Salary for 5 Years Experience:")
print(round(prediction[0], 2), "LPA")