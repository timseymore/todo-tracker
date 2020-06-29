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
        # preprocessing details
        self.load_from_disk()
        current_task = self.root

        # widgets go here

        # show current task
        # current_task.add_doable(Task("task 1")) # test line only
        # current_task.add_doable(Task("task 2")) # test line only
        # current_task.add_doable(Task("task 3")) # test line only
        lb1 = Listbox(self.top)
        lb1.insert(1, current_task)
        index = 2
        for sub in current_task.nodes:
            lb1.insert(index, self.indent_space + str(sub))
            index += 1

        # pack widgets
        lb1.pack()

        # main loop
        self.top.mainloop()


if __name__ == "__main__":
    ToDoTrackerGui().main()
