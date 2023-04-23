#
# File: mcata002_rose.py
# Author: Troy McAnally
# Email Id: mcata002
# Version: 1.0 31 Mar 2023
# Description: Assignment 1 - Petals Around the Rose Guessing Game
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

import random
import dice

greeting = """
File : mcata002_rose.py
Author : Troy McAnally
Stud ID : 110406456
Email ID : mcata002
This is my own work as defined by the University's Academic Misconduct Policy.


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

play = ""
die_count = [0, 0, 0, 0, 0, 0, 0]
num_of_games = 1
correct_guess = 0
incorrect_guess = 0
incorrect_in_a_row = 0
correct_in_a_row = 0

while play != "y" and play != "n":
    play = input("Would you like to play Petals Around the Rose [y|n]? ").lower()

    if play != "y" and play != "n":
        print("Please enter either 'y' or 'n'.")

    if play == "n":
        print("No worries... another time perhaps... :)")
    else:
        again = ""
        
        while again != "n":
            counter = 0
            player_dice = [1, 2, 3, 4, 5]

            while counter < 5:
                num = random.randint(1, 6)
                die_count[num] += 1
                player_dice[counter] = num
                counter += 1

            dice.display_dice(player_dice[0], player_dice[1], player_dice[2], player_dice[3], player_dice[4])

            petals = 0

            for i in player_dice:
                if i % 2 != 0:
                    num = i - 1
                    petals += num

            guess = int(input("Please enter your guess for the roll: "))

            if guess == "":
                guess = int(input(("Please ensure you enter a guess for the roll: ")))

            if guess % 2 != 0:
                print(f"No sorry, it's {petals} not {guess}. The score is always even.")
                incorrect_guess += 1
                correct_in_a_row = 0
                incorrect_in_a_row += 1
            elif guess == petals:
                print("Well done! You guessed it!")
                correct_guess += 1
                incorrect_in_a_row = 0
                correct_in_a_row += 1
            else:
                print(f"No sorry, it's {petals} not {guess}.")
                incorrect_guess += 1
                correct_in_a_row = 0
                incorrect_in_a_row += 1

            if correct_in_a_row == 3:
                print("Congratulations! You have worked out the secret!")
                print("Make sure you don't tell anyone!\n")
                again = "n"
            elif incorrect_in_a_row == 3:
                print("Hint: The name of the game is important... Petals Around the Rose.\n")
                again = "n"
            else:
                again = input("Roll dice again [y|n]? ").lower()

            if again != "y" and again != "n":
                print("Please enter either 'y' or 'n'.")
            elif again == "y":
                num_of_games += 1


        print(f"Game Summary")
        print(f"============\n")
        print(f"You played {num_of_games} games:")
        print(f"  |---> Number of correct guesses:      {correct_guess}")
        print(f"  |---> Number of incorrect guesses:    {incorrect_guess}\n")
        print(f"Dice Roll Stats:")
        print(f"Face    Frequency")

        count = 1

        while count <= 6:
            asterix = ""
            asterix_iter = 0
            

            num_asterix = die_count[count]
            while asterix_iter < num_asterix:
                asterix += "*"
                asterix_iter += 1

            print(f"   {count}    {asterix}")

            count += 1

        print(("Thanks for playing!"))
    
