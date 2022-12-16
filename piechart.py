"""Feature to display pie chart of recorded income and expenses"""

import os
import csv
import matplotlib as ply
import pandas
from tracker_menu import tracker_menu


def create_piechart():

def read_csv():
    with open('data.csv', 'r', newline="") as csvfile:
        reader = csv.reader(csvfile)
        # Count number of rows in file
        row_count = 0
        for row in reader:
            row_count += 1
        # If not enough data, advise user to add income or expense
        if row_count < 2:
            print("\nNot enough data. Please record an income or expense")
            os.system("pause")
            tracker_menu()



