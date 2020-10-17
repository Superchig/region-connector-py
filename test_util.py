import unittest
import util

class TestIntToCol(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(util.int_to_col(1), 'A', 'Should be A')
        self.assertEqual(util.int_to_col(3), 'C', 'Should be C')

    def test_double_digit(self):
        self.assertEqual(util.int_to_col(27), 'AA')
        self.assertEqual(util.int_to_col(29), 'AC')

class TestColToInt(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(util.col_to_int('A'), 1)
        self.assertEqual(util.col_to_int('C'), 3)
        self.assertEqual(util.col_to_int('Y'), 25)
        self.assertEqual(util.col_to_int('Z'), 26)

    def test_double_digit(self):
        self.assertEqual(util.col_to_int('AA'), 27)
        self.assertEqual(util.col_to_int('AC'), 29)

class TestSplitCell(unittest.TestCase):
    def test_split_cell(self):
        self.assertEqual(util.split_cell('C7'), ('C', 7))
        self.assertEqual(util.split_cell('E32'), ('E', 32))
        self.assertEqual(util.split_cell('BD9'), ('BD', 9))
        self.assertEqual(util.split_cell('EF48'), ('EF', 48))

if __name__ == '__main__':
    unittest.main()
