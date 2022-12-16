"""Feature to allow user to track their expenses"""

import os
import csv
import datetime
from income_tracker import input_date, input_amount, file_does_not_exist


def expense_category():
    




def store_expense_data():
    with open("data.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")

        category = expense_category()
        date = input_date()
        amount = input_amount()

        writer.writerow([date, category, amount])


def expense_tracker():
    os.system("cls")
    print("Please enter your expenses:\n")
    if not os.path.exists("data.csv"):
        file_does_not_exist()
    if os.path.exists("data.csv"):
        store_expense_data()