import random

VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]
ALT_CHOICES = ["r", "p", "s", "l", "sp"]

WINNING_COMBOS = {
    "rock":      ["scissors", "lizard"],
    "paper":     ["rock",     "spock"],
    "scissors":  ["paper",    "lizard"],
    "lizard":    ["paper",    "spock"],
    "spock":     ["rock",     "scissors"], 
}

def prompt(message):
    print(f"==> {message}")

def welcome():
    prompt("""Welcome to Python Rock Paper Scissors: Big Bang Edition :D\n
    This game introduces two new options: 'spock' and lizard'.\n
    With these new options: Scissors cuts Paper, Paper covers Rock.\n
    Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors.\n
    Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock.\n
    Spock vaporizes Rock, and Rock crushes Scissors. First to 3 wins :D\n""")

def get_player_choice():
    prompt(f"Choose one: {", ".join(VALID_CHOICES)}:")
    while True:
        choice = input()

        if choice in ALT_CHOICES:
            choice = fix_choice(choice)

        if choice not in VALID_CHOICES:
            prompt("Not a valid choice")
        else:
            return choice

def fix_choice(selection):
    position = ALT_CHOICES.index(selection)
    return VALID_CHOICES[position]

def determine_winner(player, computer):
    if computer in WINNING_COMBOS[player]:
        prompt("You win :D")
        return "win"
    if player == computer:
        prompt("You tie :/")
        return "tie"

    prompt("You lose D:")
    return "lose"

def display_round_winner(p_score):
    prompt("Round Over")
    if p_score == 3:
        prompt("You won the round :)")
    else:
        prompt("You lost the round ):")

def play_again():
    prompt("Would you like to play again? (y/n):")
    answer = input().lower()
    while True:
        if answer.startswith("n") or answer.startswith("y"):
            break

        prompt("Please enter 'y' or 'n':")
        answer = input().lower()

    return answer[0] == "n"

def increment_computer_score(result, cpu_score):
    if result == "lose":
        cpu_score += 1

    return cpu_score

def increment_player_score(result, human_score):
    if result == "win":
        human_score += 1

    return human_score

def main():
    player_score = 0
    computer_score = 0
    running = True

    welcome()

    while running:
        choice = get_player_choice()

        computer_choice = random.choice(VALID_CHOICES)

        prompt(f"You chose {choice}, CPU chose {computer_choice}.")

        result = determine_winner(choice, computer_choice)

        computer_score = increment_computer_score(result, computer_score)
        player_score = increment_player_score(result, player_score)

        prompt(f"Player score: {player_score}. CPU score: {computer_score}")

        if player_score == 3 or computer_score == 3:
            display_round_winner(player_score)

            player_score = 0
            computer_score = 0

            if play_again():
                prompt("Thanks for playing :D")
                running = False

main()

        # match result:
        #     case "win":
        #         prompt("You win :D")
        #         player_score += 1
        #     case "tie":
        #         prompt("You tie :/")
        #     case "lose":
        #         prompt("You lose D:")
        #         computer_score += 1