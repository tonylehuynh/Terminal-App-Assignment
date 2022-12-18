"""Testing of the budget projection feature of the app"""

import pytest
from budget_projection import (
    monthly_budget_calculation,
    projected_expenses,
    projected_income,
)


def test_projected_expenses_output_error(monkeypatch):
    """
    Test that the projeted expenses function flags invalid user input.

    This test verifies that a ValueError is raised if user input is not a
    float or integer.
    """

    def mock_user_input(prompt):
        return "Test Invalid Input"

    monkeypatch.setattr("builtins.input", mock_user_input)
    # Test run successfully and function was updated to handle invalid input.
    with pytest.raises(ValueError):
        projected_expenses()


def test_projected_expenses_output_type(monkeypatch):
    """
    Test that projected expenses functions correct data type.

    This test makes a mock user input and verifies that the function
    should return a float data type.
    """

    def mock_user_input(prompt):
        return 232

    monkeypatch.setattr("builtins.input", mock_user_input)
    result = projected_expenses()
    assert isinstance(result, float)


def test_projected_income_output_type(monkeypatch):
    """
    Test that projected income functions correct data type.

    This test makes a mock user input and verifies that the function
    should return a float data type.
    """

    def mock_user_input(prompt):
        return 100

    monkeypatch.setattr("builtins.input", mock_user_input)
    result = projected_income()
    assert isinstance(result, float)


# Below two test cases for if total monthly budget calculation is correct
def test_monthly_budget_calculation_positive():
    """
    Test that the budget calculation function returns the correct result.

    This test verifies that the calculation of estimated budget is correct
    when given input of $100 income and $20 expense.
    """
    assert monthly_budget_calculation(100, 20) == 80


def test_monthly_budget_calculation_negative():
    """
    Test that the budget calculation function returns the correct negative result.

    This test verifies that the calculation of estimated budget is correct
    when given input of $20 income and $100 expense.
    """
    assert monthly_budget_calculation(20, 100) == -80
