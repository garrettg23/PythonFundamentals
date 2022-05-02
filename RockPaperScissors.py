# make rock paper scissors game in python.

import random

#make list of choices (not tuple or set)
#say you want to ask the player if they want to play again... write the whole bitch as a while loop.
while True:
    choice = ["rock","paper","scissors"]
    #need to do this for while loop.
    player = None

    #computer uses random module to select random value from choice list (rock paper scissors). see the choice of computer.
    computer = random.choice(choice)

    #gets what user plays. see what player chose, and prevent player from picking anything else using while loop.
    #need to initialize the player variable above as none before defining it in the while loop!!!!!
    #this will continue over and over until player picks rock paper scissors, try it. Case sensitive to it, but use lower why not.
    while player not in choice:
        player = input("rock, paper, or scissors?: ").lower()
    print("player picked: " + player)
    print("computer picked: " + computer)

    #showcase results:
    if player == computer:
        print("Tie! Try again till you loose dumb ass")
    #repeat elif for scissors and paper and boom your done ez
    elif player == "rock":
        if computer == "paper":
            print("You loose headass lol")
        if computer == "scissors":
            print("You win congrats dingus lol")
    elif player == "paper":
        if computer == "scissors":
            print("You loose headass lol")
        if computer == "rock":
            print("You win congrats dingus lol")
    elif player == "scissors":
        if computer == "rock":
            print("You loose headass lol")
        if computer == "paper":
            print("You win congrats dingus lol")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        #used to break out of while loop
        break
#after you break the while loop then you print goodbye bitch
print("Thanks for playing you shit head")




