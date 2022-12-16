"""This is the feature for Option 2 'Track Budget' of this Terminal Application"""

import os


def tracker_menu():
    os.system("cls")
    print("It's time to track your income and expenses!\n")
    print("Please enter 1, 2 or 3 for the following options:\n")
    print("1. Track income and expenses")
    print("2. See visual graph of your expenses by category")
    print("3. Return to main menu")
    while True:
        option = input("\nChoose an option:\n")
        if option == "3":
            break
        elif option == "1":
            break
        elif option == "2":
            break
        else:
            print("INVALID INPUT... Please enter 1, 2 or 3:")

tracker_menu()
