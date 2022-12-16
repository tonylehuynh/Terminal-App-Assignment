import pandas as pd
import os
import csv


def display_last_rows():
    with open("data.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        # Count number of rows in file
        row_count = 0
        for row in reader:
            row_count += 1
        # If not enough data, advise user to add income or expense
        if row_count < 11:
            os.system("cls")
            print(
                "\nNot enough entries. You need to record more income or expenses first."
            )
        else:
            os.system("cls")
            dataframe = pd.read_csv("data.csv")
            print(dataframe.tail(10))
            print(
                "\nListed above are your last 10 recorded entries for income and expenses."
            )
