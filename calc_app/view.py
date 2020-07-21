import tkinter
import pdb

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
        self.buttons = []
        for i in range(10):
            self.buttons.append(tkinter.Button(master, fg='black', bg='white', height=1, width=7, text=str(i)))

        #pdb.set_trace()

        self.plus = tkinter.Button(master, text=' + ', fg='black', bg='white', height=1, width=7)
        self.log10 = tkinter.Button(master, text=' log10( ', fg='black', bg='white',height=1, width=7)
        self.mad = tkinter.Button(master, text=' MAD([ ', fg='black', bg='white',height=1, width=7)
        self.minus = tkinter.Button(master, text=' - ', fg='black', bg='white', height=1, width=7)
        self.sinx = tkinter.Button(master, text=' sin( ', fg='black', bg='white', height=1, width=7)
        self.sd = tkinter.Button(master, text=' SD([ ', fg='black', bg='white', height=1, width=7)
        self.multiply = tkinter.Button(master, text=' * ', fg='black', bg='white', height=1, width=7)
        self.cosh = tkinter.Button(master, text=' cosh( ', fg='black', bg='white', height=1, width=7)
        self.clear_button = tkinter.Button(master, text='Clear', fg='black', bg='white', height=1, width=7)
        self.equal = tkinter.Button(master, text=' = ', fg='black', bg='white', height=1, width=7)
        self.divide = tkinter.Button(master, text=' / ', fg='black', bg='white', height=1, width=7)
        self.power10 = tkinter.Button(master, text=' 10^( ', fg='black', bg='white',height=1, width=7)
        self.power = tkinter.Button(master, text=' ^ ', fg='black', bg='white', height=1, width=7)
        self.decimal = tkinter.Button(master, text='.', fg='black', bg='white', height=1, width=7)
        self.answer_button = tkinter.Button(master, text='Ans', fg='black', bg='white', height=1, width=7)
        self.open_par = tkinter.Button(master, text=' ( ', fg='black', bg='white', height=1, width=7)
        self.close_par = tkinter.Button(master, text=' ) ', fg='black', bg='white', height=1, width=7)
        self.open_brac = tkinter.Button(master, text=' [ ', fg='black', bg='white', height=1, width=7)
        self.close_brac = tkinter.Button(master, text=' ] ', fg='black', bg='white', height=1, width=7)
        self.coma = tkinter.Button(master, text=' , ', fg='black', bg='white', height=1, width=7)
        self.pi = tkinter.Button(master, text=' \u03C0 ', fg='black', bg='white', height=1,
                           width=7)
        self.sqrt = tkinter.Button(master, text=' \u221A ', fg='black', bg='white',height=1,
                      width=7)


        self.equal.grid(row=0, column=4)
        self.clear_button.grid(row=0, column=5)
        self.buttons[1].grid(row=2, column=0)
        self.buttons[2].grid(row=2, column=1)
        self.buttons[3].grid(row=2, column=2)
        self.plus.grid(row=2, column=3)
        self.answer_button.grid(row=2, column=4)
        self.mad.grid(row=2, column=5)
        self.buttons[4].grid(row=3, column=0)
        self.buttons[5].grid(row=3, column=1)
        self.buttons[6].grid(row=3, column=2)
        self.minus.grid(row=3, column=3)
        self.sinx.grid(row=3, column=4)
        self.sd.grid(row=3, column=5)
        self.buttons[7].grid(row=4, column=0)
        self.buttons[8].grid(row=4, column=1)
        self.buttons[9].grid(row=4, column=2)
        self.multiply.grid(row=4, column=3)
        self.cosh.grid(row=4, column=4)
        self.log10.grid(row=4, column=5)
        self.decimal.grid(row=5, column=0)
        self.buttons[0].grid(row=5, column=1)
        self.coma.grid(row=5, column=2)
        self.divide.grid(row=5, column=3)
        self.power10.grid(row=5, column=4)
        self.power.grid(row=5, column=5)
        self.open_par.grid(row=6, column=0)
        self.close_par.grid(row=6, column=1)
        self.open_brac.grid(row=6, column=2)
        self.close_brac.grid(row=6, column=3)
        self.pi.grid(row=6, column=4)
        self.sqrt.grid(row=6, column=5)


