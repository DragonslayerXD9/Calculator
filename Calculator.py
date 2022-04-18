import re
import tkinter
from tkinter import *


class Calculator:
    def __init__(self, master):
        self.master = master

        self.allow_operator = False
        self.allow_dot = True
        self.button_set = True

        self.display_text = tkinter.StringVar()
        display = Label(self.master, textvariable=self.display_text, height=6, bg='gray', font=("Arial", 15),
                        justify=RIGHT)
        display.grid(row=0, column=1, columnspan=4)

        self.buttons = []
        self.create_buttons(self.master)
        self.equal_button

    def create_buttons(self, master):

        controls = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', 'x'],
            ['1', '2', '3', '-'],
            ['C', '0', '.', '+'],
        ]

        index = 0

        for i in range(0, len(controls)):
            for j in range(0, len(controls[i])):
                button_text = controls[i][j]
                self.buttons.append(Button(master, text=button_text, height=6, width=12))
                self.buttons[index].grid(row=i + 1, column=j)
                self.buttons[index].config(command=lambda button=button_text: self.add_to_display(button))
                index += 1
        self.equal_button = Button(master, text='=', height=26, width=12)
        self.equal_button.grid(column=len(controls) + 1, row=1, rowspan=4)
        self.equal_button.config(command=self.calculate)

    def add_to_display(self, button):
        if button == "+" or button == "-" or button == "x" or button == "/":
            if self.allow_operator:
                if button == "x":
                    button = "*"
                self.add(button)
                self.allow_operator = False
        elif button == "C":
            self.display_text.set("")
            self.allow_operator = True
            self.allow_dot = True
            return
        elif button == ".":
            if self.allow_dot:
                if self.display_text.get() == "":
                    self.add("0" + button)
                else:
                    self.add(button)
                self.allow_dot = False
        else:
            self.add(button)
            self.allow_operator = True

    def add(self, button):
        s = self.display_text.get()
        s += button
        self.display_text.set(s)

    def calculate(self):
        try:
            self.display_text.set(round(eval(self.display_text.get()), 2))
        except SyntaxError:
            self.display_text.set("Invalid Syntax")



def main():
    window = Tk()
    window.title('Calculator')
    window.geometry('470x540')
    window.configure(bg="gray")
    e = Calculator(window)
    window.resizable(False, False)
    window.mainloop()


if __name__ == "__main__":
    main()
