"""
Run Budget Terminal Application from this app.py file
"""

import os
from budget_projection import budget_projection
from tracker_menu import tracker_menu


def main_menu():
    """
    This function contains the main menu for this budget app.

    User can input a number to choose option they wish to proceed with.
    """
    os.system("cls")
    print("Welcome to your personal budget app!\n")
    print("Please enter 1, 2, 3 for the following options:\n")
    print("1. Estimate Budget projection")
    print("2. Track your budget")
    print("3. Exit application")
    while True:
        option = input("\nChoose an option:\n")
        if option == "3":
            print("Exiting the program... Have a nice day!")
            quit()
        elif option == "1":
            budget_projection()
            main_menu()
        elif option == "2":
            tracker_menu()
            main_menu()
        else:
            print("INVALID INPUT... Please enter 1, 2 or 3:")


main_menu()
