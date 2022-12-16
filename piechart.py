"""Feature to display pie chart of recorded income and expenses"""

import os
import csv
import matplotlib as ply
import pandas


def create_piechart():
    print("Successful")


def piechart_read():
    with open("data.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        # Count number of rows in file
        row_count = 0
        for row in reader:
            row_count += 1
        # If not enough data, advise user to add income or expense
        if row_count < 2:
            os.system("cls")
            print("\nNot enough data. Please record an income or expense first.")
        else:
            create_piechart()


