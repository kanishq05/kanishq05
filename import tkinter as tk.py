import tkinter as tk
from tkinter import messagebox
import random

class MiniGameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mini-Game App")
        self.geometry("400x400")
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_window()
        tk.Label(self, text="Welcome to Mini-Game App!", font=("Helvetica", 16)).pack(pady=20)
        
        tk.Button(self, text="Tic-Tac-Toe", command=self.tic_tac_toe).pack(pady=10)
        tk.Button(self, text="Hangman", command=self.hangman).pack(pady=10)
        tk.Button(self, text="Rock-Paper-Scissors", command=self.rock_paper_scissors).pack(pady=10)

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    # Tic-Tac-Toe Game
    def tic_tac_toe(self):
        self.clear_window()
        self.ttt_board = [' ' for _ in range(9)]
        self.ttt_current_player = 'X'
        
        self.ttt_buttons = []
        for i in range(9):
            button = tk.Button(self, text=' ', font=('Helvetica', 20), width=5, height=2,
                               command=lambda i=i: self.ttt_click(i))
            button.grid(row=i//3, column=i%3)
            self.ttt_buttons.append(button)

    def ttt_click(self, index):
        if self.ttt_board[index] == ' ':
            self.ttt_board[index] = self.ttt_current_player
            self.ttt_buttons[index].config(text=self.ttt_current_player)
            if self.ttt_check_win():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.ttt_current_player} wins!")
                self.create_main_menu()
            elif ' ' not in self.ttt_board:
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.create_main_menu()
            else:
                self.ttt_current_player = 'O' if self.ttt_current_player == 'X' else 'X'

    def ttt_check_win(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        return any(self.ttt_board[a] == self.ttt_board[b] == self.ttt_board[c] != ' ' for a, b, c in win_conditions)

    # Hangman Game
    def hangman(self):
        self.clear_window()
        self.hangman_word = random.choice(['PYTHON', 'HANGMAN', 'CHALLENGE', 'PROGRAMMING']).upper()
        self.hangman_guessed = ['_' for _ in self.hangman_word]
        self.hangman_attempts = 6
        self.hangman_guessed_letters = set()
        
        self.hangman_word_label = tk.Label(self, text=' '.join(self.hangman_guessed), font=("Helvetica", 20))
        self.hangman_word_label.pack(pady=20)
        
        self.hangman_input = tk.Entry(self, font=("Helvetica", 20))
        self.hangman_input.pack(pady=10)
        
        self.hangman_button = tk.Button(self, text="Guess", command=self.hangman_guess)
        self.hangman_button.pack(pady=10)
        
        self.hangman_attempts_label = tk.Label(self, text=f"Attempts remaining: {self.hangman_attempts}", font=("Helvetica", 16))
        self.hangman_attempts_label.pack(pady=10)

    def hangman_guess(self):
        guess = self.hangman_input.get().upper()
        self.hangman_input.delete(0, tk.END)
        
        if len(guess) != 1 or not guess.isalpha() or guess in self.hangman_guessed_letters:
            messagebox.showwarning("Hangman", "Invalid guess or already guessed. Try again.")
            return
        
        self.hangman_guessed_letters.add(guess)
        if guess in self.hangman_word:
            for i, letter in enumerate(self.hangman_word):
                if letter == guess:
                    self.hangman_guessed[i] = guess
        else:
            self.hangman_attempts -= 1

        self.hangman_word_label.config(text=' '.join(self.hangman_guessed))
        self.hangman_attempts_label.config(text=f"Attempts remaining: {self.hangman_attempts}")
        
        if '_' not in self.hangman_guessed:
            messagebox.showinfo("Hangman", f"Congratulations, you guessed the word: {self.hangman_word}")
            self.create_main_menu()
        elif self.hangman_attempts == 0:
            messagebox.showinfo("Hangman", f"Game over! The word was: {self.hangman_word}")
            self.create_main_menu()

    # Rock-Paper-Scissors Game
    def rock_paper_scissors(self):
        self.clear_window()
        tk.Label(self, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 16)).pack(pady=20)
        
        for choice in ['Rock', 'Paper', 'Scissors']:
            tk.Button(self, text=choice, font=("Helvetica", 16),
                      command=lambda choice=choice: self.rps_play(choice)).pack(pady=10)
        
        self.rps_result_label = tk.Label(self, text="", font=("Helvetica", 16))
        self.rps_result_label.pack(pady=20)

    def rps_play(self, player_choice):
        choices = ['Rock', 'Paper', 'Scissors']
        computer_choice = random.choice(choices)
        result = self.rps_get_result(player_choice, computer_choice)
        self.rps_result_label.config(text=f"Player chose {player_choice}, Computer chose {computer_choice}. {result}")

    def rps_get_result(self, player, computer):
        if player == computer:
            return "It's a draw!"
        if (player == 'Rock' and computer == 'Scissors') or \
           (player == 'Paper' and computer == 'Rock') or \
           (player == 'Scissors' and computer == 'Paper'):
            return "You win!"
        else:
            return "You lose!"

if __name__ == "__main__":
    app = MiniGameApp()
    app.mainloop()
