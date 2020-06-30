""" To-Do Tracker
 
A simple task manager console app

- 2019 Tim Seymore
"""
from tkinter import *

import tkinter as tk
import pickle
import sys


class Doable:
    """ Composite Pattern object """

    def __init__(self, description: str):
        """ Creates object instance """
        self.complete = False
        self.description = description
        self.indent_level = " " * 2

    def get_complete(self) -> bool:
        """ Getter method """
        return self.complete

    def get_description(self) -> str:
        """ Returns description string """
        return self.description

    def set_complete(self):
        """ sets complete to True """
        self.complete = True

    def display(self, indent_space: str):
        """ Prints Doable to console

        - indent_space: starting indent space
        """
        pass

    def __str__(self) -> str:
        """ Returns string for printing object """
        return self.description


class ToDo(Doable):
    """ A to-do entry in a given task
    
     - description: String ; description of To-do
     - date: String ; date to complete To-do
     - location: String ; time to complete To-do
     """
    def __init__(self, description: str, date="", location=""):
        """ Constructor method """

        super().__init__(description) 
        self.date = date
        self.location = location

    # Getters
    def get_date(self) -> str:
        """ Getter method """
        return self.date

    def get_location(self) -> str:
        """ Getter method """
        return self.location

    # Setters

    def set_date(self, d: str):
        """ Setter method """
        if type(d) == str:
            self.date = d

    def set_location(self, t: str):
        """ Setter method """
        if type(t) == str:
            self.location = t

    def get_description(self) -> str:
        date_str = ""
        loc_str = ""
        if not self.date == "":
            date_str = " on " + self.date
        if not self.location == "":
            loc_str = " @ " + self.location
        return self.description + date_str + loc_str

    def set_complete(self):
        """ Sets complete to True unless already True """
        if not self.complete:
            self.complete = True

    def display(self, indent_space: str):
        """ Prints To-do to console

        - indent_space: starting indent space
        """
        print(indent_space + self.get_description())


class Task(Doable):
    """ A task with a list of Doables """

    def __init__(self, description: str):
        """ Creates object instance """
        super().__init__(description)
        self.subDoablesComplete = False
        self.nodes = []

    def get_subs(self):
        """ Getter method """
        return self.nodes

    def set_complete(self):
        """ Set self as complete if all subs are complete

        check that all subs are complete and set complete to True if so,
        otherwise print error message and exit function
        """
        for sub in self.nodes:
            if not sub.get_complete():
                print("ERROR: not all todos complete")
                return
        self.complete = True

    def num_subs(self) -> int:
        """ Returns the number of sub-components in task """
        return self.nodes.__len__()

    def contains(self, t: Doable) -> bool:
        """ Returns True if Component is in self.nodes
        
        Checks for Component with matching description
        and returns True if found, False otherwise
        """
        for sub in self.nodes:
            if t.get_description() == sub.get_description():
                return True
        return False

    def add_doable(self, t: Doable):
        """ Adds Component to self.subs

        checks if Component is already in list
        and adds it if not found.
        """
        if not self.contains(t):
            self.nodes.append(t)
        else:
            print("ERROR: Doable already exists in current task")

    def remove_doable(self, t: str):
        """ Removes Component from self.subs

        checks for Component with matching description
        and removes it if found.
        """
        for sub in self.nodes:
            if t == sub.get_description():
                self.nodes.remove(sub)
                return
        print("ERROR: Doable not found in task")

    def display(self, indent_space: str):
        """ Prints Task and all subs to console

        - indent_space: starting indent space
        """
        print(indent_space + self.description)
        for sub in self.nodes:
            try:
                sub.display(indent_space + sub.indent_level)
            except AttributeError:
                print("ERROR: " + sub.description + " has no attribute 'indent_level'")

    def display_gui(self, indent_space: str, top):
        lb1 = Listbox(top)
        lb1.insert(1, self)
        index = 2
        for sub in self.nodes:
            lb1.insert(index, indent_space + str(sub))
            index += 1
            for node in sub.nodes:
                lb1.insert(index, indent_space * 2 + str(node))
        # pack widgets
        lb1.pack()


