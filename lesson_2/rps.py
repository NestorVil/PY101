# Rock Paper Scissors Game
# If the player picks rock and computer scissors, player wins
# If the player picks scissors and the computer paper, player wins
# If the player picks paper and the computer rock, player wins
# If both choose the same item, its a tie
# Else the computer wins

# Initialize a list of options for the player to pick from
# Ask the user to make a choice
# Verify that its an adequate choice
# Make the computer make a choice at random from the options
# Calculate the win
# Display the winner
# Ask of they want to play again

import random

VALID_CHOICES = ["rock", "paper", "scissors"]
running = True

def prompt(message):
    print(f"==> {message}")

def display_winner(player, computer):
    if ((player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")):
        prompt("You win :D")
    elif player == computer:
        prompt("It's a tie :/")
    else:
        prompt("You lose D:")


prompt("Welcome to Python Rock Paper Scissors!")

while running:
    prompt(f"Choose one: {", ".join(VALID_CHOICES)}")
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f"You chose {choice}, computer chose {computer_choice}.")

    display_winner(choice, computer_choice)

    prompt("Would you like to play again? (y/n):")
    answer = input().lower()
    while True:
        if answer.startswith("n") or answer.startswith("y"):
            break

        prompt('Please enter "y" or "n".')
        answer = input().lower()

    if answer[0] == "n":
        prompt("Thanks for playing :D")
        running = False