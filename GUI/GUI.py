# Python program to  create a simple GUI
# calculator using Tkinter

# import everything from tkinter module
from tkinter import *
from Calculator import Transcendental

# globally declare the entry variable
entry = ""
fullEntry = ""

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
    if eqValue == "^(":
        for i in range(len(fullEntry)-1,0,-1):
            if fullEntry[len(fullEntry)-1-i] == '+' or fullEntry[len(fullEntry)-1-i] == '-' or fullEntry[len(fullEntry)-1-i] == '*' or fullEntry[len(fullEntry)-1-i] == '/':

                s = fullEntry[len(fullEntry)-i:]
                fullEntry = fullEntry[:len(fullEntry)-i]
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

    # Put that code inside the try block
    # which may generate the error
    try:

        global entry, fullEntry
        complete()
        # eval function evaluate the entry
        # and str function convert the result
        # into string
        total = str(eval(fullEntry))

        equation.set(total)
        list.insert(END, entry+" = "+total)
        # initialze the entry variable
        # by empty string
        entry = ""
        fullEntry = ""

    # if error is generate then handle
    # by the except block
    except Exception as e:
        list.insert(END, entry + " = " + str(type(e)) + " " + str(e.args)+" / "+ str(e))
        equation.set(" error ")
        entry = ""
        fullEntry = ""

# Function to clear the contents
# of text entry box
def clear():
    global entry, fullEntry
    entry = ""
    fullEntry = ""
    equation.set("")


def complete():
    global entry, fullEntry
    #Fills the missing brackets
    counterE = 0
    for i in range(0, len(entry)):
        if entry[i] == '[':
            counterE = counterE + 1;
        elif entry[i] == ']':
            counterE = counterE - 1

    for i in range(0, counterE):
        entry = entry + ']'
        fullEntry = fullEntry + ']'

    #Fills the missing parentheses
    counterE = 0
    for i in range(0,len(entry)):
        if entry[i] == '(':
            counterE = counterE+1;
        elif entry[i] == ')':
            counterE = counterE - 1

    for i in range(0,counterE):
        entry = entry + ')'
        fullEntry = fullEntry + ')'


# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()


    log = Tk()
    log.title("User Log")

    list = Listbox(log, width = 200)
    list.grid(row = 0, column = 0)
    # set the background colour of GUI window
    gui.configure(background="light grey")
    gui.resizable(0,0)
    # set the title of GUI window
    gui.title("ETERNITY")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the entry .
    entry_field = Entry(gui, textvariable=equation)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    entry_field.grid(columnspan=4, ipadx=70)

    equation.set('')

    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(gui, text=' 1 ', fg='black', bg='white', command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='white', command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='white', command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    plus = Button(gui, text=' + ', fg='black', bg='white', command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    log10 = Button(gui, text=' log10( ', fg='black', bg='white', command=lambda: funcPress("Transcendental.log10(", "log10("), height=1, width=7)
    log10.grid(row=2, column=4)

    mad = Button(gui, text=' MAD([ ', fg='black', bg='white', command=lambda: funcPress("Transcendental.MAD([", "MAD(["), height=1, width=7)
    mad.grid(row=2, column=5)

    button4 = Button(gui, text=' 4 ', fg='black', bg='white', command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='white', command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='white', command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    minus = Button(gui, text=' - ', fg='black', bg='white', command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    sinx = Button(gui, text=' sin( ', fg='black', bg='white', command=lambda: funcPress("Transcendental.sin(", "sin("), height=1, width=7)
    sinx.grid(row=3, column=4)

    sd = Button(gui, text=' SD([ ', fg='black', bg='white', command=lambda: funcPress("Transcendental.standard_deviation([", "SD(["), height=1, width=7)
    sd.grid(row=3, column=5)

    button7 = Button(gui, text=' 7 ', fg='black', bg='white', command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='white', command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='white', command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    multiply = Button(gui, text=' * ', fg='black', bg='white', command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    cosh = Button(gui, text=' cosh( ', fg='black', bg='white', command=lambda: funcPress("Transcendental.cosh(", "cosh("), height=1, width=7)
    cosh.grid(row=4, column=4)

    button0 = Button(gui, text=' 0 ', fg='black', bg='white', command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)

    clear = Button(gui, text='Clear', fg='black', bg='white', command=clear, height=1, width=7)
    clear.grid(row=5, column=1)

    equal = Button(gui, text=' = ', fg='black', bg='white', command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)

    divide = Button(gui, text=' / ', fg='black', bg='white', command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    power10 = Button(gui, text=' 10^( ', fg='black', bg='white', command=lambda: funcPress("Transcendental.powTen(", "10^("), height=1, width=7)
    power10.grid(row=5, column=4)

    power = Button(gui, text=' ^ ', fg='black', bg='white', command=lambda: funcPress("Transcendental.power(", "^("), height=1, width=7)
    power.grid(row=5, column=5)

    Decimal = Button(gui, text='.', fg='black', bg='white', command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)

    closePar = Button(gui, text=' ) ', fg='black', bg='white', command=lambda: press(')'), height=1, width=7)
    closePar.grid(row=6, column=1)

    closeBrac = Button(gui, text=' ] ', fg='black', bg='white', command=lambda: press(']'), height=1, width=7)
    closeBrac.grid(row=6, column=2)

    coma = Button(gui, text=' , ', fg='black', bg='white', command=lambda: press(', '), height=1, width=7)
    coma.grid(row=6, column=3)



    # start the GUI
    def on_closing():
        gui.destroy()
        log.destroy()


    gui.protocol("WM_DELETE_WINDOW", on_closing)
    log.protocol("WM_DELETE_WINDOW", log.iconify)
    gui.mainloop()
    log.mainloop()

