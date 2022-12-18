"""Feature allows user to track and record their income"""

import os
import csv
import datetime


def input_date():
    """
    This function receives user input for a date for their income/expense
    entry.

    User input is converted from string and returns a 'datetime.date obeject.
    """
    while True:
        try:
            date_string = input(
                "Enter the date this transaction took place (YYYY-MM-DD): "
            )
            date_input = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
            today = datetime.datetime.now().date()
            if date_input > today:
                print("Unable to enter dates in the future...")
                continue
            break
        except ValueError:
            print(
                "\nInvalid date format... Please enter a date in the format YYYY-MM-DD.\n"
            )
    return date_input


def input_amount():
    """
    This function receives user input for income/expense amount and returns a float. 
    """
    while True:
        try:
            amount_input = float(input("Enter the amount: $"))
            if amount_input < 0:
                raise ValueError
            break
        except ValueError:
            print("\nInvalid input...")
            print("Please try again and ensure you only enter positive number values\n")
    return amount_input


def store_income_data():
    """
    This function appends user income data to the data.csv file.
    """
    os.system("cls")
    print("Please enter your income received:\n")
    with open("data.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")

        category = "Income"
        date = input_date()
        amount = input_amount()

        writer.writerow([date, category, amount])
