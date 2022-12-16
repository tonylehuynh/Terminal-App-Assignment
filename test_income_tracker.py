"""Testing of the income tracker feature"""

import os
import csv
import datetime
from income_tracker import store_income_data
from tracker_menu import file_does_not_exist


# Test that function will successfully create csv file
def test_create_csv_file():
    file_does_not_exist()
    csv_file_exists = os.path.exists("data.csv")
    # File should be created and return true
    assert csv_file_exists == True


# Case 2 - Ensure function outputs correct file format
def test_file_format():
    file_does_not_exist()
    wrong_format = os.path.exists("data.txt")
    # Should return false as file should only be in csv form
    assert wrong_format == False


# Test that function will correctly append data to csv file
# Case 1 - Function only appends string values into csv file
def test_append_csv_string():
    store_income_data()
    with open("data.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)
        # Below returns true as the string values have been temporarily written in
        assert rows[-1] == ["date", "income", "amount"]

# Case 2 - Function instead appends a date & float value into csv file
def test_append_csv_float_date():
    store_income_data()
    with open("data.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)
        test_date = str(datetime.datetime(2022, 6, 6))
        test_float = str(100.20)
        # Returns true. Function outputs date & float values however csv stores these as string values
        assert rows[-1] == [test_date, "income", test_float]
