# UNDER CONSTRUCTION
from tkinter import *

import tkinter as tk
from todo import *


# classes
class ToDoTrackerGui(ToDoTracker):
    def __init__(self):
        self.root = Task("ToDo Tracker")
        self.top = tk.Tk()

    def main(self):
        # preprocessing details
        self.load_from_disk()

        # widgets go here
        lb1 = Listbox(self.top)
        lb1.insert(1, "Todo Tracker")
        lb2 = Listbox(self.top)
        lb2.insert(1, "todo 1")

        # pack widgets
        lb1.pack()
        lb2.pack()

        # main loop
        self.top.mainloop()


if __name__ == "__main__":
    ToDoTrackerGui().main()
