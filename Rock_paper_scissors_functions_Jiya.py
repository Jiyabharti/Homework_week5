import random
#  So I can use all the random

def get_user_choice():
    """Get user's choice (Rock, Paper, or Scissors)."""
    user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").capitalize()
    while user_choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")
        user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").capitalize()
    return user_choice


def opponent_choice():
    """Generate computer's choice randomly."""
    return random.choice(["Rock", "Paper", "Scissors"])


def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "Uh oh, It's a tie!"
    elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "Are you a mind reader! :/ You win!"
    else:
        return "Opponent wins!!! Haha"


def play_game():
    """Play the Rock, Paper, Scissors game."""
    print("Welcome to a legendary game of Rock, Paper, Scissors!\nMay the odds be ever in your favour!")

    player_choice = get_user_choice()
    NPC_choice = opponent_choice()
    # I thought calling it an NPC was kinda funny
    print(f"\nYour choice: {player_choice}")
    print(f"Oppenents's choice: {NPC_choice}\n")

    result = determine_winner(player_choice, NPC_choice)
    print(result)


# In order to play the whole game and run the game
# The required defined statement is needed below
play_game()
# This above actually is so essential otherwise nothing would run without it