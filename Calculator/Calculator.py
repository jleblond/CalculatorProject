from MathHelper.MathHelper import MathHelper

"""
    Contains the transcendental functions required for the operation of the ETERNITY calculator.

    Date: 2020-05-23
    Authors:
        Andrew Korolus (40055081)

"""
class Calculator:

    """
        Default constructor for the Calculator class.
        Simply initializes the fLastAnswer to 0
    """
    def __init__(self):
        # To store the last calculated answer to a function.
        self.fLastAnswer = 0        
    # End function __init__

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
    def power(self, fBase, fExponent):

        # The first easy case is to check if the exponent is equal to 0
        # Any number to the power of 0 is equal to 1
        if fExponent == 0: 
            self.fLastAnswer = 1
            return 1
        
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

        # Define the result variable
        fResult = 0

        # If the exponent is a simple integer, then we can calculate the power using the simple power function
        if isinstance(fPositiveExponent, int) :
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
        Calculates Mean Aboslute Deviation (MAD)

        Author: Jeffrey Lam (40090989)
        Date: 2020-05-30
        
    """

    @staticmethod
    def MAD(numList):
        average = MathHelper.average(numList)
        difference = []
        abs_difference = []

        #Calculate the difference between each element and the average
        for num in numList:
            difference.append(num - average)

        #Converting the difference into absolute values
        for j in difference:
            abs_difference.append(abs(j)) 
        
        #Return average of absolute differences
        return average(abs_difference)

    # End function Mean Absolute Deviation (MAD)

# End class Calculator