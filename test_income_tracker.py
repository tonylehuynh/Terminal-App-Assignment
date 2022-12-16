"""Testing of the income tracker feature"""

import os
from income_tracker import file_does_not_exist_income



# Test that function will successfully create csv file
def test_create_csv_file():
    file_does_not_exist_income()
    csv_file_exists = os.path.exists("income.csv")
    # File should be created and return true
    assert csv_file_exists == True 

# Case 2 - Ensure function outputs correct file format
def test_file_format():
    file_does_not_exist_income()
    wrong_format = os.path.exists("income.txt")
    # Should return false as file should only be in csv form
    assert wrong_format == False
