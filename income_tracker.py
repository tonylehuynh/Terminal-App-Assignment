"""Feature to allow user to track their income"""


import os
import csv
import datetime


def income_category():
    return "income"


def input_date():
    while True:
        try:
            date_string = input("Enter the date this transaction took place (YYYY-MM-DD): ")
            date_input = datetime.datetime.strptime(date_string, "%Y-%m-%d")
            break
        except ValueError:
            print("\nInvalid input...")
            print("Invalid date format... Please enter a date in the format YYYY-MM-DD.\n")
    return date_input


def input_amount():
    while True:
        try:
            amount_input = float(
                input("Enter the amount: $")
            )
            break
        except ValueError:
            print("\nInvalid input...")
            print("Please try again and ensure you only enter number values\n")
    return amount_input


def file_does_not_exist():
    with open("data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(["Date", "Category", "Amount"])


def store_budget_data():
    with open("data.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")

        category = income_category()
        test_date = datetime.datetime(2022, 6, 6)
        date = test_date
        amount = 100.20

        writer.writerow([date, category, amount])


def income_tracker():
    if not os.path.exists("data.csv"):
        file_does_not_exist()
    if os.path.exists("data.csv"):
        store_budget_data()
