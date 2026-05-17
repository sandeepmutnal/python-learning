# Project 6
# Disease Prediction System

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report


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


# Features and Label

X = df[["Fever", "Cough", "Headache", "Fatigue"]]
y = df["Disease"]


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

model = DecisionTreeClassifier()

model.fit(X_train, y_train)


# Predictions

y_pred = model.predict(X_test)

print("\nPredictions:")
print(y_pred)


# Accuracy

accuracy = model.score(X_test, y_test)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")


# Confusion Matrix

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)


# Classification Report

print("\nClassification Report:")
print(classification_report(y_test, y_pred))