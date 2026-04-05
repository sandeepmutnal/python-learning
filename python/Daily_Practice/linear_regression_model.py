# Practice Day 23
# First Machine Learning Model: Linear Regression

import pandas as pd
from sklearn.linear_model import LinearRegression


# 1️⃣ Create Dataset

data = {
    "Study_Hours": [2, 4, 6, 8, 10],
    "Marks": [40, 50, 65, 80, 95]
}

df = pd.DataFrame(data)

print("Dataset:\n")
print(df)


# 2️⃣ Split Features and Labels

X = df[["Study_Hours"]]   # Feature
y = df["Marks"]          # Label


# 3️⃣ Create Model

model = LinearRegression()


# 4️⃣ Train Model

model.fit(X, y)


# 5️⃣ Predict Output

prediction = model.predict([[7]])

print("\nPredicted Marks for 7 study hours:")
print(prediction)