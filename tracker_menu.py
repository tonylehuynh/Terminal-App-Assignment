"""This is the menu displayed for Option 2 'Track Budget' of this Terminal Application"""

import os
import csv
from income_tracker import store_income_data
from expense_tracker import store_expense_data
from piechart import piechart_read


def check_for_file():
    if not os.path.exists("data.csv"):
        file_does_not_exist()


def file_does_not_exist():
    with open("data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(["Date", "Category", "Amount"])


def tracker_menu():
    os.system("cls")
    print("~ It's time to track your income and expenses ~\n")
    print("Please enter 1, 2, 3, 4 or 5 for the following options:\n")
    print("1. Record income")
    print("2. Record expenses")
    print("3. See visual graph of your income and expenses by category")
    print("4. Return to main menu")
    print("5. Exit application")
    while True:
        option = input("\nChoose an option:\n")
        if option == "4":
            break
        elif option == "5":
            print("Exiting the program... Have a nice day!")
            quit()
        elif option == "1":
            check_for_file()
            store_income_data()
            print("Income entry has been saved.")
            os.system("pause")
            tracker_menu()
        elif option == "2":
            check_for_file()
            store_expense_data()
            print("Expense entry has been saved.")
            os.system("pause")
            tracker_menu()
        elif option == "3":
            check_for_file()
            piechart_read()
            os.system("pause")
            tracker_menu()
        else:
            print("INVALID INPUT... Please enter 1, 2, 3, 4 or 5:")
