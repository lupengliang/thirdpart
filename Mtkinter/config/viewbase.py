# -*- coding:utf-8 -*-
# author:lupengliang
import tkinter as tk

# the function of creating GUI base
class ViewBase:
    def __init__(self):
        self.window = tk.Tk()

    # create GUI
    def create_gui(self, title, length, width):
        self.window.title(title)
        self.window.geometry(f'{length}x{width}+480+220')

    # create canvas
    def create_canvas(self, location, height, width, bg):
        canvas = tk.Canvas(location, height=height, width=width, bg=bg)
        return canvas

    # create label
    def create_label(self, location, text):
        label = tk.Label(location, text=text, font=('Arial', 14), anchor='n')
        return label

    # get user input info
    def get_userinfo(self, location, var):
        new_var = tk.Entry(location, textvariable=var, font=('Arial', 14))
        return new_var

    # create button
    def create_button(self, location, text, func):
        button = tk.Button(location, text=text, command=func)
        return button

    # loop while
    def loop_window(self):
        self.window.mainloop()

if __name__ == '__main__':
    pass
