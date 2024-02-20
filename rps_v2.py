# Import random used to select random integer for computers choice
import random

# users choice input uses string to prompt player to enter letter
# use while not in to error check only relevant letters are used & print error statement
# use lower to convert all in to same to make sure no errors
def get_user_choice():
    user_choice = input("Enter 'r' for Rock, 'p' for Paper, or 's' for Scissors: ").lower()
    while user_choice not in ['r', 'p', 's']:
        print("Invalid input. Please enter 'r', 'p', or 's'.")
        user_choice = input("Enter 'r' for Rock, 'p' for Paper, or 's' for Scissors: ").lower()
    return user_choice

# use random.randint to generate computer choice from 0-2
def get_computer_choice():
    return random.randint(0, 2)

# use if/elif to convert the number to the relevant letter
# == check to see if the 2 operands are the equal
def convert_choice(choice):
    if choice == 0:
        return 'Rock'
    elif choice == 1:
        return 'Paper'
    elif choice == 2:
        return 'Scissors'

# use if/elif/or/else to determine the logic of the winning player
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        return "You win!"
    else:
        return "Computer wins!"

# used dictionary to convert number integer & use this going forward to compare for win
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    user_choice_int = {'r': 0, 'p': 1, 's': 2}[user_choice]

    print(f"You chose {convert_choice(user_choice_int)}.")
    print(f"The computer chose {convert_choice(computer_choice)}.")

    print(determine_winner(user_choice_int, computer_choice))


play_game()
