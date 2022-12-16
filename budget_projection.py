"""This is the feature for Option 1 'Budget Projection' of the application."""

import os


def projected_expenses():
    while True:
        try:
            expense_types = [
                "rent",
                "mortgage",
                "food",
                "transport",
                "insurance",
                "debt",
                "misc",
            ]
            expense_variables = []
            for expense in expense_types:
                expense_value = float(input(f"{expense.capitalize()}: $"))
                if expense_value < 0:
                    raise ValueError("Error: Only enter a positive value.")
                else:
                    expense_variables.append(expense_value)
            total_expenses = sum(expense_variables)
            break
        except ValueError:
            print("\nInvalid input...")
            print("Please try again and ensure you only enter positive number values\n")
    return total_expenses


def projected_income():
    while True:
        try:
            total_income = float(
                input("Enter your projected monthly post-tax primary income: $")
            )
            if total_income < 0:
                print("Invalid input... Only enter positive values.")
                continue
            break
        except ValueError:
            print("\nInvalid input...")
            print("Please try again and ensure you only enter number values\n")
    return total_income


def monthly_budget_calculation(income, expense):
    return income - expense


def budget_projection():
    os.system("cls")
    print("We will now project your budget for the next month & year!\n")
    print("Don't worry about being exact with the numbers.")
    print("This is simply a general estimate and projection of your budget.\n")
    income_total = projected_income()
    os.system("cls")
    print("Great! Now please enter your projected monthly expenses:\n")
    print("(Enter '0' for any expense that isn't applicable)")
    expense_total = projected_expenses()
    os.system("cls")
    print("After projecting your total income minus total expenses:\n")
    monthly_budget_amount = monthly_budget_calculation(income_total, expense_total)
    yearly_budget_amount = monthly_budget_amount * 12
    if monthly_budget_amount > 0:
        print(
            "You will have $",
            "{:.2f}".format(monthly_budget_amount),
            "left over in a month.",
        )
        print(
            "This means you will have $",
            "{:.2f}".format(yearly_budget_amount),
            "left over in a year.\n",
        )
    else:
        print(
            "You will be $", "{:.2f}".format(monthly_budget_amount), "short in a month."
        )
        print(
            "This means you will be $",
            "{:.2f}".format(yearly_budget_amount),
            "short in a year.",
        )
        print("\nPlease consider increasing your income or decreasing your expenses.\n")
    os.system("pause")
