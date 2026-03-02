# ==================================
# Number Guessing Game - GUI Version (Day 3)
# ==================================

import tkinter as tk
import random
import os

BEST_SCORE_FILE = "best_score.txt"


# -------------------------------
# Load & Save Best Score
# -------------------------------
def load_best_score():
    if os.path.exists(BEST_SCORE_FILE):
        with open(BEST_SCORE_FILE, "r") as file:
            return int(file.read())
    return 0


def save_best_score(score):
    with open(BEST_SCORE_FILE, "w") as file:
        file.write(str(score))


# -------------------------------
# Game Class
# -------------------------------
class GuessingGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Number Guessing Game")
        self.root.geometry("400x400")

        self.best_score = load_best_score()

        self.max_number = 10
        self.max_attempts = 5

        self.secret = random.randint(1, self.max_number)
        self.attempts = 0

        # ---------------- UI ----------------
        self.title_label = tk.Label(root, text="🎯 Guess the Number!", font=("Arial", 16))
        self.title_label.pack(pady=10)

        self.info_label = tk.Label(root, text="Between 1 and 10", font=("Arial", 12))
        self.info_label.pack()

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack()

        self.attempt_label = tk.Label(root, text=f"Attempts left: {self.max_attempts}")
        self.attempt_label.pack()

        self.score_label = tk.Label(root, text=f"Best Score: {self.best_score}")
        self.score_label.pack(pady=5)

        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.restart_button = tk.Button(root, text="Restart", command=self.restart_game)
        self.restart_button.pack(pady=5)

    # -------------------------------
    # Check Guess
    # -------------------------------
    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess == self.secret:
                score = self.max_attempts - self.attempts + 1
                self.result_label.config(text=f"✅ Correct! Score: {score}")

                if score > self.best_score:
                    self.best_score = score
                    save_best_score(score)
                    self.score_label.config(text=f"Best Score: {self.best_score}")

            elif guess < self.secret:
                self.result_label.config(text="📉 Too Low!")
            else:
                self.result_label.config(text="📈 Too High!")

            remaining = self.max_attempts - self.attempts
            self.attempt_label.config(text=f"Attempts left: {remaining}")

            if remaining == 0 and guess != self.secret:
                self.result_label.config(text=f"❌ Game Over! Number was {self.secret}")

        except ValueError:
            self.result_label.config(text="⚠ Enter a valid number!")

    # -------------------------------
    # Restart Game
    # -------------------------------
    def restart_game(self):
        self.secret = random.randint(1, self.max_number)
        self.attempts = 0
        self.result_label.config(text="")
        self.attempt_label.config(text=f"Attempts left: {self.max_attempts}")
        self.entry.delete(0, tk.END)


# -------------------------------
# Run App
# -------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGameGUI(root)
    root.mainloop()