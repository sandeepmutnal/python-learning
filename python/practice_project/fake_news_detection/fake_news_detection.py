# Project 7
# Fake News Detection System

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report


# Dataset

data = {
    "News": [
        "Government launches new healthcare scheme",
        "Aliens landed in Bangalore yesterday",
        "Scientists discover new medicine for cancer",
        "Actor secretly became king of India",
        "New technology improves solar energy",
        "Moon made of chocolate discovered",
        "Doctors develop new heart treatment",
        "Ghost seen driving bus in Mysore"
    ],

    "Label": [
        "Real",
        "Fake",
        "Real",
        "Fake",
        "Real",
        "Fake",
        "Real",
        "Fake"
    ]
}


df = pd.DataFrame(data)

print("Dataset Loaded Successfully ✅\n")
print(df)


# Features and Labels

X = df["News"]
y = df["Label"]


# Train/Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)


# TF-IDF Vectorization

vectorizer = TfidfVectorizer()

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)


# Model

model = MultinomialNB()

model.fit(X_train_vectorized, y_train)


# Predictions

y_pred = model.predict(X_test_vectorized)

print("\nPredictions:")
print(y_pred)


# Accuracy

accuracy = model.score(X_test_vectorized, y_test)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")


# Confusion Matrix

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)


# Classification Report

print("\nClassification Report:")
print(classification_report(y_test, y_pred))