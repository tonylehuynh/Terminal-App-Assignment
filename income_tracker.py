"""Feature to allow user to track their income"""


import os
import csv
import datetime


def income_category():
    return "income"


def input_date():
    pass


def input_amount():
    pass


def file_does_not_exist():
    with open("data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(["Date", "Category", "Amount"])


def store_budget_data():
    with open("data.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")

        category = "income"
        test_date = datetime.datetime(2022, 6, 6)
        date = test_date
        amount = 100.20

        writer.writerow([date, category, amount])


def income_tracker():
    if not os.path.exists("data.csv"):
        file_does_not_exist()
    if os.path.exists("data.csv"):
        store_budget_data()
