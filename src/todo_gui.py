"""

ToDo Tracker GUI
================

UNDER CONSTRUCTION




MIT License

Copyright (c) 2020 Tim Seymore

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""""
from tkinter import *

import tkinter as tk
from todo import *


# classes
class ToDoTrackerGui(ToDoTracker):
    def __init__(self):
        self.root = Task("ToDo Tracker")
        self.top = tk.Tk()
        self.indent_space = "    "
        self.current_task = self.root
        self.frame = Frame(self.top, bg="blue", bd=3)

    def main(self):
        # - set up - #
        self.load_from_disk()
        self.frame.pack()

        # - widgets - #
        self.display_menu()
        self.display_current()

        # - main loop - #
        self.top.mainloop()

    def display_current(self):
        self.current_task.display_gui(self.indent_space, self.frame)

    # TODO
    def add_task(self):
        self.current_task.add_doable(Task("test task"))
        self.display_current()

    # TODO
    def add_todo(self):
        self.current_task.add_doable(ToDo("test todo"))
        self.display_current()

    # TODO
    def change_task(self):
        self.top.quit()

    def display_menu(self):
        menu_bar = Menu(self.top)
        # options menu
        option_menu = Menu(menu_bar, tearoff=0, fg="blue")
        option_menu.add_command(label="Change task", command=self.change_task)
        option_menu.add_command(label="Add task", command=self.add_task)
        option_menu.add_command(label="Add todo", command=self.add_todo)
        option_menu.add_separator()
        option_menu.add_command(label="Exit", command=self.exit)
        menu_bar.add_cascade(label="Options", menu=option_menu)

        self.top.config(menu=menu_bar)

    # TODO
    def exit(self):
        self.top.quit()


if __name__ == "__main__":
    ToDoTrackerGui().main()
