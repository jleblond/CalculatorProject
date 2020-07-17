'''
this module contains the transcendental functions 
required for the operation of the ETERNITY calculator.
1. x^y
2. log10(x)
3. std
4. MAD
5. Trig: sin(x), radSin(x), cos(x), radCos(x)
6. 10^x
7. cosh(x)
'''

import calc_app.mathlib.math_helper as math_helper
import calc_app.util.errors as errors

def power(base, exponent):
    ''' 
    Calculate the power of the first number raised to the second number.        
    Supports any Real number for the base and exponent.
    Uses the general formula: pow(a, b) = exp(b * ln(a)), for non-integer exponents b.

    Date: 2020-05-23
    Author: Andrew Korolus (40055081)
    Transcendental function: x^y

    fBase : float
        The base value of the expression.
    fExponent : float
        The exponent value of the expression.
    '''    
    # The first easy case is to check if the exponent is equal to 0
    # Any number to the power of 0 is equal to 1
    if exponent == 0:        
        return 1

    # Any power with a base 0 is equal to 0
    if base == 0:        
        return 0

    # The second easy case is to check if the exponent is equal to 1
    # Any number to the power of 1 is equal to itself
    if exponent == 1:        
        return base

    # Check if the exponent is a negative number or a positive number
    # We also need to store the positive value of the exponent, so let's declare a
    # new variable to store the positive exponent, and a boolean to indicate whether
    # the exponent was negative or not
    positive_exponent = exponent
    exponent_is_negative = False

    # Check if the value is negative
    if exponent < 0:
        # Multiply the value by -1 to convert it to a positive number
        positive_exponent = exponent * -1
        exponent_is_negative = True

    # Check if the base is 0 and the exponent is negative
    # This is an illegal case
    if exponent_is_negative and base == 0:
        return False

    # Define the result variable
    result = 0

    # If the exponent is a simple integer, then we can calculate the power using the simple power function
    if isinstance(positive_exponent, int) or (positive_exponent).is_integer():
        result = math_helper.simple_pow(base, int(positive_exponent))
    # Otherwise, we must compute the power using the general formula stated above.
    else:
        log_result = math_helper.ln(base)
        exponent = positive_exponent * log_result
        result = math_helper.exp(exponent)

    # Now if the exponent was a negative value, we must calculate the inverse of the result
    if exponent_is_negative:
        result = 1 / result

    # Set the last answer value and return the answer    
    return result
# End function xExponentY


# formula based on: Beebe, N. H. (2017). 10.3.2. In The Mathematical-Function Computation Handbook: Programming Using the MathCW
# Portable Software Library (pp. 287-290). Springer International Publishing. doi:https://doi-org.lib-ezproxy.concordia.ca/10.1007/978-3-319-64110-2
# A simplified version of the formula is used here
def log10(x):
    ''' 
    Calculate log base 10 of x

    Date: May 25th 2020
    Author: Alexis Laurens-Renner - 40055137
    Transcendental function: log10(x)
    '''
    if (x <= 0):
        raise errors.IllegalArgumentError(x, 'log10(x)', "log10() is undefined for x = " + str(x))
    if (x == 1):
        return 0
    n = 0  # Start exponent of base 10
    while (x >= 1.0):
        x = x / 10.0
        n += 1
    while (x <= 0.316227766016838):
        x = x * 10.0
        n = n - 1
    # Produce a change of variable
    z = (x - 1.0) / (x + 1.0)
    D = 0.868588963807
    # Taylor series
    sum = z
    for k in range(3, 53, 2):
        sum += (pow(z, k)) / k
    return D * sum + n
#end of log10(X)


def standard_deviation(arr_of_ints):
    ''' 
    Calculate the standard deviation from a sample set of values expressed as an array of integer values

    Date: 2020-05-31
    Author: Jasmine Leblond-Chartrand
    Transcendental function: σ (Standard Deviation) 
    '''
    if len(arr_of_ints) == 1:
        return 0
    mean_val = math_helper.average(arr_of_ints)
    sum_sqr_diffs = 0
    for i in arr_of_ints:
        abs_diff = math_helper.absolute(i - mean_val)
        sum_sqr_diffs += math_helper.simple_pow(abs_diff, 2)
    return math_helper.square_root(sum_sqr_diffs / (len(arr_of_ints) - 1))
# End function Standard Deviation


def MAD(numList):
    '''
    Calculates Mean Aboslute Deviation (MAD)

    Author: Jeffrey Lam (40090989)
    Date: 2020-05-30
    '''
    average = math_helper.average(numList)
    difference = []
    abs_difference = []
    # Calculate the difference between each element and the average
    for num in numList:
        difference.append(num - average)
    # Converting the difference into absolute values
    for j in difference:
        abs_difference.append(math_helper.absolute(j))
    # Return average of absolute differences
    return math_helper.average(abs_difference)
# End function Mean Absolute Deviation (MAD)


def rad_sin(x):
    '''
    Computes the taylor series for Sin.
    Source: https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
    '''
    x = x %(2 * math_helper.compute_pi())
    out = 0
    sign = -1
    for i in range(1, 100, 2):
        sign = -sign
        out += sign * math_helper.int_pow(x,i)/math_helper.factorial_loop(i)
    return out


#   Same concesp as Cos, converts radSin by inputing (X+(Pi/2))
def rad_cos(x):
    return rad_sin(x + (math_helper.compute_pi() / 2))


#   converts input into Rad, then  runs radSin
def sin(x):
    x = math_helper.radian(x)
    return rad_sin(x)


#   Computes Cos by doing Sin(X + 90)
def cos(x):
    return sin(x + 90)


def pow_ten(exp):
    '''
    Calculates Exponent 10

    Author: William Kang (40099021)
    Date: 2020-06-02
    '''
    return power(10, exp)
# End function pow_ten


def cosh(x):
    '''
    Calculates hyperbolic cosine function (cosh)

    Author: Kyungjin Kim (40066802)
    Date: 2020-06-01
    '''
    return (math_helper.exp(x) + math_helper.exp(-x))/2
# End function cosh

# End module Transcendental