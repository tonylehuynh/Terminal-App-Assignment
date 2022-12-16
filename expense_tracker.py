"""Feature to allow user to track their expenses"""

import os
import csv
import datetime
from income_tracker import input_date, input_amount, file_does_not_exist


def expense_category():
    category = {
        1: "Rent",
        2: "Mortgage",
        3: "Food",
        4: "Transportation",
        5: "Utilities",
        6: "Internet",
        7: "Phone",
        8: "Insurance",
        9: "Subscriptions",
        10: "Clothing",
        11: "Exercise",
        12: "Socialising",
        13: "Miscellaneous",
    }
    print("Here are the categories of expenses:\n")
    print("1. Rent")
    print("2. Mortgage")
    print("3. Food")
    print("4. Transportation")
    print("5. Utilities")
    print("6. Internet")
    print("7. Phone")
    print("8. Insurance")
    print("9. Subscriptions")
    print("10. Clothing")
    print("11. Exercise")
    print("12. Socialising")
    print("13. Miscellaneous")
    while True:
        try:
            user_input = int(
                input(
                    "\nEnter a number to choose your option (e.g. Type 1 for Rent):\n"
                )
            )
            expense_type = category.get(user_input)
            break
        except ValueError:
            print("\nInvalid input...")
            print("Please try again and ensure you only enter number values\n")
    return expense_type


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
