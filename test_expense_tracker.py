"""Testing of expense tracking feature"""

from expense_tracker import expense_category


def test_expense_category():
    """
    Test that the correct dict values are returned based on user input.

    This test verifies that the correct expense categories are returned
    based on user input as an integer. 
    """
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
        (0, None),  # Two invalid edge cases of 0 and 14 included
        (14, None)
    ]
    for x in test_cases:
        output = expense_category()
        assert output == x[1]