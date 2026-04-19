# Project 1
# Student Marks Predictor GUI App

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import tkinter as tk


# Dataset

data = {
    "Study_Hours": [2,4,6,8,10,3,5,7,9],
    "Sleep_Hours": [7,6,6,5,5,7,6,6,5],
    "Attendance": [60,70,80,90,95,65,75,85,92],
    "Marks": [40,50,65,80,95,45,60,75,88]
}

df = pd.DataFrame(data)


# Features & Labels

X = df[["Study_Hours", "Sleep_Hours", "Attendance"]]
y = df["Marks"]


# Train Test Split

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

def predict_marks():
    
    study = float(entry_study.get())
    sleep = float(entry_sleep.get())
    attendance = float(entry_attendance.get())

    prediction = model.predict([[study, sleep, attendance]])

    result_label.config(
        text="Predicted Marks: " + str(round(prediction[0], 2))
    )


# GUI Window

window = tk.Tk()
window.title("Student Marks Predictor AI App")
window.geometry("350x300")


# Labels

tk.Label(window, text="Study Hours").pack()
entry_study = tk.Entry(window)
entry_study.pack()

tk.Label(window, text="Sleep Hours").pack()
entry_sleep = tk.Entry(window)
entry_sleep.pack()

tk.Label(window, text="Attendance (%)").pack()
entry_attendance = tk.Entry(window)
entry_attendance.pack()


# Predict Button

predict_button = tk.Button(
    window,
    text="Predict Marks",
    command=predict_marks
)

predict_button.pack(pady=10)


# Result Label

result_label = tk.Label(window, text="")
result_label.pack()


# Run App

window.mainloop()