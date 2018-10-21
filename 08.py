#Here's a second version, which is built for one player, while the second player's choice is chosen at random.
stop = False
while (not stop):
    print "Let's play Rock, Paper, Scissors!"
    import random
    prs = ["paper", "rock", "scissors"]
    pl2 = random.choice(prs)
    pl1 = raw_input("Player 1: please enter your option: ").lower()
    if pl1 == "rock" and pl2 == "scissors":
        print "The computer chooses scissors. Rock beats scissors: you win!"
    elif pl1 == "rock" and pl2 == "paper":
        print "The computer chooses paper. Paper beats rock: the computer wins!"
    elif pl1 == "scissors" and pl2 == "rock":
        print "The computer chooses rock. Rock beats scissors: the computer wins!"
    elif pl1 == "scissors" and pl2 == "paper":
        print "The computer chooses paper. Scissors beats paper: you win!"
    elif pl1 == "paper" and pl2 == "scissors":
        print "The computer chooses scissors. Scissors beats paper: the computer wins!"
    elif pl1 == "paper" and pl2 == "rock":
        print "The computer chooses rock. Paper beats rock: you win!"
    elif pl1 == pl2:
        print "The computer chooses " + pl1 + ". Oooo, it's a draw!"
    else:
        print "Incorrect response, please try again!"
    answer = raw_input("Do you want to keep playing? (yes or no)").lower()
    if answer == "no":
        stop = True
        print "Game Over"
    elif answer == "yes":
        print "The game will start over."
    else:
        print "Wrong answer, please type 'yes' or 'no'."