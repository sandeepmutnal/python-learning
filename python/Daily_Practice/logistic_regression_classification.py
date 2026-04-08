# Practice Day 26
# Logistic Regression Classification Model

import pandas as pd
from sklearn.linear_model import LogisticRegression


# 1️⃣ Create Dataset

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Pass": [0, 0, 0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

print("Dataset:\n", df)


# 2️⃣ Split Features and Label

X = df[["Study_Hours"]]
y = df["Pass"]


# 3️⃣ Create Model

model = LogisticRegression()


# 4️⃣ Train Model

model.fit(X, y)


# 5️⃣ Predict Result

prediction = model.predict([[5]])

print("\nPrediction (Pass=1, Fail=0):")
print(prediction)


# 6️⃣ Probability Prediction

probability = model.predict_proba([[5]])

print("\nPrediction Probability:")
print(probability)