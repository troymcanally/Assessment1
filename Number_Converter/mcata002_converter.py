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


def convert_to_binary(decimal_number):
    binary_string = ""

    while decimal_number > 0:
        quotient = decimal_number // 2
        binary_string += str(decimal_number % 2)
        decimal_number = quotient
    
    binary_string = reverse_binary_string(binary_string)    
    return binary_string


def reverse_binary_string(binary_string):
    reversed_string = ""
    index = len(binary_string)

    while index:
        index -= 1
        reversed_string += binary_string[index]
    
    return reversed_string


def convert_to_decimal(binary_number):
    decimal = 0
    index = 0

    while binary_number != 0:
        dec = binary_number % 10
        decimal = decimal + dec * pow(2, index)
        binary_number = binary_number // 10
        index += 1
    
    return decimal


def count_in_binary(decimal_number):
    index = 1

    while index <= decimal_number:
        print(f"Decimal: {index} = binary: {convert_to_binary(index)}")
        index += 1


def validate_decimal(user_input):
    index = 0
    is_valid = False
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    while index < len(user_input):
        if user_input[index] not in digits:
            is_valid = False
            return is_valid
        else:
            is_valid = True
            index += 1
    
    return is_valid


def validate_binary(user_input):
    index = 0
    is_valid = False

    while index < len(user_input):
        if user_input[index] != "0" and user_input[index] != "1":
            is_valid = False
            return is_valid
        else:
            is_valid = True
            index += 1

    return is_valid


display_details()

menu_choice = 0

while menu_choice != "4":
    menu_choice = get_menu_choice()

    match menu_choice:
        case "1":
            number = input("Please enter number: ")
            
            while not validate_decimal(number):
                print("Please make sure your number contains digits 0-9 only.")
                number = input("Please enter number: ")
            
            number = int(number)
            print(f"Binary number:  {convert_to_binary(number)}")
        case "2":
            binary_num = input("Please enter binary number: ")
            
            while not validate_binary(binary_num):
                print("Please make sure your number contains digits 0-1 only.")                
                binary_num = input("Please enter binary number: ")
            
            binary_num = int(binary_num)
            print(f"Decimal number:  {convert_to_decimal(binary_num)}")
        case "3":
            number = input("Please enter number: ")

            while not validate_decimal(number):
                print("Please make sure your number contains digits 0-9 only.")
                number = input("Please enter number: ")

            number = int(number)
            count_in_binary(number)

print("Goodbye.")