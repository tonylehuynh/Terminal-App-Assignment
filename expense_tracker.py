"""Feature to allow user to track their expenses"""

import os
import csv
from income_tracker import input_date, input_amount


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
        # Try except block to ensure user can only input integers
        try:
            user_input = int(
                input(
                    "\nEnter a number to choose your option (e.g. Type 1 for Rent):\n"
                )
            )
            # If statement to ensure user can only input 1-13
            if not (0 < user_input < 14):
                print("\nInvalid input...")
                print("Please only enter in number between 1 and 13...")
                continue
            expense_type = category.get(user_input)
            break
        except ValueError:
            print("\nInvalid input...")
            print("Please try again and ensure you only enter whole number values\n")
    return expense_type


def store_expense_data():
    os.system("cls")
    print("Please enter your expenses\n")
    with open("data.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")

        category = expense_category()
        print(f"Category: {category}")
        date = input_date()
        amount = input_amount()

        writer.writerow([date, category, amount])


