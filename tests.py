"""

All these test functions work for this test_data.csv file.
    date	volume	        area	solar_exposure	rainfall	max_temperature	min_temperature	humidity	wind_speed
0   201407	5657697449.14	22363375	9.2	        -14.2	    0.5	                12.2	       58	    1.13
1   201408	6975301986.76	27934375	-5	        56.2	    12.7	            0.1		                1.01
2   20149	8059054929.9	39915625	16.4	    33.3	    16.8	            3.8	           49	    1.2
3   201410	6554638526.69	-15101250	20.7		            21.3	            6	           47	    1.32
4   201411	6815030704.04	23045000		        34	        25.2	            9.2	           41	    1.45
5   201412	-7075422881.39	30988750	25.1	    141.6	    25.3	            12.1	       37	    1.57
6           6584181053.81	16002500	22.9	    148.3	    25.2		                       -37	    1.51
7   201502	3443037970.08	8032187.5	19.5	    21		                        12	           40	    -1.32
8   201503	301894886.35	61875	    18.2	    12.5	    23.5	            8.8	           42	    1.32
9   201504	7025003908.26		        9.7	        92.2	    17.6	            6.9	           46	    1.26
10  201505		            34861406.25	10.3	    9.1	        15.4	            2.8	           54
11  201506	10363822652.11	40272187.5	8.7	        44.3	    12.7	            -1.3	       60	    1.13


"""




import sys

import pytest
import numpy as np
import pandas as pd

import model as assignment


def test_read_data():
    """
    Checks if dataframe is read or not, checks if dataframe is empty after if any imputing done.

    """
    message = "Reading data unsuccessful.Required dataframe empty status should be {} but is {} "
    message1 = "Number of columns in data should be {} but is {}"
    message2 = "Number of rows in data should be {} but is {}"
    message3 = "Number of missing values in data is {}, should be {}"
    data = assignment.read_dataset("test_data.csv")
    # checks if data is read
    result = data.empty
    result_column_len = len(data.columns)
    result_row_len = len(data.index)
    assert result == False, message.format(False, result)
    assert result_column_len == 9, message1.format(9, result_column_len)
    assert result_row_len == 12, message2.format(12, result_row_len)
    # checks for missing values
    check = np.where(pd.isnull(data))
    assert check[0].size == 0, message3.format(check[0].size, 0)


def test_largest_area():
    """
    Checks largest area of test_datset, compares with expected result and asserts it
    """
    message = "Largest area should be {} but function returned {}"
    data = assignment.read_dataset("test_data.csv")
    result = assignment.largest_area(data)
    expected = max(22363375, 27934375, 39915625, 24347728.125, 23045000, 30988750, 16002500, 8032187.5, 61875,
                   24347728.125, 34861406.25, 40272187.5)
    assert result == expected, message.format(expected, result)


def test_average_volume():
    """
    Checks average volume of test_datset, compares with expected result and asserts it
    """
    message = "Average volume should be {} but your function returned {}"
    data = assignment.read_dataset("test_data.csv")
    result = assignment.average_volume(data)
    volume = (5657697449.14, 6975301986.76, 8059054929.9, 6554638526.69, 6815030704.04, 4973112835.0682, 6584181053.81,
              3443037970.08, 301894886.35, 7025003908.26, 6068434263.8371, 10363822652.11)
    expected = round(np.mean(volume), 2)
    assert result == expected, message.format(expected, result)


def test_most_average_rainfall():
    """
    Checks month closest to average rainfall of test_datset, compares with expected result and asserts it
    """
    message = "Most average rainfall month is supposed to be {} but function returned {}"
    data = assignment.read_dataset("test_data.csv")
    result = assignment.most_average_rainfall(data)
    # Uses index_to_name_month from assignment to get a part of expected result
    expected = assignment.index_to_name_month(9) + ", " + "2014"
    assert result == expected, message.format(expected, result)


def test_hottest_month():
    """
    Checks hottest month of test dataset , compares with expected and asserts the result
    """
    message = "Hottest month is supposed to be {} but function returned {}"
    data = assignment.read_dataset("test_data.csv")
    result = assignment.hottest_month(data)
    expected = assignment.index_to_name_month(11)
    assert result == expected, message.format(expected, result)


def test_index_to_name_month():
    """
    Checks the month returned for each index is matching with the expected results or not using the index_to_month_name function
    """
    message = 'For {}, month should be {} but returned {}'
    true_tests = (
    (0, 'January'), (1, 'February'), (2, 'March'), (3, 'April'), (4, 'May'), (5, 'June'), (6, 'July'), (7, 'August'),
    (8, 'September'), (9, 'October'), (10, 'November'), (11, 'December'))
    for index, month in true_tests:
        result = assignment.index_to_name_month(index)
        assert result == month, message.format(index, month, result)


if __name__ == '__main__':
    pytest.main(sys.argv)
