"""Feature to allow user to track their income"""


import os
import csv
import datetime


def file_does_not_exist_expense():
    with open("income.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(['Date', 'Amount'])

file_does_not_exist_expense()
