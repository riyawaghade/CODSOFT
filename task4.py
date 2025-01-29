import tkinter as tk
from tkinter import messagebox
import random


class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("400x400")

        # Score Variables
        self.user_score = 0
        self.computer_score = 0

        # Heading
        self.heading_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 18, "bold"))
        self.heading_label.pack(pady=10)

        # User Choice Buttons
        self.rock_button = tk.Button(root, text="Rock", command=lambda: self.play("Rock"), bg="gray", fg="white", width=10)
        self.rock_button.pack(pady=5)

        self.paper_button = tk.Button(root, text="Paper", command=lambda: self.play("Paper"), bg="gray", fg="white", width=10)
        self.paper_button.pack(pady=5)

        self.scissors_button = tk.Button(root, text="Scissors", command=lambda: self.play("Scissors"), bg="gray", fg="white", width=10)
        self.scissors_button.pack(pady=5)

        # Result Label
        self.result_label = tk.Label(root, text="Make your choice!", font=("Arial", 14))
        self.result_label.pack(pady=20)

        # Score Label
        self.score_label = tk.Label(root, text="Score: You 0 - 0 Computer", font=("Arial", 12, "bold"))
        self.score_label.pack(pady=10)

        # Play Again Button
        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset_game, bg="blue", fg="white")
        self.play_again_button.pack(pady=10)

    def play(self, user_choice):
        options = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(options)

        # Determine winner
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = f"You win! {user_choice} beats {computer_choice}."
            self.user_score += 1
        else:
            result = f"You lose! {computer_choice} beats {user_choice}."
            self.computer_score += 1

        # Update the result and score
        self.result_label.config(text=f"User: {user_choice} | Computer: {computer_choice}\n{result}")
        self.score_label.config(text=f"Score: You {self.user_score} - {self.computer_score} Computer")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.result_label.config(text="Make your choice!")
        self.score_label.config(text="Score: You 0 - 0 Computer")


# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
