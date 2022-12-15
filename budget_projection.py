import os



def projected_expenses():
    try:
        housing = float(input("Rent/mortgage expense: $"))
        utilities = float(input("Utilities total expense: $"))
        food = float(input("Groceries expense: $"))
        travel = float(input("Travel/commute expense: $"))
        misc = float(input("Any additional miscellaneous expenses: $"))
        total_expenses = housing + utilities + food + travel + misc
    except ValueError:
        print("\nInvalid input...")
        print("Please try again and ensure you only enter number values")
        projected_expenses()
    return total_expenses


def projected_income():
    try:
        total_income = float(
            input("Enter your projected monthly post-tax primary income: $")
        )
    except ValueError:
        print("\nInvalid input...")
        print("Please try again and ensure you only enter number values")
        projected_income()
    return total_income


def budget_projection():
    os.system("cls")
    print("We will now project your budget for the next month & year!\n")
    print("Don't worry about being exact with the numbers.")
    print("This is simply a general estimate and projection of your budget.\n")
    income_total = projected_income()
    os.system("cls")
    print("Great! Now please enter your projected monthly expenses:\n")
    expense_total = projected_expenses()
    os.system("cls")
    print('After projecting your total income minus total expenses:\n')
    monthly_budget_amount = income_total - expense_total
    yearly_budget_amount = monthly_budget_amount * 12
    if monthly_budget_amount > 0:
        print('You will have $', '{:.2f}'.format(monthly_budget_amount), 'left over in a month.')
        print('This means you will have $', '{:.2f}'.format(yearly_budget_amount), 'left over in a year.\n')
        os.system('pause')
    else:
        print('You will be $', '{:.2f}'.format(monthly_budget_amount), 'short in a month.')
        print('This means you will be $', '{:.2f}'.format(yearly_budget_amount), 'short in a year.')
        print('\nPlease consider increasing your income or decreasing your expenses.\n')
        os.system('pause')


budget_projection()