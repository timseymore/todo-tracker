# UNDER CONSTRUCTION
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
        option_menu = Menu(menu_bar, tearoff=0)
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
