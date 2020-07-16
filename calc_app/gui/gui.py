# import everything from tkinter module
from tkinter import *
import app.math as transcendental
import app.math.math_helper as math_helper
import app.util.log as log
import app.util.errors as errors

class CalculatorModel:
    def __init__(self):
        self.entry = ''
        self.full_entry = ''
        self.ans = ''

class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def value_pressed(self, value):
        self.model.full_entry = self.model.full_entry + str(value)
        self.model.entry = self.model.entry + str(value)


# globally declare the entry variable
entry = ''
fullEntry = ''
ans = ''


# Function to update entry
# in the text entry box
def press(eqValue):
    # point out the global entry variable
    global entry, fullEntry
    # concatenation of string
    fullEntry = fullEntry + str(eqValue)
    entry = entry + str(eqValue)

    # update the entry by using set method
    equation.set(entry)


def funcPress(value, eqValue):
    # point out the global entry variable
    global entry, fullEntry

    # concatenation of string
    # handling of the power function is tricky as we need to find the first argument for the function in fullEntry. For the time being, this function does not support chaining within other functions
    #We find the last full number
    if eqValue == '^(':
        #interate backards in fullEntry to find the last operator that is not defined in MathHelper or transcendental
        for i in range(len(fullEntry) - 1, 0, -1):
            if fullEntry[len(fullEntry) - 1 - i] == '+' or fullEntry[len(fullEntry) - 1 - i] == '-' or fullEntry[len(fullEntry) - 1 - i] == '*' or fullEntry[len(fullEntry) - 1 - i] == '/':
                #if found, use that as the first argument of the power function
                s = fullEntry[len(fullEntry) - i:]
                fullEntry = fullEntry[:len(fullEntry) - i]
                fullEntry = fullEntry + str(value) + str(s) + ','
                entry = entry + str(eqValue)
                break
        else:
            s = fullEntry
            fullEntry = str(value) + str(s) + ','
            entry = entry + str(eqValue)
    else:
        fullEntry = fullEntry + str(value)
        entry = entry + str(eqValue)

    # update the entry by using set method
    equation.set(entry)


# Function to evaluate the final entry
def equalpress():
    # Try and except statement is used
    # for handling syntax errors, invalid values is checked inside the function itself
    global entry, fullEntry, ans
    # Put that code inside the try block
    # which may generate the error
    try:
        complete()
        # eval function evaluate the entry
        # and str function convert the result
        # into string
        if len(entry) == 0:
            return
        total = str(eval(fullEntry))

        equation.set(total)
        ins = entry + ' =  ' + total
        while len(ins) > 25:
            lst.insert(END, ins[0:25])
            ins = ins[25:len(ins)]
        lst.insert(END, ins)
        lst.yview(END)
        ans = total
        log.success_calc(entry,total)
        # initialize the entry variable
        # by empty string
        entry = ''
        fullEntry = ''

    # if error is generate then handle
    # by the except block
    except Exception as e:
        ins = entry + ' = Error - ' + str(e.args[0])
        while len(ins) > 25:
            lst.insert(END, ins[0:25])
            ins = ins[25:len(ins)]
        lst.insert(END, ins)
        lst.yview(END)
        log.error_calc(entry, e)
        equation.set(' Error ')
        entry = ''
        fullEntry = ''


# Function to clear the contents
# of text entry box
def clear():
    global entry, fullEntry
    entry = ''
    fullEntry = ''
    equation.set('')


def complete():
    global entry, fullEntry
    # Fills the missing brackets
    counterE = 0
    for i in range(0, len(entry)):
        if entry[i] == '[':
            counterE = counterE + 1
        elif entry[i] == ']':
            counterE = counterE - 1

    for i in range(0, counterE):
        entry = entry + ']'
        fullEntry = fullEntry + ']'

    # Fills the missing parentheses
    counterE = 0
    for i in range(0, len(entry)):
        if entry[i] == '(':
            counterE = counterE + 1
        elif entry[i] == ')':
            counterE = counterE - 1

    for i in range(0, counterE):
        entry = entry + ')'
        fullEntry = fullEntry + ')'

