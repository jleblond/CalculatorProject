import sys

"""
    _SERIES_ITERATION_LIMIT : integer
        Constant limit to the number of iterations a series can perform.
"""
_SERIES_ITERATION_LIMIT = 9999

"""
    _FACTORIAL_ITERATION_LIMIT : integer
        Constant limit to how far the factorial calculation can be reached using Python's primitive data types.
        A regular float cannot store the factorial of 171 in memory.
"""
_FACTORIAL_ITERATION_LIMIT = 170

"""
    Calculate e to the power of the provided exponent.

    Author: Andrew Korolus (40055081)
    Date: 2020-05-23

    fExponent : float
        The exponent to be applied to Euler's number (e).
"""
def exp(fExponent):
    # Define the loop iterator
    i = 0

    # Define the result
    fResult = 0

    # To calculate the exponential, we can use the sumation of i=0->inf [ (fExponent^i) / i! ]
    while i < _FACTORIAL_ITERATION_LIMIT:
        # Calculate the basic power for the numerator
        fNumerator = simplePow(fExponent, i)

        # Calculate the factorial for the demonimator
        iDemoninator = factorial(i, 1)
        
        # Calculate this step's value
        fStepValue = fNumerator / iDemoninator

        # Add up the values
        fResult += fStepValue

        # Increment the loop iterator
        i += 1
    # End while

    # Return the result
    return fResult
# End function exp

"""
    Calculate the natural logarithm of the provided value.

    Author: Andrew Korolus (40055081)
    Date: 2020-05-23

    fValue : float
        The value to be applied to the natural logarithm.
"""
def ln(fValue):
    # Negatives don't work for natural logs
    if fValue < 0: return False
    
    # Define the loop iterator
    i = 0

    # Define the result
    fResult = 0

    # To calculate the natural logarithm, we can use the sumation of i=0->inf [ ( 2 / (2i + 1) ) * ( ( fVal -1 ) / ( fVal + 1 ) )^( 2i + 1 ) ]
    while i < _SERIES_ITERATION_LIMIT:
        iStepValue = (2 * i) + 1
        
        # Calculate the first part of the multiplication
        fFirstPart = 2 / iStepValue

        # Calculate the second part of the muliplication
        fStepBase = (fValue - 1) / (fValue + 1)
        fSecondPart = simplePow(fStepBase, iStepValue)
        
        # Multiply the two parts together
        fStepResult = fFirstPart * fSecondPart
                    
        # Sum up the values
        fResult += fStepResult
        
        # Increment the loop iterator
        i += 1
    # End while

    # Return the result
    return fResult
# End function ln

"""
    Calculate the factorial of a number.
    This method uses tail recursion to save on function stacks.

    Author: Andrew Korolus (40055081)
    Date: 2020-05-23

    iValue : integer
        The value to be applied to the factorial.
    iAccumulator : integer 
        Keeping track of the current factorial value.
"""
def factorial(iValue, iAccumulator = 1):
    # We require the value be an integer
    if isinstance(iValue, int) == False: return False

    # We require the accumulator be an integer as well
    if isinstance(iAccumulator, int) == False: return False
    
    # Negatives don't work for simple factorial
    if iValue < 0: return False
    
    if iValue == 0: return 1
    elif iValue == 1: return iAccumulator
    else: return factorial(iValue - 1, iValue * iAccumulator)
# End function factorial

"""
    Calculate a simple power between a Real base and an integer exponent.
    A "simple" power, here, is defined as a^b, where b is a positive integer number.
    Algorithm used: Power Algorithm by Alvaro Videla

    Author: Andrew Korolus (40055081)
    Date: 2020-05-23

    fBase : float
        The base of the power function.
    iExponent : integer
        The exponent of the power function.
"""
def simplePow(fBase, iExponent):
    # A simple power requires the exponent to be positive
    if iExponent < 0: return False

    # A simple power also requires the exponent be an integer
    if isinstance(iExponent, int) == False: return False
    
    # Define what we will be returning as our answer
    fReturnVal = 1

    while True:
        fTest = iExponent % 2
        iExponent = int(iExponent / 2)

        if fTest == 1:
            fReturnVal *= fBase
        
        if iExponent == 0:
            break
        
        fBase = fBase * fBase
    # End while

    return fReturnVal
# End function simplePow


"""
    Author: Jasmine Leblond-Chartrand
    Date: 2020-05-31
"""


def exponential(a, b):
    result = 1
    for i in range(b):
        result *= a
    return result


def absolute(n):
    return n if n > 0 else (0 - n)

def square_root(n):
    # using Newton Method for Square Root
    # source: https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Example

    if n == 0:
        return 0
    elif n < 0:
        raise Exception("Square root of negative number impossible" )

    x_prev = n
    precision_value = 0.0001
    x = 0
    while(True):
        x = (x_prev + n/x_prev)/2
        if absolute(x_prev - x) < precision_value:
            return x
        x_prev = x



def average(numList):
    total = 0
    for i in numList:
        total += i

    avg = total/len(numList)

    return avg
# End function average
    
# End class MathHelper



