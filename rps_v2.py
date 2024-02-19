import random

def get_user_choice():
    user_choice = input("Enter 'r' for Rock, 'p' for Paper, or 's' for Scissors: ").lower()
    while user_choice not in ['r', 'p', 's']:
        print("Invalid input. Please enter 'r', 'p', or 's'.")
        user_choice = input("Enter 'r' for Rock, 'p' for Paper, or 's' for Scissors: ").lower()
    return user_choice

def get_computer_choice():
    return random.randint(0, 2)

def convert_choice(choice):
    if choice == 0:
        return 'Rock'
    elif choice == 1:
        return 'Paper'
    elif choice == 2:
        return 'Scissors'

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'r' and computer_choice == 2) or \
         (user_choice == 's' and computer_choice == 1) or \
         (user_choice == 'p' and computer_choice == 0):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    user_choice_int = {'r': 0, 'p': 1, 's': 2}[user_choice]

    print(f"You chose {convert_choice(user_choice_int)}.")
    print(f"The computer chose {convert_choice(computer_choice)}.")

    print(determine_winner(user_choice_int, computer_choice))


play_game()