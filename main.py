import random
import time
import os

print("Welcome to rock paper scissors")

while True:
    user = input("Chose: (rock  paper scissors) ")
    posibleChoice = ["rock", "paper", "scissors"]
    computerAction = random.choice(posibleChoice)

    print(f"\n You chose {user}, computer chose {computerAction}.\n")

    if user == computerAction:
        print(f"Both players selecter {user}. It's a tie!")
    elif user == "rock":
        if computerAction == "scissors":
            print("Rock smashes scissors! You win!")
        else: 
            print("paper covers rock! You lose.")
    elif user == "paper":
        if computerAction == "rock":
            print("Paper covers rock! You win")
        else:
            print("Scissors cuts paper! You lose.")
    elif user == "scissors":
        if computerAction == "paper":
            print("Scissors cuts paper! You win")
        else:
            print("Rock smashes scissors! you lose")

    print("\n")
    playAgain = input("Play again? (y/n): ")
    if playAgain.lower() != "y":
        break
    print("\n")