class ToDoTracker:
    """ Main app ui 
    
    Run with self.main()
    """

    def __init__(self):
        """ Creates object instance """
        self.root = Task("ToDo Tracker")
        self.input_prompt = '>>> '
        self.commands = [
            'help',
            'exit',
            'addtask',
            'addtodo',
            'rmtask',
            'rmtodo',
            'ls',
            'ct',
            'pwt'
        ]

    def main(self):
        """ Runs main ui """
        self.load_from_disk()
        current_task = self.root
        print()
        print("  ToDo Tracker")
        print("-----------------")
        print("type 'help' for help")
        while True:
            choice = self.get_input()
            current_task = self.handle_input(choice, current_task)

    def get_input(self) -> str:
        """ Get and Return input from user

        Continue prompting for input until valid command is entered
        RETURN: valid input
        """
        print()
        inpt = input(self.input_prompt)
        while inpt not in self.commands:
            inpt = input(self.input_prompt)
        print()
        return inpt

    def handle_input(self, inp: str, current: Task) -> Task:
        """ Handle given user input

         - inp: input choice
         - current: current task
         Return: new current task
         """
        if inp == 'exit':
            self.exit_program()
            sys.exit()
        elif inp == 'help':
            self.show_help_menu()
        elif inp == 'ls':
            current.display("")
        elif inp == 'pwt':
            print(current)
        elif inp == 'ct':
            print("Change to:")
            try:
                current = self.change_task(input(self.input_prompt), current)
            except AttributeError:
                print("ERROR: ToDo object has no subs : Changing to ToDoTracker")
                current = self.root
        elif inp == 'addtask':
            print("New Task:")
            try:
                current.add_doable(Task(input(self.input_prompt)))
            except AttributeError:
                print("ERROR: ToDo object has no subs")
        elif inp == 'addtodo':
            print("New To-do:")
            name = input(self.input_prompt)
            print("Date (optional):")
            date = input(self.input_prompt)
            print("Location (optional):")
            location = input(self.input_prompt)
            new = ToDo(name, date, location)
            try:
                current.add_doable(new)
            except AttributeError:
                print("ERROR: ToDo object has no subs")
        elif inp == 'rmtask':
            print("Task to remove:")
            try:
                current.remove_doable(input(self.input_prompt))
            except AttributeError:
                print("ERROR: ToDo object has no subs")
        elif inp == 'rmtodo':
            print("To-do to remove:")
            try:
                current.remove_doable(input(self.input_prompt))
            except AttributeError:
                print("ERROR: ToDo object has no subs")
        return current

    def change_task(self, task: str, current: Task) -> Task:
        """ Change current working task

        RETURN: new task if it exists in current or
                root task otherwise and prints Error message
        """
        for t in current.get_subs():
            if task == t.get_description():
                return t
        if task != self.root.get_description():
            print("ERROR: task not found in current working task - changing to 'ToDo Tracker'")
        return self.root

    def save_to_disk(self):
        """ Save ToDoTracker object to file """
        try:
            temp_file = open("data.obj", 'wb')
            pickle.dump(self.root, temp_file)
            temp_file.close()
        except FileNotFoundError:
            print("ERROR: FileNotFound")

    def load_from_disk(self):
        """ Load saved data from file """
        try:
            temp_file = open('data.obj', 'rb')
            self.root = pickle.load(temp_file)
            temp_file.close()
        except FileNotFoundError:
            print("ERROR: FileNotFound")

    def exit_program(self):
        """ Prompt to save and exit program """
        valid_lst = ['Yes', 'yes', 'Y', 'y', 'No', 'no',  'N', 'n']
        yes_lst = valid_lst[:4]
        choice = ""
        while choice not in valid_lst:
            print("Save changes before exiting? (y/n)")
            choice = input(self.input_prompt)
        if choice in yes_lst:
            self.save_to_disk()
            print("Changes saved")
        else:
            print("Changes not saved")
        print("Exiting program")

    @staticmethod
    def show_help_menu():
        """ Print help menu to console """
        print("                   COMMANDS")
        print("=================================================")
        print(" | exit    : Exit program")
        print(" | help    : Help Menu")
        print(" | ls      : List current working task and todos")
        print(" | ct      : Change current working task")
        print(" | pwt     : Show present working task")
        print(" | addtask : Add new task to current task")
        print(" | addtodo : Add new to-do to current task")
        print(" | rmtask  : Delete task from current task")
        print(" | rmtodo  : Delete to-do from current task")


if __name__ == "__main__":
    ToDoTracker().main()
