# FUNCTIONS

# Questions for victoria
# Line 52, the or statement use, it would not work without it?
# I can import random but it won't be orange?
# WHy do we have to add (): this next to a function, I kept forgetting to do so

import random


# Plan - We need the players choice, the opponents choice (which is the program), we need both together
# in order to figure out the winner


def players_choice():
    """This will grasp the choice that you input into the program once it runs"""
    player_choice = input("Enter your choice (Rock, Paper, or Scissors): ").lower()
    # Assigning it into a variable
    while player_choice not in ["r", "p", "s"]:
        print("This answer is unacceptable, please only use - 'r','p' or 's'")
        return player_choice
    # while is used for creating a loop
    # for example here it is saying that while the players choice is not in the r, p, or s
    # letters then the program should print that it is unacceptable


# Asks the computer to generate a random value between 0 and 2
def opponents_choice():
    """Generate computer's choice randomly using random values."""
    from random import randint
    opponent_choice = randint(0,2)
    return opponent_choice

# Below is another way to do it, wihtout the use of integers
# def opponent_choice():
#     """Generate computer's choice randomly."""
#     return random.choice(["r", "p", "s"])

# Convert the computer's choice. O becomes Rock; 1 becomes Paper; 2 becomes Scissors
def convert(choice):
    if choice == 0:
       return "rock"
    elif choice == 1:
        return "paper"
    elif choice == 2:
        return "scissors"

# Compare the user's choice with the computer's choice to display a
# message indicating whether the user won, lost or drew against the computer

def winner(player_choice, opponent_choice):
    """This is the function which compares both and gives us the winner"""
    if player_choice == opponent_choice:
        return "It's a tie! We think alike ;)"
    elif (player_choice == 0 and opponent_choice == 2) or \
         (player_choice == 1 and opponent_choice == 0) or \
         (player_choice == 2 and opponent_choice == 1):
        return "Are you a mind reader! :/ You win!"
    else:
        return "Haha, you lost to an NPC"
# HAVING SYNTAX PROBLEM ABOVE FOR AGES AFTER BRACKETS - so i saw online to use or \
# elif means else if and basically allows to add more conditionals to the function
# Showcase what you have learned about conditional statements and create your own functions


def play_game():
    print("Welcome to a legendary game of Rock, Paper, Scissors!\nMay the odds be ever in your favour!")
    player_choice = players_choice()
    opponent_choice = opponents_choice()
    numbtoint = {"r": 0, "p": 1, "s": 2}[player_choice]
    print(f"\nYour choice: {player_choice}")
    print(f"Opponent's choice: {convert(opponent_choice)}\n")
    result = winner(numbtoint, opponent_choice)
    print(result)

# calling the function to use the game
play_game()

# In order to play the whole game and run the game
# The required defined statement is needed below
# This above actually is so essential otherwise nothing would run without it





#  DUNDERSCORE EXAMPLE - IT TESTS THE FUNCTIONS
# if __name__ == "__main__":
#     # test the function
#     print('this is a test')
