"""This is the feature where user's last 10 income/expense entries are displayed in a table"""

import pandas as pd
import os
import csv


def display_last_rows():
    """
    This function reads data.csv file and displays a table of the user's last
    10 income/expense recorded entries.

    If data.csv file does not have enough rows, table will not show.
    """
    with open("data.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        row_count = 0
        for row in reader:
            row_count += 1
        if row_count < 11:
            os.system("cls")
            print(
                "Not enough entries. You need to record more income or expenses first."
            )
        else:
            os.system("cls")
            dataframe = pd.read_csv("data.csv")
            print(dataframe.tail(10))
            print(
                "\nListed above are your last 10 recorded entries for income and expenses."
            )
