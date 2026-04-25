# Project 2
# Salary Predictor GUI App

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import tkinter as tk


# Dataset

data = {
    "Experience": [1,2,3,4,5,6,7,8,9,10],
    "Salary": [2,3,4,5,6.5,7.5,8.5,9.5,10.5,12]
}

df = pd.DataFrame(data)


# Features & Labels

X = df[["Experience"]]
y = df["Salary"]


# Train/Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Train Model

model = LinearRegression()
model.fit(X_train, y_train)


# Prediction Function

def predict_salary():
    try:
        exp = float(entry_exp.get())
        prediction = model.predict([[exp]])
        result_label.config(
            text="Predicted Salary: ₹" + str(round(prediction[0], 2)) + " LPA"
        )
    except:
        result_label.config(text="Please enter valid number")


# GUI Window

window = tk.Tk()
window.title("Salary Predictor AI App")
window.geometry("350x250")


# Input Label

tk.Label(window, text="Years of Experience").pack(pady=5)

entry_exp = tk.Entry(window)
entry_exp.pack()


# Button

tk.Button(
    window,
    text="Predict Salary",
    command=predict_salary
).pack(pady=10)


# Result Label

result_label = tk.Label(window, text="")
result_label.pack()


# Run App

window.mainloop()