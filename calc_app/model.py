import calc_app.mathlib.transcendental as transcendental
import calc_app.mathlib.math_helper as math_helper

class Model():
    def __init__(self):
        self.full_entry = ''
        self.entry = ''
        self.answer = ''

    def reset_entries(self):
        self.full_entry = ''
        self.entry = ''

    def full_reset(self):
        self.reset_entries()
        self.answer = ''

    def update_entry(self, eq_value):
        self.full_entry += str(eq_value)
        self.entry += str(eq_value)

    def fill_missing_bracket(self):
        counter_e = 0
        for i in range(0, len(self.entry)):
            if self.entry[i] == '[':
                counter_e += 1
            elif self.entry[i] == ']':
                counter_e -= 1

        for _ in range(0, counter_e):
            self.update_entry(']')

    def fill_missing_parenthesis(self):
        counter_e = 0
        for i in range(0, len(self.entry)):
            if self.entry[i] == '(':
                counter_e += 1
            elif self.entry[i] == ')':
                counter_e -= 1

        for _ in range(0, counter_e):
            self.update_entry(')')

    def apply_function(self, value, eq_value):
        # concatenation of string
        # handling of the power function is tricky as we need to find the first argument for the function in fullEntry. For the time being, this function does not support chaining within other functions
        # We find the last full number
        if eq_value == '^(':
            # interate backards in fullEntry to find the last operator that is not defined in MathHelper or transcendental
            for i in range(len(self.full_entry) - 1, 0, -1):
                if self.full_entry[len(self.full_entry) - 1 - i] == '+' \
                        or self.full_entry[len(self.full_entry) - 1 - i] == '-' \
                        or self.full_entry[len(self.full_entry) - 1 - i] == '*' \
                        or self.full_entry[len(self.full_entry) - 1 - i] == '/':
                    # if found, use that as the first argument of the power function
                    s = self.full_entry[len(self.full_entry) - i:]
                    self.full_entry = self.full_entry[:len(self.full_entry) - i]
                    self.full_entry = self.full_entry + str(value) + str(s) + ','
                    self.entry += str(eq_value)
                    break
            else:
                s = self.full_entry
                self.full_entry = str(value) + str(s) + ','
                self.entry += str(eq_value)
        else:
            self.full_entry += str(value)
            self.entry += str(eq_value)

    def evaluate_entry(self):
        # eval function evaluate the entry and str function convert the result into string
        if len(self.entry) == 0:
            return
        return str(eval(self.full_entry))
