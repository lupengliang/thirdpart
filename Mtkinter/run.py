# -*- coding:utf-8 -*-
# author:lupengliang
import json
import re

from config.viewbase import ViewBase
import tkinter as tk

# generate config data
class OutsideView(ViewBase):
    def __init__(self):
        super().__init__()
        self.create_gui(title='Config Data', length=600, width=400)
        canvas = self.create_canvas(location=self.window, height=100, width=600, bg='green')
        image_file = tk.PhotoImage(file='./config/picture/pic.gif')
        image = canvas.create_image(200, 0, anchor='n', image=image_file)
        canvas.pack(side='top')

        # create keyword message
        self.create_label(location=self.window, text='username').place(x=70, y=140)
        self.create_label(location=self.window, text='password').place(x=70, y=180)
        self.create_label(location=self.window, text='ip').place(x=70, y=220)
        self.create_label(location=self.window, text='port').place(x=70, y=260)

        # the message of user input in window
        self.var_username = tk.StringVar()
        self.var_password = tk.StringVar()
        self.var_ip = tk.StringVar()
        self.var_port = tk.StringVar()
        self.get_userinfo(location=self.window, var=self.var_username).place(x=200, y=140)
        self.get_userinfo(location=self.window, var=self.var_password).place(x=200, y=180)
        self.get_userinfo(location=self.window, var=self.var_ip).place(x=200, y=220)
        self.get_userinfo(location=self.window, var=self.var_port).place(x=200, y=260)

        # create button
        self.create_button(self.window, text='   yes   ', func=self.get_data).place(x=200, y=320)
        self.create_button(self.window, text='  clear  ', func=self.clear_data).place(x=370, y=320)

        # remember data as init data
        with open('./config/config.txt', encoding='utf-8') as f:
            content = f.read()
            result_list = re.findall("'*': '(.*?)'", content)
            self.var_username.set(result_list[0]) if result_list[0] else self.var_username.set('')
            self.var_password.set(result_list[1]) if result_list[1] else self.var_username.set('')
            self.var_ip.set(result_list[2]) if result_list[2] else self.var_username.set('')
            self.var_port.set(result_list[3]) if result_list[3] else self.var_username.set('')
        canvas.pack()
        self.loop_window()

    # get user input data
    def get_data(self):
        username = self.var_username.get()
        password = self.var_password.get()
        ip = self.var_ip.get()
        port = self.var_port.get()
        data = {'username': username, 'password': password, 'ip': ip, 'port': port}
        with open('./config/config.txt', 'w', encoding='utf-8') as f:
            f.write(str(data))
        self.window.destroy()

    # clear all data and restart input
    def clear_data(self):
        self.var_username.set('')
        self.var_password.set('')
        self.var_ip.set('')
        self.var_port.set('')

if __name__ == '__main__':
    ov = OutsideView()