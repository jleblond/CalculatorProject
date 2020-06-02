from MathHelper import MathHelper

"""
    Contains the transcendental functions required for the operation of the ETERNITY calculator.

    Date: 2020-05-23
    Authors:
        Andrew Korolus (40055081)

"""

""" 
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
"""


def power(fBase, fExponent):
    # The first easy case is to check if the exponent is equal to 0
    # Any number to the power of 0 is equal to 1
    if fExponent == 0:
        self.fLastAnswer = 1
        return 1

    # Any power with a base 0 is equal to 0
    if fBase == 0:
        self.fLastAnswer = 0
        return 0

    # The second easy case is to check if the exponent is equal to 1
    # Any number to the power of 1 is equal to itself
    if fExponent == 1:
        self.fLastAnswer = fBase
        return fBase

        # Check if the exponent is a negative number or a positive number
    # We also need to store the positive value of the exponent, so let's declare a
    # new variable to store the positive exponent, and a boolean to indicate whether
    # the exponent was negative or not
    fPositiveExponent = fExponent
    bExponentIsNegative = False

    # Check if the value is negative
    if fExponent < 0:
        # Multiply the value by -1 to convert it to a positive number
        fPositiveExponent = fExponent * -1
        bExponentIsNegative = True
    # End if

    # Check if the base is 0 and the exponent is negative
    # This is an illegal case
    if bExponentIsNegative and fBase == 0:
        return False

    # Define the result variable
    fResult = 0

    # If the exponent is a simple integer, then we can calculate the power using the simple power function
    if isinstance(fPositiveExponent, int):
        fResult = MathHelper.simplePow(fBase, fPositiveExponent)
    # Otherwise, we must compute the power using the general formula stated above.
    else:
        fLogResult = MathHelper.ln(fBase)
        fExpExponent = fPositiveExponent * fLogResult
        fResult = MathHelper.exp(fExpExponent)
    # End if

    # Now if the exponent was a negative value, we must calculate the inverse of the result
    if bExponentIsNegative:
        fResult = 1 / fResult
    # End if

    # Set the last answer value and return the answer
    self.fLastAnswer = fResult
    return fResult


# End function xExponentY


""" 
       Calculate the standard deviation from a dataset expressed as an array of integer values

       Date: 2020-05-31
       Author: Jasmine Leblond-Chartrand
       Transcendental function: σ (Standard Deviation) 

"""


def standard_deviation(arr_of_ints):
    if len(arr_of_ints) == 1:
        return 0

    mean_val = MathHelper.average(arr_of_ints)
    sum_sqr_diffs = 0
    for i in arr_of_ints:
        abs_diff = MathHelper.absolute(i - mean_val)
        sum_sqr_diffs += MathHelper.exponential(abs_diff, 2)

    return MathHelper.square_root(sum_sqr_diffs / (len(arr_of_ints) - 1))


# End function Standard Deviation



"""
    Calculates Mean Aboslute Deviation (MAD)

    Author: Jeffrey Lam (40090989)
    Date: 2020-05-30

"""


def MAD(numList):
    average = MathHelper.average(numList)
    difference = []
    abs_difference = []

    # Calculate the difference between each element and the average
    for num in numList:
        difference.append(num - average)

    # Converting the difference into absolute values
    for j in difference:
        abs_difference.append(MathHelper.absolute(j))

    # Return average of absolute differences
    return MathHelper.average(abs_difference)

# End function Mean Absolute Deviation (MAD)