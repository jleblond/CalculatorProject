'''
Defines custom exception

Author: Alexis Laurens-Renner 40055137
Date: 2020-07-03
'''
class IllegalArgumentError(Exception):
    '''
    Used for all illegal arguments passed to the functions
    takes the value of the faulty argument as val
    takes the function associated as func
    can take a custom message for the Log if needed
    '''
    def __init__(self, val, func, message = "Illegal Argument"):
        self.val = val
        self.message = message
        self.func = func
        super().__init__(self.message)

class NotSupportedError(Exception):
    '''
    Used for specific operations/actions that ETERNITY does not yet support to avoid a system crash
    '''
    def __init__(self, message = "Unsupported"):
        self.message = message
        super().__init__(self.message)