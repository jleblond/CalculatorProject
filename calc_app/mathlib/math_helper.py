'''
Helper methods to implement the core functions in `app.math.transcendental` module
'''

'''
SERIES_ITERATION_LIMIT : integer
    Constant limit to the number of iterations a series can perform.
'''
_SERIES_ITERATION_LIMIT = 9999

'''
FACTORIAL_ITERATION_LIMIT : integer
    Constant limit to how far the factorial calculation can be 
    reached using Python's primitive data types. A regular float 
    cannot store the factorial of 171 in memory.
'''
_FACTORIAL_ITERATION_LIMIT = 170

def exp(exponent):
    '''
    Calculate e to the power of the provided exponent.

    Author: Andrew Korolus (40055081)
    Date: 2020-05-23

    fExponent : float
        The exponent to be applied to Euler's number (e).
    '''
    # Define the loop iterator
    i = 0
    # Define the result
    result = 0
    # To calculate the exponential, we can use the sumation of i=0->inf [(fExponent^i) / i!]
    while i < _FACTORIAL_ITERATION_LIMIT:
        # Calculate the basic power for the numerator
        numerator = simple_pow(exponent, i)
        # Calculate the factorial for the demonimator
        denominator = factorial_recursive(i, 1)
        # Calculate this step's value
        step_value = numerator / denominator
        # Add up the values
        result += step_value
        # Increment the loop iterator
        i += 1
    return result


def ln(value):
    '''
    Calculate the natural logarithm of the provided value.

    Author: Andrew Korolus (40055081)
    Date: 2020-05-23

    fValue : float
        The value to be applied to the natural logarithm.
    '''
    # Negatives don't work for natural logs
    if value < 0: return False
    # Define the loop iterator
    i = 0
    # Define the result
    result = 0
    # To calculate the natural logarithm, we can use the sumation of i=0->inf [(2 / (2i + 1)) * ((val - 1) / (val + 1))^(2i + 1)]
    while i < _SERIES_ITERATION_LIMIT:
        step_value = (2 * i) + 1
        # Calculate the first part of the multiplication
        first_part = 2 / step_value
        # Calculate the second part of the muliplication
        step_base = (value - 1) / (value + 1)
        second_part = simple_pow(step_base, step_value)
        # Multiply the two parts together
        step_result = first_part * second_part
        # Sum up the values
        result += step_result
        # Increment the loop iterator
        i += 1
    return result


def factorial_recursive(value, accumulator = 1):
    '''
    Calculate the factorial of a number.
    This method uses tail recursion to save on function stacks.

    Author: Andrew Korolus (40055081)
    Date: 2020-05-23

    iValue : integer
        The value to be applied to the factorial.
    iAccumulator : integer 
        Keeping track of the current factorial value.
    '''
    # We require the value and the accumlator to be an integer
    if not isinstance(value, int) or not isinstance(accumulator, int): 
        return False
    # Negatives don't work for simple factorial
    if value < 0:
        return False
    elif value == 0:
        return 1
    elif value == 1:
        return accumulator
    else:
        return factorial_recursive(value - 1, value * accumulator)


def simple_pow(base, exponent):
    '''
    Calculate a simple power between a Real base and an integer exponent.
    A "simple" power, here, is defined as a^b, where b is a positive integer number.
    Algorithm used: Power Algorithm by Alvaro Videla

    Author: Andrew Korolus (40055081)
    Date: 2020-05-23

    fBase : float
        The base of the power function.
    iExponent : integer
        The exponent of the power function.
    '''
    # A simple power requires the exponent to be positive
    if exponent < 0:
        return False
    # A simple power also requires the exponent be an integer
    if not isinstance(exponent, int):
        return False
    # Define what we will be returning as our answer
    return_val = 1
    while True:
        test = exponent % 2
        exponent = int(exponent / 2)
        if test == 1:
            return_val *= base
        if exponent == 0:
            break
        base = base * base
    return return_val


def absolute(n):
    '''
    returns the absolute value of a number

    Author: Jasmine Leblond-Chartrand
    Date: 2020-05-31
    '''
    return n if n > 0 else (0 - n)


def square_root(n):
    # Using Newton Method for Square Root
    # Source: https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Example
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


def average(num_list):
    '''
    unweighted mean of a list of numbers

    Author: Jeffrey Lam
    Date: 2020-05-31
    '''
    total = 0
    for i in num_list:
        total += i
    avg = total/len(num_list)
    return avg


# Roman's Helper Functions
def compute_pi():
    '''
    Computes an estimation of pi; the result is copied into the pi function for quick reference.
    '''
    pi = 3
    sign = -1
    for i in range(2,500000,2):
        sign = -sign
        pi += sign*4/((i)*(i+1)*(i+2))
    return pi


def pi():
    '''
    This function returns the first 16 digits of Pi, as calculated by `compute_pi()`
    '''
    return 3.141592653589793


def int_pow(x, y):
    '''
    Simple multiplication loop to serve as a power function for integer exponents
    '''
    x = 1
    for _ in range(1, y+1):
        x *= x
    return x


def factorial_loop(x):
    '''
    Simple looping multiplication to return a factorial
    '''
    out = 1
    for i in range(1, x+1):
        out *= i
    return out


def radian(x):
    '''
    Converts from Degrees to Radians, required as the taylor series for Sin functions in Rad
    '''
    return x * compute_pi()/180


def degrees(x):
    '''
    Converts from Radians to Degrees
    '''
    return x * 180/compute_pi()