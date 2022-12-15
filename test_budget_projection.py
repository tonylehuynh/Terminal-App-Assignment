"""Testing of the budget projection feature of the app"""

from budget_projection import monthly_budget_calculation



# Below two tests are testing that the total monthly budget calculation is correct
def test_monthly_budget_calculation_positive():
    """Income of $100 minus expenses of $20 should result in $80 leftover"""
    assert monthly_budget_calculation(100, 20) == 80


def test_monthly_budget_calculation_negative():
    """Expenses being higher than income should return a negative value"""
    assert monthly_budget_calculation (20, 100) == -80
