#
# File: mcata002@mymail.unisa.edu.au_rose.py
# Author: Troy McAnally
# Email Id: mcata002@mymail.unisa.edu.au
# Version: 1.0 31 Mar 2023
# Description: Petals Around the Rose Guessing Game
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

import random
import dice

"""
The introduction function prints the game's introduction and prompts the user to play.
Calls play_game if yes and prints goodbye message if no
"""
def introduction():    
    greeting = """
    Petals Around the Rose
    ----------------------
    The name of the game is 'Petals Around the Rose'. The name of the
    game is important. The computer will roll five dice and ask you to
    guess the score for the roll. The score will always be zero or an
    even number. Your mission, should you choose to accept it, is to
    work out how the computer calculates the score. If you succeed in
    working out the secret and guess correctly three times in a row, you
    become a Potentate of the Rose.
    """

    print(greeting)
    answer = input("Would you like to play Petals Around the Rose [y|n]?").lower()

    if answer == "n":
        print("No worries... another time perhaps... :)")
    # else:
    #     play_game()


"""
The roll_dice function rolls 5 dice and returns a list of the values.

:return: A list of 5 random integers between 1 and 6.
"""
def roll_dice():
    counter = 0
    dice = [1, 2, 3, 4, 5]

    while counter < 5:
        num = random.randint(1, 6)
        dice[counter] = num
        counter += 1
    
    return dice


"""
The display_dice function takes in a list of 5 integers and displays the dice
    corresponding to those numbers. The function uses the display_dice function from
    the dice module.

:param player_dice: Used to Pass the dice values to the display_dice function.
:return: A graphical representation of the dice as ASCII art fom the "dice" module provided.
"""
def display_dice(player_dice):
    dice.display_dice(player_dice[0], player_dice[1], player_dice[2], player_dice[3], player_dice[4])


# def play_game():

# NOTE: name the dice vairiable player_dice and not dice you idiot!!!!

