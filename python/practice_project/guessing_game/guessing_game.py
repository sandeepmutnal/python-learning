# ==================================
# Number Guessing Game (Improved)
# ==================================

import random


def play_game():
    print("\n🎯 Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 10.")

    secret = random.randint(1, 10)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == secret:
                print(f"✅ Correct! You guessed it in {attempts} attempts.")
                return
            elif guess < secret:
                print("📉 Too low!")
            else:
                print("📈 Too high!")

            print(f"Attempts left: {max_attempts - attempts}")

        except ValueError:
            print("⚠ Please enter a valid number!")

    print(f"\n❌ Game Over! The number was {secret}.")


# Main loop for replay
while True:
    play_game()

    again = input("\nDo you want to play again? (y/n): ").lower()
    if again != "y":
        print("👋 Thanks for playing!")
        break
