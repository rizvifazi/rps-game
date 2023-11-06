# import library to select random choice
import random


def getChoice():
    player_choice = input("Select from (rock, paper, scissors): ").lower()
    options = ["rock", "paper", "scissors"]

    # selcet a random option from list through random library.
    computer_choice = random.choice(options)
    print(f"You selected {player_choice}, computer selected {computer_choice}")
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def checkWinner(player, computer):

    if player == computer:
        return "It's a TIE!"
    elif player == "rock":
        if computer == "paper":
            return "Paper covers rock, You LOOSE :("
        elif computer == "scissors":
            return "Rock smashes scissors, You WIN! :)"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock, You WIN! :)"
        elif computer == "scissors":
            return "Scissors cuts paper, You LOOSE :("
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors, You LOOSE :("
        elif computer == "paper":
            return "Scissors cuts paper, You WIN! :("
    else:
        return "Invalid selection"


quit = 'a'

while (quit != 'q'):
    print("Rock-Paper-Scissors Game")
    choices = getChoice()
    p_choice = choices["player"]
    pc_choice = choices["computer"]
    print(checkWinner(p_choice, pc_choice))
    quit = input("Press 'Enter' key to continue, press 'q' to quit \n")
