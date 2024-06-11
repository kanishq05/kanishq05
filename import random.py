import random

def main():
    while True:
        print("\nWelcome to Mini-Game App!")
        print("1. Tic-Tac-Toe")
        print("2. Hangman")
        print("3. Rock-Paper-Scissors")
        print("4. Exit")
        choice = input("Select a game to play (1-4): ")

        if choice == '1':
            tic_tac_toe()
        elif choice == '2':
            hangman()
        elif choice == '3':
            rock_paper_scissors()
        elif choice == '4':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Tic-Tac-Toe Game
def tic_tac_toe():
    board = [' ' for _ in range(9)]
    current_player = 'X'
    
    def print_board():
        for row in [board[i:i+3] for i in range(0, 9, 3)]:
            print('|'.join(row))
            print('-' * 5)
    
    def check_win(player):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)
    
    def check_draw():
        return ' ' not in board

    while True:
        print_board()
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
        if board[move] == ' ':
            board[move] = current_player
            if check_win(current_player):
                print_board()
                print(f"Player {current_player} wins!")
                break
            elif check_draw():
                print_board()
                print("It's a draw!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

# Hangman Game
def hangman():
    words = ['python', 'hangman', 'challenge', 'programming']
    word = random.choice(words).upper()
    guessed = ['_' for _ in word]
    guessed_letters = set()
    attempts = 6

    while attempts > 0 and '_' in guessed:
        print(' '.join(guessed))
        print(f"Attempts remaining: {attempts}")
        guess = input("Guess a letter: ").upper()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            guessed_letters.add(guess)
            attempts -= 1

    if '_' not in guessed:
        print(f"Congratulations, you guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

# Rock-Paper-Scissors Game
def rock_paper_scissors():
    choices = ['Rock', 'Paper', 'Scissors']
    player_choice = input("Enter Rock, Paper, or Scissors: ").capitalize()
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a draw!")
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    main()
