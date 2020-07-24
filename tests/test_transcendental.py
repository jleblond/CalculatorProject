import unittest
import statistics
import math
import pandas
import calc_app.util.errors as errors
from calc_app.mathlib.transcendental import *
from calc_app.mathlib.math_helper import *


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
    '''
    Test custom Transcendental Standard Deviation function result over statistics.stdev result

    Date: 2020-07-05
    Author: Jasmine Leblond-Chartrand
    Transcendental function: σ (Standard Deviation)
    '''
    def test_standard_deviation(self):
        test_arr = [0, 9, 10, 345, 903]
        rounded_std_deviation = round(standard_deviation(test_arr), 4)
        rounded_math_stdev = round(statistics.stdev(test_arr), 4)
        self.assertEqual(rounded_std_deviation, rounded_math_stdev)


class TestLog10(unittest.TestCase):
    '''
    Test custom Transcendental log10(x) function result over math.log10(x) result

    Date: 2020-07-05
    Author: Alexis Laurens-Renner 40055137
    Transcendental function: log10(x)
    '''
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


class TestMAD(unittest.TestCase):
    '''
    Test custom Mean Abosolute Deviation (MAD) function over pandas.Series().mad()

    Date: 2020-07-07
    Author: Jeffrey Lam Yuk Tseung
    Transcendental function: Mean Aboslute Deviation ()
    '''
    def test_mad(self):
        test_arr = [5, 57, 106, 0, 28, 22, 15, 156, 9, 86, 65, 37, 0, 16] 
        rounded_result = MAD(test_arr)
        pandas_series = pandas.Series(test_arr)
        rounded_pandas_result = pandas_series.mad()
        self.assertEqual(rounded_result, rounded_pandas_result)

        
class TestPower(unittest.TestCase):
    """
    Test custom Transcendental Power function result over math.pow result

    Date: 2020-07-12
    Author: Andrew Korolus (40055081)
    Transcendental function: power (x^y)
    """
    def test_positive_power(self):
        x = 3
        y = 8
        cust_power = power(x, y)
        real_power = math.pow(x, y)
        self.assertEqual(cust_power, real_power)

    def test_negative_power(self):
        x = 26
        y = -3
        cust_power = power(x, y)
        real_power = math.pow(x, y)
        self.assertEqual(cust_power, real_power)

    def test_zero_exp_power(self):
        x = 2
        y = 0
        cust_power = power(x, y)
        real_power = math.pow(x, y)
        self.assertEqual(cust_power, real_power)

    def test_zero_base_power(self):
        x = 0
        y = 9
        cust_power = power(x, y)
        real_power = math.pow(x, y)
        self.assertEqual(cust_power, real_power)

    def test_decimal_base_power(self):
        x = 0.89
        y = 5
        cust_power = round(power(x, y), 4)
        real_power = round(math.pow(x, y), 4)
        self.assertEqual(cust_power, real_power)

    def test_decimal_exp_power(self):
        x = 5
        y = 0.89
        cust_power = round(power(x, y), 4)
        real_power = round(math.pow(x, y), 4)
        self.assertEqual(cust_power, real_power)

    def test_neg_decimal_exp_power(self):
        x = 5
        y = -0.89
        cust_power = round(power(x, y), 4)
        real_power = round(math.pow(x, y), 4)
        self.assertEqual(cust_power, real_power)

    def test_large_power(self):
        x = 12
        y = 25
        cust_power = power(x, y)
        real_power = math.pow(x, y)
        self.assertEqual(cust_power, real_power)

    def test_transcendental_power(self):
        x = 8
        y = compute_pi()
        cust_power = round(power(x, y), 4)
        real_power = round(math.pow(x, y), 4)
        self.assertEqual(cust_power, real_power)

    def test_small_power(self):
        x = 89
        y = 0.00000000000061
        cust_power = round(power(x, y), 4)
        real_power = round(math.pow(x, y), 4)
        self.assertEqual(cust_power, real_power)

class TestSin(unittest.TestCase):
    """
    Test custom Transcendental Sine function result over math.sin result

    Date: 2020-07-12
    Author: Roman Lewandowski (40062108)
    Transcendental function: Sin(x)

    """
    def test_positive_sin(self):
        x = 15
        cust_sin = rad_sin(x)
        real_sin = math.sin(x)
        self.assertEqual(round(cust_sin,6), round(real_sin,6))

    def test_negative_sin(self):
        x = -45
        cust_sin = rad_sin(x)
        real_sin = math.sin(x)
        self.assertEqual(round(cust_sin,6), round(real_sin,6))

    def test_large_sin(self):
        x = 400000000
        cust_sin = rad_sin(x)
        real_sin = math.sin(x)
        self.assertEqual(round(cust_sin,6), round(real_sin,6))

    def test_small_sin(self):
        x = 0.000000000012
        cust_sin = rad_sin(x)
        real_sin = math.sin(x)
        self.assertEqual(round(cust_sin,6), round(real_sin,6))

    def test_negative_sin(self):
        x = -45
        cust_sin = rad_sin(x)
        real_sin = math.sin(x)
        self.assertEqual(round(cust_sin,6), round(real_sin,6))

    def test_zero_sin(self):
        x = 0
        cust_sin = rad_sin(x)
        real_sin = math.sin(x)
        self.assertEqual(round(cust_sin,6), round(real_sin,6))

    def test_ninety_sin(self):
        x = 90
        cust_sin = rad_sin(x)
        real_sin = math.sin(x)
        self.assertEqual(round(cust_sin,6), round(real_sin,6))



if __name__ == '__main__':
    unittest.main()