class CalculatorView:
    def __init__(self):
        # main window
        self.gui = Tk()
        self.gui.title('ETERNITY')
        self.gui.configure(bg='light blue')
        self.gui.resizable(0,0)

        # listbox on the side
        self.lst = Listbox(self.gui, width=25)
        self.lst.grid(row=0, column=7, rowspan=7)

        # textbox for inputs
        self.equation = StringVar()
        #self.equation.set('0')
        entry_field = Entry(self.gui, textvariable=self.equation)
        entry_field.grid(row=0, columnspan=4, ipadx=54)

        # numeric input buttons
        self.add_numeric_buttons()

        # auxilary buttons
        self.add_value_button(' . ', 5, 0, press, '.', '.')
        self.add_value_button(' , ', 5, 2, press, ',', ',')
        self.add_value_button(' ( ', 6, 0, press, '(', '(')
        self.add_value_button(' ) ', 6, 1, press, ')', ')')
        #self.add_value_button(' [ ', 6, 2, press, '[', '[')
        #self.add_value_button(' [ ', 6, 3, press, ']', ']')

        # basic operands
        self.add_value_button(' + ', 2, 3, press, '+', '+')
        self.add_value_button(' - ', 3, 3, press, '-', '-')
        self.add_value_button(' * ', 4, 3, press, '*', '*')
        self.add_value_button(' / ', 5, 3, press, '/', '/')

        # transcendental
        self.add_value_button('')


    def add_value_button(self, text, row, column, command, event, *command_args):
        '''
        helper method - adds a button with predefined specifications
        
        - text: str - label on the button
        - row: int - horizontal location of the button
        - column: int - vertical location of the button
        - command: func - to be executed upon press
        - event: str - tkinter keyboard command associated with this button
        - *command_args - variable length arguments for command.
        '''
        button = Button(self.gui, text=text, fg='black', bg='white', command=lambda: command(*command_args), height = 1, width = 7)
        button.grid(row=row, column=column)
        print(event, command, *command_args)
        self.gui.bind(event, lambda: command(*command_args))
    

    def add_numeric_buttons(self):
        '''
        helper method: adds 0 ~ 9 buttons.
        '''
        for i in range(1, 10):
            row_index = ((i - 1) // 3) + 2
            column_index = (i + 2) % 3
            print(i, row_index, column_index)
            self.add_value_button(f' {i} ', row_index, column_index, press, str(i), str(i))
        self.add_value_button(' 0 ', 5, 1, press, '0', '0')
        

try:

    log10 = Button(gui, text = ' log10( ', fg = 'black', bg = 'white',
                   command = lambda: funcPress('transcendental.log10(', 'log10('), height = 1, width = 7)
    log10.grid(row = 4, column = 5)
    gui.bind('<Control-l>', lambda event: funcPress('transcendental.log10(', 'log10('))

    mad = Button(gui, text = ' MAD([ ', fg = 'black', bg = 'white',
                 command = lambda: funcPress('transcendental.MAD([', 'MAD(['), height = 1, width = 7)
    mad.grid(row = 2, column = 5)
    gui.bind('<Control-m>', lambda event: funcPress('transcendental.MAD([', 'MAD(['))

    sinx = Button(gui, text = ' sin( ', fg = 'black', bg = 'white',
                  command = lambda: funcPress('transcendental.sin(', 'sin('), height = 1, width = 7)
    sinx.grid(row = 3, column = 4)
    gui.bind('<Control-s>', lambda event: funcPress('transcendental.sin(', 'sin('))

    sd = Button(gui, text = ' SD([ ', fg = 'black', bg = 'white',
                command = lambda: funcPress('transcendental.standard_deviation([', 'SD(['), height = 1, width = 7)
    sd.grid(row = 3, column = 5)
    gui.bind('<Control-Alt-s>', lambda event: funcPress('transcendental.standard_deviation([', 'SD(['))

    cosh = Button(gui, text = ' cosh( ', fg = 'black', bg = 'white',
                  command = lambda: funcPress('transcendental.cosh(', 'cosh('), height = 1, width = 7)
    cosh.grid(row = 4, column = 4)
    gui.bind('<Control-c>', lambda event: funcPress('transcendental.cosh(', 'cosh('))

    clearButton = Button(gui, text = 'Clear', fg = 'black', bg = 'white', command = clear, height = 1, width = 7)
    clearButton.grid(row = 0, column = 5)
    gui.bind('<BackSpace>', lambda event: clear())

    equal = Button(gui, text = ' = ', fg = 'black', bg = 'white', command = equalpress, height = 1, width = 7)
    equal.grid(row = 0, column = 4)
    gui.bind('=', lambda event: equalpress())
    gui.bind('<Return>', lambda event: equalpress())

    divide = Button(gui, text = ' / ', fg = 'black', bg = 'white', command = lambda: press('/'), height = 1, width = 7)
    divide.grid(row = 5, column = 3)
    gui.bind('/', lambda event: press('/'))

    power10 = Button(gui, text = ' 10^( ', fg = 'black', bg = 'white',
                     command = lambda: funcPress('transcendental.powTen(', '10^('), height = 1, width = 7)
    power10.grid(row = 5, column = 4)
    gui.bind('<Control-Alt-p>', lambda event: funcPress('transcendental.powTen(', '10^('))

    power = Button(gui, text = ' ^ ', fg = 'black', bg = 'white',
                   command = lambda: funcPress('transcendental.power(', '^('), height = 1, width = 7)
    power.grid(row = 5, column = 5)
    gui.bind('<Control-p>', lambda event: funcPress('transcendental.power(', '^('))
    gui.bind('^', lambda event: funcPress('transcendental.power(', '^('))

    Decimal = Button(gui, text = '.', fg = 'black', bg = 'white', command = lambda: press('.'), height = 1, width = 7)
    Decimal.grid(row = 5, column = 0)
    gui.bind('.', lambda event: press('.'))

    ansButton = Button(gui, text = 'Ans', fg = 'black', bg = 'white', command = lambda: press(ans), height = 1, width = 7)
    ansButton.grid(row = 2, column = 4)
    gui.bind('<Control-a>', lambda event: press(ans))

    openPar = Button(gui, text = ' ( ', fg = 'black', bg = 'white', command = lambda: press('('), height = 1, width = 7)
    openPar.grid(row = 6, column = 0)
    gui.bind('(', lambda event: press('('))

    closePar = Button(gui, text = ' ) ', fg = 'black', bg = 'white', command = lambda: press(')'), height = 1, width = 7)
    closePar.grid(row = 6, column = 1)
    gui.bind(')', lambda event: press(')'))

    openBrac = Button(gui, text = ' [ ', fg = 'black', bg = 'white', command = lambda: press('['), height = 1, width = 7)
    openBrac.grid(row = 6, column = 2)
    gui.bind('[', lambda event: press('['))

    closeBrac = Button(gui, text = ' ] ', fg = 'black', bg = 'white', command = lambda: press(']'), height = 1, width = 7)
    closeBrac.grid(row = 6, column = 3)
    gui.bind(']', lambda event: press(']'))

    coma = Button(gui, text = ' , ', fg = 'black', bg = 'white', command = lambda: press(', '), height = 1, width = 7)
    coma.grid(row = 5, column = 2)
    gui.bind(',', lambda event: press(', '))

    displayPi = Button(gui, text = ' \u03C0 ', fg = 'black', bg = 'white', command = lambda: funcPress('math_helper.compute_pi()','\u03C0'), height = 1,
                       width = 7)
    displayPi.grid(row = 6, column = 4)
    #gui.bind(']', lambda event: press(']'))

    sqrt = Button(gui, text = ' \u221A ', fg = 'black', bg = 'white', command = lambda: funcPress('math_helper.square_root(', '\u221A('), height = 1,
                       width = 7)
    sqrt.grid(row = 6, column = 5)
    #gui.bind(']', lambda event: press(']'))


    gui.bind('<Escape>', lambda event: gui.iconify())

    ''''
    def on_closing():
        gui.destroy()
    gui.protocol('WM_DELETE_WINDOW', on_closing)
    '''
    # start the GUI
    gui.mainloop()

# For Calculation related errors, display them in log.txt
# For other errors, specifically to GUI design related errors, system will crash
except (SyntaxError, ZeroDivisionError, errors.IllegalArgumentError) as e:
    log.error_calc('', e)
except errors.NotSupportedError as e:
    log.error_eternity(e)
except Exception as e:
    log.critical_eternity(e)
