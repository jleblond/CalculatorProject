class IllegalArgumentError(Exception):
    def __init__(self, val, func, message = ""):
        self.val = val
        self.message = message
        self.func = func
        super().__init__(self.message)