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
    _SERIES_ITERATION_LIMIT = sys.getrecursionlimit() - 50 # Seemed to crash at around 986, not sure why so I subtracted 50 to be safe...

    """
        _FACTORIAL_ITERATION_LIMIT : integer
            Constant limit to how far the factorial calculation can be reached using Python's primitive data types.    
    """
    _FACTORIAL_ITERATION_LIMIT = 170

    """
        Calculate e to the power of the provided exponent.

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

        iValue : integer
            The value to be applied to the factorial.
        iAccumulator : integer 
            Keeping track of the current factorial value.
    """
    @staticmethod
    def factorial(iValue, iAccumulator = 1):
        if iValue == 0: return 1
        elif iValue == 1: return iAccumulator
        else: return MathHelper.factorial(iValue - 1, iValue * iAccumulator)
    # End function factorial

    """
        Calculate a simple power between a Real base and an integer exponent.

        fBase : float
            The base of the power function.
        iExponent : integer
            The exponent of the power function.
    """
    @staticmethod
    def simplePow(fBase, iExponent):
        # Case 1: The exponent is equal to 0
        if iExponent == 0: 
            return 1

        # Case 2: The exponent is even
        elif iExponent % 2 == 0:
            iHalfedExponent = iExponent / 2
            return MathHelper.simplePow(fBase, iHalfedExponent) * MathHelper.simplePow(fBase, iHalfedExponent)

        # Case 3: The exponent is odd
        else:
            return fBase * MathHelper.simplePow(fBase, iExponent - 1)
    # End function simplePow

# End class MathHelper