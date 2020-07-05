import unittest
import MathHelper
import math

class TestMathHelper(unittest.TestCase):
    """
    Test custom Math helper functions over math functions
    Date: 2020-07-05
    Author: Jasmine Leblond-Chartrand
    Functions: absolute, square_root
    """
    def test_absolute(self):
        test_arr = [-29, 4534, 0, 4.5]
        for i in test_arr:
            self.assertEqual(abs(i), MathHelper.absolute(i))

    def test_square_root(self):
        test_arr = [0, 9, 10, 345, 903]
        for i in test_arr:
            rounded_math_sqrt = round(math.sqrt(i), 6)
            rounded_math_helper_sqrt = round(MathHelper.square_root(i), 6)
            self.assertEqual(rounded_math_sqrt, rounded_math_helper_sqrt)


if __name__ == '__main__':
    unittest.main()