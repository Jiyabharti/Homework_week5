import random
from function_rps import start_the_game
from function_rps import game_rules
options = ["Rock", "Paper", "Scissors"]

user_choice = input("Choose Rock, Paper, or Scissors: ").lower()

computer_choice = random.choice(options).lower()

start_the_game(user_choice, computer_choice)
game_rules(user_choice, computer_choice)