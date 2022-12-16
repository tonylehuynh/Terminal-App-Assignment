"""Test piechart functionality"""

import csv
from piechart import piechart_read


# Test Case 1 - Piechart won't be created as data.csv has insufficient data
def test_piechart_will_not_open():
    # Overwrite data.csv file to have insufficient rows
    with open("data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Date", "Category", "Amount"])

    result = piechart_read()
    # Returns none as csv file has insufficient rows
    assert result is None



