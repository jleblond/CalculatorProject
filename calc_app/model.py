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
        self.full_entry += str(value)
        self.entry += str(eq_value)

    def evaluate_entry(self):
        # eval function evaluate the entry and str function convert the result into string
        if len(self.entry) == 0:
            return
        return str(round(eval(self.full_entry), 4))
