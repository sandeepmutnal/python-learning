# Project 7
# Fake News Detection System

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


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


# TF-IDF Vectorizer

vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)


# Output

print("\nText Converted into Numbers Successfully ✅")

print("\nShape of Data:")
print(X_vectorized.shape)


print("\nFeature Names:")
print(vectorizer.get_feature_names_out())