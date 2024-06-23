import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        
        self.user_score = 0
        self.computer_score = 0
        
        self.create_widgets()

    def create_widgets(self):
       
        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.grid(row=1, column=0, padx=10, pady=10)
        
        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.grid(row=1, column=1, padx=10, pady=10)
        
        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.grid(row=1, column=2, padx=10, pady=10)
        
        # Labels for displaying choices and result
        self.user_choice_label = tk.Label(self.root, text="Your Choice: ")
        self.user_choice_label.grid(row=2, column=0, columnspan=3, pady=10)
        
        self.computer_choice_label = tk.Label(self.root, text="Computer's Choice: ")
        self.computer_choice_label.grid(row=3, column=0, columnspan=3, pady=10)
        
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.result_label.grid(row=4, column=0, columnspan=3, pady=10)
        
       
        self.user_score_label = tk.Label(self.root, text=f"Your Score: {self.user_score}")
        self.user_score_label.grid(row=5, column=0, pady=10)
        
        self.computer_score_label = tk.Label(self.root, text=f"Computer's Score: {self.computer_score}")
        self.computer_score_label.grid(row=5, column=2, pady=10)

    def get_computer_choice(self):
        choices = ["rock", "paper", "scissors"]
        return random.choice(choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return "user"
        else:
            return "computer"

    def play(self, user_choice):
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner(user_choice, computer_choice)
        
        self.user_choice_label.config(text=f"Your Choice: {user_choice}")
        self.computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
        
        if winner == "tie":
            self.result_label.config(text="It's a tie!", fg="blue")
        elif winner == "user":
            self.result_label.config(text="You win!", fg="green")
            self.user_score += 1
        else:
            self.result_label.config(text="You lose!", fg="red")
            self.computer_score += 1
        
        self.user_score_label.config(text=f"Your Score: {self.user_score}")
        self.computer_score_label.config(text=f"Computer's Score: {self.computer_score}")
        
        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if not play_again:
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
