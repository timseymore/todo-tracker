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
        frame = Frame(self.top)
        frame.pack()

        # show current task
        # task1 = Task("task 1")
        # task1.add_doable(ToDo("todo 1"))
        # task4 = Task("task 4")
        # task1.add_doable(task4)
        # task4.add_doable(ToDo("todo 2"))
        # current_task.add_doable(task1)  # test line only
        # current_task.add_doable(Task("task 2"))  # test line only
        # current_task.add_doable(Task("task 3"))  # test line only
        current_task.display_gui(self.indent_space, self.top)

        # main loop #
        self.top.mainloop()


if __name__ == "__main__":
    ToDoTrackerGui().main()
