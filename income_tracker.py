"""Feature to allow user to track their income"""


import os
import csv
import datetime


def file_does_not_exist():
    with open("data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(["Date", "Category", "Amount"])



def income_tracker():
    if not os.path.exists("data.csv"):
        file_does_not_exist()
    if os.path.exists("data.csv"):
        with open("data.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=",")

            category = "income"
            date = "date"
            amount = "amount"

            writer.writerow([date,category,amount])

income_tracker()

