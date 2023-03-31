#
# File: mcata002@mymail.unisa.edu.au_converter.py
# Author: Troy McAnally
# Email Id: mcata002
# Version: 1.0 01 Apr 2023
# Description: Assignment 1 - Converts decimal number to binary and binary number to decimal
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

"""
The display_details function prints the author's details to the console.
"""
def display_details():
    details = """
    File : mcata002@mymail.unisa.edu.au_converter.py
    Author : Troy McAnally
    Stud ID : 110406456
    Email ID : mcata002
    This is my own work as defined by the University's Academic Misconduct Policy.
    """

    print(details)


"""
The get_menu_choice function displays the menu and prompts the user for a choice.
It then returns that choice to main.

:return: A string containing the user choice.
"""
def get_menu_choice():
    menu_string = """
    *** Menu ***
    1. Convert to binary
    2. Convert to decimal
    3. Binary counting
    4. Quit
    """
    choice = ""

    print(menu_string)

    while choice != "1" and choice != "2" and choice != "3" and choice != "4":
        choice = input("What would you like to do [1,2,3,4]? ")
    
    return choice


# def convert_to_binary(decimal_number):


# def convert_to_decimal(binary_number):

display_details()

menu_choice = 0

while menu_choice != "4":
    menu_choice = get_menu_choice()

    match menu_choice:
        case "1":
            print("In command 1 - convert to binary")
        case "2":
            print("In command 2 - convert to decimal")
        case "3":
            print("In command 3 - Binary Counting")

print("Goodbye.")