"""Testing of expense tracking feature"""

from expense_tracker import expense_category


# Test to ensure function returns the correct dict string values based on integer input
def test_expense_category():
    # Two edge cases of 0 and 14 included
    test_cases = [
        (1, 'Rent'), 
        (2, 'Mortgage'), 
        (3, 'Food'),
        (4, 'Transportation'),
        (5, 'Utilities'),
        (6, 'Internet'),
        (7, 'Phone'),
        (8, 'Insurance'),
        (9, 'Subscriptions'),
        (10, 'Clothing'),
        (11, 'Exercise'),
        (12, 'Socialising'),
        (13, 'Miscellaneous'),
        (0, None), 
        (14, None)
    ]

    for x in test_cases:
        output = expense_category()
        assert output == x[1]