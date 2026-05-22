# Project 7
# Fake News Detection System

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


# Dataset

data = {
    "News": [
        "Government launches new healthcare scheme",
        "Aliens landed in Bangalore yesterday",
        "Scientists discover new medicine for cancer",
        "Actor secretly became king of India",
        "New technology improves solar energy"
    ],

    "Label": [
        "Real",
        "Fake",
        "Real",
        "Fake",
        "Real"
    ]
}


df = pd.DataFrame(data)

print("Dataset Loaded Successfully ✅\n")
print(df)


# Features and Labels

X = df["News"]
y = df["Label"]


# TF-IDF Vectorization

vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)


# Create Model

model = MultinomialNB()


# Train Model

model.fit(X_vectorized, y)


# Test News

test_news = [
    "Aliens attacked India yesterday"
]


# Convert Test News into Numbers

test_vector = vectorizer.transform(test_news)


# Prediction

prediction = model.predict(test_vector)

print("\nPrediction Result:")
print(prediction[0])