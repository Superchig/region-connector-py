import string
import re

def int_to_col(col_num):
    """
    Converts an integer into its corresponding string column value.

    Essentially performs binary conversion into base-26, except that
    the digits start from 'A' rather than '0'.
    """

    result = ""

    while col_num > 26:
        rem = col_num % 26
        col_num //= 26

        ch = string.ascii_uppercase[rem - 1]
        result += ch

    ch = string.ascii_uppercase[col_num - 1]
    result += ch

    return result[::-1]

def col_to_int(col_str):
    """
    Converts a string representing a column in Google Sheets into an integer.
    """

    result = 0
    base_mult = 1

    for ch in col_str[::-1]:
        result += (ord(ch) - 64) * base_mult
        base_mult *= 26

    return result

def split_cell(cell):
    """
    Converts a string representing a Google Sheets cell position
    into its component column and row parts.
    """

    results = re.findall('[A-Z]+|[0-9]+', cell)
    return (results[0], int(results[1]))
