# Project 7
# Fake News Detection System

import pandas as pd


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

print("Fake News Dataset Loaded Successfully ✅\n")
print(df)