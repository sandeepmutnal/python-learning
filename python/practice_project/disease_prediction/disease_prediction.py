# Project 6
# Disease Prediction System

import pandas as pd
import matplotlib.pyplot as plt


# Dataset

data = {
    "Fever": [1, 1, 0, 1, 0, 0],
    "Cough": [1, 1, 1, 0, 0, 1],
    "Headache": [1, 0, 1, 1, 0, 0],
    "Fatigue": [1, 1, 0, 1, 0, 0],
    "Disease": ["Flu", "Flu", "Cold", "Flu", "Healthy", "Cold"]
}

df = pd.DataFrame(data)

print("Disease Dataset Loaded Successfully ✅\n")
print(df)


# 📊 Visualization 1: Fever vs Disease

plt.scatter(df["Fever"], df["Disease"])

plt.xlabel("Fever (0 = No, 1 = Yes)")
plt.ylabel("Disease")
plt.title("Fever vs Disease")

plt.show()


# 📊 Visualization 2: Cough vs Disease

plt.scatter(df["Cough"], df["Disease"])

plt.xlabel("Cough (0 = No, 1 = Yes)")
plt.ylabel("Disease")
plt.title("Cough vs Disease")

plt.show()


# 📊 Visualization 3: Headache vs Disease

plt.scatter(df["Headache"], df["Disease"])

plt.xlabel("Headache (0 = No, 1 = Yes)")
plt.ylabel("Disease")
plt.title("Headache vs Disease")

plt.show()


# 📊 Visualization 4: Fatigue vs Disease

plt.scatter(df["Fatigue"], df["Disease"])

plt.xlabel("Fatigue (0 = No, 1 = Yes)")
plt.ylabel("Disease")
plt.title("Fatigue vs Disease")

plt.show()