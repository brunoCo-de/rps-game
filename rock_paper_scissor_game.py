# pylint: disable=missing-module-docstring
#This progam implements the famous  child game Rock, papper, scissor game

import random

def play():
    "This implements the game"

    test = True
    while test:
        player = input("Rock (R/s), papper (P/p), scissor (S/s) : ").lower()
        if player not in ['r','p','s'] :
            print("Enter R/s, P/s or S/s :")
        else :
            test = False

    machine = random.choice(['r','p','s'])
    print(f'machine choosed : {machine.upper()}')

    if player == machine :
        return "It's a tie"

    if is_win(player, machine) :
        return "Yay !! You win ;)"

    return "Uhh !! You lost."


def is_win(player,machine) :
    "This function determines if the user win."
    # Rules: p>r, r>s, s>p
    if (player == 'p' and machine == 'r') or (player == 'r' and machine == 's') \
        or (player == 's' and machine == 'p') :
        return True
    return False

RESULT = play()

print(RESULT)
