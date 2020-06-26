# UNDER CONSTRUCTION
from tkinter import *

import tkinter as tk
import todo

top = tk.Tk()

# widgets go here
lb1 = Listbox(top)
lb1.insert(1, "Todo Tracker")
lb2 = Listbox(top)
lb2.insert(1, "todo 1")

# pack widgets
lb1.pack()
lb2.pack()

# main loop
top.mainloop()
