import os


def budget_projection():
    pass


def projected_expenses():
    try:
        housing = float(input('Enter your monthly rent/mortgage expense: $'))
        utilities = float(input('Enter your monthly utilities total expense: $'))
        food = float(input('Enter your monthly groceries expense: $'))
        travel = float(input('Enter your monthly travel/commute expenses: $'))
        misc = float(input('Enter any additional monthly misc expense: $'))
        total_expenses = housing + utilities + food + travel + misc
    except ValueError:
        print('\nInvalid input...') 
        print('Please try again and ensure you only enter number values')
        projected_expenses()
    return total_expenses

def projected_income():
    try:
        total_income = float(input('Enter your monthly post-tax primary income: $'))
    except ValueError:
        print('\nInvalid input...') 
        print('Please try again and ensure you only enter number values')
        projected_income()
    return total_income


os.system('cls')
print('We will now project your budget for the next month & year!\n')
print('Don\'t worry about being exact with the numbers.')
print('This is simply a general estimate and projection of your budget.\n')


income_total = projected_income()
os.system('cls')
print('Great! Now please provide your projected monthly expenses:\n')

expense_total = projected_expenses()

margin = income_total - expense_total

print(f'\nYes {margin}')
