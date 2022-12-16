"""Feature to allow user to track their income"""


import os
import csv
import datetime


def input_date():
    while True:
        try:
            date_string = input("Enter the date this transaction took place (YYYY-MM-DD): ")
            date_input = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
            today = datetime.datetime.now().date()
            if date_input > today:
                print("Unable to enter dates in the future...")
                continue
            break
        except ValueError:
            print("\nInvalid date format... Please enter a date in the format YYYY-MM-DD.\n")
    return date_input


def input_amount():
    while True:
        try:
            amount_input = float(
                input("Enter the amount: $")
            )
            if amount_input < 0:
                raise ValueError 
            break
        except ValueError:
            print("\nInvalid input...")
            print("Please try again and ensure you only enter positive number values\n")
    return amount_input


def file_does_not_exist():
    with open("data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(["Date", "Category", "Amount"])


def store_income_data():
    os.system("cls")
    print("Please enter your income received:\n")
    with open("data.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")

        category = "Income"
        date = input_date()
        amount = input_amount()

        writer.writerow([date, category, amount])


# def income_tracker():
#     os.system("cls")
#     print("Please enter your income received:\n")
#     if not os.path.exists("data.csv"):
#         file_does_not_exist()
#     else:
#         store_income_data()

def check_for_file():
    if not os.path.exists("data.csv"):
        file_does_not_exist()
