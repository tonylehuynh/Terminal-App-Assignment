"""Feature to display pie chart of recorded income and expenses"""

import os
import csv
import matplotlib.pyplot as plt


def create_piechart():
    """
    This function reads column 2 of data.csv and returns a piechart.

    The piechart displays the % distribution of income/expense categories.
    """
    category_counts = {}
    with open("data.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        # Get the category values from second column of csv file. Skip first row.
        next(reader)
        for row in reader:
            category = row[1]
            if category in category_counts:
                category_counts[category] += 1
            else:
                category_counts[category] = 1
    # Create pie chart
    labels = list(category_counts.keys())
    sizes = list(category_counts.values())
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct="%1.1f%%")
    ax.axis("equal")
    ax.set_title("Income and Expenses distribution")
    plt.show()


def piechart_read():
    """
    This function counts number of rows in data.csv file. 

    If there are insufficient rows, user will be told there isn't enough data.
    """

    with open("data.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        row_count = 0
        for row in reader:
            row_count += 1
        if row_count < 2:
            os.system("cls")
            print("Not enough data. Please record an income or expense first.")
        else:
            create_piechart()

