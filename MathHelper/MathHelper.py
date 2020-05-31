import sys

"""
    Contains helper functions related to basic arithmetic.

    Date: 2020-05-23
    Authors:
        Andrew Korolus (40055081)
"""
class MathHelper:

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
    @staticmethod
    def exp(fExponent):
        # Define the loop iterator
        i = 0

        # Define the result
        fResult = 0

        # To calculate the exponential, we can use the sumation of i=0->inf [ (fExponent^i) / i! ]
        while i < MathHelper._FACTORIAL_ITERATION_LIMIT:
            # Calculate the basic power for the numerator
            fNumerator = MathHelper.simplePow(fExponent, i)

            # Calculate the factorial for the demonimator
            iDemoninator = MathHelper.factorial(i, 1)
            
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
    @staticmethod
    def ln(fValue):
        # Negatives don't work for natural logs
        if fValue < 0: return False
        
        # Define the loop iterator
        i = 0

        # Define the result
        fResult = 0

        # To calculate the natural logarithm, we can use the sumation of i=0->inf [ ( 2 / (2i + 1) ) * ( ( fVal -1 ) / ( fVal + 1 ) )^( 2i + 1 ) ]
        while i < MathHelper._SERIES_ITERATION_LIMIT:
            iStepValue = (2 * i) + 1
            
            # Calculate the first part of the multiplication
            fFirstPart = 2 / iStepValue

            # Calculate the second part of the muliplication
            fStepBase = (fValue - 1) / (fValue + 1)
            fSecondPart = MathHelper.simplePow(fStepBase, iStepValue)
            
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
    @staticmethod
    def factorial(iValue, iAccumulator = 1):
        # We require the value be an integer
        if isinstance(iValue, int) == False: return False

        # We require the accumulator be an integer as well
        if isinstance(iAccumulator, int) == False: return False
        
        # Negatives don't work for simple factorial
        if iValue < 0: return False
        
        if iValue == 0: return 1
        elif iValue == 1: return iAccumulator
        else: return MathHelper.factorial(iValue - 1, iValue * iAccumulator)
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
    @staticmethod
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
        Calculates a power of base 10.
        Calls simplePow Function.

        Author: William Kang (40099021)
        Date: 2020-05-30
        
    """
    
    @staticmethod
    def powTen(x):
        return MathHelper.simplePow(10, x)
    # End function powTen

    """
        Calculates average of given list

        Author: Jeffrey Lam (40090989)
        Date: 2020-05-30
        
    """

    @staticmethod
    def average(numList):
        for i in numList:
            total += i
        
        avg = total/len(numList)

        return avg
    # End function average
    
# End class MathHelper
