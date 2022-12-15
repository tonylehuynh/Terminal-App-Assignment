"""Testing of the budget projection feature of the app"""

import pytest
from budget_projection import monthly_budget_calculation, projected_expenses, projected_income


# # Test that projected_expenses function will output as an error if user input is not a float or integer
def test_projected_expenses_output_error(monkeypatch):
    """Should return as a ValueError if user inputs text"""

    def mock_user_input(prompt):
        return "Test Invalid Input"

    monkeypatch.setattr("builtins.input", mock_user_input)
    with pytest.raises(ValueError):
        projected_expenses()
    # Test was run successfully and function was further updated to handle invalid inputs
    # This test should not be run again due to the while loop in place to handle invalid inputs. 


# Test to make sure projected_expenses function output returns as a float
def test_projected_expenses_output_type(monkeypatch):
    "Output of the projected expenses function should result in a float data type"

    def mock_user_input(prompt):
        return 232

    monkeypatch.setattr("builtins.input", mock_user_input)
    result = projected_expenses()
    assert isinstance(result, float)

# Test to make sure projected_income function output returns as a float
def test_projected_income_output_type(monkeypatch):
    "Output of the projected income function should result in a float data type"

    def mock_user_input(prompt):
        return 100

    monkeypatch.setattr("builtins.input", mock_user_input)
    result = projected_income()
    assert isinstance(result, float)


# Below two test cases are testing that the total monthly budget calculation is correct
def test_monthly_budget_calculation_positive():
    """Income of $100 minus expenses of $20 should result in $80 leftover"""
    assert monthly_budget_calculation(100, 20) == 80


def test_monthly_budget_calculation_negative():
    """Expenses being higher than income should return a negative value"""
    assert monthly_budget_calculation(20, 100) == -80
