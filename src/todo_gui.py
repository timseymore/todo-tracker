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

    def main(self):
        # preprocessing details #
        self.load_from_disk()
        current_task = self.root

        # widgets go here #

        # main frame
        frame = Frame(self.top, bg="blue", bd=3)
        frame.pack()

        # menu
        menubar = Menu(self.top)

        optionmenu = Menu(menubar, tearoff=0)
        optionmenu.add_command(label="Exit", command=self.top.quit)
        optionmenu.add_separator()
        optionmenu.add_command(label="Exit", command=self.top.quit)
        menubar.add_cascade(label="Options", menu=optionmenu)

        self.top.config(menu=menubar)

        # show current task
        # task1 = Task("task 1")
        # task1.add_doable(ToDo("todo 1"))
        # task4 = Task("task 4")
        # task1.add_doable(task4)
        # task4.add_doable(ToDo("todo 2"))
        # current_task.add_doable(task1)  # test line only
        # current_task.add_doable(Task("task 2"))  # test line only
        # current_task.add_doable(Task("task 3"))  # test line only
        current_task.display_gui(self.indent_space, frame)

        # main loop #
        self.top.mainloop()


if __name__ == "__main__":
    ToDoTrackerGui().main()
