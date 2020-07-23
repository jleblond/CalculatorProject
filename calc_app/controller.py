import tkinter
from calc_app.model import *
from calc_app.view import *
import calc_app.util.log as log
import calc_app.util.errors as errors
import pdb

class Controller():
    def __init__(self):
        self.root = tkinter.Tk()
        self.model = Model()
        self.view = View(self.root)
        self.listbox_view = ListBoxView(self.root)

        # StringVar() is the variable class - we create an instance of this class
        self.equation = tkinter.StringVar()
        # create the text entry box for showing the entry .
        self.entry_field = tkinter.Entry(self.root, textvariable=self.equation)

        # grid method is used for placing the widgets at respective positions in table like structure .
        self.entry_field.grid(row=0, columnspan=4, ipadx=54)

        self.equation.set('0')

        self.configure_commands()
        self.bind_keys()

    def run(self):
        self.root.title("ETERNITY")
        self.root.configure(background='light blue')
        self.root.resizable(0, 0)
        self.root.deiconify()
        self.root.mainloop()

    def config_button_press(self, button, press_arg):
        button.config(command=lambda: self.press(press_arg))

    def config_button_func_press(self, button, arg1, arg2):
        button.config(command=lambda: self.func_press(arg1, arg2))

    def configure_commands(self):
        for index in range(len(self.view.number_buttons)):
            self.config_button_press(self.view.number_buttons[index], index)

        for index, key in enumerate(self.view.transcendental_buttons_attrs):
            command_args = self.view.transcendental_buttons_attrs[key]['command_args']
            self.config_button_func_press(self.view.transcendental_buttons[index], command_args[0], command_args[1])

        for index, key in enumerate(self.view.math_helper_buttons_attrs):
            command_args = self.view.math_helper_buttons_attrs[key]['command_args']
            self.config_button_func_press(self.view.math_helper_buttons[index], command_args[0], command_args[1])

        for index, key in enumerate(self.view.math_buttons_attrs):
            press_arg = self.view.math_buttons_attrs[key]['text'].strip()
            self.config_button_press(self.view.math_buttons[index], press_arg)

        for index, key in enumerate(self.view.other_char_buttons_attrs):
            press_arg = self.view.other_char_buttons_attrs[key]['text'].strip()
            self.config_button_press(self.view.other_char_buttons[index], press_arg)

        self.view.answer_button.config(command=lambda: self.press(self.model.answer))
        self.view.clear_button.config(command=lambda: self.clear())
        self.view.equal.config(command=lambda: self.equal_press())

    def bind_key_simple_button(self, button_value):
        str_button_value = str(button_value)
        self.root.bind(str_button_value, lambda event: self.press(str_button_value))

    def bind_keys(self):
        for i in range(len(self.view.number_buttons)):
            self.bind_key_simple_button(i)

        simple_operator_keys = [',', '.', '+', '-', '*', '/', '(', ')', '[', ']']
        for i in range(len(simple_operator_keys)):
            self.bind_key_simple_button(simple_operator_keys[i])

        self.root.bind('<Escape>', lambda event: self.root.iconify())
        self.root.bind('<Return>', lambda event: self.equal_press())
        self.root.bind('<BackSpace>', lambda event: self.clear())

        self.root.bind('<Control-l>', lambda event: self.func_press('transcendental.log10(', 'log10('))
        self.root.bind('<Control-m>', lambda event: self.func_press('transcendental.MAD([', 'MAD(['))
        self.root.bind('<Control-s>', lambda event: self.func_press('transcendental.sin(', 'sin('))
        self.root.bind('<Control-Alt-s>', lambda event: self.func_press('transcendental.standard_deviation([', 'SD(['))
        self.root.bind('<Control-c>', lambda event: self.func_press('transcendental.cosh(', 'cosh('))
        self.root.bind('<Control-Alt-p>', lambda event: self.func_press('transcendental.pow_ten(', '10^('))
        self.root.bind('<Control-p>', lambda event: self.func_press('transcendental.power(', '^('))
        self.root.bind('^', lambda event: self.func_press('transcendental.power(', '^('))

        self.root.bind('<Control-a>', lambda event: self.press(self.model.answer))


    # Function to clear the contents of text entry box
    def clear(self):
        self.model.reset_entries()
        self.equation.set('')

    # Function to update entry in the text entry box
    def press(self, eq_value):
        self.model.update_entry(eq_value)
        self.equation.set(self.model.entry)

    def func_press(self, value, eq_value):
        self.model.apply_function(value, eq_value)

        # update the entry by using set method
        self.equation.set(self.model.entry)

    # Function to evaluate the final entry
    def equal_press(self):
        # Put that code inside the try block
        # which may generate the error
        try:
            self.complete()

            total = self.model.evaluate_entry()
            self.equation.set(total)

            ins = self.model.entry + ' =  ' + total
            while len(ins) > 25:
                self.listbox_view.insert(tkinter.END, ins[0:25])
                ins = ins[25:len(ins)]
            self.listbox_view.insert(tkinter.END, ins)
            self.listbox_view.yview(tkinter.END)

            self.model.answer = total
            log.success_calc(self.model.entry, total)

            # initialize the entry variable  by empty string
            self.model.reset_entries()

        # if error is generate then handle
        # by the except block
        except Exception as e:
            ins = self.model.entry + ' = Error - ' + str(e.args[0])
            while len(ins) > 25:
                self.listbox_view.insert(tkinter.END, ins[0:25])
                ins = ins[25:len(ins)]
            self.listbox_view.insert(tkinter.END, ins)
            self.listbox_view.yview(tkinter.END)
            log.error_calc(self.model.entry, e)
            self.equation.set(' Error ')
            self.model.reset_entries()


    def complete(self):
        self.model.fill_missing_bracket()
        self.model.fill_missing_parenthesis()