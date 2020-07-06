import unittest
import statistics
import math
import app.util.errors as errors
from app.math.transcendental import *
from app.math.math_helper import *


# tests cosh function from calculator.transcendental
# Kyungjin Kim

ACCURACY_DIGITS = '.10g'
REALLY_LARGE_NUMBER = 10000000000
REALLY_SMALL_NUMBER = 0.0000000001


class TestCosh(unittest.TestCase):
    def test_high(self):
        # as x -> +infty, y -> +infty
        x = 0
        y1 = cosh(x)
        y2 = math.cosh(x)
        difference = format(y1, ACCURACY_DIGITS) == format(y2, ACCURACY_DIGITS)
        while difference:
            x += 1.3
            y1 = cosh(x)
            y2 = math.cosh(x)
            difference = format(y1, ACCURACY_DIGITS) == format(y2, ACCURACY_DIGITS)
        #print(f'maximum within error threshold: x={x}, cosh(x)={y1}, expected cosh(x)={y2}')
        self.assertGreater(y2, REALLY_LARGE_NUMBER)

    def test_low(self):
        # as x -> -infty, y -> +infty
        x = 0
        y1 = cosh(x)
        y2 = math.cosh(x)
        difference = format(y1, ACCURACY_DIGITS) == format(y2, ACCURACY_DIGITS)
        while difference:
            x -= 1.3
            y1 = cosh(x)
            y2 = math.cosh(x)
            difference = format(y1, ACCURACY_DIGITS) == format(y2, ACCURACY_DIGITS)
        #print(f'minimum within error threshold: x={x}, cosh(x)={y1}, expected cosh(x)={y2}')
        self.assertGreater(y2, REALLY_LARGE_NUMBER)

    def test_transcendental_nb(self):
        self.assertEqual(format(cosh(compute_pi()), ACCURACY_DIGITS), format(math.cosh(math.pi), ACCURACY_DIGITS))

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


class TestLog10(unittest.TestCase):
    """
        Test custom Transcendental log10(x) function result over math.log10(x) result

        Date: 2020-07-05
        Author: Alexis Laurens-Renner 40055137
        Transcendental function: log10(x)
        """
    def test_log10(self):
        x = 1000
        while x >0:
            rounded_log10 = round(log10(x), 6)
            rounded_math_log10 = round(math.log10(x), 6)
            self.assertEqual(rounded_log10, rounded_math_log10)
            x -= 0.1

    def test_log10_neg(self):
        x = -1
        self.assertRaises(errors.IllegalArgumentError, log10, x)
        x = 0
        self.assertRaises(errors.IllegalArgumentError, log10, x)

if __name__ == '__main__':
    unittest.main()