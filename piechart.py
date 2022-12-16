"""Feature to display pie chart of recorded income and expenses"""

import os
import csv
import matplotlib.pyplot as plt


def create_piechart():
    category_counts = {}
    with open("data.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        # Get the category values from second column of csv file. Skip first row.
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
    ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title("Income and Expenses distribution")
    plt.show()


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

