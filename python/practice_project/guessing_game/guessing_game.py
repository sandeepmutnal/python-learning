# ==================================
# Advanced GUI Number Guessing Game (Day 4 - Improved)
# ==================================

import tkinter as tk
from tkinter import ttk
import random
import os

BEST_SCORE_FILE = "best_score.txt"


# -------------------------------
# File Handling
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
class AdvancedGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Advanced Guessing Game")
        self.root.geometry("450x520")
        self.root.configure(bg="#f0f4f8")

        self.best_score = load_best_score()
        self.wins = 0
        self.losses = 0

        self.timer_id = None
        self.game_active = True

        self.create_widgets()
        self.start_game()

    # ---------------- UI ----------------
    def create_widgets(self):
        tk.Label(self.root, text="🎯 Guess the Number", font=("Arial", 18, "bold"), bg="#f0f4f8").pack(pady=10)

        tk.Label(self.root, text="Select Difficulty", bg="#f0f4f8").pack()
        self.difficulty = ttk.Combobox(self.root, values=["Easy", "Medium", "Hard"], state="readonly")
        self.difficulty.current(0)
        self.difficulty.pack(pady=5)

        self.info_label = tk.Label(self.root, text="", bg="#f0f4f8", font=("Arial", 11))
        self.info_label.pack()

        self.timer_label = tk.Label(self.root, text="⏱ Time: 30", font=("Arial", 12, "bold"), bg="#f0f4f8")
        self.timer_label.pack()

        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda event: self.check_guess())  # Enter key support

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12), bg="#f0f4f8")
        self.result_label.pack()

        self.attempt_label = tk.Label(self.root, text="", bg="#f0f4f8")
        self.attempt_label.pack()

        self.stats_label = tk.Label(self.root, text="", bg="#f0f4f8")
        self.stats_label.pack(pady=5)

        self.best_label = tk.Label(self.root, text=f"🥇 Best Score: {self.best_score}", bg="#f0f4f8")
        self.best_label.pack()

        self.guess_button = tk.Button(self.root, text="Guess", command=self.check_guess, bg="#4CAF50", fg="white")
        self.guess_button.pack(pady=5)

        tk.Button(self.root, text="Restart", command=self.start_game, bg="#2196F3", fg="white").pack(pady=5)

    # ---------------- Game Setup ----------------
    def start_game(self):
        # Stop previous timer
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        level = self.difficulty.get()

        if level == "Easy":
            self.max_number, self.max_attempts = 10, 5
        elif level == "Medium":
            self.max_number, self.max_attempts = 50, 7
        else:
            self.max_number, self.max_attempts = 100, 10

        self.secret = random.randint(1, self.max_number)
        self.attempts = 0
        self.time_left = 30
        self.game_active = True

        self.entry.config(state="normal")
        self.guess_button.config(state="normal")
        self.entry.delete(0, tk.END)

        self.result_label.config(text="")
        self.info_label.config(text=f"Guess between 1 and {self.max_number}")

        self.update_attempts()
        self.update_stats()

        self.run_timer()

    # ---------------- Timer ----------------
    def run_timer(self):
        if not self.game_active:
            return

        if self.time_left > 0:
            self.timer_label.config(text=f"⏱ Time: {self.time_left}")
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.run_timer)
        else:
            self.losses += 1
            self.end_game(False, "⏰ Time's up!")

    # ---------------- Guess Logic ----------------
    def check_guess(self):
        if not self.game_active:
            return

        try:
            guess = int(self.entry.get())
            self.attempts += 1
            self.entry.delete(0, tk.END)

            if guess == self.secret:
                score = self.max_attempts - self.attempts + 1
                self.wins += 1
                self.end_game(True, f"✅ Correct! Score: {score}")

                if score > self.best_score:
                    self.best_score = score
                    save_best_score(score)
                    self.best_label.config(text=f"🥇 Best Score: {self.best_score}")

            elif guess < self.secret:
                self.result_label.config(text="📉 Too Low!")
            else:
                self.result_label.config(text="📈 Too High!")

            self.update_attempts()

            if self.attempts >= self.max_attempts:
                self.losses += 1
                self.end_game(False, f"❌ Game Over! Number was {self.secret}")

        except ValueError:
            self.result_label.config(text="⚠ Enter a valid number!")

    # ---------------- End Game ----------------
    def end_game(self, win, message):
        self.game_active = False
        self.result_label.config(text=message)

        self.entry.config(state="disabled")
        self.guess_button.config(state="disabled")

        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        self.update_stats()

    # ---------------- Updates ----------------
    def update_attempts(self):
        remaining = self.max_attempts - self.attempts
        self.attempt_label.config(text=f"Attempts left: {remaining}")

    def update_stats(self):
        self.stats_label.config(text=f"📊 Wins: {self.wins} | Losses: {self.losses}")


# ---------------- Run App ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedGame(root)
    root.mainloop()