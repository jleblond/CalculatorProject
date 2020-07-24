# import everything from tkinter module
from tkinter import *
import calc_app.mathlib.transcendental as transcendental
import calc_app.mathlib.math_helper as math_helper
import calc_app.util.log as log
import calc_app.util.errors as errors

# globally declare the entry variable
entry = ''
full_entry = ''
answer = ''


# Function to update entry
# in the text entry box
def press(eqValue):
    # point out the global entry variable
    global entry, full_entry
    # concatenation of string
    fullEntry = fullEntry + str(eqValue)
    entry = entry + str(eqValue)

    # update the entry by using set method
    equation.set(entry)


def funcPress(value, eqValue):
    # point out the global entry variable
    global entry, full_entry

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
    global entry, full_entry, answer
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
    global entry, full_entry
    entry = ''
    fullEntry = ''
    equation.set('')


def complete():
    global entry, full_entry
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


try:
    # Driver code
    # create a GUI window
    gui = Tk()
    lst = Listbox(gui, width = 25)
    lst.grid(row = 0, column = 7, rowspan=7)
    # set the background colour of GUI window
    gui.configure(background = 'light blue')
    gui.resizable(0, 0)
    # set the title of GUI window
    gui.title('ETERNITY')

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()
    # create the text entry box for
    # showing the entry .
    entry_field = Entry(gui, textvariable = equation)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    entry_field.grid(row = 0, columnspan = 4, ipadx = 54)

    equation.set('0')

    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(gui, text = ' 1 ', fg = 'black', bg = 'white', command = lambda: press(1), height = 1, width = 7)
    button1.grid(row = 2, column = 0)
    gui.bind('1', lambda event: press(1))

    button2 = Button(gui, text = ' 2 ', fg = 'black', bg = 'white', command = lambda: press(2), height = 1, width = 7)
    button2.grid(row = 2, column = 1)
    gui.bind('2', lambda event: press(2))

    button3 = Button(gui, text = ' 3 ', fg = 'black', bg = 'white', command = lambda: press(3), height = 1, width = 7)
    button3.grid(row = 2, column = 2)
    gui.bind('3', lambda event: press(3))

    plus = Button(gui, text = ' + ', fg = 'black', bg = 'white', command = lambda: press('+'), height = 1, width = 7)
    plus.grid(row = 2, column = 3)
    gui.bind('+', lambda event: press('+'))

    log10 = Button(gui, text = ' log10( ', fg = 'black', bg = 'white',
                   command = lambda: funcPress('transcendental.log10(', 'log10('), height = 1, width = 7)
    log10.grid(row = 4, column = 5)
    gui.bind('<Control-l>', lambda event: funcPress('transcendental.log10(', 'log10('))

    mad = Button(gui, text = ' MAD([ ', fg = 'black', bg = 'white',
                 command = lambda: funcPress('transcendental.MAD([', 'MAD(['), height = 1, width = 7)
    mad.grid(row = 2, column = 5)
    gui.bind('<Control-m>', lambda event: funcPress('transcendental.MAD([', 'MAD(['))

    button4 = Button(gui, text = ' 4 ', fg = 'black', bg = 'white', command = lambda: press(4), height = 1, width = 7)
    button4.grid(row = 3, column = 0)
    gui.bind('4', lambda event: press(4))

    button5 = Button(gui, text = ' 5 ', fg = 'black', bg = 'white', command = lambda: press(5), height = 1, width = 7)
    button5.grid(row = 3, column = 1)
    gui.bind('5', lambda event: press('5'))

    button6 = Button(gui, text = ' 6 ', fg = 'black', bg = 'white', command = lambda: press(6), height = 1, width = 7)
    button6.grid(row = 3, column = 2)
    gui.bind('6', lambda event: press('6'))

    minus = Button(gui, text = ' - ', fg = 'black', bg = 'white', command = lambda: press('-'), height = 1, width = 7)
    minus.grid(row = 3, column = 3)
    gui.bind('-', lambda event: press('-'))

    sinx = Button(gui, text = ' sin( ', fg = 'black', bg = 'white',
                  command = lambda: funcPress('transcendental.sin(', 'sin('), height = 1, width = 7)
    sinx.grid(row = 3, column = 4)
    gui.bind('<Control-s>', lambda event: funcPress('transcendental.sin(', 'sin('))

    sd = Button(gui, text = ' SD([ ', fg = 'black', bg = 'white',
                command = lambda: funcPress('transcendental.standard_deviation([', 'SD(['), height = 1, width = 7)
    sd.grid(row = 3, column = 5)
    gui.bind('<Control-Alt-s>', lambda event: funcPress('transcendental.standard_deviation([', 'SD(['))

    button7 = Button(gui, text = ' 7 ', fg = 'black', bg = 'white', command = lambda: press(7), height = 1, width = 7)
    button7.grid(row = 4, column = 0)
    gui.bind('7', lambda event: press(7))

    button8 = Button(gui, text = ' 8 ', fg = 'black', bg = 'white', command = lambda: press(8), height = 1, width = 7)
    button8.grid(row = 4, column = 1)
    gui.bind('8', lambda event: press(8))

    button9 = Button(gui, text = ' 9 ', fg = 'black', bg = 'white', command = lambda: press(9), height = 1, width = 7)
    button9.grid(row = 4, column = 2)
    gui.bind('9', lambda event: press(9))

    multiply = Button(gui, text = ' * ', fg = 'black', bg = 'white', command = lambda: press('*'), height = 1, width = 7)
    multiply.grid(row = 4, column = 3)
    gui.bind('*', lambda event: press('*'))

    cosh = Button(gui, text = ' cosh( ', fg = 'black', bg = 'white',
                  command = lambda: funcPress('transcendental.cosh(', 'cosh('), height = 1, width = 7)
    cosh.grid(row = 4, column = 4)
    gui.bind('<Control-c>', lambda event: funcPress('transcendental.cosh(', 'cosh('))

    button0 = Button(gui, text = ' 0 ', fg = 'black', bg = 'white', command = lambda: press(0), height = 1, width = 7)
    button0.grid(row = 5, column = 1)
    gui.bind('0', lambda event: press(0))

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
                     command = lambda: funcPress('transcendental.pow_ten(', '10^('), height = 1, width = 7)
    power10.grid(row = 5, column = 4)
    gui.bind('<Control-Alt-p>', lambda event: funcPress('transcendental.pow_ten(', '10^('))

    power = Button(gui, text = ' ^ ', fg = 'black', bg = 'white',
                   command = lambda: funcPress('transcendental.power(', '^('), height = 1, width = 7)
    power.grid(row = 5, column = 5)
    gui.bind('<Control-p>', lambda event: funcPress('transcendental.power(', '^('))
    gui.bind('^', lambda event: funcPress('transcendental.power(', '^('))

    Decimal = Button(gui, text = '.', fg = 'black', bg = 'white', command = lambda: press('.'), height = 1, width = 7)
    Decimal.grid(row = 5, column = 0)
    gui.bind('.', lambda event: press('.'))

    ansButton = Button(gui, text = 'Ans', fg = 'black', bg = 'white', command = lambda: press(answer), height = 1, width = 7)
    ansButton.grid(row = 2, column = 4)
    gui.bind('<Control-a>', lambda event: press(answer))

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