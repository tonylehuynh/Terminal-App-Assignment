"""Test piechart functionality"""

import csv
from piechart import piechart_read


def test_piechart_will_not_open():
    """
    Test that piechart will not be created if csv doesn't have enough data.
    """
    with open("data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Date", "Category", "Amount"])
    result = piechart_read()
    assert result is None
