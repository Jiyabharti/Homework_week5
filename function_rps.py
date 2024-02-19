def start_the_game(user_choice, computer_choice):
    user_choice = user_choice
    computer_choice = computer_choice

    print("You chose: ", user_choice)
    print("Computer chose: ", computer_choice)

def game_rules(user_choice, computer_choice):

    if user_choice == computer_choice:
        print("It's a tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")

    else:
        print("Computer wins!")

