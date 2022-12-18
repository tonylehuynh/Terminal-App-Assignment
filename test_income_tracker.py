"""Testing of the income tracker feature"""

import os
import csv
import datetime
from income_tracker import store_income_data
from tracker_menu import file_does_not_exist


def test_create_csv_file():
    """
    Test that the create_csv file function will successfully create the
    data.csv file. 
    """
    file_does_not_exist()
    csv_file_exists = os.path.exists("data.csv")
    assert csv_file_exists == True


def test_file_format():
    """
    Test that the file created by create_csv function is in the correct format
    
    File format should be a csv file and not a .txt file.
    """
    file_does_not_exist()
    wrong_format = os.path.exists("data.txt")
    assert wrong_format == False


def test_append_csv_string():
    """
    Test Case 1 that the function will appends correct string values to the csv file.
    """
    store_income_data()
    with open("data.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)
        # Below returns true as the string values have been temporarily recorded for this test.
        assert rows[-1] == ["date", "income", "amount"]


def test_append_csv_float_date():
    """
    Test Case 2 where function will append correct date & float values to the csv file.
    """
    store_income_data()
    with open("data.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)
        test_date = str(datetime.datetime(2022, 6, 6))
        test_float = str(100.20)
        # Returns true. Function outputs date & float values however csv stores these as string values
        assert rows[-1] == [test_date, "income", test_float]
