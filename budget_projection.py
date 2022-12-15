import os


def budget_projection():
    pass

def expenses():
    housing = float(input('Enter your monthly rent/mortgage expense: $'))
    utilities = float(input('Enter your monthly utilities total expense: $'))
    food = float(input('Enter your monthly groceries expense: $'))
    travel = float(input('Enter your monthly travel/commute expenses: $'))
    misc = float(input('Enter any additional monthly misc expense: $'))
    total_expenses = housing + utilities + food + travel + misc
    return total_expenses


os.system("cls")
print("We will now project your budget for the next month & year!\n")
print("Don't worry about being exact with the numbers.")
print("This is simply a general estimate and projection of your budget.\n")


income = float(input('Enter your monthly post-tax primary income: $'))

print('Great! Now please provide your projected monthly expenses\n')

expense_total = expenses()

margin = income - expense_total




    
