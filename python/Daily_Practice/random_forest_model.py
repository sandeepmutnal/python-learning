# Practice Day 28
# Random Forest Classification Model

import pandas as pd
from sklearn.ensemble import RandomForestClassifier


# 1️⃣ Create Dataset

data = {
    "Study_Hours": [2, 4, 6, 8, 10],
    "Attendance": [60, 70, 80, 90, 95],
    "Pass": [0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

print("Dataset:\n", df)


# 2️⃣ Split Features and Label

X = df[["Study_Hours", "Attendance"]]
y = df["Pass"]


# 3️⃣ Create Model

model = RandomForestClassifier()


# 4️⃣ Train Model

model.fit(X, y)


# 5️⃣ Predict Result

prediction = model.predict([[7, 85]])

print("\nPrediction (Pass=1, Fail=0):")
print(prediction)