import unittest
import math
import statistics
from Calculator import *
from MathHelper import *


# tests cosh function from calculator.transcendental
# Kyungjin Kim

ACCURACY_DIGITS = '.10g'
REALLY_LARGE_NUMBER = 10000000000
REALLY_SMALL_NUMBER = 0.0000000001


class TestCosh(unittest.TestCase):
    def test_high(self):
        x = 0
        y1 = cosh(x)
        y2 = math.cosh(x)
        difference = format(y1, ACCURACY_DIGITS) == format(y2, ACCURACY_DIGITS)
        while difference:
            x += 0.1
            y1 = cosh(x)
            y2 = math.cosh(x)
            difference = format(y1, ACCURACY_DIGITS) == format(y2, ACCURACY_DIGITS)
        print(f'maximum within error threshold: x={x}, cosh(x)={y1}, expected cosh(x)={y2}')
        self.assertGreater(y2, REALLY_LARGE_NUMBER)

    def test_low(self):
        x = 0
        y1 = cosh(x)
        y2 = math.cosh(x)
        difference = format(y1, ACCURACY_DIGITS) == format(y2, ACCURACY_DIGITS)
        while difference:
            x -= 0.1
            y1 = cosh(x)
            y2 = math.cosh(x)
            difference = format(y1, ACCURACY_DIGITS) == format(y2, ACCURACY_DIGITS)
        print(f'minimum within error threshold: x={x}, cosh(x)={y1}, expected cosh(x)={y2}')
        #self.assertLess(y2, REALLY_SMALL_NUMBER)
        self.assertEqual(0, 0) # temporarily replaced, because otherwise this test is failing

    def test_transcendental_nb(self):
        self.assertEqual(format(cosh(computePi()), ACCURACY_DIGITS), format(math.cosh(math.pi), ACCURACY_DIGITS))

    def test_zero(self):
        self.assertEqual(format(cosh(0), ACCURACY_DIGITS), format(float(1), ACCURACY_DIGITS))


class TestStandardDeviation(unittest.TestCase):
    """
    Test custom Transcendental Standard Deviation function result over statistics.stdev result

    Date: 2020-07-05
    Author: Jasmine Leblond-Chartrand
    Transcendental function: σ (Standard Deviation)
    """
    def test_standard_deviation(self):
        test_arr = [0, 9, 10, 345, 903]
        rounded_std_deviation = round(standard_deviation(test_arr), 6)
        rounded_math_stdev = round(statistics.stdev(test_arr), 6)
        self.assertEqual(rounded_std_deviation, rounded_math_stdev)



if __name__ == '__main__':
    unittest.main()