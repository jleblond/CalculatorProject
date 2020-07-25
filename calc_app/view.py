import tkinter


class ListBoxView(tkinter.Toplevel):
    def __init__(self, master):
        self.listbox = tkinter.Listbox(master, width=25)
        self.listbox.grid(row=0, column=7, rowspan=7)

    def insert(self, ins1, ins2):
        self.listbox.insert(ins1, ins2)

    def yview(self, v1):
        self.listbox.yview(v1)


class View(tkinter.Toplevel):
    def __init__(self, master):
        self.number_buttons = []
        self.transcendental_buttons = []
        self.math_helper_buttons = []
        self.math_buttons = []
        self.other_char_buttons = []

        self.number_buttons_attrs = {
            0: {'row': 5, 'column': 1},
            1: {'row': 2, 'column': 0},
            2: {'row': 2, 'column': 1},
            3: {'row': 2, 'column': 2},
            4: {'row': 3, 'column': 0},
            5: {'row': 3, 'column': 1},
            6: {'row': 3, 'column': 2},
            7: {'row': 4, 'column': 0},
            8: {'row': 4, 'column': 1},
            9: {'row': 4, 'column': 2},
        }
        self.transcendental_buttons_attrs = {
            'mad': {'text': ' MAD([ ', 'row': 2, 'column': 5, 'command_args': ['transcendental.MAD([', 'MAD([']},
            'sinx': {'text': ' sin( ', 'row': 3, 'column': 4, 'command_args': ['transcendental.rad_sin(', 'sin(']},
            'sd': {'text': ' SD([ ', 'row': 3, 'column': 5, 'command_args': ['transcendental.standard_deviation([', 'SD([']},
            'cosh': {'text': ' cosh(', 'row': 4, 'column': 4, 'command_args': ['transcendental.cosh(', 'cosh(']},
            'log10': {'text': 'log10( ', 'row': 4, 'column': 5, 'command_args': ['transcendental.log10(', 'log10(']},
            'power10': {'text': ' pow10 ', 'row': 5, 'column': 4, 'command_args': ['transcendental.pow_ten(', 'pow10(']},
            'power': {'text': ' pow( ', 'row': 5, 'column': 5, 'command_args': ['transcendental.power(', 'pow(']},
        }
        self.math_helper_buttons_attrs = {
            'pi': {'text': ' \u03C0 ', 'row': 6, 'column': 4, 'command_args': ['math_helper.compute_pi()', '\u03C0']},
            'sqrt': {'text': ' \u221A ', 'row': 6, 'column': 5, 'command_args': ['math_helper.square_root(', '\u221A(']}
        }
        self.math_buttons_attrs = {
            'plus': {'text': ' + ', 'row': 2, 'column': 3},
            'minus': {'text': ' - ', 'row': 3, 'column': 3},
            'multiply': {'text': ' * ', 'row': 4, 'column': 3},
            'divide': {'text': '/', 'row': 5, 'column': 3}
        }
        self.other_char_buttons_attrs = {
            'decimal': {'text': '.', 'row': 5, 'column': 0},
            'comma': {'text': ' , ', 'row': 5, 'column': 2},
            'open_par': {'text': ' ( ', 'row': 6, 'column': 0},
            'close_par': {'text': ' ) ', 'row': 6, 'column': 1},
            'open_brac': {'text': ' [ ', 'row': 6, 'column': 2},
            'close_brac': {'text': ' ] ', 'row': 6, 'column': 3},
        }
        self._create_and_position_all_buttons(master)


    def _create_and_position_all_buttons(self, master):
        for i in range(10):
            self.number_buttons.append(tkinter.Button(master, fg='black', bg='white', height=1, width=7, text=str(i)))
            self.number_buttons[i].grid(row=self.number_buttons_attrs[i]['row'],
                                        column=self.number_buttons_attrs[i]['column'])

        self._create_and_position_buttons(master, self.transcendental_buttons, self.transcendental_buttons_attrs)
        self._create_and_position_buttons(master, self.math_helper_buttons, self.math_helper_buttons_attrs)
        self._create_and_position_buttons(master, self.math_buttons, self.math_buttons_attrs)
        self._create_and_position_buttons(master, self.other_char_buttons, self.other_char_buttons_attrs)

        self.clear_button = tkinter.Button(master, text='Clear', fg='black', bg='white', height=1, width=7)
        self.equal = tkinter.Button(master, text=' = ', fg='black', bg='white', height=1, width=7)
        self.answer_button = tkinter.Button(master, text='Ans', fg='black', bg='white', height=1, width=7)

        self.equal.grid(row=0, column=4)
        self.clear_button.grid(row=0, column=5)
        self.answer_button.grid(row=2, column=4)


    def _create_and_position_buttons(self, master, arr_buttons, hash_buttons_attrs):
        for index, key in enumerate(hash_buttons_attrs):
            button_text = hash_buttons_attrs[key]['text']
            arr_buttons.append(tkinter.Button(master, text=button_text, fg='black', bg='white', height=1, width=7))
            arr_buttons[index].grid(row=hash_buttons_attrs[key]['row'],column=hash_buttons_attrs[key]['column'])


